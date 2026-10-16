"""The served-stats ledger and its reports.

``stats/<target>.json`` is the ledger (committed): one compact entry for every finished run on any machine, keyed by
the run's name, holding what was served (identity), the ruler cells, the engine's rounds, suite scores and the checks'
one-line results. STATS.md, STATS.txt and STATS.pdf at the repo root are rendered from every target's ledger, so a
machine that only holds its own runs/ still writes the whole picture. ``record`` adds a run and renders again; a run
and an export call it, and so does ``python3 -m harness stats``.
"""

from __future__ import annotations

import json
import time
import tomllib
from pathlib import Path

from . import pdf as typeset

ROOT = Path(__file__).resolve().parent.parent
LEDGER = ROOT / "stats"
PHASES = ("prose", "code", "structured", "list")


def _json(p: Path):
    try:
        return json.loads(p.read_text())
    except (OSError, ValueError):
        return None


def _r(x, n=1):
    return round(x, n) if isinstance(x, (int, float)) else x


def target_facts(name: str) -> dict:
    """What the report labels a target with: its model, hardware and engine (the committed target file's own words)."""
    try:
        t = tomllib.loads((ROOT / "targets" / f"{name}.toml").read_text())
    except (OSError, ValueError):
        return {}
    return {k: t[k] for k in ("model_name", "hardware", "engine", "description") if k in t}


def entry(run: Path) -> dict | None:
    """A run folder as a ledger entry; None for a run that measured nothing (aborted before its first check)."""
    meta = _json(run / "meta.json")
    if not isinstance(meta, dict) or not meta.get("checks"):
        return None
    ident = meta.get("identity") or {}
    e = {"run": run.name, "target": meta.get("target"), "model": meta.get("model"), "plan": meta.get("plan"),
         "started": meta.get("started"), "finished": meta.get("finished"), "status": meta.get("status"),
         "identity": {k: (v.get("value", v.get("got")) if isinstance(v, dict) else v) for k, v in ident.items()},
         "rulers": {}, "rounds": {}, "suite": {}, "checks": {}, **target_facts(meta.get("target") or "")}
    for c in meta["checks"]:
        if c.get("skipped"):
            continue
        e["checks"][c["name"]] = {"ok": c.get("ok"), "summary": c.get("summary")}
        s = _json(run / f"{c['name']}.summary.json") or {}
        m = s.get("metrics") or {}
        if c.get("type") == "ruler" and m.get("cells"):
            e["rulers"][c["name"]] = [{"c": x["concurrency"], "phase": x["phase"], "agg": _r(x.get("aggregate")),
                                       "per_stream": _r(x.get("per_stream")), "ttft": _r(x.get("ttft"), 3)} for x in m["cells"]]
            if m.get("engine"):
                e["rounds"][c["name"]] = {n: {k: _r(v, 3) for k, v in lv.items()} for n, lv in m["engine"].items()}
        if c.get("type") == "suite" and m.get("scores"):
            e["suite"][c["name"]] = {k: {"passed": v.get("passed"), "cases": v.get("cases")} for k, v in m["scores"].items()}
    return e


def record(run: Path, render_after: bool = True) -> Path | None:
    """The run added to (or replaced in) its target's ledger, then every report rendered again."""
    e = entry(run)
    if e is None or not e.get("target"):
        return None
    LEDGER.mkdir(exist_ok=True)
    path = LEDGER / f"{e['target']}.json"
    book = _json(path) or {"target": e["target"], "runs": []}
    book["runs"] = [r for r in book["runs"] if r.get("run") != e["run"]] + [e]
    book["runs"].sort(key=lambda r: (r.get("started") or "", r.get("run") or ""))
    path.write_text(json.dumps(book, indent=1) + "\n")
    if render_after:
        render()
    return path


