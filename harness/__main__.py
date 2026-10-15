"""python3 -m harness run|compare|export|scrub|tables|targets|plans|check"""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

from . import api, session
from .compare import compare
from .config import ROOT, ConfigError, load_plan, load_target
from .export import export, tables
from .scrub import scan_diff, scan_tree


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(prog="python3 -m harness", description=__doc__)
    sub = ap.add_subparsers(dest="cmd", required=True)
    r = sub.add_parser("run", help="a plan against a target: lock, down/up, identity, checks, results under runs/")
    r.add_argument("target")
    r.add_argument("--plan", default="quick")
    r.add_argument("--no-restart", action="store_true", help="use the server as it is (it must be healthy)")
    r.add_argument("--dry-run", action="store_true", help="show the commands and checks, touch nothing")
    c = sub.add_parser("compare", help="run B against run A (the baseline): scores, tok/s, first token, checks")
    c.add_argument("a", type=Path)
    c.add_argument("b", type=Path)
    c.add_argument("--threshold", type=float, default=5.0, help="percent beyond which a slowdown is a regression")
    c.add_argument("--out", type=Path, help="also write the report here")
    e = sub.add_parser("export", help="copy a run into <recipe>/evidence/<name>/, scrubbed, and print its tables")
    e.add_argument("run", type=Path)
    e.add_argument("recipe", type=Path)
    e.add_argument("name")
    t = sub.add_parser("tables", help="README-ready markdown tables of a run or an evidence folder")
    t.add_argument("run", type=Path)
    s = sub.add_parser("scrub", help="personal or machine details in a tree, a file, or a repo's staged diff")
    s.add_argument("path", type=Path)
    s.add_argument("--diff", nargs="?", const="--cached", help="scan `git diff <ref>` of the repo at path (default: staged)")
    sub.add_parser("targets", help="the targets and their settings")
    sub.add_parser("plans", help="the plans and their checks")
    h = sub.add_parser("check", help="is a target's server healthy now (no lock, no restart)")
    h.add_argument("target")
    st = sub.add_parser("stats", help="add runs to the stats/ ledger and render STATS.md, STATS.txt and STATS.pdf")
    st.add_argument("runs", type=Path, nargs="*", help="run folders to add (default: every finished run under runs/)")
    st.add_argument("--import-evidence", type=Path, metavar="RECIPE", help="a recipe checkout: every dated evidence/ folder into --target's ledger")
    st.add_argument("--target", help="the ledger to import into (a target name; a new one for a new model or machine)")
    st.add_argument("--source", help="where the evidence is published, e.g. github.com/<owner>/<recipe>")
    st.add_argument("--served-model", help="the served model name")
    st.add_argument("--model-name", help="the report's model column")
    st.add_argument("--hardware", help="the report's hardware column")
    st.add_argument("--engine", help="the report's engine (e.g. 'TensorFold native, CUDA')")
    a = ap.parse_args(argv)
    try:
        return COMMANDS[a.cmd](a)
    except ConfigError as err:
        print(f"config: {err}", file=sys.stderr)
        return 2


def cmd_run(a) -> int:
    target, plan = load_target(a.target), load_plan(a.plan)
    if a.dry_run:
        from .checks import applies
        print(f"target {target.name}: {target.url} as {target.model}; cwd {target.cwd}")
        for k, v in target.section("commands").items():
            print(f"  {k}: {target.expand(v, out='<out>', args='<args>', concurrency='<c>', since='<since>')}")
        for item in target.get("identity", []):
            print(f"  identity {item['name']}: {target.expand(item['cmd'])}" + (f" == {target.expand(item['expect'])}" if "expect" in item else ""))
        print(f"  session: {target.section('session')}")
        print(f"plan {a.plan}: restart {plan.get('restart', True) and not a.no_restart}")
        for spec in plan["checks"]:
            print(f"  {spec['type']:10s} {'' if applies(target, spec['type'], spec) else '(skipped: not served) '}{ {k: v for k, v in spec.items() if k != 'type'} }")
        return 0
    run_dir = session.run(target, plan, a.plan, restart=False if a.no_restart else None)
    meta = json.loads((run_dir / "meta.json").read_text())
    _record(run_dir)
    print(tables(run_dir))
    return 0 if meta["status"] == "done" and not any(c.get("ok") is False for c in meta["checks"]) else 1


