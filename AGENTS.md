# Working in recipe-harness (any machine, any session)

- **Kept measurements go through the harness.** A TensorFold recipe's performance or quality numbers that will be
  kept or quoted come from `python3 -m harness run <target> --plan <plan>`, not ad-hoc scripts.
- **The served stats stay current.** `stats/<target>.json` (the ledger) and `STATS.md`, `STATS.txt`, `STATS.pdf` (by
  model and hardware) are updated with every kept run, export or recipe republish: a run and an export record
  themselves; otherwise run `python3 -m harness stats`. Then `python3 -m harness scrub . --diff`, pull/rebase, and
  commit and push `stats/` and `STATS.*` with the run's other changes.
- **Every model and machine is its own target** with `model_name`, `hardware` and `engine` set, so it gets its own row.
- **Publish as BobClawblaw only**, nothing personal or machine-specific (names, hostnames, addresses, home paths):
  scrub before every commit. `runs/` and `*.local.toml` never leave the machine.