def _evidence_entry(folder: Path, target: str, source: str, facts: dict) -> dict | None:
    """A published recipe's evidence folder as a ledger entry: its rulers, a benchmark's one-stream cells, its suites."""
    name = folder.name
    day = name[:10].replace("-", "") if len(name) >= 10 and name[4] == "-" and name[7] == "-" else None
    if not day:
        return None
    e = {"run": f"evidence/{name}", "target": target, "model": facts.get("served_model"), "plan": "published evidence",
         "started": f"{day}-0000", "status": "published", "source": f"{source}/evidence/{name}", "identity": {},
         "rulers": {}, "rounds": {}, "suite": {}, "checks": {}, **{k: v for k, v in facts.items() if k != "served_model"}}
    for p in sorted(folder.glob("ruler*.json")):
        if p.name.endswith((".summary.json", ".engine.json")) or "vllm" in p.name:
            continue
        j = _json(p)
        if isinstance(j, dict) and j.get("cells"):
            e["rulers"][p.stem] = [{"c": x["concurrency"], "phase": x["phase"], "agg": _r(x.get("aggregate")),
                                    "per_stream": _r(x.get("per_stream")), "ttft": _r(x.get("ttft"), 3)} for x in j["cells"]]
    for p in sorted(folder.glob("*bench_openai*.json")):
        if "vllm" in p.name:
            continue
        j = _json(p)
        if isinstance(j, list) and j and isinstance(j[0], dict) and "decode_tps_median" in j[0]:
            e["rulers"][p.stem] = [{"c": 1, "phase": x.get("prompt", "?"), "agg": _r(x.get("decode_tps_median")),
                                    "per_stream": _r(x.get("decode_tps_median")), "ttft": _r(x.get("ttft_s_median"), 3)} for x in j]
    for rep in sorted(folder.glob("**/report.json")):
        rel = str(rep.parent.relative_to(folder))
        if "vllm" in rel or "/dev" in rel:
            continue
        j = _json(rep)
        if isinstance(j, dict) and j.get("results"):
            e["suite"]["suite" if rel == "." else rel] = {r["name"]: {"passed": r.get("passed"), "cases": r.get("cases")} for r in j["results"]}
    return e if e["rulers"] or e["suite"] else None


def import_evidence(recipe: Path, target: str, source: str, facts: dict) -> int:
    """Every dated folder of a published recipe's evidence/ into ``target``'s ledger (dev/ sweeps left out)."""
    LEDGER.mkdir(exist_ok=True)
    path = LEDGER / f"{target}.json"
    book = _json(path) or {"target": target, "runs": []}
    n = 0
    for folder in sorted(p for p in (recipe / "evidence").iterdir() if p.is_dir() and p.name != "dev"):
        e = _evidence_entry(folder, target, source, facts)
        if e:
            book["runs"] = [r for r in book["runs"] if r.get("run") != e["run"]] + [e]
            n += 1
    book["runs"].sort(key=lambda r: (r.get("started") or "", r.get("run") or ""))
    path.write_text(json.dumps(book, indent=1) + "\n")
    return n


def _books() -> list[dict]:
    return [b for b in (_json(p) for p in sorted(LEDGER.glob("*.json"))) if isinstance(b, dict) and b.get("runs")]


def _cell(s) -> str:
    """Text for one table cell: its lines joined, its pipes escaped, so a multi-line summary keeps the table whole."""
    return "; ".join(x.strip() for x in str(s).splitlines() if x.strip()).replace("|", "\\|")


def _when(stamp: str | None) -> str:
    if not stamp or len(stamp) < 13:
        return stamp or "?"
    return f"{stamp[0:4]}-{stamp[4:6]}-{stamp[6:8]} {stamp[9:11]}:{stamp[11:13]}"


def _ruler_rows(cells: list[dict]) -> list[str]:
    by: dict[int, dict] = {}
    for x in cells:
        by.setdefault(x["c"], {})[x["phase"]] = x
    rows = ["| streams | " + " | ".join(f"{p} total (a stream)" for p in PHASES) + " | first token |", "|---:|" + "---:|" * len(PHASES) + "---:|"]
    for n, ph in sorted(by.items()):
        rates = [f"{ph[p]['agg']:.1f} ({ph[p]['per_stream']:.1f})" if p in ph and ph[p].get("agg") and ph[p].get("per_stream") else
                 f"{ph[p]['agg']:.1f}" if p in ph and ph[p].get("agg") else "-" for p in PHASES]
        t = [ph[p]["ttft"] for p in ph if ph[p].get("ttft")]
        rows.append(f"| {n} | " + " | ".join(rates) + (f" | {min(t):.2f}-{max(t):.2f} s |" if t else " | |"))
    return rows


def _engine_rows(levels: dict) -> list[str]:
    rows = ["| streams | tokens a round | drafts a round | accepted | ms a round | requests |", "|---:|---:|---:|---:|---:|---:|"]
    for n, s in sorted(levels.items(), key=lambda kv: int(kv[0])):
        if not s.get("requests"):
            continue
        acc = f"{s['accept_rate'] * 100:.0f}%" if s.get("accept_rate") is not None else ""
        rows.append(f"| {n} | {s.get('tokens_a_round', '')} | {s.get('drafts_a_round', '')} | {acc} | {s.get('ms_a_round', '')} | {s.get('requests')} |")
    return rows


