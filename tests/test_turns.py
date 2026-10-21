"""The turns check against a fake server whose reply is set by the exact prompt and whose kept prompts a restart drops:
a trailing space in the system prompt is one more token (Flint's template), so the padded cold turn is a different
request; after a restart the same conversation is cold with the same tokens."""

import hashlib
import json
import tempfile
import threading
import unittest
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path

from harness import config
from harness.checks import server


class Fake(BaseHTTPRequestHandler):
    kept: set = set()
    resumed_differs = False  # an engine whose resumed reply differs from the same prompt cold

    def log_message(self, *a):
        pass

    def do_GET(self):
        raw = json.dumps({"data": [{"id": "m"}]}).encode()
        self.send_response(200)
        self.send_header("Content-Length", str(len(raw)))
        self.end_headers()
        self.wfile.write(raw)

    def do_POST(self):
        body = json.loads(self.rfile.read(int(self.headers.get("Content-Length", 0))) or b"{}")
        if self.path == "/restart":
            Fake.kept.clear()
            self.send_response(200)
            self.send_header("Content-Length", "0")
            self.end_headers()
            return
        prompt = "".join(f"<{m['role']}>{m['content']}" for m in body["messages"])
        cached = max((len(p) for p in Fake.kept if prompt.startswith(p)), default=0)
        Fake.kept.add(prompt)
        text = hashlib.sha256(prompt.encode()).hexdigest()[:16] + ("-resumed" if cached and Fake.resumed_differs else "")
        usage = {"prompt_tokens": len(prompt.split(" ")), "prompt_tokens_details": {"cached_tokens": len(prompt[:cached].split(" ")) if cached else 0}}
        self.send_response(200)
        self.send_header("Content-Type", "text/event-stream")
        self.end_headers()
        for d in ({"choices": [{"delta": {"content": text}, "finish_reason": None}]}, {"choices": [{"delta": {}, "finish_reason": "length"}], "usage": usage}):
            self.wfile.write(f"data: {json.dumps(d)}\n\n".encode())
        self.wfile.write(b"data: [DONE]\n\n")


class Turns(unittest.TestCase):
    def setUp(self):
        self.http = ThreadingHTTPServer(("127.0.0.1", 0), Fake)
        threading.Thread(target=self.http.serve_forever, daemon=True).start()
        self.dir = tempfile.TemporaryDirectory()
        Fake.kept, Fake.resumed_differs = set(), False

    def tearDown(self):
        self.http.shutdown()
        self.http.server_close()
        self.dir.cleanup()

    def run_turns(self, restart: bool) -> dict:
        url = f"http://127.0.0.1:{self.http.server_address[1]}"
        t = config.Target("t", {"url": url, "model": "m", "cwd": self.dir.name,
                                "commands": {"up": f"curl -s -X POST {url}/restart"}, "session": {"health_wait": 10}}, {})
        return server.turns(t, {"rules": 3, "restart": restart}, Path(self.dir.name), "turns")

    def test_cold_after_a_restart_is_the_same_request(self):
        res = self.run_turns(restart=True)
        self.assertIs(res["ok"], True, res["summary"])
        self.assertIn("cold (after a restart): True", res["summary"])
        self.assertEqual(res["metrics"]["cached"]["turn3_cold"], 0)

    def test_a_padded_prompt_of_another_length_is_not_compared(self):
        res = self.run_turns(restart=False)
        self.assertIsNone(res["ok"], res["summary"])
        self.assertIn("not compared", res["summary"])
        self.assertTrue(res["metrics"]["again"])

    def test_a_resumed_reply_that_differs_from_cold_fails(self):
        Fake.resumed_differs = True
        res = self.run_turns(restart=True)
        self.assertIs(res["ok"], False, res["summary"])
        self.assertIn("cold (after a restart): False", res["summary"])


if __name__ == "__main__":
    unittest.main()
