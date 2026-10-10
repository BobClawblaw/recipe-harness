"""Two runs (or evidence folders) side by side: suite scores, ruler tok/s and first-token time, server checks."""

from __future__ import annotations

import json
from pathlib import Path

RULER_ALIASES = {"ruler-fresh": ["ruler-fresh", "ruler"], "ruler-after": ["ruler-after"], "ruler": ["ruler", "ruler-fresh"]}


def _json(p: Path):
    try:
        return json.loads(p.read_text())
    except (OSError, ValueError):
        return None


def rulers(d: Path) -> dict[str, dict]:
    out = {}
    for p in sorted(d.glob("ruler*.json")):
        if p.name.endswith(".summary.json"):
            continue
        j = _json(p)
        if isinstance(j, dict) and "cells" in j:
            out[p.stem] = {(c["concurrency"], c["phase"]): c for c in j["cells"]}
    return out


def suites(d: Path) -> dict[str, dict]:
    out = {}
    for rep in sorted(d.glob("**/report.json")):
        j = _json(rep)
        if isinstance(j, dict) and "results" in j:
            out[str(rep.parent.relative_to(d))] = {r["name"]: r for r in j["results"]}
    return out


def summaries(d: Path) -> dict[str, dict]:
    return {p.name[: -len(".summary.json")]: _json(p) for p in sorted(d.glob("*.summary.json"))}


def _pair(a: dict, b: dict, key: str) -> tuple[str | None, str | None]:
    for k in RULER_ALIASES.get(key, [key]):
        if k in a:
            for k2 in RULER_ALIASES.get(key, [key]):
                if k2 in b:
                    return k, k2
    return None, None


def compare(a: Path, b: Path, threshold: float = 5.0) -> tuple[str, list[str]]:
    """Markdown report of B against A (the baseline) and the regressions beyond ``threshold`` percent."""
    lines, regress = [f"# {b} against {a}", ""], []
    ra, rb = rulers(a), rulers(b)
    done = set()
    for key in sorted(set(ra) | set(rb)):
        ka, kb = _pair(ra, rb, key)
        if not ka or (ka, kb) in done:
            continue
        done.add((ka, kb))
        lines += [f"## {ka} -> {kb}: aggregate tok/s (first token)", "", "| users | phase | A | B | change | ttft A | ttft B |",
                  "|---:|---|---:|---:|---:|---:|---:|"]
        for cell in sorted(set(ra[ka]) & set(rb[kb])):
            x, y = ra[ka][cell], rb[kb][cell]
            va, vb = x.get("aggregate") or 0, y.get("aggregate") or 0
            pct = (vb - va) / va * 100 if va else 0
            ta, tb = x.get("ttft"), y.get("ttft")
            flag = ""
            if pct < -threshold:
                flag = " **slower**"
                regress.append(f"{kb} c={cell[0]} {cell[1]}: {va:.1f} -> {vb:.1f} tok/s ({pct:+.1f}%)")
            if ta and tb and tb > ta * (1 + threshold / 100) and tb - ta > 0.05:
                flag += " **ttft**"
                regress.append(f"{kb} c={cell[0]} {cell[1]}: first token {ta:.2f} -> {tb:.2f} s")
            lines.append(f"| {cell[0]} | {cell[1]} | {va:.1f} | {vb:.1f} | {pct:+.1f}%{flag} | "
                         f"{ta:.2f} | {tb:.2f} |" if ta and tb else f"| {cell[0]} | {cell[1]} | {va:.1f} | {vb:.1f} | {pct:+.1f}%{flag} | | |")
        lines.append("")
    sa, sb = suites(a), suites(b)
    pairs = [(k, k) for k in sorted(set(sa) & set(sb))]
    if not pairs and len(sa) == 1 and len(sb) == 1:
        pairs = [(next(iter(sa)), next(iter(sb)))]
    for ka, kb in pairs:
        lines += [f"## suite {ka} -> {kb}", "", "| check | A | B | change |", "|---|---:|---:|---:|"]
        for name in [n for n in sa[ka] if n in sb[kb]]:
            x, y = sa[ka][name], sb[kb][name]
            d = (y.get("passed") or 0) - (x.get("passed") or 0)
            flag = " **worse**" if d < 0 else ""
            if d < 0:
                regress.append(f"suite {name}: {x.get('passed')}/{x.get('cases')} -> {y.get('passed')}/{y.get('cases')}")
            lines.append(f"| {name} | {x.get('passed')}/{x.get('cases')} | {y.get('passed')}/{y.get('cases')} | {d:+d}{flag} |")
        lines.append("")
    ma, mb = summaries(a), summaries(b)
    shared = [n for n in mb if n in ma and not n.startswith(("ruler", "suite"))]
    if shared:
        lines += ["## checks", "", "| check | A | B |", "|---|---|---|"]
        for n in shared:
            x, y = ma[n], mb[n]
            if x.get("ok") is True and y.get("ok") is False:
                regress.append(f"{n}: passed in A, fails in B ({y.get('summary')})")
            lines.append(f"| {n} | {x.get('summary')} | {y.get('summary')} |")
        lines.append("")
    lines += ["## regressions", ""] + ([f"- {r}" for r in regress] or [f"none beyond {threshold:g}%"])
    return "\n".join(lines) + "\n", regress
