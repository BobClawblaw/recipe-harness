"""The checks a plan can run. Each takes (target, spec, run_dir, name), writes its files under run_dir and returns
{"ok": True | False | None, "summary": one line, "metrics": {...}}; ok None means measured, nothing to pass or fail."""

from __future__ import annotations

from pathlib import Path

from ..config import Target
from . import capacity, memory, recipe, server, thinking

REGISTRY = {
    "suite": recipe.suite,
    "ruler": recipe.ruler,
    "structured": server.structured,
    "sampling": server.sampling,
    "turns": server.turns,
    "urls": server.urls,
    "capacity": capacity.run,
    "thinking": thinking.run,
    "memory": memory.run,
}

# a check whose feature the target turns off is skipped (e.g. a greedy-only engine has no sampling)
NEEDS = {"structured": "structured", "sampling": "sampling", "urls": "vision_urls", "capacity": "capacity",
         "thinking": "thinking", "turns": "prompt_cache"}


def applies(target: Target, kind: str, spec: dict) -> bool:
    if kind not in REGISTRY:
        raise KeyError(f"unknown check type {kind!r}; known: {', '.join(REGISTRY)}")
    if kind in ("suite", "ruler") and kind not in target.section("commands"):
        return False
    if kind == "memory" and not target.get("memory"):
        return False
    return bool(target.feature(NEEDS[kind])) if kind in NEEDS else True


def run(kind: str, target: Target, spec: dict, run_dir: Path, name: str) -> dict:
    return REGISTRY[kind](target, spec, run_dir, name)
