import json
import tempfile
import unittest
from pathlib import Path

from harness import compare, config, export, scrub
from harness.checks import applies, engine, memory, recipe, thinking


def ruler(cells):
    return {"cells": [{"concurrency": c, "phase": p, "aggregate": a, "per_stream": a / c, "ttft": t} for c, p, a, t in cells]}


class Compare(unittest.TestCase):
    def test_slower_cell_and_worse_suite_are_regressions(self):
        with tempfile.TemporaryDirectory() as d:
            a, b = Path(d, "a"), Path(d, "b")
            for p, cells, passed in ((a, [(1, "prose", 100.0, 0.1)], 12), (b, [(1, "prose", 90.0, 0.1)], 11)):
                (p / "suite").mkdir(parents=True)
                (p / "ruler.json").write_text(json.dumps(ruler(cells)))
                (p / "suite" / "report.json").write_text(json.dumps({"results": [{"name": "drafts", "passed": passed, "cases": 12}]}))
            text, reg = compare.compare(a, b, 5)
            self.assertEqual(len(reg), 2)
            self.assertIn("-10.0%", text)

    def test_fresh_pairs_with_plain_ruler(self):
        with tempfile.TemporaryDirectory() as d:
            a, b = Path(d, "a"), Path(d, "b")
            a.mkdir(), b.mkdir()
            (a / "ruler.json").write_text(json.dumps(ruler([(1, "code", 100.0, 0.1)])))
            (b / "ruler-fresh.json").write_text(json.dumps(ruler([(1, "code", 99.0, 0.1)])))
            text, reg = compare.compare(a, b, 5)
            self.assertEqual(reg, [])
            self.assertIn("ruler -> ruler-fresh", text)


class Suite(unittest.TestCase):
    def verdict(self, results):
        with tempfile.TemporaryDirectory() as d:
            f = Path(d, "report.json")
            f.write_text(json.dumps({"results": results}))
            return recipe.suite_verdict(f)

    def test_soak_mismatch_fails(self):
        v = self.verdict([{"name": "drafts", "passed": 12, "cases": 12}, {"name": "soak", "passed": 0, "cases": 60}])
        self.assertIs(v["ok"], False)
        self.assertIn("not exact: soak", v["summary"])

    def test_scores_below_all_are_measured(self):
        v = self.verdict([{"name": "soak", "passed": 60, "cases": 60}, {"name": "gsm8k", "passed": 230, "cases": 250}])
        self.assertIsNone(v["ok"])


class Scrub(unittest.TestCase):
    def test_generic_patterns(self):
        with tempfile.TemporaryDirectory() as d:
            f = Path(d, "x.md")
            f.write_text("ok line\nlogs in /home/someone/x\nhost 192.168.1.4\nCo-Authored-By: a bot\n")
            self.assertEqual(len(scrub.scan_tree(Path(d))), 3)

    def test_binary_and_local_skipped(self):
        with tempfile.TemporaryDirectory() as d:
            Path(d, "k.cubin").write_bytes(b"/home/someone/")
            Path(d, "t.local.toml").write_text("/home/someone/")
            self.assertEqual(scrub.scan_tree(Path(d)), [])


class Targets(unittest.TestCase):
    def test_committed_targets_parse_and_expand(self):
        for name in ("qwen38-int4mixed", "glm53-m5", "qwen38-27b-5090"):
            raw = config._load(config.ROOT / "targets" / f"{name}.toml")
            t = config.Target(name, raw, {k: "X" for k in raw.get("vars", {})})
            for cmd in raw["commands"].values():
                t.expand(cmd, out="o", args="", concurrency="1", since="0")
            for item in raw.get("identity", []):
                t.expand(item["cmd"])

    def test_features_skip_checks(self):
        t = config.Target("g", {"url": "http://h", "features": {"sampling": False}, "commands": {}}, {})
        self.assertFalse(applies(t, "sampling", {}))
        self.assertFalse(applies(t, "suite", {}))
        self.assertTrue(applies(t, "turns", {}))
        self.assertTrue(applies(t, "structured_speed", {}))

    def test_unset_var_refused(self):
        t = config.Target("g", {"url": "http://h"}, {})
        with self.assertRaises(config.ConfigError):
            t.expand("ssh $mac true")


