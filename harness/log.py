"""Timestamped lines to the terminal and the run's log."""

from __future__ import annotations

import sys
import time
from pathlib import Path

_file: Path | None = None


def to(path: Path | None) -> None:
    global _file
    _file = path


def log(msg: str) -> None:
    line = f"{time.strftime('%Y-%m-%dT%H:%M:%S')} {msg}"
    print(line, flush=True)
    if _file:
        with open(_file, "a") as f:
            f.write(line + "\n")


def warn(msg: str) -> None:
    log(f"WARN {msg}")
    sys.stdout.flush()
