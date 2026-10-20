"""The TensorFold leaderboard: the recipe down, `tensorfold benchmark` on its public checkpoint in the suite the board
accepts (its /suites listing decides), the recipe back up, the receipt scrubbed, then published with the stored
contributor login."""

from __future__ import annotations

import json
import os
import re
import subprocess
import time
import urllib.request
from pathlib import Path

from . import api
from .config import ROOT, ConfigError, Target
from .log import log, to, warn
from .scrub import scan_tree
from .session import Abort, Lock, bring_up, sh, tail

URL = re.compile(r"https://\S+/benchmarks\?result=[0-9a-f-]+")
SUBMISSION = re.compile(r"Submission (\S+): (\w+)")
BOARD = "https://tensorfold.dev/api/benchmarks/v1"


def _settings(target: Target) -> dict:
    b = target.section("leaderboard")
    for key in ("model", "binary"):
        if key not in b:
            raise ConfigError(f"{target.name}: [leaderboard] needs `{key}` (the public checkpoint ID and the engine binary)")
    return b


def _env(target: Target, b: dict) -> dict:
    env = dict(os.environ)
    for k, v in b.get("env", {}).items():
        env[k] = os.path.expanduser(target.expand(str(v)))
    return env


def _wait_free(target: Target, b: dict) -> None:
    """The recipe's devices released: [leaderboard] free (a command that exits 0 once they are) polled for a while."""
    cmd = b.get("free")
    if not cmd:
        return
    end = time.time() + float(b.get("free_wait", 120))
    while time.time() < end:
        if sh(target, cmd, timeout=60)[0] == 0:
            return
        time.sleep(2)
    raise Abort(f"{target.name}: the devices were not free {b.get('free_wait', 120)}s after down")


def board_suites(b: dict) -> list[str]:
    """The suites the board accepts, as its /suites lists them ([leaderboard] upload_url, else tensorfold.dev)."""
    req = urllib.request.Request(f"{b.get('upload_url', BOARD).rstrip('/')}/suites", headers={"User-Agent": "recipe-harness"})
    with urllib.request.urlopen(req, timeout=30) as r:  # the board refuses urllib's own agent
        return [s["id"] for s in json.loads(r.read())["suites"]]


def binary_suites(target: Target, b: dict) -> tuple[str, list[str]]:
    """The suite the engine runs by default (`benchmark suites`), and the ones `--suite` can choose (its help)."""
    binary = os.path.expanduser(target.expand(b["binary"]))
    env = _env(target, b)
    default = json.loads(subprocess.run([binary, "benchmark", "suites"], env=env, capture_output=True, text=True, timeout=60).stdout)["id"]
    helptext = subprocess.run([binary, "benchmark", "--help"], env=env, capture_output=True, text=True, timeout=60).stdout
    lines = " ".join(l for l in helptext.splitlines() if l.strip().startswith("--suite "))
    return default, sorted(set(re.findall(r"community-v\d+", lines)) | {default})


def suite_args(accepted: list[str], default: str, runs: list[str]) -> list[str]:
    """The flags that run the board's suite: none when it takes the engine's default, else --suite with the first suite
    the board lists that the engine runs. The board is authoritative: with no suite in common, nothing runs."""
    if default in accepted:
        return []
    for s in accepted:
        if s in runs:
            return ["--suite", s]
    raise Abort(f"the board accepts {', '.join(accepted) or 'no suite'}; this engine runs {', '.join(runs)}")


def benchmark(target: Target, out: Path, suite: list[str] = ()) -> tuple[int, str]:
    """Stop the recipe, run the board's suite with the target's engine, and start the recipe again whatever happens."""
    b = _settings(target)
    c = target.section("commands")
    binary = os.path.expanduser(target.expand(b["binary"]))
    cmd = [binary, "benchmark", target.expand(b["model"]), "--output", str(out)] + list(suite) + target.expand(b.get("args", "")).split()
    if "down" in c:
        rc, o = sh(target, c["down"], timeout=target.section("session").get("down_timeout", 600))
        log(f"down (exit {rc}): {tail(o, 1)}")
    try:
        _wait_free(target, b)
        log("benchmark: " + " ".join(cmd))
        p = subprocess.run(cmd, cwd=target.cwd, env=_env(target, b), capture_output=True, text=True, timeout=float(b.get("timeout", 7200)))
        return p.returncode, p.stdout + p.stderr
    finally:
        if target.section("session").get("leave_up", True):
            try:
                bring_up(target)
            except Abort as e:
                warn(f"could not bring the recipe back up: {e}")


def publish(target: Target, receipt: Path) -> dict:
    """`benchmark publish --yes` with the CLI's stored login (or TENSORFOLD_BENCHMARK_TOKEN); the board's answer."""
    b = _settings(target)
    p = subprocess.run([os.path.expanduser(target.expand(b["binary"])), "benchmark", "publish", str(receipt), "--yes"], env=_env(target, b),
                       capture_output=True, text=True, timeout=600)
    out = p.stdout + p.stderr
    return {**parse(out), "exit": p.returncode, "output": tail(out, 4)}


def parse(out: str) -> dict:
    """The board's answer in `benchmark publish` output: the submission, its status and the public URL."""
    sub = SUBMISSION.search(out)
    url = URL.search(out)
    return {"submission": sub.group(1) if sub else None, "status": sub.group(2) if sub else None, "url": url.group(0) if url else None}


def run(target: Target, publish_it: bool = True) -> Path:
    stamp = time.strftime("%Y%m%d-%H%M%S")
    run_dir = ROOT / "runs" / target.name / f"{stamp}-leaderboard"
    run_dir.mkdir(parents=True, exist_ok=True)
    to(run_dir / "run.log")
    receipt = run_dir / "receipt.json"
    meta = {"target": target.name, "plan": "leaderboard", "started": stamp, "status": "running"}
    write = lambda: (run_dir / "meta.json").write_text(json.dumps(meta, indent=1))
    write()
    try:
        b = _settings(target)
        accepted = board_suites(b)
        default, runs = binary_suites(target, b)
        suite = suite_args(accepted, default, runs)
        meta["suite"] = suite[1] if suite else default
        log(f"the board accepts {', '.join(accepted)}; running {meta['suite']}")
        with Lock(target.section("session").get("lock")):
            rc, out = benchmark(target, receipt, suite)
        (run_dir / "benchmark.log").write_text(out)
        log(tail(out, 8))
        meta["benchmark_exit"] = rc
        if rc != 0 or not receipt.is_file():
            raise Abort(f"the benchmark did not complete (exit {rc}); nothing published")
        hits = scan_tree(receipt)
        if hits:
            raise Abort("the receipt has personal or machine details; nothing published:\n" + "\n".join(hits))
        if publish_it:
            meta["publish"] = publish(target, receipt)
            log(f"published: {meta['publish']['status']} {meta['publish']['url']}")
            if meta["publish"]["exit"] != 0:
                raise Abort(f"publish failed: {meta['publish']['output']}")
        meta["status"] = "done"
    except Abort as e:
        meta["status"] = f"aborted: {e}"
        warn(str(e))
    finally:
        meta["finished"] = time.strftime("%Y%m%d-%H%M%S")
        write()
    log(f"leaderboard {meta['status']}: {run_dir}")
    to(None)
    if not api.healthy(target.url):
        warn(f"{target.url} is not healthy after the leaderboard run")
    return run_dir
