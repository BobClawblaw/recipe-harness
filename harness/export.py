"""A run into a recipe's evidence folder, scrubbed, with README-ready tables."""

from __future__ import annotations

import json
import shutil
from pathlib import Path

from .compare import rulers, suites

PHASES = ["prose", "code", "structured", "list"]
HARNESS_FILES = {"run.log", "meta.json"}


def ruler_table(cells: dict) -> str:
    rows = sorted({c[0] for c in cells})
    out = ["| Users | " + " | ".join(PHASES) + " | first token |", "|---:|" + "---:|" * (len(PHASES) + 1)]
    for n in rows:
        vals = [cells.get((n, p), {}).get("aggregate") for p in PHASES]
        ttfts = [cells[(n, p)]["ttft"] for p in PHASES if (n, p) in cells and cells[(n, p)].get("ttft")]
        tt = f"{min(ttfts):.2f}-{max(ttfts):.2f} s" if ttfts else ""
        out.append(f"| {n} | " + " | ".join(f"{v:.1f}" if v else "-" for v in vals) + f" | {tt} |")
    return "\n".join(out)


def suite_table(results: dict) -> str:
    out = ["| Check | Result |", "|---|---|"]
    for name, r in results.items():
        note = (r.get("notes") or [""])[0]
        out.append(f"| {name} | {r.get('passed')}/{r.get('cases')}" + (f" ({note})" if note else "") + " |")
    return "\n".join(out)


def tables(run: Path) -> str:
    parts = []
    for name, cells in rulers(run).items():
        parts += [f"### {name}", "", ruler_table(cells), ""]
    for name, res in suites(run).items():
        parts += [f"### suite ({name})", "", suite_table(res), ""]
    summ = sorted(run.glob("*.summary.json"))
    if summ:
        parts += ["### checks", "", "| Check | Result |", "|---|---|"]
        for p in summ:
            s = json.loads(p.read_text())
            if s.get("type") not in ("ruler", "suite"):
                parts.append(f"| {s['name']} | {s['summary']} |")
        parts.append("")
    return "\n".join(parts)


def export(run: Path, recipe: Path, name: str, include_harness: bool = False) -> Path:
    dest = recipe / "evidence" / name
    if dest.exists():
        raise FileExistsError(f"{dest} exists; pick another name")
    shutil.copytree(run, dest, ignore=None if include_harness else shutil.ignore_patterns(*HARNESS_FILES, "*.summary.json"))
    return dest
