"""What the generated resources call: the request function's shape and small helpers."""
from __future__ import annotations

import urllib.parse
import warnings
from typing import Any, Callable, Dict, Optional, TypedDict


class RequestOptions(TypedDict, total=False):
    """Per-call overrides."""

    timeout: float
    """Seconds before the call gives up (raises CrafvyError with status 408)."""
    retries: int
    """How often a 429 (or a 5xx of an idempotent method) is retried."""
    headers: Dict[str, str]
    """Extra headers."""


# (method, path, *, query, body, multipart, options) -> the decoded JSON answer
Requester = Callable[..., Any]


class _Resource:
    def __init__(self, request: Requester) -> None:
        self._request = request


def _seg(value: Any) -> str:
    """A path parameter, URL-encoded."""
    return urllib.parse.quote(str(value), safe="")


def _pick(value: Any, path: str) -> Any:
    """The value at a dotted path of an answer (an operation's ``returns``)."""
    for key in path.split("."):
        if not isinstance(value, dict):
            return None
        value = value.get(key)
    return value


def _deprecated(operation_id: str) -> None:
    warnings.warn(f"Crafvy: {operation_id} is deprecated — see its docstring for what to use instead.", DeprecationWarning, stacklevel=3)
