"""The official Python SDK of the Crafvy API.

::

    from crafvy import Crafvy

    crafvy = Crafvy("pb_...")
    for project in crafvy.projects.list():
        print(project["name"])
"""
from ._client import DEFAULT_BASE_URL, Crafvy, Transport, paginate, urllib_transport
from ._errors import (
    AuthenticationError,
    AuthorizationError,
    ConflictError,
    CrafvyError,
    NotFoundError,
    RateLimitError,
    ValidationError,
)
from ._generated.operations import API_VERSION, OPERATIONS
from ._runtime import RequestOptions

__version__ = API_VERSION

__all__ = [
    "API_VERSION",
    "AuthenticationError",
    "AuthorizationError",
    "ConflictError",
    "Crafvy",
    "CrafvyError",
    "DEFAULT_BASE_URL",
    "NotFoundError",
    "OPERATIONS",
    "RateLimitError",
    "RequestOptions",
    "Transport",
    "ValidationError",
    "paginate",
    "urllib_transport",
]
