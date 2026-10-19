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

1. Takes the target's lock, if it has one. The qwen pair's lock is shared with every GPU job on the two nodes. Two
   runs of one target never overlap either: each takes `runs/.locks/<target>.lock`.
2. Runs `down`, then `up`, until `/health` and `/v1/models` answer. It retries `up_retries` times, waiting
   `retry_wait` between tries. A start counts only when `up` exits 0. A URL still answering `down_wait` seconds
   (60) after `down` belongs to a server the harness did not start (a launchd unit, another run): the run aborts
   rather than measure it.
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
| `suite` | the recipe's quality suite (`commands.suite`, `$args` from the plan); its report goes in `<name>/` | fails when a check has no cases (errors) or drafts, concurrent or soak is not exact (soak: concurrent resumes of ~6k-token kept states, every reply equal to the same request alone) |
| `ruler` | the recipe's ruler (`commands.ruler`, `concurrency = [...]`); label it `fresh`, then `after` other traffic, to catch long-session slowdowns. With `commands.server_log` it runs one level at a time and writes `<name>.engine.json` (engine rounds, below) | fails on a cell with no replies |
| `structured` | json_object, json_schema, guided_json, regex, choice and grammar, each greedy, sampled and thinking (greedy and sampled again with `"draft": false` on a drafting target); a grammar that cannot compile must be a 400. `structured.json` keeps each case's request, reply, usage and seconds | every reply obeys, drafted equals undrafted, and the bad regex gets a 400 |
| `structured_speed` | decode speed, greedy, of two long JSON replies with the grammar off and on: one stream (and the grammar undrafted), two grammar streams at once, a plain stream beside a grammar stream against beside a plain one | measured; fails on an error or a grammar reply that is not JSON |
| `sampling` | seeded sampled replies, repeated and undrafted | equal every time |
| `turns` | a conversation that resumes its kept prompt; the third turn resumed, again, and cold | all three equal; reports cached tokens and first-token times |
| `prefill` | one cold prompt at each size in `tokens` (default 2k, 8k, 32k, 128k), words no other prompt starts with; `thinking = true` sends thinking on and times the first reasoning token | measured: prompt tokens over time to the first token; fails on an error or more than `cached_ok` (64) cached tokens |
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
- The `thinking` plan gives a 48k reasoning budget: 49,152 tokens of reasoning, then 1,024 for the answer (`max_tokens`
  50176, the suite's `--reasoning-budget 49152`). Serve it with `--thinking-budget 49152` and `--max-tokens 50176` or more.
- A reply stopped by `max_tokens` is not an answer: the `thinking` check fails on any, and a suite check fails when its
  report counts truncated replies (or, with `--thinking`, records no count at all: a suite older than the fix).

### Reading quality scores: the graders' limits

Read a suite score as what its grader accepted, not as what the model got right. Before saying one mode or build
scores lower, compare the misses themselves (each check's `<name>.json` under `details.misses`).

**MATH-500 (the GLM recipe's `quality/math500.py`): fixed on 2026-10-19.** Until then its `normalise` rejected
correct answers written in some forms:
- **Units:** it stripped `\text{...}` but dropped only a few unit words, so `2000 \text{ calories}` missed.
- **Separators:** `58{,}500` was not 58500.
- **Matrices:** its `("\\ ", "")` replacement deleted half of a matrix row break `\\ `, so a gold matrix written
  with spaces matched no answer.
- **Lists and letters:** `\{3,5,7\}` set braces, a bare list in another order (`-2, 1` for `1,-2`), and `C` for
  `\text{(C)}` all missed.

The fixed grader accepts these; tuples and intervals in brackets keep their order. It also keeps every miss with its
answer, where it used to keep only the first 40, so a run can be regraded when the rules change again.

**Why it mattered:** reasoning replies write units and LaTeX more often, so the old grader understated thinking on.
DeepSeek-V4.1-Flash on one M5 Ultra (target `deepseek-v41-m5`), regraded from the misses each run kept:

| Run | Mode | Old grader | Fixed grader |
|---|---|---|---|
| `20261018-202801-dsv41-quality` | Thinking off | 457/500 | at least 465/500 |
| `20261019-034805-dsv41-thinking` | Thinking on | 451/500 | at least 469/500 |

"At least" because those runs kept only 40 misses each. What is still marked wrong with thinking on is mostly the
same value in another form (`9a+11` for `11+9a`, `11(1+\sqrt5)` for `11\sqrt5+11`) plus four replies with no
boxed answer. Thinking off's are mostly wrong values (56 for 28, 29 for 203) plus 11 with no boxed answer.

**GSM8K (`quality/gsm8k.py`) grades the last number, so formatting does not decide it.** The same DeepSeek runs
scored 247/250 with thinking off and 243/250 with it on. All four extra misses with thinking on, asked again, are
real: the reasoning read ambiguous wording differently from the gold answer:
- "two times older" read as 1 + 2 x 1;
- "when does he start earning" answered with the break-even year, not the year after;
- two others answered a differently set-up question.

There a lower thinking-on score is the model's, not the grader's.

**Scores before and after 2026-10-19 are not comparable:** compare MATH-500 only between runs graded by the same
suite commit. Runs from 2026-10-19 on record it: `identity.suite_commit` in `meta.json`, for every target with a
`suite_dir` (`-dirty` when its checkout had changes).

## Leaderboard

Every recipe we publish also goes on the TensorFold community board (tensorfold.dev/benchmarks):

```bash
tensorfold benchmark login --token-stdin < /secure/upload-token   # once a machine: the contributor token, kept by the CLI
python3 -m harness leaderboard qwen38-27b-5090                      # the recipe down, community-v1, the recipe up, published
python3 -m harness leaderboard qwen38-27b-5090 --no-publish         # the same, the receipt kept local
```

A target's `[leaderboard]` names the public checkpoint (`model`, cached as a Hugging Face snapshot: the board refuses
local directories), the engine `binary`, extra `args`, `env` for the managed server, and `free`, a command that exits 0
once `down` has released the devices. The run takes the target's lock, runs `down`, `tensorfold benchmark`, then `up`
whatever happened, scrubs the receipt, and publishes it with `--yes`. The receipt, the benchmark's output and the
board's answer (submission, status, public URL) stay in `runs/<target>/<stamp>-leaderboard/`. A scrub hit or an
incomplete run publishes nothing. `TENSORFOLD_BENCHMARK_TOKEN` in the environment replaces the stored login for one run.

## Engine rounds

A target whose `[commands]` has `server_log` (the server's log since `$since`, Unix seconds) gets the engine's own
account of each ruler level. A TensorFold native server logs a line for every finished request
(`done … tokens=256 … rounds=55 accepted=200/259`); summed over one level, `<ruler>.engine.json` holds:

- `tokens_a_round`: tokens a stream gets from one round (1 plus its accepted drafts);
- `accept_rate` and `drafts_a_round`: how many drafts a round proposes and how many land;
- `ms_a_round`: the ruler's per-stream rate over `tokens_a_round`, the wall time of one round.

`compare` sets these side by side. A slower level whose tokens a round held is **rounds slower, same drafting**:
admission, the forward or host work between rounds, not the draft planner. Fewer tokens a round is **less
drafted**. On the qwen pair this split a 7% loss at 16 streams to batched prompt admission that a rebase had left
unwired: every round's work was the same, each round took longer.

## Served stats: the ledger and STATS.md / .txt / .pdf

`stats/<target>.json` is the ledger: one entry for every finished run on any machine, with what was served (identity),
every ruler cell (total and per-stream tok/s, first token), the engine's rounds, suite scores and each check's result.
Each target names its `model_name`, `hardware` and `engine`, so the reports group results by model and hardware.

- Every `harness run` and `harness export` adds its run and renders `STATS.md`, `STATS.txt` and `STATS.pdf` again,
  and writes each ledger out readable as `stats/<target>.md`: every run, newest first, with all it measured.
- `STATS.pdf` is typeset (`harness/pdf.py`, standard library only): an overview table, then a page or more a target.
- `python3 -m harness stats` adds every finished run under `runs/` (or the folders you name) and renders.
- The reports open with an overview (one row per model and hardware: one stream, the most streams measured, first
  token, the suite's headline scores), then each target's latest ruler, engine rounds, suite and checks, then its
  history.

`runs/` stays on the machine that ran it; the ledger and the reports are committed, so commit `stats/` and `STATS.*`
with every run you keep (scrub first). Two machines adding runs touch different entries, so pull before you push.

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
- `[session]`: `lock`, `up_retries`, `retry_wait`, `up_timeout`, `health_wait`, `down_wait`, `leave_up`;
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

### qwen38-27b-5090: Qwen3.8-27B 4-bit with image input on one RTX 5090

The [recipe](https://github.com/BobClawblaw/qwen38-27b-vision-rtx-5090) is a systemd service on the machine the harness
runs on. The harness:
- starts and stops it with `sudo -n systemctl start|stop $unit` (passwordless sudo for those two);
- runs the qwen recipe's suite and ruler from a local checkout (`suite_dir`), HumanEval's sandbox included.

Settings:
- **Features off:** capacity and a ruler past one stream (one stream at 262k), media URLs (the unit serves data URLs
  only), and structured output and turns until they are measured on this engine.
- **Identity:** the recipe's commit, the engine checkout's commit (`engine_src`), the served model list.
- **Memory:** `nvidia-smi` used and total.
- **Local values:** `recipe_dir`, `engine_src`, `suite_dir`; `port` (30000) and `unit` (`tensorfold-qwen38`) if yours
  differ.

### nemotron-bolt-5090: Nemotron 3.5 Bolt 74B-A9B with image input on one RTX 5090

NVIDIA's `Nemotron-3.5-Bolt-74B-A9B-24GB` on TensorFold's native CUDA engine. The
[recipe](https://github.com/BobClawblaw/nemotron-bolt-74b-vision-rtx-5090) runs as a plain process on the machine the harness runs on:
- `up` stops the `qwen38-27b-5090` unit first, since the two models don't fit on the card together. It then runs the
  recipe's `serve.sh` through `harness.detach`.
- `down` stops the server by its binary's full path, then waits a few seconds for the card to free its memory.
- the qwen recipe's suite and ruler run from a local checkout (`suite_dir`), HumanEval's sandbox included.

Settings:
- **Features off:** drafts (the checkpoint has no MTP head) and media URLs (data URLs only).
- **Concurrency:** two streams at a 262,144-token window with the vision tower loaded. Kept prompt states live in pinned
  host memory (`PROMPT_CACHE_GIB`, 8 by default).
- **Startup:** two tries, 20 s apart, since a stop frees the card a few seconds after the process exits. It loads in
  about 10 s.
- **Identity:** the recipe's commit, the engine checkout's commit (`engine` in the recipe), the served model list.
- **Local values:** `recipe_dir`, `harness_dir`, `suite_dir`; `port` (30000) if yours differs.

### step5-m5: Step-5-Preview 2-bit on one M5 Ultra Mac

stepfun-ai's Step-5-Preview (604B MoE, 27B active) on TensorFold's native Metal engine, branch `step5-native`. It
isn't a recipe repo yet, so the harness starts the server itself, as a plain process on this machine:
- `up` runs `tensorfold-native serve` through `harness.detach`, its output stamped with Unix seconds by a one-line
  perl filter, so `server_log` can hand each ruler level its own `done` lines.
- the qwen recipe's suite and ruler run from a local checkout (`suite_dir`).
- the checkpoint is `tools/step5_fp8_to_mlx.py`'s: routed experts affine 2-bit in groups of 128, everything else 8-bit
  in groups of 64, with the three MTP layers (`--only-mtp`) and the image tower (`--only-vision`) added.

Settings:
- **Features off:** structured output (not measured yet), turns and prompt cache (the family keeps no prompt states
  yet), media URLs (data URLs only), capacity (one stream).
- **Startup:** one start, 120 s. It loads in about 37 s, warm-up included.
- **Identity:** the engine commit, the binary's SHA-256, `/v1/models`, the chip and its RAM.
- **Memory:** `memory_pressure` and swap. About 171 GiB of weights leave 16.8 GiB of caches under the engine's
  75%-of-RAM limit; `--context 131072` fits.
- **Local values:** `harness_dir`, `engine_dir`, `model_dir`, `suite_dir`, `log_dir`.

Measured on 2026-10-15, M5 Ultra with 256 GB, engine `aa221b11`, greedy (`--plan one-stream`, in the ledger):

| Ruler, one stream | prose | code | structured | list | first token |
|---|---:|---:|---:|---:|---:|
| fresh | 39.2 | 50.6 | 40.7 | 48.2 | 0.23-0.27 s |
| after the suite | 39.2 | 50.6 | 40.6 | 48.1 | 0.23-0.27 s |

Engine rounds: 2.34 tokens a round, 69% of the MTP drafts accepted, 52.4 ms a round. Seeded sampling: 9/9 replies
equal on repeat and undrafted.

| Suite check (suite main `206803c`) | Result |
|---|---|
| drafts | 12/12, drafted 41 tok/s against 26 undrafted |
| behaviour (streaming, multiturn, stop, thinking, copy, max-tokens) | 30/30 |
| tools | 58/60 |
| json | 30/30 |
| gsm8k (50) | 49/50 |
| ifeval (50) | 41/50 loose, 37/50 strict |

The `one-stream` plan runs the suite's checks one stream serves: `soak` and `concurrent` need kept prompt states and
more than one stream. The numbers below are in `stats/notes.md`.

Measured outside the harness:
- **Prompts:** 690 / 668 / 647 / 622 tokens a second at 4k / 8k / 16k / 32k tokens. Past 4k the sparse indexer caps
  each row's keys, so the rate holds. A 131,016-token chat question about the first page of its context was answered
  exactly, 264 s end to end, with at least 23% of memory free throughout.
- **Decode, plain:** 29.6 / 21.9 / 14.7 / 14.5 tokens a second at 20 / 600 / 4,200 / 32,768 tokens of context.
- **Decode, MTP drafts** (three chained layers, every reply token-identical to `"draft": false`): code 25.7 to 44.6 tok/s
  (1.74x, 70% of drafts accepted), prose 26.4 to 34.8 (1.32x, 56%), math 26.2 to 46.0 (1.75x, 75%).
- **Images:** a 1200 x 800 PNG becomes six 504-px crops and a 728-px overview (692 prompt tokens), answered in 2.1 s;
  a 600 x 400 PNG (overview only, 193 tokens) in 0.7 s. The tower's rows are as close to an fp32 run of StepFun's encoder
  as torch's own bf16 run is.

## Plans

`plans/<name>.toml` holds `description`, `restart` and a list of `[[checks]]` (`type`, an optional `name` or `label`,
and the check's options).

| Plan | Restarts | Checks |
|---|---|---|
| `quick` | yes | one stream fresh, the serving checks, one stream after them, then the suite's soak, drafts, concurrent and behaviour checks (the recipe's AGENTS.md requires soak before an engine change ships) |
| `one-stream` | yes | one stream fresh, sampling, the suite's checks one stream serves (drafts, behaviour, tools, json, gsm8k and ifeval at 50), one stream again |
| `full` | yes | ruler at 1/4/8/16 streams, the whole suite, the serving checks, ruler at 1 and 16 after them, capacity |
| `thinking` | no | thinking-on word problems, and the suite's GSM8K with `--thinking` |
