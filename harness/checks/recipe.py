"""The recipe's own quality suite and decode ruler, run as the recipe runs them (its commands), read from their JSON."""

from __future__ import annotations

import json
from pathlib import Path

from ..config import Target


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
    scores, broken = {}, []
    for r in suite_results(report):
        scores[r["name"]] = {"passed": r.get("passed"), "cases": r.get("cases"), "score": r.get("score")}
        if not r.get("cases"):
            broken.append(r["name"])
    summary = ", ".join(f"{k} {v['passed']}/{v['cases']}" for k, v in scores.items())
    if broken:
        summary = f"no cases (errors) in {', '.join(broken)}; " + summary
    exact = [k for k in ("drafts", "concurrent") if k in scores and scores[k]["passed"] != scores[k]["cases"]]
    ok = False if broken or exact else None
    return {"ok": ok, "summary": summary, "metrics": {"scores": scores, "thinking_args": spec.get("args", "")}}


def ruler_cells(path: Path) -> list[dict]:
    d = json.loads(path.read_text())
    return d.get("cells", [])


def ruler(target: Target, spec: dict, run_dir: Path, name: str) -> dict:
    """``commands.ruler`` with $out (this check's JSON), $concurrency (space-separated) and $args."""
    out = run_dir / f"{name}.json"
    conc = " ".join(str(c) for c in spec.get("concurrency", [1]))
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
    return {"ok": False if empty else None, "summary": ("no replies: " + ", ".join(empty) + "; " if empty else "") + "; ".join(parts),
            "metrics": {"cells": [{k: c.get(k) for k in ("concurrency", "phase", "per_stream", "aggregate", "ttft")} for c in cells]}}
