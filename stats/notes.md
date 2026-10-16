## Served earlier, numbers in their READMEs only

These recipes predate the ruler's JSON, so their measurements are not in the ledger; their READMEs hold them.

| model | hardware | engine | recipe |
|---|---|---|---|
| Qwen3.8-Flash-Next, turboderp EXL3 4.05 bpw | 2x NVIDIA DGX Spark (GB10), TP=2 | TensorFold 0.6.6 (Python) with an EXL3 patch | github.com/BobClawblaw/qwen38-flashnext-exl3-2x-dgx-sparks |
| Qwen3.8-Flash-Next (TensorFold 0.6.6 recipe) | 2x NVIDIA DGX Spark (GB10), TP=2 | TensorFold 0.6.6 (Python) | github.com/BobClawblaw/qwen38-flashnext-tensorfold-2x-dgx-sparks |

## Step-5-Preview on one M5 Ultra, final build: measured outside the harness

TensorFold native Metal, branch `step5-native` at engine `6e791da6`: 2,048-row prompt chunks, the prompt cache and the
idle keepalive's kernel tick. Greedy unless said; served with `--parallel 2 --vision` at the default context (227,025).

| what | measured |
|---|---|
| prompt, 4k / 8k / 16k / 32k tokens | 868 / 863 / 840 / 800 tok/s (a 4k prompt right after a pause was 580 before the keepalive fix) |
| 212k-token chat question, one record's code of 10,500 | 2 of 3 right (records 3,000 and 9,800; missed 777), 376 s each, at least 19% of memory free |
| 129k-token chat question | 2 of 2 right (records 777 and 5,000), about 200 s each |
| MTP drafts against `"draft": false`, 200-400-token replies timed with their prompt | identical; code 25.8 to 41.2 tok/s, prose 27.0 to 36.6, math 26.9 to 48.8 |
| prompt cache, an 11.6k-token chat sent again, then two more turns | 15.3 s fresh, 1.8 s again, turns resumed at 11,601; replies identical to `--prompt-cache-gib 0` |
| prompt cache, images (1200 x 800 PNG, 688 tokens) | resent in 2.15 s instead of 3.8 s; replies identical to the cache off |
| a kept state that cannot sit beside its stream (2.4 GiB cache budget) | dropped before the pass; the prompt read again with the same reply |
| a 1-token reply after 2 / 6 / 30 / 120 s idle | 0.17 / 0.18 / 0.18 / 0.19 s (about 3 s before the kernel tick and residency set) |
| two 18k/31k-token chats at once | both right |

## Step-5-Preview on one M5 Ultra, first build (512-row chunks): measured outside the harness

TensorFold native Metal, branch `step5-native` (engine `5ad7660c`, images `aa221b11`), MLX 2-bit experts with the rest
8-bit, greedy, one stream. The harness's `step5-m5` runs hold the ruler and the suite; these are the rest.

| what | measured |
|---|---|
| prompt, 4k / 8k / 16k / 32k tokens | 690 / 668 / 647 / 622 tok/s (the sparse indexer caps each row's keys past 4k) |
| 131,016-token chat question about its first page | answered exactly, 264 s end to end, at least 23% of memory free |
| decode without drafts, 20 / 600 / 4,200 / 32,768 tokens of context | 29.6 / 21.9 / 14.7 / 14.5 tok/s |
| MTP drafts against `"draft": false` (replies token-identical) | code 25.7 to 44.6 tok/s (70% accepted), prose 26.4 to 34.8 (56%), math 26.2 to 46.0 (75%) |
| an image, 1200 x 800 PNG (six 504-px crops and the overview, 692 prompt tokens) | 2.1 s to a 4-token answer |
| an image, 600 x 400 PNG (overview only, 193 prompt tokens) | 0.7 s |
