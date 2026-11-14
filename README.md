# Crafvy — Python SDK

The official Python client of the [Crafvy](https://crafvy.com) API. Every
resource and method is generated from the API's description, the same one the
TypeScript, PHP, Go, Java and C# SDKs and the [reference](https://docs.crafvy.com/sdk)
come from — so a method here is exactly the one documented there.

No dependencies; Python 3.9 or newer.

```sh
pip install crafvy
```

## Use

```python
from crafvy import Crafvy

crafvy = Crafvy("pb_...")          # or set CRAFVY_TOKEN
# crafvy = Crafvy(base_url="https://your-instance.example")  # self-hosted

for project in crafvy.projects.list():
    print(project["name"])

space = crafvy.crm.spaces.list(workspace_id="...")[0]
```

- Methods and keyword arguments are `snake_case`; path parameters come first,
  positionally; a body is one `dict`; query parameters are keyword arguments.
- Answers are plain `dict`s and `list`s, typed with `TypedDict`s — your editor
  knows every field.
- `crafvy.raw("GET", "/api/...")` calls any endpoint directly.

## Tokens

A token acts as its owner: their roles, workspaces, feature gates and plan
limits apply exactly as in the dashboard. Create one under **Settings →
Integrations → API Access Tokens**. A token made with permissions only reaches
those families of routes; each method's docstring names the permission it needs.

## Errors

```python
from crafvy import CrafvyError, NotFoundError

try:
    crafvy.projects.get("missing")
except NotFoundError:
    ...
except CrafvyError as err:
    print(err.status, err.code, err.message)
```

`code` is the API's stable reason (`tokenPermissionMissing`, …) — branch on it,
not on the English text. 429 answers are retried with back-off (respecting
`Retry-After`); a 5xx is retried only for GET, PUT and DELETE, never for a
POST that may have been carried out.

## Options

```python
crafvy = Crafvy(token, timeout=30, retries=5)
crafvy.projects.list(options={"timeout": 5, "headers": {"X-Trace": "1"}})
```

Tests can pass `transport=` (a function taking method, url, headers, body,
timeout and returning status, headers, body) instead of real HTTP.

## Pagination

```python
from crafvy import paginate

for project in paginate(crafvy.projects.list, limit=100):
    ...
```

Changelog: [CHANGELOG.md](CHANGELOG.md). Generated — changes go into the API's
description in the Crafvy repository, not into this package.