def cmd_compare(a) -> int:
    text, regress = compare(a.a, a.b, a.threshold)
    print(text)
    if a.out:
        a.out.write_text(text)
    return 1 if regress else 0


def _record(run_dir: Path) -> None:
    """The run in the ledger and the reports rendered again; a report that fails never fails the run."""
    from . import stats
    try:
        if stats.record(run_dir):
            print(f"stats: {run_dir.name} recorded; STATS.md, STATS.txt and STATS.pdf rendered (commit stats/ and STATS.*)")
    except Exception as err:  # noqa: BLE001
        print(f"stats: not recorded ({err})", file=sys.stderr)


def cmd_stats(a) -> int:
    from . import stats
    if a.import_evidence:
        if not (a.target and a.model_name and a.hardware and a.engine):
            print("stats: --import-evidence needs --target, --model-name, --hardware and --engine", file=sys.stderr)
            return 2
        facts = {k: v for k, v in (("served_model", a.served_model), ("model_name", a.model_name), ("hardware", a.hardware),
                                   ("engine", a.engine)) if v}
        n = stats.import_evidence(a.import_evidence, a.target, a.source or a.import_evidence.name, facts)
        print(f"stats: {n} evidence folders of {a.import_evidence} in stats/{a.target}.json")
    runs = a.runs or sorted(p for p in (stats.ROOT / "runs").glob("*/*") if (p / "meta.json").is_file())
    added = [r.name for r in runs if stats.record(r, render_after=False)]
    paths = stats.render()
    print(f"stats: {len(added)} runs recorded; rendered {', '.join(p.name for p in paths)}")
    return 0


def cmd_export(a) -> int:
    _record(a.run)
    dest = export(a.run, a.recipe, a.name)
    hits = scan_tree(dest)
    print(f"exported to {dest}")
    if hits:
        print("scrub hits (fix before committing):\n" + "\n".join(hits))
    print(tables(dest))
    return 1 if hits else 0


def cmd_tables(a) -> int:
    print(tables(a.run))
    return 0


def cmd_scrub(a) -> int:
    hits = scan_diff(a.path, a.diff) if a.diff else scan_tree(a.path)
    print("\n".join(hits) if hits else "clean")
    return 1 if hits else 0


def cmd_targets(a) -> int:
    for p in sorted((ROOT / "targets").glob("*.toml")):
        if p.stem.endswith(".local") or ".example" in p.stem:
            continue
        try:
            t = load_target(p.stem)
            print(f"{p.stem}: {t.url} ({t.model}) - {t.get('description', '')}")
        except ConfigError as e:
            print(f"{p.stem}: not configured ({e})")
    return 0


def cmd_plans(a) -> int:
    for p in sorted((ROOT / "plans").glob("*.toml")):
        plan = load_plan(p.stem)
        print(f"{p.stem}: {plan.get('description', '')}\n  " + ", ".join(c.get("name", c["type"] + (f"-{c['label']}" if "label" in c else "")) for c in plan["checks"]))
    return 0


def cmd_check(a) -> int:
    t = load_target(a.target)
    ok = api.healthy(t.url)
    print(f"{t.url}: {'healthy' if ok else 'not healthy'}")
    return 0 if ok else 1


COMMANDS = {
    "run": cmd_run, "stats": cmd_stats, "compare": cmd_compare, "export": cmd_export, "tables": cmd_tables, "scrub": cmd_scrub,
            "targets": cmd_targets, "plans": cmd_plans, "check": cmd_check}

if __name__ == "__main__":
    sys.exit(main())
