"""Start a recipe that is a plain process, detached, its output to files, and return at once.

    python -m harness.detach --log server.log [--err server.err.log] -- tensorfold serve MODEL --port 8888

A target whose ``up`` is the server itself (no systemd unit or container) runs it through this: the harness captures
``up``'s output through pipes, and a server started by the shell would inherit them and keep ``up`` from returning.
Here the server gets only its log files and a closed stdin, no inherited handles, its own process group (and on
Windows no console), so ``up`` returns with the server's PID on its first line and the harness goes on to ``/health``.
"""
from __future__ import annotations

import argparse
import os
import subprocess
import sys


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("--log", required=True, help="the process's stdout")
    ap.add_argument("--err", help="its stderr (default: the same file)")
    ap.add_argument("command", nargs=argparse.REMAINDER, help="the command, after --")
    a = ap.parse_args(argv)
    cmd = a.command[1:] if a.command[:1] == ["--"] else a.command
    if not cmd:
        ap.error("no command (put it after --)")
    out = open(a.log, "ab")
    err = open(a.err, "ab") if a.err and a.err != a.log else out
    kw: dict = {"stdin": subprocess.DEVNULL, "stdout": out, "stderr": err, "close_fds": True}
    if os.name == "nt":
        kw["creationflags"] = subprocess.DETACHED_PROCESS | subprocess.CREATE_NEW_PROCESS_GROUP
    else:
        kw["start_new_session"] = True
    p = subprocess.Popen(cmd, **kw)
    print(p.pid)
    return 0


if __name__ == "__main__":
    sys.exit(main())
