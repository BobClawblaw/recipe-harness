"""The agentic check against a fake OpenAI server playing the agent: one that follows the trail to the live value, one
that keeps asking for the same read (#847's failure), one that answers with a superseded value, one that stops calling
tools, and one that reads each module twice (allowed)."""

import json
import re
import tempfile
import threading
import unittest
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path

from harness import config
from harness.checks import agentic


class Fake(BaseHTTPRequestHandler):
    mode = "good"  # good | loop | early | silent | twice

    def log_message(self, *a):
        pass

    def reply(self, msg, finish):
        prompt = sum(len(m.get("content") or "") for m in self.body["messages"]) // 3
        raw = json.dumps({"choices": [{"message": msg, "finish_reason": finish}],
                          "usage": {"prompt_tokens": prompt, "completion_tokens": 20}}).encode()
        self.send_response(200)
        self.send_header("Content-Type", "application/json")
        self.send_header("Content-Length", str(len(raw)))
        self.end_headers()
        self.wfile.write(raw)

    def call(self, name, **args):
        n = len(self.body["messages"])
        msg = {"role": "assistant", "content": "", "tool_calls": [
            {"id": f"c{n}", "type": "function", "function": {"name": name, "arguments": json.dumps(args)}}]}
        self.reply(msg, "tool_calls")

    def do_GET(self):
        raw = json.dumps({"data": [{"id": "m"}]}).encode()
        self.send_response(200)
        self.send_header("Content-Length", str(len(raw)))
        self.end_headers()
        self.wfile.write(raw)

    def do_POST(self):
        self.body = json.loads(self.rfile.read(int(self.headers["Content-Length"])))
        msgs = self.body["messages"]
        tools = [m for m in msgs if m["role"] == "tool"]
        if self.mode == "silent":
            return self.reply({"role": "assistant", "content": "I think it is probably 5."}, "stop")
        if self.mode == "loop" or not tools:
            return self.call("read_file", path="app/main.py")
        last = tools[-1]["content"]
        live = re.search(r"RETRY_LIMIT = (\d+)  # live", last)
        if live:
            return self.call("submit_answer", value=int(live.group(1)))
        old = re.search(r"RETRY_LIMIT = (\d+)  # superseded: the live value moved to (\S+)", last)
        if self.mode == "early" and old:
            return self.call("submit_answer", value=int(old.group(1)))
        nxt = old.group(2) if old else re.search(r"see (\S+\.py)", last).group(1)
        if self.mode == "twice" and len(tools) % 2:
            prev = [m for m in msgs if m["role"] == "assistant" and m.get("tool_calls")][-1]
            return self.call("read_file", path=json.loads(prev["tool_calls"][0]["function"]["arguments"])["path"])
        self.call("read_file", path=nxt)


class Agentic(unittest.TestCase):
    def setUp(self):
        self.http = ThreadingHTTPServer(("127.0.0.1", 0), Fake)
        threading.Thread(target=self.http.serve_forever, daemon=True).start()
        self.dir = tempfile.TemporaryDirectory()
        self.target = config.Target("t", {"url": f"http://127.0.0.1:{self.http.server_address[1]}", "model": "m"}, {"context": "8192"})

    def tearDown(self):
        self.http.shutdown()
        self.http.server_close()
        self.dir.cleanup()
        Fake.mode = "good"

    def run_check(self, mode, **spec):
        Fake.mode = mode
        return agentic.run(self.target, {"file_tokens": 400, **spec}, Path(self.dir.name), "a")

    def test_follows_the_trail(self):
        r = self.run_check("good")
        self.assertTrue(r["ok"], r["summary"])
        m = r["metrics"]
        self.assertEqual(m["trail_read"], m["hops"])
        self.assertEqual(m["repeat_reads"], 0)
        self.assertEqual(m["hops"], (int(8192 * 0.8) - 1024) // 400)  # the target's whole window by default
        saved = json.loads((Path(self.dir.name) / "a.json").read_text())
        self.assertEqual(saved["answer"], saved["want"])

    def test_same_read_again_and_again_is_a_loop(self):
        r = self.run_check("loop")
        self.assertFalse(r["ok"])
        self.assertIn("identical replies in a row", r["summary"])

    def test_reads_past_max_reads_fail_without_identical_replies(self):
        r = self.run_check("loop", loop=100)
        self.assertFalse(r["ok"])
        self.assertIn("app/main.py 4 times", r["summary"])

    def test_a_superseded_value_is_wrong(self):
        r = self.run_check("early")
        self.assertFalse(r["ok"])
        self.assertIn("the live value is", r["summary"])

    def test_no_tool_calls(self):
        r = self.run_check("silent")
        self.assertFalse(r["ok"])
        self.assertIn("identical replies in a row", r["summary"])  # the same text each time is a loop first
        r = self.run_check("silent", loop=100)
        self.assertIn("4 replies called no tool", r["summary"])

    def test_one_reread_each_is_allowed(self):
        r = self.run_check("twice")
        self.assertTrue(r["ok"], r["summary"])
        self.assertEqual(r["metrics"]["repeat_reads"], r["metrics"]["hops"])

    def test_window(self):
        def hops(target, **spec):
            return agentic.run(target, {"file_tokens": 400, **spec}, Path(self.dir.name), "w")["metrics"]["hops"]
        Fake.mode = "good"
        self.assertEqual(hops(self.target, context=4096), (int(4096 * 0.8) - 1024) // 400)  # the plan caps it
        self.assertEqual(hops(self.target, context=65536), (int(8192 * 0.8) - 1024) // 400)  # never past the target's
        bare = config.Target("t", {"url": self.target.url, "model": "m"}, {})
        self.assertEqual(hops(bare, hops=3), 3)

    def test_thinking_on_skips_a_target_without_thinking(self):
        from harness.checks import applies, skip_reason
        off = config.Target("t", {"url": "http://x", "features": {"thinking": False}}, {})
        self.assertTrue(applies(off, "agentic", {}))
        self.assertFalse(applies(off, "agentic", {"thinking": True}))
        self.assertIn("features.thinking = false", skip_reason(off, "agentic"))
        self.assertTrue(applies(self.target, "agentic", {"thinking": True}))

    def test_the_same_task_for_every_target(self):
        a = agentic.workspace("s-5-400", 5, 400)
        self.assertEqual(a, agentic.workspace("s-5-400", 5, 400))
        files, trail, want = a
        self.assertEqual(len(trail), 6)
        self.assertIn(f"RETRY_LIMIT = {want}  # live", files[trail[-1]])
        for here, there in zip(trail[1:], trail[2:]):
            self.assertIn(f"moved to {there}", files[here])


if __name__ == "__main__":
    unittest.main()
