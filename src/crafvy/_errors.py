"""Errors the SDK raises.

Every refusal the API sends is ``{"success": false, "error": "...", "code": "..."}``.
The SDK raises one of the classes below, carrying the HTTP ``status``, the API's
machine-readable ``code`` (``tokenPermissionMissing``, ``crmSpaceNotFound``, ...)
and the whole response ``body`` — branch on the code, not on the English text::

    try:
        crafvy.tasks.create({"workspaceId": ws, "title": "Call Anna"})
    except CrafvyError as err:
        if err.code == "tasksSpaceRequired":
            ...
"""
from __future__ import annotations

from typing import Any, Optional


class CrafvyError(Exception):
    """Any error answer of the API (and a timeout, as status 408)."""

    def __init__(self, message: str, status: int, body: Any = None, code: Optional[str] = None) -> None:
        super().__init__(message)
        self.message = message
        self.status = status
        self.body = body
        if code is None and isinstance(body, dict) and isinstance(body.get("code"), str):
            code = body["code"]
        self.code = code

    def __repr__(self) -> str:
        return f"{type(self).__name__}(status={self.status}, code={self.code!r}, message={self.message!r})"


class ValidationError(CrafvyError):
    """400 — the request was refused as invalid."""


class AuthenticationError(CrafvyError):
    """401 — no token, or one that is not valid (any more)."""


class AuthorizationError(CrafvyError):
    """403 — not allowed: the owner's roles, or the token's permissions (``tokenPermissionMissing``, ``tokenScopeInsufficient``)."""


class NotFoundError(CrafvyError):
    """404 — nothing there, or nothing the token's owner may see."""


class ConflictError(CrafvyError):
    """409 — it clashes with what is there now (a name taken, a field changed meanwhile)."""


class RateLimitError(CrafvyError):
    """429 — too many requests, after the SDK's own retries. ``retry_after`` is in seconds, when the API said."""

    def __init__(self, message: str, body: Any = None, retry_after: Optional[float] = None) -> None:
        super().__init__(message, 429, body)
        self.retry_after = retry_after


_BY_STATUS = {
    400: ValidationError,
    401: AuthenticationError,
    403: AuthorizationError,
    404: NotFoundError,
    409: ConflictError,
}


def error_for(status: int, body: Any, retry_after: Optional[float] = None) -> CrafvyError:
    message = body.get("error") if isinstance(body, dict) and isinstance(body.get("error"), str) else f"HTTP {status}"
    if status == 429:
        return RateLimitError(message, body, retry_after)
    cls = _BY_STATUS.get(status, CrafvyError)
    if cls is CrafvyError:
        return CrafvyError(message, status, body)
    return cls(message, status, body)
