# recipe-harness

Measure an inference recipe the same way every time: take the machines' lock, restart the recipe, check what is
serving, run a plan of checks, keep the results, compare them with an earlier run, and export them into the recipe's
`evidence/`.

The harness drives a recipe from outside:
- its own commands (`spark up`, `mac up`, ...);
- its OpenAI-compatible endpoint;
- its own quality suite and ruler, run as commands.

Recipes stay self-contained: nothing here is imported by a recipe, and no recipe code is copied here. Python 3.11+,
standard library only.

## Install

```bash
git clone https://github.com/BobClawblaw/recipe-harness.git && cd recipe-harness
cp targets/qwen38-int4mixed.local.example.toml targets/qwen38-int4mixed.local.toml && $EDITOR targets/qwen38-int4mixed.local.toml
cp harness.local.example.toml harness.local.toml && $EDITOR harness.local.toml     # your scrub patterns
python3 -m harness targets          # which targets are configured
python3 -m unittest discover -s tests
```

## Run

```bash
python3 -m harness run qwen38-int4mixed --plan quick --dry-run   # the commands and checks, touches nothing
python3 -m harness run qwen38-int4mixed --plan quick             # ~25 min under the lock; results in runs/
python3 -m harness run qwen38-int4mixed --plan full              # the release measurement, 2-3 hours
python3 -m harness run qwen38-int4mixed --plan thinking          # thinking-on checks against the running server
python3 -m harness check qwen38-int4mixed                        # is it healthy now
```

A run does these steps in order:

1. Takes the target's lock, if it has one. The qwen pair's lock is shared with every GPU job on the two nodes.
2. Runs `down`, then `up`, until `/health` and `/v1/models` answer. It retries `up_retries` times, waiting
   `retry_wait` between tries.
3. Records the target's `[[identity]]` values. An entry with `expect` must match: for qwen, the image's patch label
   must equal the patch that `recipe.toml` pins. A mismatch aborts the run.
4. Runs the plan's checks in order.
5. If the server dies or never comes up, the run aborts and records nothing more. No empty results are saved.
6. Leaves the recipe up and releases the lock.

Everything is logged with timestamps to `runs/<target>/<stamp>-<plan>/run.log`. The exit code is nonzero when the run
aborted or a check failed.

## Checks

| Type | What it does | Pass / fail |
|---|---|---|
| `suite` | the recipe's quality suite (`commands.suite`, `$args` from the plan); its report goes in `<name>/` | fails when a check has no cases (errors) or drafts/concurrent are not exact |
| `ruler` | the recipe's ruler (`commands.ruler`, `concurrency = [...]`); label it `fresh`, then `after` other traffic, to catch long-session slowdowns | fails on a cell with no replies |
| `structured` | json_object, json_schema, guided_json, regex, choice and grammar, each greedy, sampled and thinking; a grammar that cannot compile must be a 400 | every reply obeys and the bad regex gets a 400 |
| `sampling` | seeded sampled replies, repeated and undrafted | equal every time |
| `turns` | a conversation that resumes its kept prompt; the third turn resumed, again, and cold | all three equal; reports cached tokens and first-token times |
| `urls` | a public HTTPS image, a loopback address, plain HTTP | 200 with an answer, 400, 400 |
| `capacity` | N long prompts at once (`streams`, `tokens`), then a short request | the short request succeeds and no request is lost without a reply |
| `thinking` | the harness's word problems with `enable_thinking: true` | answers right, reasoning in `reasoning_content`, no `<think>` leaks |
| `memory` | the target's `[[memory]]` commands (`free -b` read as GiB available) | measured |

Each check writes `<name>.json` (its data) and `<name>.summary.json` (`ok`, a one-line summary, metrics). Targets turn
off checks they don't serve in `[features]`. A greedy-only engine, for example, skips `sampling`.

**Thinking on.** The qwen suite honours `--thinking` for GSM8K only and sends thinking off everywhere else.
- The `thinking` plan runs the harness's own thinking-on problems, plus the suite with `--only gsm8k --thinking`.
- A run's `suite-thinking.summary.json` records exactly which arguments the suite ran with.
- Every other suite score in a run is thinking off.

## Compare, tables, export, scrub

