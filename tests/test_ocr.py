import json
import tempfile
import unittest
from pathlib import Path
from unittest import mock

from harness import config
from harness.checks import ocr

PAGE_1 = "<PAGE><BLOCK>title<LEVEL1>[89, 64, 411, 91]<FORK>1. Report\n<BLOCK>text[88, 108, 682, 174]<FORK>Revenue rose.\n"
PAGE_2 = "<PAGE><BLOCK>text[88, 108, 682, 173]<FORK>Outlook steady.\n"


def target(d: Path) -> config.Target:
    return config.Target("t", {"url": "http://h", "model": "m"}, {"ocr_dir": str(d)})


def folder(d: Path, refs: dict[str, str]) -> None:
    (d / "pages").mkdir()
    (d / "refs").mkdir()
    for p in ("a", "b"):
        (d / "pages" / f"{p}.png").write_bytes(b"\x89PNG fake " + p.encode())
    for name, text in refs.items():
        (d / "refs" / f"{name}.txt").write_text(text)


def server(replies):
    """api.stream's stand-in: the reply for the pages a request carries, from `replies` (pages count -> text or a list)."""
    calls = []

    def stream(url, model, messages, timeout=None, **extra):
        n = sum(1 for c in messages[0]["content"] if c["type"] == "image_url")
        calls.append(n)
        r = replies[n]
        text = r.pop(0) if isinstance(r, list) else r
        return {"status": 200, "text": text, "ttft": 0.5, "s": 1.5, "finish": "stop",
                "usage": {"prompt_tokens": 909 * n, "completion_tokens": 101}}
    return stream, calls


class Boxes(unittest.TestCase):
    def test_text_alone_and_how_far_boxes_moved(self):
        b = ocr._boxes("x[1, 2, 3, 4]y[5, 6, 7, 8]", "x[1, 2, 3, 6]y[5, 6, 7, 8]")
        self.assertEqual(b, {"text_identical": True, "boxes": [2, 2], "coords_moved": 1, "coords": 8, "coord_max_move": 2})
        self.assertFalse(ocr._boxes("x[1, 2, 3, 4]y", "z[1, 2, 3, 4]y")["text_identical"])


class Check(unittest.TestCase):
    spec = {"streams": 2, "cases": [{"name": "one", "pages": ["a"]}, {"name": "doc", "pages": ["a", "b"]}]}

    def test_pages_answered_like_the_reference(self):
        with tempfile.TemporaryDirectory() as d:
            d = Path(d)
            moved = PAGE_1.replace("[88, 108, 682, 174]", "[88, 109, 682, 174]")
            folder(d, {"one": PAGE_1, "doc": PAGE_1 + PAGE_2})
            stream, calls = server({1: moved, 2: PAGE_1 + PAGE_2})
            with mock.patch.object(ocr.api, "stream", stream):
                res = ocr.run(target(d), self.spec, d, "ocr")
            self.assertTrue(res["ok"], res["summary"])
            self.assertEqual(calls, [1, 1, 1, 1, 2, 2, 2, 2])  # each case: once, again, then 2 at once
            one, doc = res["metrics"]["cases"]["one"], res["metrics"]["cases"]["doc"]
            self.assertEqual(doc["page_marks"], 2)
            self.assertTrue(doc["reference_identical"])
            self.assertFalse(one["reference_identical"])
            self.assertEqual(one["reference_boxes"]["coords_moved"], 1)
            self.assertEqual(one["decode_tps"], 100.0)  # 100 tokens after the first, over 1.0 s
            self.assertIn("identical 1/2", res["summary"])
            self.assertIn("text without boxes identical 2/2, box coords moved 1/20 (at most 1)", res["summary"])
            self.assertTrue((d / "ocr.json").exists())

    def test_a_missing_page_a_changed_repeat_and_a_failed_request_fail(self):
        with tempfile.TemporaryDirectory() as d:
            d = Path(d)
            folder(d, {})
            stream, _ = server({1: [PAGE_1, PAGE_2, PAGE_1, PAGE_1], 2: PAGE_1})
            with mock.patch.object(ocr.api, "stream", stream):
                res = ocr.run(target(d), self.spec, d, "ocr")
            self.assertFalse(res["ok"])
            self.assertIn("one: a second run differs", res["summary"])
            self.assertIn("doc: 1 page markers for 2 pages", res["summary"])
            refused = lambda *a, **k: {"status": 500, "error": "boom"}
            with mock.patch.object(ocr.api, "stream", refused):
                res = ocr.run(target(d), {"cases": [{"name": "one", "pages": ["a"]}]}, d, "ocr")
            self.assertFalse(res["ok"])
            self.assertIn("one: status 500", res["summary"])


class Report(unittest.TestCase):
    def test_a_run_with_only_an_ocr_check_is_shown(self):
        from harness import stats
        with tempfile.TemporaryDirectory() as d:
            run = Path(d, "20261103-152737-ocr")
            run.mkdir()
            meta = {"target": "unlimited-ocr-2-m5", "model": "m", "plan": "ocr", "started": "20261103-152737", "status": "done",
                    "identity": {}, "checks": [{"name": "ocr", "type": "ocr", "ok": True, "summary": "6/6 cases answered"}]}
            (run / "meta.json").write_text(json.dumps(meta))
            old = stats.LEDGER
            stats.LEDGER = Path(d, "stats")
            try:
                stats.record(run, render_after=False)
                md = stats.markdown()
            finally:
                stats.LEDGER = old
            self.assertIn("## Unlimited-OCR-2, bf16 on 1x Apple M5 Ultra", md)
            self.assertIn("| ocr | pass: 6/6 cases answered |", md)


class Target(unittest.TestCase):
    def test_the_target_and_plan_load(self):
        raw = config._load(config.ROOT / "targets" / "unlimited-ocr-2-m5.toml")
        t = config.Target("unlimited-ocr-2-m5", raw, {k: "X" for k in raw.get("vars", {})})
        for cmd in raw["commands"].values():
            t.expand(cmd, since="0")
        for item in raw.get("identity", []):
            t.expand(item["cmd"])
        plan = config.load_plan("ocr")
        self.assertEqual([c["type"] for c in plan["checks"]], ["memory", "ocr", "memory"])


if __name__ == "__main__":
    unittest.main()
