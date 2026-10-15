# Working in recipe-harness (any machine, any session)

## The served-stats document: always current

`STATS.md`, `STATS.txt` and `STATS.pdf` are one document in three formats: every model we have served, on every
machine, with its measured performance and quality. They are rendered from the ledger, `stats/<target>.json`.

**Every time stats change, update the document in all three formats and push it.** That means after:
- a kept `python3 -m harness run` (it records itself and renders all three);
- a `python3 -m harness export` (records and renders too);
- a recipe republish, a new evidence folder, or numbers measured any other way. Bring them in, then render:
  - a harness run: `python3 -m harness stats [runs/<target>/<run>]`;
  - a recipe's published evidence: `python3 -m harness stats --import-evidence <recipe checkout> --target <name>
    --model-name "<model>" --hardware "<hardware>" --engine "<engine>" --source github.com/<owner>/<recipe>`;
  - numbers that fit neither (README-only): a row in `stats/notes.md`, then `python3 -m harness stats`.

Then, every time:
1. `python3 -m harness scrub . --diff` (nothing personal or machine-specific may be committed);
2. `git pull --rebase` (other machines add their own targets' runs);
3. commit `stats/` and `STATS.md`, `STATS.txt`, `STATS.pdf` together, and push.

Never edit the three STATS files by hand: change the ledger or `stats/notes.md` and render.

## Targets

Every model and machine is its own target (`targets/<name>.toml`) with `model_name`, `hardware` and `engine` set, so
it gets its own row in the overview. Machine-specific values go in `targets/<name>.local.toml` (git-ignored).

## Measuring

Kept or quoted numbers for a TensorFold recipe come from `python3 -m harness run <target> --plan <plan>`, not ad-hoc
scripts. Targets on TensorFold's native server set `commands.server_log` so the ruler records the engine's rounds.

## Publishing

As BobClawblaw only. `runs/` and `*.local.toml` never leave the machine. Scrub before every commit.
