"""The recipe's own quality suite and decode ruler, run as the recipe runs them (its commands), read from their JSON."""

from __future__ import annotations

import json
import time
from pathlib import Path

from ..config import Target
from . import engine


def _sh(target, cmd, **extra):
    from ..session import sh
    return sh(target, cmd, **extra)


def suite_results(report: Path) -> list[dict]:
    d = json.loads(report.read_text())
    return d.get("results", d if isinstance(d, list) else [])


def suite(target: Target, spec: dict, run_dir: Path, name: str) -> dict:
    """``commands.suite`` with $out (this check's folder) and $args (the plan's, e.g. ``--only drafts concurrent``)."""
    out = run_dir / name
    rc, text = _sh(target, target["commands"]["suite"], timeout=spec.get("timeout", 4 * 3600), out=out, args=spec.get("args", ""))
    (run_dir / f"{name}.log").write_text(text)
    report = out / "report.json"
    if not report.is_file():
        return {"ok": False, "summary": f"no report (exit {rc}): {text.strip().splitlines()[-1:] or ''}", "metrics": {}}
    return suite_verdict(report, spec.get("args", ""))


# checks whose every case must pass: replies equal drafted and undrafted, alone and beside others, and resuming kept
# states under load (soak: the recipe's AGENTS.md requires it before an engine change ships)
EXACT = ("drafts", "concurrent", "soak")


def suite_verdict(report: Path, args: str = "") -> dict:
    scores, broken = {}, []
    for r in suite_results(report):
        scores[r["name"]] = {"passed": r.get("passed"), "cases": r.get("cases"), "score": r.get("score")}
        if not r.get("cases"):
            broken.append(r["name"])
    summary = ", ".join(f"{k} {v['passed']}/{v['cases']}" for k, v in scores.items())
    if broken:
        summary = f"no cases (errors) in {', '.join(broken)}; " + summary
    exact = [k for k in EXACT if k in scores and scores[k]["passed"] != scores[k]["cases"]]
    if exact:
        summary = f"not exact: {', '.join(exact)}; " + summary
    ok = False if broken or exact else None
    return {"ok": ok, "summary": summary, "metrics": {"scores": scores, "thinking_args": args}}


def ruler_cells(path: Path) -> list[dict]:
    d = json.loads(path.read_text())
    return d.get("cells", [])


def _levels_with_logs(target: Target, spec: dict, run_dir: Path, name: str, levels: list[int]) -> tuple[int, str, dict[int, dict]]:
    """The ruler one level at a time, each level's server log read after it; its cells merged into $out."""
    out = run_dir / f"{name}.json"
    merged: dict | None = None
    texts, done, rc = [], {}, 0
    for n in levels:
        part = run_dir / f"{name}.c{n}.json"
        since = int(time.time()) - 1
        rc, text = _sh(target, target["commands"]["ruler"], timeout=spec.get("timeout", 3 * 3600), out=part, concurrency=str(n),
                       args=spec.get("args", ""))
        texts.append(text)
        _, log = _sh(target, target["commands"]["server_log"], timeout=120, since=str(since))
        done[n] = engine.parse(log)
        if part.is_file():
            j = json.loads(part.read_text())
            if merged is None:
                merged = j
            else:
                merged["cells"] = merged.get("cells", []) + j.get("cells", [])
            part.unlink()
    if merged is not None:
        out.write_text(json.dumps(merged, indent=1))
    return rc, "\n".join(texts), done


def ruler(target: Target, spec: dict, run_dir: Path, name: str) -> dict:
    """``commands.ruler`` with $out (this check's JSON), $concurrency (space-separated) and $args. With
    ``commands.server_log`` each level runs on its own and the engine's round counters for it go in <name>.engine.json."""
    out = run_dir / f"{name}.json"
    most = target.feature("max_concurrency", None)
    levels = [c for c in spec.get("concurrency", [1]) if most is None or c <= most] or [1]
    done: dict[int, list[dict]] = {}
    if "server_log" in target.section("commands"):
        rc, text, done = _levels_with_logs(target, spec, run_dir, name, levels)
    else:
        conc = " ".join(str(c) for c in levels)
        rc, text = _sh(target, target["commands"]["ruler"], timeout=spec.get("timeout", 3 * 3600), out=out, concurrency=conc,
                       args=spec.get("args", ""))
    (run_dir / f"{name}.log").write_text(text)
    if not out.is_file():
        return {"ok": False, "summary": f"no ruler JSON (exit {rc})", "metrics": {}}
    cells = ruler_cells(out)
    rows: dict[int, dict] = {}
    for c in cells:
        rows.setdefault(c["concurrency"], {})[c["phase"]] = c
    empty = [f"c={c['concurrency']} {c['phase']}" for c in cells if not c.get("aggregate")]
    parts = []
    for n, phases in sorted(rows.items()):
        rates = "/".join(f"{p['aggregate']:.1f}" if p.get("aggregate") else "-" for p in phases.values())
        ttfts = [p["ttft"] for p in phases.values() if p.get("ttft")]
        parts.append(f"c={n} {rates}" + (f" ttft {min(ttfts):.2f}-{max(ttfts):.2f}s" if ttfts else ""))
    metrics = {"cells": [{k: c.get(k) for k in ("concurrency", "phase", "per_stream", "aggregate", "ttft")} for c in cells]}
    line = ("no replies: " + ", ".join(empty) + "; " if empty else "") + "; ".join(parts)
    if done:
        stats = {}
        for n, reqs in done.items():
            rates = [p["per_stream"] for p in rows.get(n, {}).values() if p.get("per_stream")]
            stats[n] = engine.level(reqs, sum(rates) / len(rates) if rates else None)
        (run_dir / f"{name}.engine.json").write_text(json.dumps({"levels": {str(n): s for n, s in stats.items()}}, indent=1))
        metrics["engine"] = {str(n): s for n, s in stats.items()}
        line += "; engine: " + engine.summary(stats)
    return {"ok": False if empty else None, "summary": line, "metrics": metrics}
