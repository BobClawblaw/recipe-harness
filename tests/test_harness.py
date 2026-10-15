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
