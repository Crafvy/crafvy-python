"""Every operation of sdks/conformance.json: the request that goes out, and what comes back."""
import json
import warnings
import os
import unittest
import urllib.parse

from crafvy import Crafvy
from crafvy._generated._calls import CALLS

HERE = os.path.dirname(__file__)
# In the Crafvy repository it is sdks/conformance.json; in the public SDK repository, beside the package.
_SUITE_PATH = next(p for p in (os.path.join(HERE, "..", "conformance.json"), os.path.join(HERE, "..", "..", "conformance.json")) if os.path.exists(p))
with open(_SUITE_PATH, encoding="utf-8") as f:
    SUITE = json.load(f)


class Recorder:
    def __init__(self):
        self.sent = []
        self.reply = (200, {}, b"{}")

    def __call__(self, method, url, headers, body, timeout):
        self.sent.append((method, url, headers, body))
        return self.reply


class Conformance(unittest.TestCase):
    def test_every_operation(self):
        rec = Recorder()
        client = Crafvy("pb_test", base_url="https://api.test", transport=rec, retries=0)
        for case in SUITE["cases"]:
            with self.subTest(case["id"]):
                chain, name, query_names = CALLS[case["id"]]
                target = client
                for attr in chain:
                    target = getattr(target, attr)
                method = getattr(target, name)
                kwargs = {query_names[k]: v for k, v in (case["query"] or {}).items()}
                args = list(case["pathArgs"])
                if case["body"] is not None:
                    args.append(case["body"])
                elif case["expect"]["method"] in ("POST", "PUT", "PATCH") and _takes_body(method):
                    args.append({})
                rec.reply = (200, {"Content-Type": "application/json"}, json.dumps(case["response"]).encode())
                with warnings.catch_warnings():
                    warnings.simplefilter("ignore", DeprecationWarning)
                    result = method(*args, **kwargs)
                sent_method, url, headers, body = rec.sent[-1]
                parsed = urllib.parse.urlsplit(url)
                self.assertEqual(sent_method, case["expect"]["method"])
                self.assertEqual(parsed.path, case["expect"]["path"])
                self.assertEqual(dict(urllib.parse.parse_qsl(parsed.query)), case["expect"]["query"])
                if case["expect"]["body"] is not None:
                    self.assertEqual(json.loads(body), case["expect"]["body"])
                self.assertEqual(headers["Authorization"], "Bearer pb_test")
                self.assertEqual(result, case["result"])


def _takes_body(method):
    import inspect

    return "body" in inspect.signature(method).parameters


class Runtime(unittest.TestCase):
    def test_path_parameters_are_encoded(self):
        rec = Recorder()
        client = Crafvy("pb_test", base_url="https://api.test", transport=rec)
        rec.reply = (200, {}, b'{"success":true}')
        client.raw("GET", "/api/x")
        chain, name, _ = CALLS["projects.get"]
        getattr(client.projects, name)("a b/c")
        self.assertTrue(rec.sent[-1][1].startswith("https://api.test/api/projects/a%20b%2Fc"))

    def test_errors_carry_status_and_code(self):
        from crafvy import AuthorizationError, CrafvyError, NotFoundError

        rec = Recorder()
        client = Crafvy("pb_test", base_url="https://api.test", transport=rec, retries=0)
        rec.reply = (403, {}, b'{"success":false,"error":"No","code":"tokenPermissionMissing"}')
        with self.assertRaises(AuthorizationError) as ctx:
            client.raw("GET", "/api/projects")
        self.assertEqual(ctx.exception.code, "tokenPermissionMissing")
        self.assertEqual(ctx.exception.status, 403)
        rec.reply = (404, {}, b'{"success":false,"error":"Not found"}')
        with self.assertRaises(NotFoundError):
            client.raw("GET", "/api/projects/x")
        rec.reply = (418, {}, b"")
        with self.assertRaises(CrafvyError) as ctx:
            client.raw("GET", "/api/x")
        self.assertEqual(ctx.exception.status, 418)

    def test_retries_429_and_idempotent_5xx_only(self):
        replies = [(429, {"Retry-After": "0"}, b""), (200, {}, b'{"ok":true}')]
        sent = []

        def transport(method, url, headers, body, timeout):
            sent.append(method)
            return replies.pop(0)

        client = Crafvy("pb_test", base_url="https://api.test", transport=transport)
        self.assertEqual(client.raw("POST", "/api/x", body={}), {"ok": True})
        self.assertEqual(len(sent), 2)

        sent.clear()
        replies[:] = [(503, {"Retry-After": "0"}, b'{"error":"down"}')]
        from crafvy import CrafvyError

        with self.assertRaises(CrafvyError):
            client.raw("POST", "/api/x", body={})
        self.assertEqual(len(sent), 1, "a POST that failed with a 5xx is not sent again")

    def test_structured_query_values_travel_as_json(self):
        rec = Recorder()
        client = Crafvy("pb_test", base_url="https://api.test", transport=rec)
        client.raw("GET", "/api/x", query={"filters": [{"a": 1}], "on": True, "skip": None})
        q = dict(urllib.parse.parse_qsl(urllib.parse.urlsplit(rec.sent[-1][1]).query))
        self.assertEqual(q, {"filters": '[{"a": 1}]', "on": "true"})

    def test_token_from_environment(self):
        os.environ["CRAFVY_TOKEN"] = "pb_env"
        try:
            rec = Recorder()
            Crafvy(transport=rec).raw("GET", "/api/x")
            self.assertEqual(rec.sent[-1][2]["Authorization"], "Bearer pb_env")
        finally:
            del os.environ["CRAFVY_TOKEN"]


if __name__ == "__main__":
    unittest.main()
