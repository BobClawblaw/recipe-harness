"""Personal and machine-specific details in a tree or a diff, before anything is published.

The committed patterns are generic (home folders, private addresses, temp scratch paths, attribution trailers);
names, hostnames and emails belong in harness.local.toml ([scrub] patterns, allow), which git ignores."""

from __future__ import annotations

import re
import subprocess
from pathlib import Path

from .config import local_settings

DEFAULT = [
    r"/home/[a-z_][a-z0-9_-]*/",
    r"/Users/[A-Za-z_][A-Za-z0-9_-]*/",
    r"\b10\.\d{1,3}\.\d{1,3}\.\d{1,3}\b",
    r"\b192\.168\.\d{1,3}\.\d{1,3}\b",
    r"\b172\.(1[6-9]|2\d|3[01])\.\d{1,3}\.\d{1,3}\b",
    r"/tmp/claude",
    r"[A-Za-z0-9._%+-]+@(gmail|yahoo|hotmail|outlook|icloud|proton(mail)?)\.[a-z.]+",
    r"Co-Authored-By:",
    r"Generated with \[?Claude Code",
]
SKIP_DIRS = {".git", "__pycache__", "runs", "node_modules"}
BINARY = {".cubin", ".bin", ".png", ".jpg", ".jpeg", ".gif", ".safetensors", ".so", ".o", ".pyc", ".gz", ".xz", ".zip", ".mp4"}


def patterns() -> tuple[list[re.Pattern], list[str]]:
    s = local_settings().get("scrub", {})
    pats = DEFAULT + list(s.get("patterns", []))
    return [re.compile(p, re.I) for p in pats], list(s.get("allow", []))


def _hits(text: str, where: str, pats, allow) -> list[str]:
    out = []
    for n, line in enumerate(text.splitlines(), 1):
        if any(a in line for a in allow):
            continue
        for p in pats:
            m = p.search(line)
            if m:
                out.append(f"{where}:{n}: {m.group(0)!r} in {line.strip()[:140]}")
                break
    return out


def scan_tree(root: Path, extra_allow: list[str] | None = None) -> list[str]:
    pats, allow = patterns()
    allow += extra_allow or []
    hits = []
    files = [root] if root.is_file() else [p for p in root.rglob("*") if p.is_file() and not (set(p.relative_to(root).parts) & SKIP_DIRS)]
    for p in files:
        if p.suffix.lower() in BINARY or p.name.endswith(".local.toml"):
            continue
        try:
            text = p.read_text(errors="strict")
        except (UnicodeDecodeError, OSError):
            continue
        hits += _hits(text, str(p), pats, allow)
    return hits


def scan_diff(repo: Path, ref: str = "--cached") -> list[str]:
    """Added lines of ``git diff <ref>`` (default: what is staged) in ``repo``."""
    pats, allow = patterns()
    diff = subprocess.run(["git", "-C", str(repo), "diff", "--text", "-U0", ref], capture_output=True, text=True).stdout
    added = "\n".join(l[1:] for l in diff.splitlines() if l.startswith("+") and not l.startswith("+++"))
    return _hits(added, f"{repo} diff {ref}", pats, allow)
