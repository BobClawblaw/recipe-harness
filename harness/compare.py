"""Two runs (or evidence folders) side by side: suite scores, ruler tok/s and first-token time, the engine's rounds
(when both runs logged them), server checks."""

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


def engines(d: Path) -> dict[str, dict[int, dict]]:
    """A ruler's engine counters by level (<ruler>.engine.json), keyed by the ruler's name."""
    out = {}
    for p in sorted(d.glob("ruler*.engine.json")):
        j = _json(p)
        if isinstance(j, dict) and "levels" in j:
            out[p.name[: -len(".engine.json")]] = {int(n): s for n, s in j["levels"].items()}
    return out


def _engine_rows(ea: dict[int, dict], eb: dict[int, dict], label: str, threshold: float, regress: list[str]) -> list[str]:
    """Tokens a stream-round, drafts accepted and ms a round side by side; a slower level is named rounds or drafting."""
    lines = [f"## {label}: engine rounds", "", "| users | tokens a round A | B | accepted A | B | ms a round A | B | change |",
             "|---:|---:|---:|---:|---:|---:|---:|---:|"]
    for n in sorted(set(ea) & set(eb)):
        x, y = ea[n], eb[n]
        if not x.get("requests") or not y.get("requests"):
            continue
        ta, tb = x.get("tokens_a_round") or 0, y.get("tokens_a_round") or 0
        ma, mb = x.get("ms_a_round"), y.get("ms_a_round")
        acc = lambda s: f"{s['accept_rate'] * 100:.0f}%" if s.get("accept_rate") is not None else ""
        change = ""
        if ma and mb:
            pct = (mb - ma) / ma * 100
            change = f"{pct:+.1f}%"
            work = (tb - ta) / ta * 100 if ta else 0
            if pct > threshold and abs(work) <= threshold / 2:
                change += " **rounds slower, same drafting**"
                regress.append(f"{label} c={n}: rounds {ma:.1f} -> {mb:.1f} ms with the same tokens a round ({ta:.2f} -> {tb:.2f})")
            elif work < -threshold:
                change += " **less drafted**"
                regress.append(f"{label} c={n}: tokens a round {ta:.2f} -> {tb:.2f}")
        lines.append(f"| {n} | {ta:.2f} | {tb:.2f} | {acc(x)} | {acc(y)} | {ma or ''} | {mb or ''} | {change} |")
    return lines + [""]


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
        ea, eb = engines(a).get(ka), engines(b).get(kb)
        if ea and eb:
            lines += _engine_rows(ea, eb, f"{ka} -> {kb}", threshold, regress)
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
