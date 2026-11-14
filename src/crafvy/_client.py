"""The client: authentication, the HTTP transport, retries and errors."""
from __future__ import annotations

import json
import os
import random
import time
import urllib.error
import urllib.parse
import urllib.request
import uuid
from typing import Any, Callable, Dict, Iterator, List, Mapping, Optional, Tuple

from ._errors import CrafvyError, error_for
from ._generated.operations import API_VERSION
from ._generated.resources import Resources
from ._runtime import RequestOptions

# (method, url, headers, body bytes or None, timeout seconds) -> (status, headers, body bytes)
Transport = Callable[[str, str, Dict[str, str], Optional[bytes], Optional[float]], Tuple[int, Mapping[str, str], bytes]]

DEFAULT_BASE_URL = "https://app.crafvy.com"
_IDEMPOTENT = {"GET", "HEAD", "PUT", "DELETE"}
_RETRYABLE_5XX = {500, 502, 503, 504}


def urllib_transport(method: str, url: str, headers: Dict[str, str], body: Optional[bytes], timeout: Optional[float]) -> Tuple[int, Mapping[str, str], bytes]:
    """The default transport: the standard library's urllib, no dependencies."""
    req = urllib.request.Request(url, data=body, method=method, headers=headers)
    try:
        with urllib.request.urlopen(req, timeout=timeout) as res:
            return res.status, dict(res.headers.items()), res.read()
    except urllib.error.HTTPError as err:
        return err.code, dict(err.headers.items()) if err.headers else {}, err.read() or b""
    except TimeoutError as err:
        raise CrafvyError(f"Request timed out after {timeout}s", 408) from err
    except urllib.error.URLError as err:
        if isinstance(err.reason, TimeoutError):
            raise CrafvyError(f"Request timed out after {timeout}s", 408) from err
        raise


class Crafvy(Resources):
    """The Crafvy API.

    ::

        from crafvy import Crafvy

        crafvy = Crafvy("pb_...")  # or the CRAFVY_TOKEN environment variable
        projects = crafvy.projects.list(workspace_id="...")

    A token acts as its owner: their roles, workspaces, feature gates and plan
    limits apply exactly as in the dashboard. Create one under Settings →
    Integrations → API Access Tokens.
    """

    def __init__(
        self,
        token: Optional[str] = None,
        *,
        base_url: Optional[str] = None,
        timeout: Optional[float] = 60.0,
        retries: int = 3,
        transport: Optional[Transport] = None,
    ) -> None:
        token = token or os.environ.get("CRAFVY_TOKEN")
        if not token:
            raise ValueError("Crafvy: pass a token, or set CRAFVY_TOKEN")
        self._token = token
        self._base_url = (base_url or os.environ.get("CRAFVY_BASE_URL") or DEFAULT_BASE_URL).rstrip("/")
        self._timeout = timeout
        self._retries = retries
        self._transport = transport or urllib_transport
        super().__init__(self._call)

    def raw(self, method: str, path: str, *, query: Optional[Dict[str, Any]] = None, body: Any = None, options: Optional[RequestOptions] = None) -> Any:
        """Calls any path of the API directly — for an endpoint this SDK version has no method for yet."""
        return self._call(method.upper(), path, query=query, body=body, options=options)

    def _call(
        self,
        method: str,
        path: str,
        *,
        query: Optional[Dict[str, Any]] = None,
        body: Any = None,
        multipart: bool = False,
        options: Optional[RequestOptions] = None,
    ) -> Any:
        options = options or {}
        url = self._base_url + path
        if query:
            pairs = [(k, _query_value(v)) for k, v in query.items() if v is not None]
            if pairs:
                url += "?" + urllib.parse.urlencode(pairs)
        headers = {
            "Authorization": f"Bearer {self._token}",
            "Accept": "application/json",
            "User-Agent": f"crafvy-python/{API_VERSION}",
        }
        data: Optional[bytes] = None
        if body is not None:
            if multipart:
                data, content_type = _multipart(body)
                headers["Content-Type"] = content_type
            else:
                data = json.dumps(body).encode("utf-8")
                headers["Content-Type"] = "application/json"
        headers.update(options.get("headers", {}))
        retries = options.get("retries", self._retries)
        timeout = options.get("timeout", self._timeout)

        attempt = 0
        while True:
            status, res_headers, raw = self._transport(method, url, headers, data, timeout)
            retryable = status == 429 or (status in _RETRYABLE_5XX and method in _IDEMPOTENT)
            if retryable and attempt < retries:
                time.sleep(_delay(attempt, _header(res_headers, "Retry-After")))
                attempt += 1
                continue
            parsed: Any = None
            if raw:
                try:
                    parsed = json.loads(raw.decode("utf-8"))
                except ValueError:
                    parsed = raw.decode("utf-8", errors="replace")
            if status >= 400:
                ra = _header(res_headers, "Retry-After")
                raise error_for(status, parsed, float(ra) if ra and ra.replace(".", "", 1).isdigit() else None)
            return parsed


def _query_value(v: Any) -> str:
    if isinstance(v, bool):
        return "true" if v else "false"
    if isinstance(v, (dict, list)):
        return json.dumps(v)
    return str(v)


def _header(headers: Mapping[str, str], name: str) -> Optional[str]:
    for k, v in headers.items():
        if k.lower() == name.lower():
            return v
    return None


def _delay(attempt: int, retry_after: Optional[str]) -> float:
    if retry_after:
        try:
            return float(retry_after)
        except ValueError:
            pass
    return 0.5 * (2**attempt) + random.random() * 0.1


def _multipart(fields: Mapping[str, Any]) -> Tuple[bytes, str]:
    boundary = f"crafvy-{uuid.uuid4().hex}"
    out: List[bytes] = []
    for key, value in fields.items():
        if value is None:
            continue
        if isinstance(value, (bytes, bytearray)):
            out.append(f'--{boundary}\r\nContent-Disposition: form-data; name="{key}"; filename="{key}"\r\nContent-Type: application/octet-stream\r\n\r\n'.encode())
            out.append(bytes(value))
            out.append(b"\r\n")
        elif isinstance(value, tuple) and len(value) >= 2:
            filename, content = value[0], value[1]
            ctype = value[2] if len(value) > 2 else "application/octet-stream"
            out.append(f'--{boundary}\r\nContent-Disposition: form-data; name="{key}"; filename="{filename}"\r\nContent-Type: {ctype}\r\n\r\n'.encode())
            out.append(content if isinstance(content, bytes) else str(content).encode())
            out.append(b"\r\n")
        else:
            text = json.dumps(value) if isinstance(value, (dict, list)) else _query_value(value)
            out.append(f'--{boundary}\r\nContent-Disposition: form-data; name="{key}"\r\n\r\n{text}\r\n'.encode())
    out.append(f"--{boundary}--\r\n".encode())
    return b"".join(out), f"multipart/form-data; boundary={boundary}"


def paginate(fetch: Callable[..., Any], *, limit: int = 50, start_page: int = 1, **kwargs: Any) -> Iterator[Any]:
    """Every item of a page-based list, one page at a time behind the scenes.

    ::

        for project in paginate(crafvy.projects.list, workspace_id=ws):
            ...
    """
    page = start_page
    while True:
        items = fetch(page=page, limit=limit, **kwargs)
        if isinstance(items, dict):
            items = next((v for v in items.values() if isinstance(v, list)), [])
        if not items:
            return
        yield from items
        if len(items) < limit:
            return
        page += 1
