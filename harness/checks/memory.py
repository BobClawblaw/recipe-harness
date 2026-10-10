"""Memory on each node: the target's [[memory]] commands' output (``free -b`` lines read as available GiB)."""

from __future__ import annotations

import json
from pathlib import Path

from ..config import Target


def _available_gib(text: str) -> float | None:
    for line in text.splitlines():
        parts = line.split()
        if parts[:1] == ["Mem:"] and len(parts) >= 7 and parts[6].isdigit():
            return round(int(parts[6]) / 2**30, 1)
    return None


def run(target: Target, spec: dict, run_dir: Path, name: str) -> dict:
    from ..session import sh
    res = {}
    for item in target.get("memory", []):
        rc, out = sh(target, item["cmd"], timeout=60)
        res[item["name"]] = {"output": out.strip(), "available_gib": _available_gib(out), "exit": rc}
    (run_dir / f"{name}.json").write_text(json.dumps(res, indent=1))
    return {"ok": None, "summary": "; ".join(f"{k} {v['available_gib']} GiB available" if v["available_gib"] is not None
                                            else f"{k}: {v['output'][:60]}" for k, v in res.items()),
            "metrics": {k: v["available_gib"] for k, v in res.items()}}
