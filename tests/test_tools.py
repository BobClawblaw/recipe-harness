"""The tools check and the structured skip probe against a fake OpenAI server: one that has lost its grammar library
(the 2026-10-20 5090 deploy: forced tool calls and json_schema refused, auto still fine), one that serves everything,
and one whose arguments leave the schema."""

import json
import tempfile
import threading
import unittest
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path

from harness import config
from harness.checks import applies, server, skip_reason

GRAMMAR = ("structured output: libtfgrammar.so is required for structured output and required tool calls; "
           "restore the matching release archive's lib directory or build zig build grammar")
BOOKING = {"from": "Oslo", "to": "Rome", "cabin": "business", "passengers": [{"name": "Ana", "age": 31}, {"name": "Leo", "age": 6}]}


class Fake(BaseHTTPRequestHandler):
    mode = "good"  # good | no_grammar | off_schema

    def log_message(self, *a):
        pass

    def reply(self, status, body):
        raw = json.dumps(body).encode()
        self.send_response(status)
        self.send_header("Content-Type", "application/json")
        self.send_header("Content-Length", str(len(raw)))
        self.end_headers()
        self.wfile.write(raw)

    def do_GET(self):
        self.reply(200, {"data": [{"id": "m"}]})

    def do_POST(self):
        body = json.loads(self.rfile.read(int(self.headers["Content-Length"])))
        forced = body.get("tool_choice") not in (None, "auto") or "response_format" in body
        if self.mode == "no_grammar" and forced:
            return self.reply(400, {"error": {"message": GRAMMAR, "type": "invalid_request_error"}})
        if "response_format" in body:
            msg = {"role": "assistant", "content": json.dumps({"name": "Ana", "age": 31, "hobbies": []})}
            return self.reply(200, {"choices": [{"message": msg, "finish_reason": "stop"}]})
        booking = dict(BOOKING, cabin="coach") if self.mode == "off_schema" else BOOKING
        calls = [("book_flight", booking)]
        if body.get("tool_choice") != server.NAMED:
            calls.append(("get_weather", {"city": "Rome"}))
        calls = [{"id": f"c{i}", "type": "function", "function": {"name": n, "arguments": json.dumps(a)}} for i, (n, a) in enumerate(calls)]
        if not body.get("stream"):
            msg = {"role": "assistant", "content": None, "tool_calls": calls}
            return self.reply(200, {"choices": [{"message": msg, "finish_reason": "tool_calls"}], "usage": {}})
        self.send_response(200)
        self.send_header("Content-Type", "text/event-stream")
        self.end_headers()
        chunks = []
        for i, c in enumerate(calls):  # the name first, then the arguments in two pieces, as servers stream them
            args = c["function"]["arguments"]
            chunks += [{"index": i, "id": c["id"], "type": "function", "function": {"name": c["function"]["name"], "arguments": ""}},
                       {"index": i, "function": {"arguments": args[:10]}}, {"index": i, "function": {"arguments": args[10:]}}]
        for tc in chunks:
            self.wfile.write(f"data: {json.dumps({'choices': [{'delta': {'tool_calls': [tc]}, 'finish_reason': None}]})}\n\n".encode())
        self.wfile.write(f"data: {json.dumps({'choices': [{'delta': {}, 'finish_reason': 'tool_calls'}]})}\n\ndata: [DONE]\n\n".encode())


class Tools(unittest.TestCase):
    def setUp(self):
        self.http = ThreadingHTTPServer(("127.0.0.1", 0), Fake)
        threading.Thread(target=self.http.serve_forever, daemon=True).start()
        self.dir = tempfile.TemporaryDirectory()

    def tearDown(self):
        self.http.shutdown()
        self.http.server_close()
        self.dir.cleanup()
        Fake.mode = "good"

    def target(self, **features):
        return config.Target("t", {"url": f"http://127.0.0.1:{self.http.server_address[1]}", "model": "m", "features": features}, {})

    def run_tools(self, mode, **features):
        Fake.mode = mode
        return server.tools(self.target(**features), {}, Path(self.dir.name), "tools")

    def test_a_server_without_its_grammar_fails_and_names_the_library(self):
        r = self.run_tools("no_grammar")
        self.assertFalse(r["ok"])
        self.assertIn("libtfgrammar.so is required", r["summary"])
        self.assertTrue(r["summary"].startswith("1/5 "))  # auto needs no grammar, so it still works: that hid the deploy

    def test_a_server_that_serves_everything_passes_all_five(self):
        r = self.run_tools("good")
        self.assertTrue(r["ok"], r["summary"])
        self.assertEqual(r["summary"], "5/5 tool cases right")

    def test_arguments_outside_the_schema_fail(self):
        r = self.run_tools("off_schema")
        self.assertFalse(r["ok"])
        self.assertIn("outside the schema", r["summary"])

    def test_without_structured_only_auto_runs_and_the_summary_says_what_was_not(self):
        r = self.run_tools("no_grammar", structured=False)
        self.assertTrue(r["ok"], r["summary"])
        self.assertIn("not tested (features.structured = false): required, named", r["summary"])

    def test_the_tools_feature_skips_the_check(self):
        self.assertTrue(applies(self.target(), "tools", {}))
        self.assertFalse(applies(self.target(tools=False), "tools", {}))

    def test_a_structured_skip_asks_the_server(self):
        Fake.mode = "no_grammar"
        self.assertIn("refuses json_schema (400", skip_reason(self.target(structured=False), "structured"))
        Fake.mode = "good"  # a stale flag: the engine gained grammars and the target still turns them off
        self.assertIn("turn features.structured on", skip_reason(self.target(structured=False), "structured_speed"))
        self.assertEqual(skip_reason(self.target(sampling=False), "sampling"), "features.sampling = false")


if __name__ == "__main__":
    unittest.main()
