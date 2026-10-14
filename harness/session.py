"""One run: the lock, the recipe down and up (with retries), its identity, the plan's checks, the recipe left up."""

from __future__ import annotations

import json
import os
import subprocess
import time
from pathlib import Path

from . import api, checks
from .config import ROOT, Target
from .log import log, to, warn


class Abort(Exception):
    """The server died or never came up: the run stops and records nothing more."""


def sh(target: Target, cmd: str, timeout: float | None = None, **extra) -> tuple[int, str]:
    """A target command (expanded) in the target's cwd: exit code and combined output."""
    cmd = target.expand(cmd, **extra)
    try:
        p = subprocess.run(cmd, shell=True, cwd=target.cwd, capture_output=True, text=True, timeout=timeout)
        return p.returncode, (p.stdout + p.stderr)
    except subprocess.TimeoutExpired as e:
        out = (e.stdout or b"").decode(errors="replace") if isinstance(e.stdout, bytes) else (e.stdout or "")
        return 124, out + f"\n(timed out after {timeout}s)"


def tail(text: str, n: int = 6) -> str:
    return "\n".join(l for l in text.strip().splitlines()[-n:])


def _lock(fd, block: bool) -> None:
    """An exclusive lock on an open file: flock on POSIX, msvcrt's byte lock on Windows (BlockingIOError if held)."""
    if os.name == "nt":
        import msvcrt
        fd.seek(0)
        while True:
            try:
                msvcrt.locking(fd.fileno(), msvcrt.LK_NBLCK, 1)
                return
            except OSError:
                if not block:
                    raise BlockingIOError from None
                time.sleep(1)
    import fcntl
    fcntl.flock(fd, fcntl.LOCK_EX | (0 if block else fcntl.LOCK_NB))


def _unlock(fd) -> None:
    if os.name == "nt":
        import msvcrt
        fd.seek(0)
        msvcrt.locking(fd.fileno(), msvcrt.LK_UNLCK, 1)
        return
    import fcntl
    fcntl.flock(fd, fcntl.LOCK_UN)


class Lock:
    """An exclusive lock on the target's lock file (shared with every other GPU job on the machines), or nothing."""

    def __init__(self, path: str | None):
        self.path = os.path.expanduser(path) if path else None
        self.fd = None

    def __enter__(self):
        if self.path:
            Path(self.path).parent.mkdir(parents=True, exist_ok=True)
            self.fd = open(self.path, "a+")
            try:
                _lock(self.fd, block=False)
            except BlockingIOError:
                log(f"waiting for the lock {self.path}")
                _lock(self.fd, block=True)
            log(f"lock taken: {self.path}")
        return self

    def __exit__(self, *exc):
        if self.fd:
            _unlock(self.fd)
            self.fd.close()
            log("lock released")


def wait_healthy(target: Target, seconds: float) -> bool:
    end = time.time() + seconds
    while time.time() < end:
        if api.healthy(target.url):
            return True
        time.sleep(5)
    return False


def bring_up(target: Target) -> None:
    """down, then up until healthy: ``up_retries`` tries, ``retry_wait`` seconds between (after a failed start)."""
    s, c = target.section("session"), target.section("commands")
    tries, wait = int(s.get("up_retries", 1)), float(s.get("retry_wait", 0))
    for i in range(1, tries + 1):
        if "down" in c:
            rc, out = sh(target, c["down"], timeout=s.get("down_timeout", 600))
            log(f"down (exit {rc}): {tail(out, 1)}")
        if i > 1 and wait:
            log(f"waiting {wait:.0f}s before start {i}")
            time.sleep(wait)
        rc, out = sh(target, c["up"], timeout=s.get("up_timeout", 3600))
        log(f"up {i}/{tries} (exit {rc}): {tail(out, 2)}")
        if wait_healthy(target, s.get("health_wait", 120)):
            log(f"healthy: {target.url}")
            return
        if "diagnose" in c:
            _, d = sh(target, c["diagnose"], timeout=60)
            log(f"start {i} failed: {tail(d, 4) or '(no diagnostics)'}")
    raise Abort(f"{target.name} never came up after {tries} starts")


def identity(target: Target) -> dict:
    """Each [[identity]] command's output; with ``expect``, a command whose output must match, or the run aborts."""
    out = {}
    for item in target.get("identity", []):
        rc, got = sh(target, item["cmd"], timeout=120)
        got = got.strip()
        rec = {"value": got, "exit": rc}
        if "expect" in item:
            _, want = sh(target, item["expect"], timeout=120)
            rec["expected"] = want.strip()
            if rec["expected"] != got:
                raise Abort(f"identity {item['name']}: serving {got!r}, expected {rec['expected']!r}")
        out[item["name"]] = rec
        log(f"identity {item['name']}: {got[:120]}")
    return out


def run(target: Target, plan: dict, plan_name: str, out_root: Path | None = None, restart: bool | None = None) -> Path:
    stamp = time.strftime("%Y%m%d-%H%M%S")
    run_dir = (out_root or ROOT / "runs" / target.name) / f"{stamp}-{plan_name}"
    run_dir.mkdir(parents=True, exist_ok=True)
    to(run_dir / "run.log")
    meta = {"target": target.name, "plan": plan_name, "url": target.url, "model": target.model, "started": stamp,
            "status": "running", "checks": []}
    write = lambda: (run_dir / "meta.json").write_text(json.dumps(meta, indent=1))
    write()
    restart = plan.get("restart", True) if restart is None else restart
    log(f"run {run_dir.name}: target {target.name}, plan {plan_name}, restart {restart}")
    with Lock(target.section("session").get("lock")):
        try:
            if restart:
                bring_up(target)
            elif not api.healthy(target.url):
                raise Abort(f"{target.url} is not healthy and the plan does not restart it")
            meta["identity"] = identity(target)
            write()
            for spec in plan["checks"]:
                kind = spec["type"]
                name = spec.get("name", kind + (f"-{spec['label']}" if "label" in spec else ""))
                if not checks.applies(target, kind, spec):
                    log(f"skip {name}: the target does not serve it")
                    meta["checks"].append({"name": name, "skipped": True})
                    continue
                log(f"check {name}")
                t0 = time.time()
                res = checks.run(kind, target, spec, run_dir, name)
                res.update(name=name, type=kind, seconds=round(time.time() - t0, 1))
                if not api.healthy(target.url):
                    (run_dir / f"{name}.json").unlink(missing_ok=True)
                    raise Abort(f"the server died during {name}; its result is discarded")
                (run_dir / f"{name}.summary.json").write_text(json.dumps(res, indent=1))
                meta["checks"].append({k: res[k] for k in ("name", "type", "ok", "summary", "seconds")})
                log(f"{'PASS' if res['ok'] else 'FAIL' if res['ok'] is False else 'DONE'} {name}: {res['summary']}")
                write()
            meta["status"] = "done"
        except Abort as e:
            meta["status"] = f"aborted: {e}"
            warn(str(e))
            if target.section("session").get("leave_up", True) and not api.healthy(target.url):
                try:
                    bring_up(target)
                except Abort as e2:
                    warn(f"could not leave the recipe up: {e2}")
        finally:
            meta["finished"] = time.strftime("%Y%m%d-%H%M%S")
            write()
    log(f"run {meta['status']}: {run_dir}")
    to(None)
    return run_dir