def _fresh(e: dict) -> list[dict] | None:
    """The run's main ruler: ruler-fresh or ruler, else the one with the most stream levels that is not a variant."""
    for k in ("ruler-fresh", "ruler"):
        if k in e["rulers"]:
            return e["rulers"][k]
    plain = {k: v for k, v in e["rulers"].items() if not any(w in k for w in ("sampled", "old", "before", "vllm", "repeat"))}
    pool = plain or e["rulers"]
    if not pool:
        return None
    return max(pool.values(), key=lambda cells: (len({x["c"] for x in cells}), len(cells)))


def markdown() -> str:
    out = ["# Served stats", "",
           f"Rendered {time.strftime('%Y-%m-%d %H:%M UTC', time.gmtime())} from `stats/*.json`, the ledger every `harness run` "
           "and `harness export` adds to (`python3 -m harness stats` renders it again). Aggregate tok/s, greedy, 256-token "
           "replies, the recipe's own ruler; engine rounds from the server's own counters.", ""]
    books = _shown()
    out += overview(books)
    for b in books:
        out += section(b)
    notes = LEDGER / "notes.md"  # what the ledger cannot hold (README-only recipes), kept by hand
    if notes.is_file():
        out += [notes.read_text().rstrip(), ""]
    return "\n".join(out) + "\n"


def _shown() -> list[dict]:
    return [b for b in _books() if any(r.get("rulers") or r.get("suite") for r in b["runs"])]


def section(b: dict) -> list[str]:
    """One target's part of the report: its latest run's rulers, rounds, suite and checks, then its history."""
    runs = [r for r in b["runs"] if r.get("rulers") or r.get("suite")]
    last = runs[-1]
    facts = {**last, **target_facts(b["target"])}
    out = [f"## {facts.get('model_name') or last.get('model')} on {facts.get('hardware') or b['target']}", "",
            f"Target `{b['target']}`: {facts.get('description', '')}. Engine: {facts.get('engine', '?')}; served as `{last.get('model')}`. "
            f"Latest: run `{last['run']}` ({_when(last.get('started'))}, plan {last.get('plan')}, {last.get('status')}).", ""]
    out += _run_lines(last, "###")
    out += ["### history", "", "| run | plan | status | 1 stream code | 16 streams code | 16 streams first token | suite |",
            "|---|---|---|---:|---:|---:|---|"]
    for r in reversed(runs):
        cells = _fresh(r) or []
        pick = lambda n: next((x for x in cells if x["c"] == n and x["phase"] == "code"), None)
        one, sixteen = pick(1), pick(16)
        ttft16 = [x["ttft"] for x in cells if x["c"] == 16 and x.get("ttft")]
        suite = next(iter(r["suite"].values()), {})
        passed = sum(v.get("passed") or 0 for v in suite.values())
        cases = sum(v.get("cases") or 0 for v in suite.values())
        out.append(f"| {_when(r.get('started'))} | {r.get('plan')} | {r.get('status')} | {one['agg'] if one else ''} | "
                   f"{sixteen['agg'] if sixteen else ''} | {f'{min(ttft16):.2f}-{max(ttft16):.2f} s' if ttft16 else ''} | "
                   f"{f'{passed}/{cases}' if cases else ''} |")
    out.append("")
    return out


def _run_lines(r: dict, h: str) -> list[str]:
    """A run's serving identity, rulers with their engine rounds, suite scores and checks; `h` its headings' level."""
    out = []
    ident = r.get("identity") or {}
    if ident:
        out += ["Serving: " + "; ".join(f"{k} `{_cell(v)[:90]}`" for k, v in ident.items() if v), ""]
    for name, cells in r.get("rulers", {}).items():
        out += [f"{h} {name}", ""] + _ruler_rows(cells) + [""]
        if name in r.get("rounds", {}):
            out += [f"Engine rounds ({name}):", ""] + _engine_rows(r["rounds"][name]) + [""]
    for name, scores in r.get("suite", {}).items():
        out += [f"{h} {name}", "", "| check | passed |", "|---|---:|"]
        out += [f"| {k} | {v['passed']}/{v['cases']} |" for k, v in scores.items()] + [""]
    other = {k: v for k, v in r.get("checks", {}).items() if not k.startswith(("ruler", "suite"))}
    if other:
        out += [f"{h} checks", "", "| check | result |", "|---|---|"]
        out += [f"| {k} | {'pass' if v['ok'] else 'FAIL' if v['ok'] is False else 'measured'}: {_cell(v['summary'])} |" for k, v in other.items()] + [""]
    return out