class Parsing(unittest.TestCase):
    def test_free_available(self):
        out = "              total used free shared buff/cache available\nMem: 100 50 10 1 40 " + str(48 * 2**30)
        self.assertEqual(memory._available_gib(out), 48.0)

    def test_answer(self):
        self.assertEqual(thinking._answer("so the total is 1,234.\nAnswer: 215"), 215)

    def test_ruler_table(self):
        cells = {(1, "prose"): {"aggregate": 69.1, "ttft": 0.08}, (1, "code"): {"aggregate": 110.0, "ttft": 0.09}}
        t = export.ruler_table(cells)
        self.assertIn("| 1 | 69.1 | 110.0 | - | - | 0.08-0.09 s |", t)


if __name__ == "__main__":
    unittest.main()


DONE = ("[tensorfold] done chatcmpl-1 prompt=35 cached=34 thinking=False effort=none tokens=256 sha=1ed1 finish=length "
        "rounds=55 accepted=200/259")


def engine_run(p: Path, per_stream: float, tokens_a_round: float):
    p.mkdir(parents=True)
    (p / "ruler.json").write_text(json.dumps(ruler([(16, "code", per_stream * 16, 0.6)])))
    lv = {"requests": 16, "tokens_a_round": tokens_a_round, "accept_rate": 0.82, "ms_a_round": round(1000 * tokens_a_round / per_stream, 2)}
    (p / "ruler.engine.json").write_text(json.dumps({"levels": {"16": lv}}))


class Engine(unittest.TestCase):
    def test_done_lines(self):
        reqs = engine.parse("noise\n" + DONE + "\n[tensorfold] 127.0.0.1 \"POST /v1/chat/completions HTTP/1.1\" 200 -\n" + DONE)
        self.assertEqual(len(reqs), 2)
        self.assertEqual(reqs[0], {"prompt": 35, "cached": 34, "tokens": 256, "rounds": 55, "accepted": 200, "proposed": 259})
        lv = engine.level(reqs, 30.0)
        self.assertAlmostEqual(lv["tokens_a_round"], 256 / 55, places=3)
        self.assertAlmostEqual(lv["ms_a_round"], 1000 * (256 / 55) / 30.0, places=1)
        self.assertEqual(engine.level([], 30.0), {"requests": 0})

    def test_slower_rounds_with_the_same_drafting_are_named(self):
        with tempfile.TemporaryDirectory() as d:
            a, b = Path(d, "a"), Path(d, "b")
            engine_run(a, 31.5, 4.4)
            engine_run(b, 29.0, 4.4)
            text, reg = compare.compare(a, b, 5)
            self.assertIn("rounds slower, same drafting", text)
            self.assertTrue(any("same tokens a round" in r for r in reg))

    def test_less_drafting_is_named(self):
        with tempfile.TemporaryDirectory() as d:
            a, b = Path(d, "a"), Path(d, "b")
            engine_run(a, 31.5, 4.4)
            engine_run(b, 27.0, 3.6)
            text, reg = compare.compare(a, b, 5)
            self.assertIn("less drafted", text)