```bash
python3 -m harness compare <baseline run or evidence folder> <new run> [--threshold 5]   # exit 1 on a regression
python3 -m harness tables runs/qwen38-int4mixed/<run>                                     # README-ready markdown
python3 -m harness export runs/qwen38-int4mixed/<run> ~/qwen38-flashnext-int4mixed 2026-10-11-my-change
python3 -m harness scrub ~/qwen38-flashnext-int4mixed            # a tree
python3 -m harness scrub ~/qwen38-flashnext-int4mixed --diff     # the staged diff of a repo
```

**`compare`** pairs the two sides' ruler files (`ruler-fresh` with `ruler`) and suite reports. It flags:
- a cell that is more than the threshold slower;
- a first token later by more than the threshold and more than 0.05 s;
- a suite check with fewer passes;
- a check that passed before and fails now.

Recipe evidence folders compare as they are, since runs use the same layout.

**`export`** copies a run's data, without the harness's log and summaries, into the recipe's `evidence/<name>/`. It then
scrubs that folder and prints the tables.

**`scrub`** looks for home folders, private addresses, temp scratch paths, personal-mail addresses and attribution
trailers. Your names and hostnames go in `harness.local.toml`. Run it before every publish.

## Targets

A target is `targets/<name>.toml`, committed with no machine details, plus `targets/<name>.local.toml`, which git
ignores and which overrides the committed file. The committed file holds:
- `url` and `model`;
- `cwd`, where the commands run;
- `[vars]`, the `$placeholders` the commands use;
- `[commands]`: `up`, `down`, `status`, `diagnose`, `suite`, `ruler`;
- `[session]`: `lock`, `up_retries`, `retry_wait`, `up_timeout`, `health_wait`, `leave_up`;
- `[[identity]]` (`name`, `cmd`, optional `expect`) and `[[memory]]` (`name`, `cmd`);
- `[features]`.

Commands are shell lines with `$url`, `$model`, `$out`, `$args`, `$concurrency` and the target's `[vars]`.

### qwen38-int4mixed: Qwen3.8-Flash-Next INT4-Mixed on two DGX Sparks

The [recipe](https://github.com/BobClawblaw/qwen38-flashnext-int4mixed-2x-dgx-sparks) serves TensorFold's native engine
at TP=2. The harness:
- runs on the head node, with the recipe checkout as `cwd`;
- uses the recipe's `spark up`, `spark down`, `quality.suite` and `bench/ruler.py`.

Settings:
- **Lock:** `~/.cache/tf-gpu-pair.lock`.
- **Startup:** up to three starts, 90 s apart. The worker sometimes refuses NCCL's first memory registration after a
  stop, and rank 0 then exits during its warm-up gather.
- **Identity:** the image's `tensorfold.patch_sha` label against `recipe.toml`, the image ID, and the server's flags.
- **Memory:** `free -b` on the head, and over ssh on the worker.
- **Local values:** `recipe_dir`, `worker`, `port`.

### glm53-m5: GLM-5.3-Flash MLX 4-bit on one M5 Ultra Mac

The [recipe](https://github.com/BobClawblaw/glm53-flash-mlx4bit-m5-ultra) is driven over ssh. This machine:
- starts and stops it with `mac up` and `mac down`;
- runs the qwen recipe's suite and ruler from a local checkout (`suite_dir`) against the Mac's endpoint. That is the
  same suite the GLM recipe pins, and HumanEval's sandbox runs here.

Settings:
- **Features off:** structured output (the engine refuses it), sampling (greedy only), media URLs, capacity (one
  stream).
- **Startup:** one start only. After a memguard kill, `mac up` refuses to start again for 15 minutes.
- **Local values:**
  - `mac`: the ssh login;
  - `mac_host`: the Mac's address;
  - `recipe_dir`: the recipe on the Mac;
  - `suite_dir`: the qwen recipe checkout here.
- **On the Mac:** `local.toml` must set `host = "0.0.0.0"`, so the Mac serves the network.

## Plans

`plans/<name>.toml` holds `description`, `restart` and a list of `[[checks]]` (`type`, an optional `name` or `label`,
and the check's options).

| Plan | Restarts | Checks |
|---|---|---|
| `quick` | yes | one stream fresh, the serving checks, one stream after them, then the suite's drafts, concurrent and behaviour checks |
| `full` | yes | ruler at 1/4/8/16 streams, the whole suite, the serving checks, ruler at 1 and 16 after them, capacity |
| `thinking` | no | thinking-on word problems, and the suite's GSM8K with `--thinking` |