def target_markdown(b: dict) -> str:
    """stats/<target>.md: the ledger readable, every run newest first with all it measured."""
    facts = {**b["runs"][-1], **target_facts(b["target"])}
    out = [f"# {facts.get('model_name') or b['target']} on {facts.get('hardware') or '?'}", "",
           f"Target `{b['target']}`: {facts.get('description', '')}. Engine: {facts.get('engine', '?')}. Rendered from "
           f"`stats/{b['target']}.json` ({len(b['runs'])} runs); aggregate tok/s, total (a stream).", ""]
    for r in reversed(b["runs"]):
        out += [f"## {_when(r.get('started'))}: run `{r['run']}`", "",
                f"Plan {r.get('plan')}, {r.get('status')}; served as `{r.get('model')}`.", ""]
        out += _run_lines(r, "###") or ["No ruler, suite or check results.", ""]
    return "\n".join(out) + "\n"


def overview(books: list[dict]) -> list[str]:
    """One row a target, grouped by model then hardware: one stream, the most streams measured, first token, the suite."""
    rows = []
    for b in books:
        runs = [r for r in b["runs"] if r.get("rulers")]
        last = runs[-1] if runs else b["runs"][-1]
        facts = {**last, **target_facts(b["target"])}
        cells = _fresh(last) or []
        top = max((x["c"] for x in cells), default=None)
        def fmt(n):
            at = [x for x in cells if x["c"] == n and x.get("agg")]
            if at and not any(x["phase"] in PHASES for x in at):  # a benchmark of named prompts: their median decode rate
                v = sorted(x["agg"] for x in at)[len(at) // 2]
                return f"{v:.0f} (median of {len(at)} prompts)"
            return "/".join(next((f"{x['agg']:.0f}" for x in at if x["phase"] == p), "-") for p in PHASES)
        t1 = [x["ttft"] for x in cells if x["c"] == 1 and x.get("ttft")]
        tt = [x["ttft"] for x in cells if x["c"] == top and x.get("ttft")]
        suites = [r for r in b["runs"] if r.get("suite")]
        sc = next(iter(suites[-1]["suite"].values()), {}) if suites else {}
        head = ", ".join(f"{k} {sc[k]['passed']}/{sc[k]['cases']}" for k in ("tools", "json", "gsm8k", "humaneval", "ifeval") if k in sc)
        rows.append((facts.get("model_name") or last.get("model") or b["target"], facts.get("hardware") or "?",
                     f"| {facts.get('model_name') or last.get('model')} | {facts.get('hardware', '?')} | {fmt(1) if cells else ''} | "
                     f"{f'{top}: ' + fmt(top) if top and top > 1 else ''} | {f'{min(t1):.2f}' if t1 else ''}{f' / {min(tt):.2f}-{max(tt):.2f}' if tt and top and top > 1 else ''} | "
                     f"{head} | {_when(last.get('started'))[:10]} |"))
    if not rows:
        return []
    rows.sort(key=lambda r: (r[0], r[1]))
    return ["## Overview: by model and hardware", "",
            "Aggregate tok/s as prose/code/structured/list; first token in seconds (one stream / the most streams).", "",
            "| model | hardware | one stream | most streams: total | first token (s) | suite | measured |",
            "|---|---|---:|---:|---:|---|---|"] + [r[2] for r in rows] + [""]


def text(md: str) -> str:
    """The markdown as plain text: headings underlined, table rules dropped, columns kept."""
    lines = []
    for line in md.splitlines():
        if line.startswith("#"):
            title = line.lstrip("#").strip()
            lines += [title, ("=" if line.startswith("# ") else "-") * len(title)]
        elif line.startswith("|") and set(line.replace("|", "").strip()) <= set("-:"):
            continue
        elif line.startswith("|"):
            lines.append("  " + "  ".join(c.strip() for c in line.strip("|").split("|")))
        else:
            lines.append(line.replace("`", ""))
    return "\n".join(lines) + "\n"


def render() -> list[Path]:
    """STATS.md, STATS.txt and STATS.pdf from every target's ledger, and each ledger readable as stats/<target>.md."""
    md = markdown()
    paths = [ROOT / "STATS.md", ROOT / "STATS.txt", ROOT / "STATS.pdf"]
    paths[0].write_text(md)
    paths[1].write_text(text(md))
    paths[2].write_bytes(typeset.render(md, "Served stats", time.strftime("%Y-%m-%d %H:%M UTC", time.gmtime())))
    for b in _books():
        p = LEDGER / f"{b['target']}.md"
        p.write_text(target_markdown(b))
        paths.append(p)
    return paths