class Stats(unittest.TestCase):
    def test_a_run_becomes_a_ledger_entry_and_reports(self):
        from harness import stats
        with tempfile.TemporaryDirectory() as d:
            run = Path(d, "20261015-171328-full")
            run.mkdir()
            cells = ruler([(1, "code", 127.0, 0.04), (16, "code", 509.8, 0.5)])["cells"]
            meta = {"target": "qwen38-int4mixed", "model": "m", "plan": "full", "started": "20261015-171328", "status": "done",
                    "identity": {"patch_sha": {"value": "186193c6", "exit": 0}},
                    "checks": [{"name": "ruler-fresh", "type": "ruler", "ok": None, "summary": "c=1 …"},
                               {"name": "memory-idle", "type": "memory", "ok": None, "summary": "free 96%\ntotal = 4096M | used"},
                               {"name": "suite", "type": "suite", "ok": None, "summary": "tools 60/60"}]}
            (run / "meta.json").write_text(json.dumps(meta))
            (run / "ruler-fresh.summary.json").write_text(json.dumps({"metrics": {"cells": cells, "engine": {"16": {"requests": 196, "tokens_a_round": 3.2, "accept_rate": 0.77, "ms_a_round": 122.6}}}}))
            (run / "suite.summary.json").write_text(json.dumps({"metrics": {"scores": {"tools": {"passed": 60, "cases": 60}}}}))
            e = stats.entry(run)
            self.assertEqual(e["identity"]["patch_sha"], "186193c6")
            self.assertEqual(e["rounds"]["ruler-fresh"]["16"]["requests"], 196)
            self.assertEqual(e["hardware"], "2x NVIDIA DGX Spark (GB10, 128 GB unified each), TP=2 over RoCE")
            old = stats.LEDGER
            stats.LEDGER = Path(d, "stats")
            try:
                stats.record(run, render_after=False)
                stats.record(run, render_after=False)  # the same run again replaces its entry
                book = json.loads((stats.LEDGER / "qwen38-int4mixed.json").read_text())
                self.assertEqual(len(book["runs"]), 1)
                md = stats.markdown()
                one = stats.target_markdown(book)
            finally:
                stats.LEDGER = old
            self.assertIn("Overview: by model and hardware", md)
            self.assertIn("509.8 (31.9)", md)
            self.assertIn("tools 60/60", md)
            # a summary's lines and pipes stay inside its cell
            self.assertIn("| memory-idle | measured: free 96%; total = 4096M \\| used |", md)
            self.assertIn("## 2026-10-15 17:13: run `20261015-171328-full`", one)
            self.assertIn("509.8 (31.9)", one)
            from harness import pdf as typeset
            doc = typeset.render(md, "Served stats", "2026-10-15 17:13 UTC")
            self.assertTrue(doc.startswith(b"%PDF-1.4") and doc.rstrip().endswith(b"%%EOF"))
            self.assertIn(b"/BaseFont /Helvetica-Bold", doc)
            self.assertIn(b"(Page 1 of ", doc)


class LeaderboardTest(unittest.TestCase):
    def test_publish_output_names_the_submission_and_its_url(self):
        from harness.leaderboard import parse
        out = "New submissions are community-reported and pending moderation.\nSubmission 6cbe0c3e-6e77: approved\nhttps://tensorfold.dev/benchmarks?result=6cbe0c3e-6e77\n"
        self.assertEqual(parse(out), {"submission": "6cbe0c3e-6e77", "status": "approved", "url": "https://tensorfold.dev/benchmarks?result=6cbe0c3e-6e77"})
        self.assertEqual(parse("error: token refused"), {"submission": None, "status": None, "url": None})

    def test_the_board_decides_the_suite(self):
        from harness.leaderboard import suite_args
        from harness.session import Abort
        self.assertEqual(suite_args(["community-v1"], "community-v1", ["community-v1"]), [])
        self.assertEqual(suite_args(["community-v1"], "community-v2", ["community-v1", "community-v2"]), ["--suite", "community-v1"])
        self.assertEqual(suite_args(["community-v2", "community-v1"], "community-v2", ["community-v1", "community-v2"]), [])
        with self.assertRaises(Abort):
            suite_args(["community-v1"], "community-v2", ["community-v2"])

    def test_a_target_without_a_leaderboard_section_is_refused(self):
        from harness.config import ConfigError, Target
        from harness.leaderboard import _settings
        with self.assertRaises(ConfigError):
            _settings(Target("x", {"url": "http://127.0.0.1:1"}))


class BringUp(unittest.TestCase):
    """A start counts only when the harness's own up succeeds and nothing else holds the URL."""

    def target(self, up: str, down: str = "true"):
        return config.Target("t", {"url": "http://127.0.0.1:1", "commands": {"up": up, "down": down},
                                   "session": {"up_retries": 1, "health_wait": 1, "down_wait": 1}}, {})

    def run_with(self, t, answers):
        from unittest import mock
        from harness import session
        with mock.patch.object(session.api, "healthy", side_effect=answers), mock.patch.object(session.time, "sleep"):
            session.bring_up(t)

    def test_an_up_that_fails_is_a_failed_start_even_when_the_url_answers(self):
        from harness.session import Abort
        with self.assertRaises(Abort):  # down leaves nothing; up fails; another run's server then answers
            self.run_with(self.target("exit 1"), [False, True, True, True])

    def test_a_server_still_answering_after_down_aborts(self):
        from harness.session import Abort
        with self.assertRaisesRegex(Abort, "still answers after down"):
            self.run_with(self.target("true"), lambda url: True)

    def test_a_clean_start(self):
        self.run_with(self.target("true"), [False, True])
