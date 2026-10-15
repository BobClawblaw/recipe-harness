## Served earlier, numbers in their READMEs only

These recipes predate the ruler's JSON, so their measurements are not in the ledger; their READMEs hold them.

| model | hardware | engine | recipe |
|---|---|---|---|
| Qwen3.8-Flash-Next, turboderp EXL3 4.05 bpw | 2x NVIDIA DGX Spark (GB10), TP=2 | TensorFold 0.6.6 (Python) with an EXL3 patch | github.com/BobClawblaw/qwen38-flashnext-exl3-2x-dgx-sparks |
| Qwen3.8-Flash-Next (TensorFold 0.6.6 recipe) | 2x NVIDIA DGX Spark (GB10), TP=2 | TensorFold 0.6.6 (Python) | github.com/BobClawblaw/qwen38-flashnext-tensorfold-2x-dgx-sparks |

## Step-5-Preview on one M5 Ultra: measured outside the harness

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
