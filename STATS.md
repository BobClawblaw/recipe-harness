# Served stats

Rendered 2026-10-30 01:43 UTC from `stats/*.json`, the ledger every `harness run` and `harness export` adds to (`python3 -m harness stats` renders it again). Aggregate tok/s, greedy, 256-token replies, the recipe's own ruler; engine rounds from the server's own counters.

## Overview: by model and hardware

Aggregate tok/s as prose/code/structured/list; first token in seconds (one stream / the most streams).

| model | hardware | one stream | most streams: total | first token (s) | suite | measured |
|---|---|---:|---:|---:|---|---|
| DeepSeek-V4.1-Flash-1017 EXL3 2.9bpw | 2x NVIDIA DGX Spark (GB10, 128 GB unified each), TP=2 over RoCE | 55/100/62/71 | 4: 106/162/112/179 | 0.19 / 0.73-0.99 |  | 2026-10-18 |
| DeepSeek-V4.1-Flash-1017 EXL3 2.9bpw | 2x NVIDIA DGX Spark (GB10, 128 GB unified each), TP=2 over RoCE | 55/104/63/71 | 8: 135/203/144/203 | 0.19 / 1.35-1.84 |  | 2026-10-18 |
| DeepSeek-V4.1-Flash-1017 EXL3 2.9bpw | 2x NVIDIA DGX Spark (GB10, 128 GB unified each), TP=2 over RoCE | 53/98/61/69 | 4: 106/158/111/176 | 0.20 / 0.75-1.00 |  | 2026-10-18 |
| DeepSeek-V4.1-Flash-1017 EXL3 2.9bpw | 2x NVIDIA DGX Spark (GB10, 128 GB unified each), TP=2 over RoCE | 55/101/63/71 | 4: 104/156/109/173 | 0.19 / 0.41-0.64 |  | 2026-10-17 |
| DeepSeek-V4.1-Flash-1017 EXL3 2.9bpw abliterated | 2x NVIDIA DGX Spark (GB10, 128 GB unified each), TP=2 over RoCE | 65/95/87/95 | 8: 226/319/250/359 | 0.10 / 1.76-3.96 |  | 2026-10-20 |
| DeepSeek-V4.1-Flash-1017, 2/3-bit experts | 1x Apple M5 Ultra (256 GB unified), macOS | 73/104/88/99 | 2: 96/115/111/147 | 0.11 / 0.22-0.28 | tools 58/60, json 30/30, gsm8k 246/250, ifeval 129/150 | 2026-10-23 |
| GLM-5.3-Flash EXL3 4bpw | 2x NVIDIA DGX Spark (GB10, 128 GB unified each), TP=2 over RoCE | 42/60/57/58 |  | 0.17 | json 30/30, ifeval 103/150 | 2026-10-17 |
| GLM-5.3-Flash EXL3 4bpw | 2x NVIDIA DGX Spark (GB10, 128 GB unified each), TP=2 over RoCE | 27/48/39/33 | 8: 78/115/98/110 | 0.18 / 1.49-1.83 |  | 2026-10-17 |
| GLM-5.3-Flash EXL3 4bpw | 2x NVIDIA DGX Spark (GB10, 128 GB unified each), TP=2 over RoCE | -/-/-/- | 16: 107/120/119/130 |  / 2.69-3.38 |  | 2026-10-18 |
| GLM-5.3-Flash EXL3 4bpw | 2x NVIDIA DGX Spark (GB10, 128 GB unified each), TP=2 over RoCE | -/-/-/- | 16: 106/120/131/138 |  / 1.32-1.62 |  | 2026-10-18 |
| GLM-5.3-Flash EXL3 4bpw | 2x NVIDIA DGX Spark (GB10, 128 GB unified each), TP=2 over RoCE | -/-/-/- | 16: 117/134/148/159 |  / 1.34-1.66 |  | 2026-10-18 |
| GLM-5.3-Flash EXL3 4bpw | 2x NVIDIA DGX Spark (GB10, 128 GB unified each), TP=2 over RoCE |  |  |  | json 30/30, ifeval 103/150 | 2026-10-17 |
| GLM-5.3-Flash EXL3 4bpw | 2x NVIDIA DGX Spark (GB10, 128 GB unified each), TP=2 over RoCE | 28/38/33/31 | 16: 124/156/150/145 | 0.18 / 8.50-17.20 |  | 2026-10-16 |
| GLM-5.3-Flash EXL3 4bpw | 2x NVIDIA DGX Spark (GB10, 128 GB unified each), TP=2 over RoCE | 28/39/34/31 | 16: 86/101/100/102 | 0.18 / 3.23-3.72 |  | 2026-10-17 |
| GLM-5.3-Flash, EXL3 4 bpw | 2x NVIDIA DGX Spark (GB10, 128 GB unified each), TP=2 over RoCE | 46/69/57/59 |  | 0.18 | tools 59/60, json 30/30, gsm8k 246/250, humaneval 159/164, ifeval 118/150 | 2026-10-14 |
| GLM-5.3-Flash, MLX 4-bit | 1x Apple M5 Ultra (256 GB unified), macOS | 74/78/78/86 |  | 0.11 | tools 57/60, json 30/30, gsm8k 246/250 | 2026-10-16 |
| Gemma 4 12B, MLX 4-bit + MTP assistant | 1x Apple M5 Ultra (256 GB unified), macOS | 140/223/205/248 |  | 0.04 | tools 58/60, json 30/30, gsm8k 239/250 | 2026-10-16 |
| Gemma 4 12B, oQ8e (8-bit) + MTP assistant | 1x Apple M5 Ultra (256 GB unified), macOS | 93/142/146/158 | 4: 262/324/328/340 | 0.05 / 0.12-0.12 |  | 2026-10-16 |
| Gemma 4 31B, MLX 4-bit + DFlash | 1x Apple M5 Ultra (256 GB unified), macOS | 87/158/157/130 |  | 0.08 |  | 2026-10-16 |
| Gemma 4 31B, oQ8e (8-bit) + DFlash | 1x Apple M5 Ultra (256 GB unified), macOS | 40/63/52/55 | 4: 110/173/142/180 | 0.10 / 0.24-0.27 |  | 2026-10-16 |
| MiniMax-M3.1-Flash, EXL3 3.06 bpw (Mia-AiLab EAQ v1), 256k context | 1x Apple M5 Ultra (256 GB unified), macOS | 32/34/31/32 | 2: 30/39/31/45 | 1.46 / 2.19-2.33 |  | 2026-10-29 |
| MiniMax-M3.1-Flash, EXL3 3.06 bpw (Mia-AiLab EAQ v1), 32k context | 2x NVIDIA DGX Spark (GB10, 128 GB unified each), TP=2 over RoCE | 25/40/30/30 |  | 0.59 |  | 2026-10-28 |
| MiniMax-M3.1-Flash, MLX mixed 3-bit (mix256k), 144k context | 1x Apple M5 Ultra (256 GB unified), macOS | 44/58/48/52 |  | 0.31 |  | 2026-10-27 |
| MiniMax-M3.1-Flash, MLX mixed 4/3-bit (mix34) | 1x Apple M5 Ultra (256 GB unified), macOS | 41/63/48/54 |  | 0.32 |  | 2026-10-27 |
| MiniMax-M3.1-Flash, NVFP4 (15 MoE layers) + 3-bit refit, 32k context | 2x NVIDIA DGX Spark (GB10, 128 GB unified each), TP=2 over RoCE | 23/41/25/32 |  | 0.47 |  | 2026-10-26 |
| MiniMax-M3.1-Flash, NVFP4 (15 MoE layers) + 3-bit refit, dense NVFP4, MXFP8 head, 32k context | 2x NVIDIA DGX Spark (GB10, 128 GB unified each), TP=2 over RoCE | 27/45/33/37 |  | 0.47 | gsm8k 242/250 | 2026-10-26 |
| NVIDIA Nemotron 3.5 Bolt 74B-A9B (24 GB: IQ2_XXS experts, Q8_0, NVFP4 Mamba) + vision | 1x NVIDIA RTX 5090 (32 GB) | 150/150/150/150 |  | 0.03 | tools 58/60, json 30/30, gsm8k 241/250, humaneval 153/164, ifeval 120/150 | 2026-10-15 |
| Nanbeige4.3-33B bf16, drafted by Nanbeige4.1-3B 4-bit | 1x Apple M5 Ultra (256 GB unified), macOS | 114/111/108/85 | 2: 63/64/64/58 | 0.23 / 0.35-0.39 |  | 2026-10-26 |
| Nanbeige4.3-33B bf16, drafted by Nanbeige4.1-3B MLX 4-bit | 1x Apple M5 Ultra (256 GB unified), macOS | 117/111/110/102 |  | 0.23 |  | 2026-10-28 |
| Nanbeige4.3-33B bf16, drafted by Nanbeige4.1-3B bf16 | 1x Apple M5 Ultra (256 GB unified), macOS | 114/98/99/107 | 2: 44/59/54/56 | 0.23 / 0.34-0.39 |  | 2026-10-29 |
| Nanbeige4.3-33B, MLX 4-bit | 1x Apple M5 Ultra (256 GB unified), macOS | 47/46/47/47 | 2: 79/76/79/79 | 0.12 / 0.18-0.20 |  | 2026-10-27 |
| Nanbeige4.3-33B, MLX 8-bit | 1x Apple M5 Ultra (256 GB unified), macOS | 28/28/28/28 |  | 0.15 |  | 2026-10-27 |
| Nanbeige4.3-33B, affine 4bit | 1x Apple M5 Ultra (256 GB unified), macOS | 48/48/49/49 | 2: 85/81/84/85 | 0.10 / 0.16-0.18 |  | 2026-10-26 |
| Nanbeige4.3-33B, affine 8bit | 1x Apple M5 Ultra (256 GB unified), macOS | 29/28/29/29 | 2: 54/52/53/54 | 0.13 / 0.19-0.23 |  | 2026-10-26 |
| Nanbeige4.3-33B, bf16 | 1x Apple M5 Ultra (256 GB unified), macOS | 16/16/16/16 | 2: 32/28/31/32 | 0.23 / 0.34-0.39 |  | 2026-10-28 |
| Ornith-1.5-122B, 4-bit MLX affine (g64) | 1x Apple M5 Ultra (256 GB unified), macOS | 66/67/66/67 | 4: 176/178/178/180 | 0.08 / 0.25-0.35 |  | 2026-10-20 |
| Ornith-1.5-122B, 4-bit MLX affine (g64) | 1x Apple M5 Ultra (256 GB unified), macOS | 93/156/133/149 | 4: 230/315/280/349 | 0.05 / 0.13-0.17 |  | 2026-10-29 |
| Ornith-1.5-122B, 4-bit MLX affine (g64), YaRN x4 to 1M context | 1x Apple M5 Ultra (256 GB unified), macOS | 78/161/106/111 | 4: 447/774/555/871 | 0.06 / 1.58-3.32 | gsm8k 247/250 | 2026-10-26 |
| Ornith-1.5-122B, 8-bit MLX affine (g64) | 1x Apple M5 Ultra (256 GB unified), macOS | 57/112/91/84 | 4: 154/240/188/247 | 0.08 / 0.21-0.28 |  | 2026-10-29 |
| Qwen3.8-27B, MLX 4-bit + DFlash2 | 1x NVIDIA RTX 5090 (32 GB) | 278/536/352/337 | 4: 742/1396/839/1218 | 0.06 / 0.15-0.15 |  | 2026-10-27 |
| Qwen3.8-Flash-Next INT4-Mixed (AutoRound) | 2x NVIDIA DGX Spark (GB10, 128 GB unified each), TP=2 over RoCE | 78/127/102/131 | 16: 305/516/393/527 | 0.04 / 0.46-0.51 | tools 60/60, json 30/30, gsm8k 241/250, humaneval 157/164, ifeval 130/150 | 2026-10-27 |
| Qwen3.8-Flash-Next, 6-bit with vision | 1x Apple M5 Ultra (256 GB unified), macOS | 142/210/173/206 | 2: 198/262/222/272 | 0.11 / 0.17-0.19 |  | 2026-10-17 |
| Qwen3.8-Flash-Next, MLX 6-bit | 1x Apple M5 Ultra (256 GB unified), macOS | 145/206/172/194 | 4: 566/816/673/854 | 0.09 / 1.63-3.07 | gsm8k 242/250, ifeval 134/150 | 2026-10-11 |
| Recursive Flint 40B-A2.5B, MLX INT4 (g64) | 1x Apple M5 Ultra (256 GB unified), macOS | 184/179/194/181 |  | 0.03 |  | 2026-10-28 |
| Spark-X2.6-4B, MLX 8-bit | 1x Apple M5 Ultra (256 GB unified), macOS | 167/167/167/167 | 4: 368/355/370/364 | 0.03 / 0.09-0.13 |  | 2026-10-25 |
| Spark-X2.6-4B, MLX 8-bit | 1x NVIDIA RTX 4090 (24 GB), Windows | 146/144/147/146 | 4: 548/547/552/550 | 0.03 / 0.07-0.07 | tools 53/60, json 30/30, gsm8k 232/250, humaneval 0/0, ifeval 117/150 | 2026-10-25 |
| Spark-X2.6-4B, MLX 8-bit | 1x NVIDIA RTX 5090 (32 GB) | 199/191/203/204 | 4: 716/709/726/729 | 0.03 / 0.06-0.06 |  | 2026-10-26 |
| Spark-X2.6-4B, bf16 | 1x Apple M5 Ultra (256 GB unified), macOS | 106/106/106/106 |  | 0.05 |  | 2026-10-25 |
| Step-5-Preview, MLX 2-bit experts (8-bit rest) + MTP | 1x Apple M5 Ultra (256 GB unified), macOS | 38/50/40/48 |  | 0.24 |  | 2026-10-16 |
| qwen38-27b | ? | 150/230/168/185 |  | 0.10 |  | 2026-10-16 |
| qwen38-27b | ? | 211/398/268/250 |  | 0.10 |  | 2026-10-16 |
| qwen38-27b | ? | 150/229/167/185 |  | 0.10 |  | 2026-10-16 |
| qwen38-27b | ? | 236/437/293/288 |  | 0.10 | gsm8k 222/250 | 2026-10-19 |
| qwen38-27b | ? | 210/397/266/259 |  | 0.10 |  | 2026-10-19 |

## DeepSeek-V4.1-Flash-1017, 2/3-bit experts on 1x Apple M5 Ultra (256 GB unified), macOS

Target `deepseek-v41-m5`: DeepSeek-V4.1-Flash-1017, 2/3-bit experts with images and DSpark drafts, TensorFold native Metal on one M5 Ultra. Engine: TensorFold native, Metal; served as `DeepSeek-V4.1-Flash`. Latest: run `20261023-021709-dsv41-quality-off` (2026-10-23 02:17, plan dsv41-quality-off, done).

Serving: engine_commit `5babc696`; binary_sha256 `a39c47da690de2f9362f88aa67232798f8cfa6fe1f469b99df381526c15f57b5`; served_model `{"object": "list", "data": [{"id": "DeepSeek-V4.1-Flash-Abliterated", "object": "model", "`; checkpoint `{'repo': 'deepseek-ai/DeepSeek-V4.1-Flash-1017', 'expert_bits': 2, 'layer_bits': '10-29:3'`; chip `Apple M5 Ultra; 274877906944`; suite_commit `277c842a1481`

### suite

| check | passed |
|---|---:|
| drafts | 12/12 |
| streaming | 4/4 |
| multiturn | 8/8 |
| stop | 3/3 |
| thinking | 10/10 |
| copy | 2/2 |
| max-tokens | 3/3 |
| tools | 58/60 |
| json | 30/30 |
| ifeval | 129/150 |
| gsm8k | 246/250 |
| mgsm | 218/240 |
| mmlu | 307/342 |
| math500 | 468/500 |

### checks

| check | result |
|---|---|
| memory-idle | measured: mac: System-wide memory free percentage: 93%; total = 1024.00M  us |

### history

| run | plan | status | 1 stream code | 16 streams code | 16 streams first token | suite |
|---|---|---|---:|---:|---:|---|
| 2026-10-23 02:17 | dsv41-quality-off | done |  |  |  | 1498/1614 |
| 2026-10-23 02:13 | speed | done | 104.5 |  |  |  |
| 2026-10-20 09:28 | dsv41-quality-off | done |  |  |  | 1488/1614 |
| 2026-10-20 09:19 | dsv41-speed | done | 104.9 |  |  |  |
| 2026-10-20 08:25 | dsv41-speed | done | 87.7 |  |  |  |
| 2026-10-20 06:19 | dsv41-speed | done | 86.4 |  |  |  |
| 2026-10-20 04:35 | dsv41-quality-off | done |  |  |  | 1490/1614 |
| 2026-10-20 04:30 | dsv41-speed | done | 88.5 |  |  |  |
| 2026-10-19 09:08 | dsv41-speed | done | 90.5 |  |  |  |
| 2026-10-18 20:28 | dsv41-quality | done |  |  |  | 1487/1614 |
| 2026-10-18 18:44 | speed | done | 87.5 |  |  |  |
| 2026-10-18 17:24 | speed | done | 92.5 |  |  |  |
| 2026-10-17 19:33 | speed | done | 96.3 |  |  |  |
| 2026-10-17 17:54 | speed | done | 90.5 |  |  |  |
| 2026-10-17 14:57 | speed | done | 56.7 |  |  |  |

## DeepSeek-V4.1-Flash-1017 EXL3 2.9bpw abliterated on 2x NVIDIA DGX Spark (GB10, 128 GB unified each), TP=2 over RoCE

Target `dsv41-1017-ablit`: DeepSeek-V4.1-Flash-1017 EXL3 2.9 bpw abliterated, TensorFold native (Zig) TP=2 on two DGX Sparks, 4 slots, 1M window. Engine: TensorFold native (Zig, CUDA) + EXL3 TP=2 kit, recipe defaults (replay prefill, DSpark drafts, thinking on); served as `DeepSeek-V4.1-Flash-1017`. Latest: run `20261020-131445-dsv41-speed8` (2026-10-20 13:14, plan dsv41-speed8, done).

Serving: image `d9acaf504779`; patches `8eb5919ff0a4`; ablit `0bdc2036`; served `{"object": "list", "data": [{"id": "DeepSeek-V4.1-Flash-1017", "object": "model", "created`; pack `6c4679e6407806ab`; suite_commit `35b24fedcc37`

### ruler-streams

| streams | prose total (a stream) | code total (a stream) | structured total (a stream) | list total (a stream) | first token |
|---:|---:|---:|---:|---:|---:|
| 1 | 65.3 (65.3) | 94.6 (94.6) | 87.3 (87.3) | 94.9 (94.9) | 0.10-0.16 s |
| 2 | 91.9 (45.9) | 132.3 (66.2) | 109.1 (54.6) | 163.3 (81.6) | 0.15-0.24 s |
| 4 | 119.5 (29.9) | 164.3 (40.0) | 136.1 (34.3) | 211.2 (51.4) | 0.25-0.41 s |
| 8 | 226.2 (27.9) | 318.9 (41.1) | 249.9 (30.6) | 358.8 (43.0) | 1.76-3.96 s |

### checks

| check | result |
|---|---|
| memory-idle | measured: head 6.5 GiB available; worker 8.4 GiB available |

### history

| run | plan | status | 1 stream code | 16 streams code | 16 streams first token | suite |
|---|---|---|---:|---:|---:|---|
| 2026-10-20 13:14 | dsv41-speed8 | done | 94.6 |  |  |  |
| 2026-10-20 13:05 | quick | done | 94.3 |  |  | 114/114 |
| 2026-10-20 12:55 | quick | done | 94.1 |  |  | 114/114 |

## DeepSeek-V4.1-Flash-1017 EXL3 2.9bpw on 2x NVIDIA DGX Spark (GB10, 128 GB unified each), TP=2 over RoCE

Target `dsv41-1017-gb10-native-vision`: DeepSeek-V4.1-Flash-1017 EXL3 2.9 bpw on native TensorFold (main + jayleaton's kit engine 9131e10a ported onto it), native images and video, TP=2 on two DGX Sparks, 4 slots, pool 200K. Engine: TensorFold native (Zig, CUDA): main 9ccf4727 + the DeepSeek-V4.1 kit engine, vision tower (TF_DSV41_IMAGES=native), video as sampled frames, DSpark drafts; served as `DeepSeek-V4.1-Flash-TF`. Latest: run `20261018-032401-dsv41-speed` (2026-10-18 03:24, plan dsv41-speed, done).

Serving: image `7b3d42e0e5865d34`; pack `778baeaf9fbcd351`

### ruler-streams

| streams | prose total (a stream) | code total (a stream) | structured total (a stream) | list total (a stream) | first token |
|---:|---:|---:|---:|---:|---:|
| 1 | 55.2 (55.2) | 100.4 (100.4) | 62.5 (62.5) | 71.4 (71.4) | 0.19-0.26 s |
| 2 | 81.0 (40.5) | 124.9 (62.5) | 84.2 (42.1) | 143.6 (71.8) | 0.31-0.40 s |
| 4 | 106.5 (26.4) | 161.6 (40.0) | 111.9 (26.9) | 178.7 (43.1) | 0.73-0.99 s |

### checks

| check | result |
|---|---|
| memory-idle | measured: head 6.6 GiB available |

### history

| run | plan | status | 1 stream code | 16 streams code | 16 streams first token | suite |
|---|---|---|---:|---:|---:|---|
| 2026-10-18 03:24 | dsv41-speed | done | 100.4 |  |  |  |

## DeepSeek-V4.1-Flash-1017 EXL3 2.9bpw on 2x NVIDIA DGX Spark (GB10, 128 GB unified each), TP=2 over RoCE

Target `dsv41-1017-gb10-native-vision8`: DeepSeek-V4.1-Flash-1017 EXL3 2.9 bpw on native TensorFold (main + the kit engine), native images and video, TP=2 on two DGX Sparks, 8 slots, pool 400K, prefill-dip reserve 2 GiB. Engine: TensorFold native (Zig, CUDA): main 9ccf4727 + the DeepSeek-V4.1 kit engine, vision tower, video as frames, DSpark drafts, 8 slots; served as `DeepSeek-V4.1-Flash-TF`. Latest: run `20261018-092218-dsv41-speed8` (2026-10-18 09:22, plan dsv41-speed8, done).

Serving: image `7b3d42e0e5865d34`; pack `778baeaf9fbcd351`

### ruler-streams

| streams | prose total (a stream) | code total (a stream) | structured total (a stream) | list total (a stream) | first token |
|---:|---:|---:|---:|---:|---:|
| 1 | 55.4 (55.4) | 103.5 (103.5) | 62.7 (62.7) | 70.9 (70.9) | 0.19-0.26 s |
| 2 | 81.5 (40.7) | 126.2 (63.1) | 89.4 (44.7) | 142.7 (71.4) | 0.30-0.48 s |
| 4 | 108.8 (26.8) | 163.8 (40.3) | 113.7 (28.4) | 180.4 (44.4) | 0.71-0.85 s |
| 8 | 134.8 (16.7) | 202.7 (25.4) | 143.6 (17.4) | 203.3 (24.8) | 1.35-1.84 s |

### checks

| check | result |
|---|---|
| memory-idle | measured: head 6.3 GiB available |

### history

| run | plan | status | 1 stream code | 16 streams code | 16 streams first token | suite |
|---|---|---|---:|---:|---:|---|
| 2026-10-18 09:22 | dsv41-speed8 | done | 103.5 |  |  |  |

## DeepSeek-V4.1-Flash-1017 EXL3 2.9bpw on 2x NVIDIA DGX Spark (GB10, 128 GB unified each), TP=2 over RoCE

Target `dsv41-1017-gb10-native`: DeepSeek-V4.1-Flash-1017 EXL3 2.9 bpw on native TensorFold (main + the deepseek_v41 CUDA family, PRs 667-727), TP=2 on two DGX Sparks, 4 slots, pool 900K. Engine: TensorFold native (Zig, CUDA): main 9ccf4727 + deepseek_v41 series, kit serving profile, DSpark drafts, images as placeholder; served as `DeepSeek-V4.1-Flash-TF`. Latest: run `20261018-020350-dsv41-speed` (2026-10-18 02:03, plan dsv41-speed, done).

Serving: image `00b298dda4527ad6`; pack `778baeaf9fbcd351`

### ruler-streams

| streams | prose total (a stream) | code total (a stream) | structured total (a stream) | list total (a stream) | first token |
|---:|---:|---:|---:|---:|---:|
| 1 | 53.3 (53.3) | 98.1 (98.1) | 61.0 (61.0) | 69.3 (69.3) | 0.20-0.28 s |
| 2 | 78.4 (39.2) | 121.8 (60.9) | 82.5 (41.3) | 139.0 (69.5) | 0.30-0.42 s |
| 4 | 105.7 (26.2) | 158.5 (39.4) | 110.6 (26.5) | 176.4 (41.4) | 0.75-1.00 s |

### checks

| check | result |
|---|---|
| memory-idle | measured: head 6.3 GiB available |

### history

| run | plan | status | 1 stream code | 16 streams code | 16 streams first token | suite |
|---|---|---|---:|---:|---:|---|
| 2026-10-18 02:03 | dsv41-speed | done | 98.1 |  |  |  |

## DeepSeek-V4.1-Flash-1017 EXL3 2.9bpw on 2x NVIDIA DGX Spark (GB10, 128 GB unified each), TP=2 over RoCE

Target `dsv41-1017-gb10`: DeepSeek-V4.1-Flash-1017 EXL3 2.9 bpw, jayleaton's DeepSeek-V4.1 recipe (Python, TensorFold 0.6.0 + patches), TP=2 on two DGX Sparks, 4 slots. Engine: TensorFold 0.6.0 (Python) + jayleaton's DeepSeek-V4.1 patches, recipe defaults (replay prefill, DSpark drafts); served as `DeepSeek-V4.1-Flash-TF`. Latest: run `20261017-231853-dsv41-speed` (2026-10-17 23:18, plan dsv41-speed, done).

Serving: image `eb2f599de2fb618a`; pack `778baeaf9fbcd351`

### ruler-streams

| streams | prose total (a stream) | code total (a stream) | structured total (a stream) | list total (a stream) | first token |
|---:|---:|---:|---:|---:|---:|
| 1 | 54.7 (54.7) | 100.6 (100.6) | 62.6 (62.6) | 71.3 (71.3) | 0.19-0.26 s |
| 2 | 77.4 (38.7) | 126.5 (63.3) | 84.0 (42.0) | 142.6 (71.3) | 0.30-0.39 s |
| 4 | 103.5 (25.4) | 155.8 (38.4) | 109.0 (27.7) | 173.2 (41.0) | 0.41-0.64 s |

### checks

| check | result |
|---|---|
| memory-idle | measured: head 8.1 GiB available |

### history

| run | plan | status | 1 stream code | 16 streams code | 16 streams first token | suite |
|---|---|---|---:|---:|---:|---|
| 2026-10-17 23:18 | dsv41-speed | done | 100.6 |  |  |  |

## Recursive Flint 40B-A2.5B, MLX INT4 (g64) on 1x Apple M5 Ultra (256 GB unified), macOS

Target `flint-40b-native-m5`: Recursive Flint 40B-A2.5B, MLX INT4 (g64), TensorFold native Metal on one M5 Ultra. Engine: TensorFold native, Metal; served as `flint`. Latest: run `20261028-091435-quick` (2026-10-28 09:14, plan quick, done).

Serving: engine_commit `99d178f80`; binary_sha256 `a78d9139c491883aa85c21572cf2f16a172abeec97d474e3a0e5b0c15e64891a`; served_model `{"object": "list", "data": [{"id": "flint", "object": "model", "created": 1793196884, "own`; chip `Apple M5 Ultra; 274877906944`; suite_commit `21db9b23f7be`

### ruler-fresh

| streams | prose total (a stream) | code total (a stream) | structured total (a stream) | list total (a stream) | first token |
|---:|---:|---:|---:|---:|---:|
| 1 | 184.3 (184.3) | 179.2 (179.2) | 194.0 (194.0) | 180.6 (180.6) | 0.03-0.04 s |

Engine rounds (ruler-fresh):

| streams | tokens a round | drafts a round | accepted | ms a round | requests |
|---:|---:|---:|---:|---:|---:|
| 1 | 1.044 | 0.076 | 52% | 5.66 | 12 |

### ruler-after

| streams | prose total (a stream) | code total (a stream) | structured total (a stream) | list total (a stream) | first token |
|---:|---:|---:|---:|---:|---:|
| 1 | 186.5 (186.5) | 181.2 (181.2) | 196.1 (196.1) | 182.7 (182.7) | 0.03-0.04 s |

Engine rounds (ruler-after):

| streams | tokens a round | drafts a round | accepted | ms a round | requests |
|---:|---:|---:|---:|---:|---:|
| 1 | 1.047 | 0.081 | 52% | 5.61 | 13 |

### suite

| check | passed |
|---|---:|
| soak | 60/60 |
| drafts | 12/12 |
| concurrent | 12/12 |
| streaming | 4/4 |
| multiturn | 8/8 |
| stop | 3/3 |
| thinking | 10/10 |
| copy | 1/2 |
| max-tokens | 3/3 |

### checks

| check | result |
|---|---|
| memory-idle | measured: mac: System-wide memory free percentage: 87%; total = 4096.00M  us |
| structured | pass: 18/18 obey, drafted == plain 12/12; a bad regex -> 400 |
| tools | pass: 5/5 tool cases right |
| sampling | pass: 9/9 seeded replies equal on repeat and undrafted; 0 errors |
| turns | pass: resumed == again: True; cold (after a restart): True; cached 4507 of 4627; ttft resumed 0.067s, cold 0.712s |
| urls | FAIL: public 400; loopback 400; http 400; unexpected: ['public'] |

### history

| run | plan | status | 1 stream code | 16 streams code | 16 streams first token | suite |
|---|---|---|---:|---:|---:|---|
| 2026-10-28 09:14 | quick | done | 179.2 |  |  | 113/114 |
| 2026-10-28 03:49 | streams | done | 177.8 |  |  | 24/24 |
| 2026-10-28 03:44 | together | done |  |  |  | 24/24 |
| 2026-10-28 03:39 | quick | done | 179.0 |  |  | 113/114 |
| 2026-10-28 01:33 | quick | done | 171.7 |  |  | 113/114 |
| 2026-10-28 00:53 | quick | done | 1284.1 |  |  | 107/114 |
| 2026-10-28 00:47 | together | done |  |  |  | 24/24 |
| 2026-10-28 00:41 | quick | done | 0.0 |  |  | 102/114 |
| 2026-10-27 21:31 | quality-off | done | 176.3 |  |  | 1457/2017 |
| 2026-10-27 21:03 | together | done |  |  |  | 24/24 |
| 2026-10-27 20:58 | quick | done | 178.5 |  |  | 113/114 |
| 2026-10-25 08:00 | quick | done | 177.8 |  |  | 113/114 |
| 2026-10-21 19:17 | mlx-speed | done | 177.0 |  |  |  |
| 2026-10-21 19:14 | speed | done | 177.6 |  |  |  |
| 2026-10-21 18:22 | mlx-speed | done | 177.0 |  |  |  |
| 2026-10-21 18:21 | speed | done | 176.2 |  |  |  |
| 2026-10-21 17:55 | mlx-speed | done | 166.2 |  |  |  |
| 2026-10-21 17:53 | speed | done | 164.9 |  |  |  |
| 2026-10-21 17:23 | speed | done | 132.7 |  |  |  |
| 2026-10-21 17:06 | mlx-speed | done | 131.3 |  |  |  |

## Gemma 4 12B, MLX 4-bit + MTP assistant on 1x Apple M5 Ultra (256 GB unified), macOS

Target `gemma4-12b-m5`: Gemma 4 12B 4-bit (groups of 64), MTP assistant drafts, images, TensorFold native Metal on one M5 Ultra. Engine: TensorFold native, Metal; served as `gemma4-12b`. Latest: run `20261016-113616-g12-quality` (2026-10-16 11:36, plan g12-quality, done).

Serving: engine_commit `74005ebe`; binary_sha256 `215b4b7e3cd14a9d8178b4dc885d9f1dffbebd0f4ec2e9b274653820b71da8d2`; served_model `{"object": "list", "data": [{"id": "gemma4-12b", "object": "model", "created": 1792168585,`; chip `Apple M5 Ultra; 274877906944`

### suite

| check | passed |
|---|---:|
| tools | 58/60 |
| json | 30/30 |
| gsm8k | 239/250 |
| mmlu | 264/342 |

### history

| run | plan | status | 1 stream code | 16 streams code | 16 streams first token | suite |
|---|---|---|---:|---:|---:|---|
| 2026-10-16 11:36 | g12-quality | done |  |  |  | 591/682 |
| 2026-10-16 11:31 | quick | done | 223.3 |  |  | 112/114 |

## Gemma 4 12B, oQ8e (8-bit) + MTP assistant on 1x Apple M5 Ultra (256 GB unified), macOS

Target `gemma4-12b-oq8e-m5`: Gemma 4 12B oQ8e (8-bit, groups of 64), MTP assistant drafts, images, TensorFold native Metal on one M5 Ultra. Engine: TensorFold native, Metal; served as `gemma4-12b-oq8e`. Latest: run `20261016-175459-speed` (2026-10-16 17:54, plan speed, done).

Serving: engine_commit `d9e36b7f`; binary_sha256 `2e29fee5da96ec1ffb1ba41302ac949dc12205572154f21b800823450eb4b2b0`; served_model `{"object": "list", "data": [{"id": "gemma4-12b-oq8e", "object": "model", "created": 179219`; chip `Apple M5 Ultra; 274877906944`

### ruler-fresh

| streams | prose total (a stream) | code total (a stream) | structured total (a stream) | list total (a stream) | first token |
|---:|---:|---:|---:|---:|---:|
| 1 | 92.8 (92.8) | 142.3 (142.3) | 145.7 (145.7) | 158.1 (158.1) | 0.05-0.05 s |
| 4 | 261.5 (64.8) | 324.2 (81.3) | 328.5 (80.7) | 340.0 (83.6) | 0.12-0.12 s |

Engine rounds (ruler-fresh):

| streams | tokens a round | drafts a round | accepted | ms a round | requests |
|---:|---:|---:|---:|---:|---:|
| 1 | 3.55 | 5.525 | 47% | 26.35 | 12 |
| 4 | 2.944 | 3.177 | 62% | 37.94 | 49 |

### suite

| check | passed |
|---|---:|
| drafts | 12/12 |
| concurrent | 12/12 |

### checks

| check | result |
|---|---|
| structured | pass: 18/18 obey; a bad regex -> 400 |

### history

| run | plan | status | 1 stream code | 16 streams code | 16 streams first token | suite |
|---|---|---|---:|---:|---:|---|
| 2026-10-16 17:54 | speed | done | 142.3 |  |  | 24/24 |
| 2026-10-16 17:37 | speed | done | 141.2 |  |  | 24/24 |

## Gemma 4 31B, MLX 4-bit + DFlash on 1x Apple M5 Ultra (256 GB unified), macOS

Target `gemma4-31b-m5`: Gemma 4 31B 4-bit (groups of 64), DFlash drafts, images, TensorFold native Metal on one M5 Ultra. Engine: TensorFold native, Metal; served as `gemma4-31b`. Latest: run `20261016-085420-quick` (2026-10-16 08:54, plan quick, done).

Serving: engine_commit `e8b60549`; binary_sha256 `d90e44c9818187ae4bc61d06312989cd796033b5dea6e0fc02164fe2730660fe`; served_model `{"object": "list", "data": [{"id": "gemma4-31b", "object": "model", "created": 1792158874,`; chip `Apple M5 Ultra; 274877906944`

### ruler-fresh

| streams | prose total (a stream) | code total (a stream) | structured total (a stream) | list total (a stream) | first token |
|---:|---:|---:|---:|---:|---:|
| 1 | 87.1 (87.1) | 157.9 (157.9) | 156.7 (156.7) | 130.4 (130.4) | 0.08-0.10 s |

Engine rounds (ruler-fresh):

| streams | tokens a round | drafts a round | accepted | ms a round | requests |
|---:|---:|---:|---:|---:|---:|
| 1 | 3.288 | 13.003 | 18% | 24.71 | 12 |

### ruler-after

| streams | prose total (a stream) | code total (a stream) | structured total (a stream) | list total (a stream) | first token |
|---:|---:|---:|---:|---:|---:|
| 1 | 92.1 (92.1) | 161.4 (161.4) | 146.6 (146.6) | 126.1 (126.1) | 0.09-0.10 s |

Engine rounds (ruler-after):

| streams | tokens a round | drafts a round | accepted | ms a round | requests |
|---:|---:|---:|---:|---:|---:|
| 1 | 3.333 | 13.215 | 18% | 25.34 | 17 |

### suite

| check | passed |
|---|---:|
| soak | 60/60 |
| drafts | 12/12 |
| concurrent | 12/12 |
| streaming | 4/4 |
| multiturn | 8/8 |
| stop | 3/3 |
| thinking | 10/10 |
| copy | 2/2 |
| max-tokens | 3/3 |

### checks

| check | result |
|---|---|
| memory-idle | measured: mac: System-wide memory free percentage: 75%; total = 3072.00M  us |
| structured | pass: 18/18 obey; a bad regex -> 400 |
| sampling | pass: 9/9 seeded replies equal on repeat and undrafted; 0 errors |
| turns | pass: resumed == again == cold: True; cached 5494 of 5564; ttft resumed 0.137s, cold 0.137s |

### history

| run | plan | status | 1 stream code | 16 streams code | 16 streams first token | suite |
|---|---|---|---:|---:|---:|---|
| 2026-10-16 08:54 | quick | done | 157.9 |  |  | 114/114 |
| 2026-10-16 06:28 | quick | done | 156.5 |  |  | 114/114 |
| 2026-10-15 20:09 | quick | done | 153.8 |  |  | 114/114 |

## Gemma 4 31B, oQ8e (8-bit) + DFlash on 1x Apple M5 Ultra (256 GB unified), macOS

Target `gemma4-31b-oq8e-m5`: Gemma 4 31B oQ8e (8-bit, groups of 64), DFlash drafts, images, TensorFold native Metal on one M5 Ultra. Engine: TensorFold native, Metal; served as `gemma4-31b-oq8e`. Latest: run `20261016-180201-speed` (2026-10-16 18:02, plan speed, done).

Serving: engine_commit `d9e36b7f`; binary_sha256 `2e29fee5da96ec1ffb1ba41302ac949dc12205572154f21b800823450eb4b2b0`; served_model `{"object": "list", "data": [{"id": "gemma4-31b-oq8e", "object": "model", "created": 179219`; chip `Apple M5 Ultra; 274877906944`

### ruler-fresh

| streams | prose total (a stream) | code total (a stream) | structured total (a stream) | list total (a stream) | first token |
|---:|---:|---:|---:|---:|---:|
| 1 | 40.3 (40.3) | 63.1 (63.1) | 52.4 (52.4) | 54.8 (54.8) | 0.10-0.11 s |
| 4 | 109.7 (27.7) | 172.9 (44.8) | 141.5 (34.2) | 180.3 (44.3) | 0.24-0.27 s |

Engine rounds (ruler-fresh):

| streams | tokens a round | drafts a round | accepted | ms a round | requests |
|---:|---:|---:|---:|---:|---:|
| 1 | 2.759 | 10.847 | 16% | 52.41 | 12 |
| 4 | 2.384 | 3.645 | 38% | 63.19 | 49 |

### suite

| check | passed |
|---|---:|
| drafts | 12/12 |
| concurrent | 12/12 |

### checks

| check | result |
|---|---|
| structured | pass: 18/18 obey; a bad regex -> 400 |

### history

| run | plan | status | 1 stream code | 16 streams code | 16 streams first token | suite |
|---|---|---|---:|---:|---:|---|
| 2026-10-16 18:02 | speed | done | 63.1 |  |  | 24/24 |

## GLM-5.3-Flash EXL3 4bpw on 2x NVIDIA DGX Spark (GB10, 128 GB unified each), TP=2 over RoCE

Target `glm53-exl3-gb10-best`: GLM-5.3-Flash EXL3 4bpw, families/glm with 4-bit dense / 8-bit head, DFlash2 and 16 streams (PRs 855+979+984 and packing), TP=2 on two DGX Sparks. Engine: TensorFold native, CUDA: families/glm, packed linears (4/8, bf16 freed), DFlash2, 16 streams, prompts together (prefill_many); served as `GLM-5.3-Flash-EXL3`. Latest: run `20261017-195233-glm-ab-ifeval` (2026-10-17 19:52, plan glm-ab-ifeval, done).

Serving: binary `cf50867102a60c38`

### suite

| check | passed |
|---|---:|
| ifeval | 103/150 |
| json | 30/30 |

### history

| run | plan | status | 1 stream code | 16 streams code | 16 streams first token | suite |
|---|---|---|---:|---:|---:|---|
| 2026-10-17 19:52 | glm-ab-ifeval | done |  |  |  | 133/180 |
| 2026-10-17 16:52 | glm-quality | done | 59.6 |  |  | 348/400 |
| 2026-10-17 16:26 | glm-streams | done | 59.5 | 131.3 | 1.27-1.66 s | 24/24 |
| 2026-10-17 15:56 | glm-streams | done | 67.7 | 132.8 | 1.23-1.59 s | 15/24 |
| 2026-10-17 15:28 | glm-streams | done | 68.3 | 127.5 | 2.63-3.30 s | 24/24 |
| 2026-10-17 14:38 | glm-streams | done | 68.7 | 123.7 | 1.77-2.24 s | 24/24 |
| 2026-10-17 12:40 | glm-streams | done | 69.4 | 125.0 | 2.55-3.17 s | 24/24 |
| 2026-10-17 11:31 | glm-streams | done | 69.8 | 136.4 | 2.55-3.14 s | 24/24 |

## GLM-5.3-Flash EXL3 4bpw on 2x NVIDIA DGX Spark (GB10, 128 GB unified each), TP=2 over RoCE

Target `glm53-exl3-gb10-dflash2`: GLM-5.3-Flash EXL3 4bpw, families/glm with DFlash2 drafts (--drafter, 4-bit), TP=2 on two DGX Sparks. Engine: TensorFold native, CUDA: families/glm + DFlash2 (incoai/GLM-5.3-Flash-DFlash2, opt-in); served as `GLM-5.3-Flash-EXL3`. Latest: run `20261017-003221-glm-streams8` (2026-10-17 00:32, plan glm-streams8, done).

Serving: binary `511e7e0521628504`

### ruler-streams

| streams | prose total (a stream) | code total (a stream) | structured total (a stream) | list total (a stream) | first token |
|---:|---:|---:|---:|---:|---:|
| 1 | 27.3 (27.3) | 48.4 (48.4) | 39.2 (39.2) | 33.1 (33.1) | 0.18-0.24 s |
| 4 | 60.0 (14.7) | 84.4 (20.8) | 75.6 (19.2) | 88.1 (21.6) | 0.71-0.88 s |
| 8 | 78.1 (9.7) | 115.4 (14.3) | 98.4 (12.4) | 109.8 (12.9) | 1.49-1.83 s |

### suite-together

| check | passed |
|---|---:|
| concurrent | 12/12 |
| drafts | 12/12 |

### history

| run | plan | status | 1 stream code | 16 streams code | 16 streams first token | suite |
|---|---|---|---:|---:|---:|---|
| 2026-10-17 00:32 | glm-streams8 | done | 48.4 |  |  | 24/24 |

## GLM-5.3-Flash EXL3 4bpw on 2x NVIDIA DGX Spark (GB10, 128 GB unified each), TP=2 over RoCE

Target `glm53-exl3-gb10-main`: TensorFold main 76aafcf2 (with #855, #979, #984, #995 merged): GLM-5.3-Flash EXL3 4bpw, DFlash2, 16 streams, TP=2 on two DGX Sparks. Engine: TensorFold native, CUDA: families/glm (main); served as `GLM-5.3-Flash-EXL3`. Latest: run `20261018-131205-glm-qual1014` (2026-10-18 13:12, plan glm-qual1014, done).

Serving: binary `e2169dae62202aec`

### ruler-c1-16

| streams | prose total (a stream) | code total (a stream) | structured total (a stream) | list total (a stream) | first token |
|---:|---:|---:|---:|---:|---:|
| 1 | 42.8 (42.3) | 67.2 (67.4) | 55.3 (54.8) | 53.1 (52.9) | 0.16-0.22 s |

### ruler-streams

| streams | prose total (a stream) | code total (a stream) | structured total (a stream) | list total (a stream) | first token |
|---:|---:|---:|---:|---:|---:|
| 8 | 90.0 (11.2) | 120.8 (15.1) | 114.7 (14.1) | 115.5 (14.1) | 1.23-1.57 s |
| 16 | 107.2 (6.6) | 119.6 (7.3) | 119.4 (7.3) | 129.6 (8.1) | 2.69-3.38 s |

### suite

| check | passed |
|---|---:|
| concurrent | 12/12 |
| drafts | 12/12 |

### history

| run | plan | status | 1 stream code | 16 streams code | 16 streams first token | suite |
|---|---|---|---:|---:|---:|---|
| 2026-10-18 13:12 | glm-qual1014 | done |  | 119.6 | 2.69-3.38 s | 24/24 |

## GLM-5.3-Flash EXL3 4bpw on 2x NVIDIA DGX Spark (GB10, 128 GB unified each), TP=2 over RoCE

Target `glm53-exl3-gb10-many-mtp`: #1014 merged onto TensorFold main 76aafcf2, MTP head only (no --drafter), GLM-5.3-Flash EXL3 4bpw, TP=2. Engine: TensorFold native, CUDA: families/glm (many-mtp); served as `GLM-5.3-Flash-EXL3`. Latest: run `20261018-205115-glm-qual1014` (2026-10-18 20:51, plan glm-qual1014, done).

Serving: binary `4f1a478269c0e4fa`

### ruler-c1-16

| streams | prose total (a stream) | code total (a stream) | structured total (a stream) | list total (a stream) | first token |
|---:|---:|---:|---:|---:|---:|
| 1 | 42.1 (41.9) | 52.5 (52.2) | 50.2 (49.9) | 49.0 (49.2) | 0.17-0.22 s |

### ruler-streams

| streams | prose total (a stream) | code total (a stream) | structured total (a stream) | list total (a stream) | first token |
|---:|---:|---:|---:|---:|---:|
| 8 | 74.8 (9.3) | 95.5 (11.9) | 100.9 (12.6) | 106.0 (13.2) | 0.84-1.05 s |
| 16 | 105.9 (6.6) | 119.7 (7.3) | 131.4 (8.3) | 138.3 (8.5) | 1.32-1.62 s |

### suite

| check | passed |
|---|---:|
| concurrent | 12/12 |
| drafts | 12/12 |

### history

| run | plan | status | 1 stream code | 16 streams code | 16 streams first token | suite |
|---|---|---|---:|---:|---:|---|
| 2026-10-18 20:51 | glm-qual1014 | done |  | 119.7 | 1.32-1.62 s | 24/24 |
| 2026-10-18 14:04 | glm-qual1014 | done |  | 118.6 | 1.28-1.58 s | 24/24 |

## GLM-5.3-Flash EXL3 4bpw on 2x NVIDIA DGX Spark (GB10, 128 GB unified each), TP=2 over RoCE

Target `glm53-exl3-gb10-many`: #1014 merged onto TensorFold main 76aafcf2: batched prompts (prefill_many) with DFlash2's feed and the hold fix, GLM-5.3-Flash EXL3 4bpw, TP=2. Engine: TensorFold native, CUDA: families/glm (many); served as `GLM-5.3-Flash-EXL3`. Latest: run `20261018-202804-glm-qual1014` (2026-10-18 20:28, plan glm-qual1014, done).

Serving: binary `4f1a478269c0e4fa`

### ruler-c1-16

| streams | prose total (a stream) | code total (a stream) | structured total (a stream) | list total (a stream) | first token |
|---:|---:|---:|---:|---:|---:|
| 1 | 42.5 (42.6) | 67.6 (68.2) | 56.1 (55.9) | 55.8 (53.2) | 0.17-0.23 s |

### ruler-streams

| streams | prose total (a stream) | code total (a stream) | structured total (a stream) | list total (a stream) | first token |
|---:|---:|---:|---:|---:|---:|
| 8 | 92.4 (11.6) | 131.0 (16.2) | 125.4 (15.6) | 147.8 (17.1) | 0.82-1.03 s |
| 16 | 117.4 (7.3) | 134.1 (8.1) | 147.9 (9.3) | 158.6 (9.7) | 1.34-1.66 s |

### suite

| check | passed |
|---|---:|
| concurrent | 12/12 |
| drafts | 12/12 |

### history

| run | plan | status | 1 stream code | 16 streams code | 16 streams first token | suite |
|---|---|---|---:|---:|---:|---|
| 2026-10-18 20:28 | glm-qual1014 | done |  | 134.1 | 1.34-1.66 s | 24/24 |
| 2026-10-18 14:29 | glm-quality | done | 60.1 |  |  | 1947/2418 |
| 2026-10-18 13:40 | glm-qual1014 | done |  | 134.1 | 1.35-1.67 s | 24/24 |

## GLM-5.3-Flash EXL3 4bpw on 2x NVIDIA DGX Spark (GB10, 128 GB unified each), TP=2 over RoCE

Target `glm53-exl3-gb10-packed`: GLM-5.3-Flash EXL3 4bpw, families/glm with 4-bit dense / 8-bit head, DFlash2 and 16 streams (PRs 855+979+984 and packing), TP=2 on two DGX Sparks. Engine: TensorFold native, CUDA: families/glm, packed linears (4/8, bf16 freed), DFlash2, 16 streams, prompts one at a time; served as `GLM-5.3-Flash-EXL3`. Latest: run `20261017-195233-glm-ab-ifeval` (2026-10-17 19:52, plan glm-ab-ifeval, done).

Serving: binary `cf50867102a60c38`

### suite

| check | passed |
|---|---:|
| ifeval | 103/150 |
| json | 30/30 |

### history

| run | plan | status | 1 stream code | 16 streams code | 16 streams first token | suite |
|---|---|---|---:|---:|---:|---|
| 2026-10-17 19:52 | glm-ab-ifeval | done |  |  |  | 133/180 |

## GLM-5.3-Flash EXL3 4bpw on 2x NVIDIA DGX Spark (GB10, 128 GB unified each), TP=2 over RoCE

Target `glm53-exl3-gb10-port`: GLM-5.3-Flash EXL3 4bpw, main's families/glm with PR 855's port, TP=2 on two DGX Sparks. Engine: TensorFold native, CUDA: families/glm on 1.0.12 (PR 855's port); served as `GLM-5.3-Flash-EXL3`. Latest: run `20261016-213802-glm-streams` (2026-10-16 21:38, plan glm-streams, done).

Serving: binary `2b666cc74334abec`

### ruler-streams

| streams | prose total (a stream) | code total (a stream) | structured total (a stream) | list total (a stream) | first token |
|---:|---:|---:|---:|---:|---:|
| 1 | 27.9 (27.9) | 38.0 (38.0) | 33.2 (33.2) | 30.6 (30.6) | 0.18-0.23 s |
| 4 | 48.9 (12.3) | 66.0 (16.7) | 64.8 (16.2) | 63.7 (16.1) | 0.79-0.86 s |
| 8 | 60.3 (7.6) | 75.9 (9.5) | 82.2 (10.3) | 76.3 (9.4) | 1.48-1.73 s |
| 16 | 123.6 (7.6) | 155.5 (9.6) | 149.5 (9.0) | 145.0 (9.1) | 8.50-17.20 s |

### suite-together

| check | passed |
|---|---:|
| concurrent | 12/12 |
| drafts | 12/12 |

### history

| run | plan | status | 1 stream code | 16 streams code | 16 streams first token | suite |
|---|---|---|---:|---:|---:|---|
| 2026-10-16 21:38 | glm-streams | done | 38.0 | 155.5 | 8.50-17.20 s | 24/24 |
| 2026-10-16 21:24 | glm-vision | done |  |  |  | 22/22 |
| 2026-10-16 21:03 | glm-vision | done |  |  |  | 4/6 |
| 2026-10-16 18:10 | glm-quality | done | 38.2 |  |  |  |

## GLM-5.3-Flash EXL3 4bpw on 2x NVIDIA DGX Spark (GB10, 128 GB unified each), TP=2 over RoCE

Target `glm53-exl3-gb10-port16`: GLM-5.3-Flash EXL3 4bpw, families/glm with 4096-row index rings, --parallel 16, TP=2 on two DGX Sparks. Engine: TensorFold native, CUDA: families/glm + index rings (16 streams at 40960); served as `GLM-5.3-Flash-EXL3`. Latest: run `20261017-062916-glm-streams` (2026-10-17 06:29, plan glm-streams, done).

Serving: binary `142bc21ac97bc065`

### ruler-streams

| streams | prose total (a stream) | code total (a stream) | structured total (a stream) | list total (a stream) | first token |
|---:|---:|---:|---:|---:|---:|
| 1 | 28.0 (28.0) | 38.6 (38.6) | 33.5 (33.5) | 30.7 (30.7) | 0.18-0.23 s |
| 4 | 51.3 (12.9) | 65.5 (16.3) | 65.7 (16.5) | 66.0 (16.5) | 0.67-0.81 s |
| 8 | 64.3 (8.1) | 82.3 (10.3) | 83.2 (10.4) | 81.8 (10.2) | 1.41-1.68 s |
| 16 | 86.4 (5.4) | 100.6 (6.3) | 100.2 (6.1) | 101.5 (6.2) | 3.23-3.72 s |

### suite-together

| check | passed |
|---|---:|
| concurrent | 12/12 |
| drafts | 12/12 |

### history

| run | plan | status | 1 stream code | 16 streams code | 16 streams first token | suite |
|---|---|---|---:|---:|---:|---|
| 2026-10-17 06:29 | glm-streams | done | 38.6 | 100.6 | 3.23-3.72 s | 24/24 |
| 2026-10-17 05:56 | glm-streams | done | 39.0 | 90.8 | 3.20-3.67 s | 24/24 |

## GLM-5.3-Flash, EXL3 4 bpw on 2x NVIDIA DGX Spark (GB10, 128 GB unified each), TP=2 over RoCE

Target `glm53-exl3-sparks`: GLM-5.3-Flash EXL3 4 bpw, TensorFold native, TP=2 on two DGX Sparks. Engine: TensorFold native, CUDA; served as `GLM-5.3-Flash-EXL3`. Latest: run `evidence/2026-10-14` (2026-10-14 00:00, plan published evidence, published).

### ruler-shipped-14fb445e-c1-sampled

| streams | prose total (a stream) | code total (a stream) | structured total (a stream) | list total (a stream) | first token |
|---:|---:|---:|---:|---:|---:|
| 1 | 45.1 (45.2) | 64.6 (65.4) | 56.5 (56.2) | 57.0 (54.9) | 0.18-0.25 s |

### ruler-shipped-14fb445e-c1

| streams | prose total (a stream) | code total (a stream) | structured total (a stream) | list total (a stream) | first token |
|---:|---:|---:|---:|---:|---:|
| 1 | 46.5 (45.4) | 68.7 (69.4) | 57.0 (56.4) | 58.8 (55.3) | 0.18-0.24 s |

### ruler-shipped-14fb445e-c16

| streams | prose total (a stream) | code total (a stream) | structured total (a stream) | list total (a stream) | first token |
|---:|---:|---:|---:|---:|---:|
| 16 | 144.0 (8.9) | 198.3 (12.1) | 180.1 (11.3) | 208.4 (12.5) | 0.91-1.19 s |

### ruler-shipped-14fb445e-c8

| streams | prose total (a stream) | code total (a stream) | structured total (a stream) | list total (a stream) | first token |
|---:|---:|---:|---:|---:|---:|
| 8 | 110.1 (13.6) | 152.5 (18.6) | 138.7 (17.5) | 157.0 (18.7) | 0.49-0.63 s |

### ruler-shipped-f95f2f70-c1-sampled

| streams | prose total (a stream) | code total (a stream) | structured total (a stream) | list total (a stream) | first token |
|---:|---:|---:|---:|---:|---:|
| 1 | 45.4 (45.4) | 65.8 (67.0) | 56.4 (55.9) | 58.1 (55.3) | 0.17-0.23 s |

### ruler-shipped-f95f2f70-c1

| streams | prose total (a stream) | code total (a stream) | structured total (a stream) | list total (a stream) | first token |
|---:|---:|---:|---:|---:|---:|
| 1 | 47.5 (46.5) | 69.5 (69.9) | 58.2 (56.9) | 60.2 (56.8) | 0.16-0.23 s |

### ruler-shipped-f95f2f70-c16

| streams | prose total (a stream) | code total (a stream) | structured total (a stream) | list total (a stream) | first token |
|---:|---:|---:|---:|---:|---:|
| 16 | 144.8 (8.9) | 202.2 (12.3) | 181.4 (11.4) | 207.6 (12.5) | 0.85-1.14 s |

### ruler-shipped-f95f2f70-c8

| streams | prose total (a stream) | code total (a stream) | structured total (a stream) | list total (a stream) | first token |
|---:|---:|---:|---:|---:|---:|
| 8 | 111.1 (13.7) | 154.1 (18.7) | 139.5 (17.2) | 157.3 (18.8) | 0.45-0.60 s |

### ablit/suite

| check | passed |
|---|---:|
| gsm8k | 246/250 |
| mmlu | 292/342 |
| humaneval | 159/164 |
| ifeval | 118/150 |
| tools | 59/60 |
| json | 30/30 |
| mgsm | 221/240 |

### suite-ab

| check | passed |
|---|---:|
| gsm8k | 244/250 |
| mmlu | 292/342 |
| humaneval | 156/164 |
| ifeval | 118/150 |
| tools | 59/60 |
| json | 30/30 |
| mgsm | 223/240 |

### history

| run | plan | status | 1 stream code | 16 streams code | 16 streams first token | suite |
|---|---|---|---:|---:|---:|---|
| 2026-10-14 00:00 | published evidence | published | 68.7 |  |  | 1125/1236 |
| 2026-10-13 00:00 | published evidence | published | 1083.6 |  |  | 1874/2172 |
| 2026-10-12 00:00 | published evidence | published | 62.8 | 169.5 | 0.45-1.19 s |  |

## GLM-5.3-Flash, MLX 4-bit on 1x Apple M5 Ultra (256 GB unified), macOS

Target `glm53-m5`: GLM-5.3-Flash MLX 4-bit, TensorFold native on one M5 Ultra Mac (one stream, greedy). Engine: TensorFold native, Metal; served as `GLM-5.3-Flash-MLX-4bit`. Latest: run `20261016-082326-glm-gate-novision` (2026-10-16 08:23, plan glm-gate-novision, done).

Serving: engine_commit `e8b60549`; binary_sha256 `d90e44c9818187ae4bc61d06312989cd796033b5dea6e0fc02164fe2730660fe`

### ruler-fresh

| streams | prose total (a stream) | code total (a stream) | structured total (a stream) | list total (a stream) | first token |
|---:|---:|---:|---:|---:|---:|
| 1 | 74.4 (74.4) | 78.3 (78.3) | 77.5 (77.5) | 86.5 (86.5) | 0.11-0.15 s |

### suite

| check | passed |
|---|---:|
| drafts | 12/12 |
| concurrent | 12/12 |
| streaming | 4/4 |
| multiturn | 8/8 |
| stop | 3/3 |
| thinking | 10/10 |
| copy | 2/2 |
| max-tokens | 3/3 |
| tools | 57/60 |
| json | 30/30 |
| gsm8k | 246/250 |
| mmlu | 290/342 |

### history

| run | plan | status | 1 stream code | 16 streams code | 16 streams first token | suite |
|---|---|---|---:|---:|---:|---|
| 2026-10-16 08:23 | glm-gate-novision | done | 78.3 |  |  | 677/736 |
| 2026-10-16 08:04 | glm-gate-novision | done | 77.6 |  |  | 679/736 |
| 2026-10-16 00:35 | glm-gate | done | 78.7 |  |  | 689/748 |
| 2026-10-10 00:00 | published evidence | published | 103.7 |  |  | 36/36 |
| 2026-10-10 00:00 | published evidence | published |  |  |  | 1128/1213 |
| 2026-10-10 00:00 | published evidence | published |  |  |  | 1137/1213 |
| 2026-10-10 00:00 | published evidence | published |  |  |  | 1079/1213 |
| 2026-10-09 00:00 | published evidence | published | 104.6 |  |  |  |
| 2026-10-09 00:00 | published evidence | published |  |  |  | 349/403 |
| 2026-10-09 00:00 | published evidence | published |  |  |  | 42/42 |

## MiniMax-M3.1-Flash, EXL3 3.06 bpw (Mia-AiLab EAQ v1), 32k context on 2x NVIDIA DGX Spark (GB10, 128 GB unified each), TP=2 over RoCE

Target `minimax-m31-exl3-gb10x2`: MiniMax-M3.1-Flash, Mia-AiLab EXL3 3.06 bpw as published, DSpark drafts, 32k x 2 streams, TensorFold native CUDA, TP=2 on two DGX Sparks. Engine: TensorFold native, CUDA; served as `MiniMax-M3.1-Flash`. Latest: run `20261028-034040-quick` (2026-10-28 03:40, plan quick, done).

Serving: engine_commit `aad9d2b8a; 0`; binary_sha256 `c23f2266dc7647101818eb9680c25ca75fc8704d13152c39e4ecf29a2dffacf5`; checkpoint_revision `Mia-AiLab/MiniMax-M3.1-Flash-EXL3-EAQ-v1-3.06-bpw c33e7a6619f0f12ac99098e07ec5e56acb7eeda9`; server_args `TF_MINIMAX_RANK=0 TF_MINIMAX_WORLD=2 NCCL_SOCKET_IFNAME=enp1s0f1np1 NCCL_IB_HCA=rocep1s0f1`; suite_commit `277c842a1481`

### ruler-fresh

| streams | prose total (a stream) | code total (a stream) | structured total (a stream) | list total (a stream) | first token |
|---:|---:|---:|---:|---:|---:|
| 1 | 24.6 (24.6) | 39.6 (39.6) | 29.7 (29.7) | 30.3 (30.3) | 0.59-0.64 s |

Engine rounds (ruler-fresh):

| streams | tokens a round | drafts a round | accepted | ms a round | requests |
|---:|---:|---:|---:|---:|---:|
| 1 | 2.708 | 3.41 | 50% | 87.21 | 12 |

### ruler-after

| streams | prose total (a stream) | code total (a stream) | structured total (a stream) | list total (a stream) | first token |
|---:|---:|---:|---:|---:|---:|
| 1 | 24.4 (24.4) | 38.8 (38.8) | 28.9 (28.9) | 30.4 (30.4) | 0.59-0.64 s |

Engine rounds (ruler-after):

| streams | tokens a round | drafts a round | accepted | ms a round | requests |
|---:|---:|---:|---:|---:|---:|
| 1 | 2.658 | 3.238 | 51% | 86.77 | 13 |

### suite

| check | passed |
|---|---:|
| soak | 60/60 |
| drafts | 12/12 |
| concurrent | 12/12 |
| streaming | 4/4 |
| multiturn | 8/8 |
| stop | 3/3 |
| thinking | 10/10 |
| copy | 2/2 |
| max-tokens | 3/3 |

### checks

| check | result |
|---|---|
| memory-idle | measured: head 27.1 GiB available; worker 26.0 GiB available |
| structured | pass: 18/18 obey, drafted == plain 12/12; a bad regex -> 400 |
| tools | pass: 5/5 tool cases right |
| sampling | pass: 9/9 seeded replies equal on repeat and undrafted; 0 errors |
| turns | pass: resumed == again: True; cold (after a restart): True; cached 4096 of 4725; ttft resumed 1.623s, cold 10.031s |
| urls | FAIL: public 400; loopback 400; http 400; unexpected: ['public'] |

### history

| run | plan | status | 1 stream code | 16 streams code | 16 streams first token | suite |
|---|---|---|---:|---:|---:|---|
| 2026-10-28 03:40 | quick | done | 39.6 |  |  | 114/114 |
| 2026-10-28 03:26 | speed | done | 38.5 |  |  |  |
| 2026-10-28 02:59 | glm-vision | done |  |  |  | 3/6 |
| 2026-10-28 02:31 | quick | done | 38.1 |  |  | 114/114 |
| 2026-10-28 02:16 | speed | done | 39.2 |  |  |  |

## MiniMax-M3.1-Flash, EXL3 3.06 bpw (Mia-AiLab EAQ v1), 256k context on 1x Apple M5 Ultra (256 GB unified), macOS

Target `minimax-m31-exl3-m5`: MiniMax-M3.1-Flash, EXL3 3.06 bpw (Mia-AiLab EAQ v1), 256k context, TensorFold native Metal on one M5 Ultra. Engine: TensorFold native, Metal; served as `MiniMax-M3.1-Flash`. Latest: run `20261029-182420-minimax-math500` (2026-10-29 18:24, plan minimax-math500, done).

Serving: engine_commit `af3573193`; binary_sha256 `90f54df38bb95056e4520d4d5a2b7c6baec75bcad6190711b9bdedbc813cdb8c`; served_model `{"object": "list", "data": [{"id": "MiniMax-M3.1-Flash", "object": "model", "created": 179`; chip `Apple M5 Ultra; 274877906944`; suite_commit `21db9b23f7be`

### suite

| check | passed |
|---|---:|
| math500 | 422/500 |

### checks

| check | result |
|---|---|
| memory-idle | measured: mac: System-wide memory free percentage: 32%; total = 4096.00M  us |

### history

| run | plan | status | 1 stream code | 16 streams code | 16 streams first token | suite |
|---|---|---|---:|---:|---:|---|
| 2026-10-29 18:24 | minimax-math500 | done |  |  |  | 422/500 |
| 2026-10-29 18:23 | glm-vision | done |  |  |  | 15/22 |
| 2026-10-29 15:57 | glm-vision | done |  |  |  | 15/22 |
| 2026-10-29 15:25 | speed | done | 33.6 |  |  |  |
| 2026-10-29 15:04 | speed | done | 33.5 |  |  |  |
| 2026-10-29 15:03 | glm-vision | done |  |  |  | 15/22 |
| 2026-10-29 14:44 | quick | done | 34.6 |  |  | 114/114 |
| 2026-10-29 13:49 | speed | done | 40.1 |  |  |  |
| 2026-10-29 13:29 | speed | done | 33.4 |  |  |  |
| 2026-10-29 13:28 | glm-vision | done |  |  |  | 15/22 |
| 2026-10-29 13:09 | quick | done | 33.3 |  |  | 114/114 |
| 2026-10-29 12:23 | speed | done | 39.6 |  |  |  |
| 2026-10-29 12:02 | speed | done | 32.6 |  |  |  |
| 2026-10-29 12:01 | glm-vision | done |  |  |  | 15/22 |
| 2026-10-29 11:42 | quick | done | 33.0 |  |  | 114/114 |
| 2026-10-29 10:36 | speed | done | 25.6 |  |  |  |
| 2026-10-29 10:12 | speed | done | 25.3 |  |  |  |
| 2026-10-29 10:11 | glm-vision | done |  |  |  | 15/22 |
| 2026-10-29 09:48 | quick | done | 25.5 |  |  | 114/114 |
| 2026-10-29 08:50 | speed | done | 20.0 |  |  |  |
| 2026-10-29 08:23 | quick | done | 20.1 |  |  | 114/114 |
| 2026-10-29 07:51 | speed | done | 19.5 |  |  |  |
| 2026-10-29 07:50 | glm-vision | done |  |  |  | 15/22 |
| 2026-10-29 07:24 | quick | done | 19.5 |  |  | 114/114 |
| 2026-10-29 06:55 | speed | done | 19.5 |  |  |  |
| 2026-10-29 06:54 | glm-vision | done |  |  |  | 15/22 |
| 2026-10-29 06:29 | quick | done | 19.5 |  |  | 114/114 |

## MiniMax-M3.1-Flash, MLX mixed 3-bit (mix256k), 144k context on 1x Apple M5 Ultra (256 GB unified), macOS

Target `minimax-m31-mix256k-m5`: MiniMax-M3.1-Flash, MLX mixed 3-bit (mix256k), 144k context, TensorFold native Metal on one M5 Ultra. Engine: TensorFold native, Metal; served as `MiniMax-M3.1-Flash`. Latest: run `20261027-233821-glm-vision` (2026-10-27 23:38, plan glm-vision, done).

Serving: engine_commit `16ef3b31b`; binary_sha256 `995f469d85230291c7ef5b6ff101dad5aea9de874847facb72a2a5a4bc073eda`; served_model `{"object": "list", "data": [{"id": "MiniMax-M3.1-Flash", "object": "model", "created": 179`; chip `Apple M5 Ultra; 274877906944`; suite_commit `a7ba7e392d57-dirty`

### suite-vision

| check | passed |
|---|---:|
| vision | 3/6 |
| vision-concurrent | 12/16 |

### history

| run | plan | status | 1 stream code | 16 streams code | 16 streams first token | suite |
|---|---|---|---:|---:|---:|---|
| 2026-10-27 23:38 | glm-vision | done |  |  |  | 15/22 |
| 2026-10-27 23:22 | quick | done | 58.2 |  |  | 114/114 |
| 2026-10-27 06:06 | glm-vision | done |  |  |  | 3/6 |
| 2026-10-27 05:40 | quick | done | 55.8 |  |  | 114/114 |
| 2026-10-26 23:32 | dsv41-quality-off | done |  |  |  | 1402/1614 |
| 2026-10-26 23:31 | glm-vision | done |  |  |  | 3/6 |
| 2026-10-26 23:29 | glm-vision | done |  |  |  | 3/6 |
| 2026-10-26 23:19 | glm-vision | done |  |  |  | 3/6 |
| 2026-10-26 23:03 | quick | done | 58.5 |  |  | 114/114 |
| 2026-10-25 08:05 | quick | done | 59.2 |  |  | 114/114 |
| 2026-10-24 20:24 | dsv41-quality-off | done |  |  |  | 1388/1614 |
| 2026-10-24 19:30 | quick | done | 58.9 |  |  | 114/114 |
| 2026-10-24 18:31 | quick | done | 58.1 |  |  | 114/114 |
| 2026-10-24 18:26 | speed | done | 58.9 |  |  |  |
| 2026-10-24 16:05 | quick | done | 57.4 |  |  | 114/114 |
| 2026-10-24 13:49 | quick | done | 57.6 |  |  | 114/114 |
| 2026-10-24 11:56 | quick | done | 56.4 |  |  | 114/114 |
| 2026-10-24 11:07 | quick | done | 54.7 |  |  | 114/114 |
| 2026-10-24 09:03 | quick | done | 54.9 |  |  | 114/114 |
| 2026-10-24 03:42 | mlx-speed | done | 44.0 |  |  |  |
| 2026-10-24 00:46 | dsv41-quality-off | done |  |  |  | 1401/1614 |
| 2026-10-24 00:39 | speed | done | 57.9 |  |  |  |

## MiniMax-M3.1-Flash, MLX mixed 4/3-bit (mix34) on 1x Apple M5 Ultra (256 GB unified), macOS

Target `minimax-m31-mix34-m5`: MiniMax-M3.1-Flash, MLX mixed 4/3-bit (mix34), TensorFold native Metal on one M5 Ultra. Engine: TensorFold native, Metal; served as `MiniMax-M3.1-Flash`. Latest: run `20261027-235721-quick` (2026-10-27 23:57, plan quick, aborted: minimax-m31-mix34-m5 never came up after 1 starts).

Serving: engine_commit `16ef3b31b`; binary_sha256 `995f469d85230291c7ef5b6ff101dad5aea9de874847facb72a2a5a4bc073eda`; served_model `{"object": "list", "data": [{"id": "MiniMax-M3.1-Flash", "object": "model", "created": 179`; chip `Apple M5 Ultra; 274877906944`; suite_commit `a7ba7e392d57-dirty`

### ruler-fresh

| streams | prose total (a stream) | code total (a stream) | structured total (a stream) | list total (a stream) | first token |
|---:|---:|---:|---:|---:|---:|
| 1 | 41.0 (41.0) | 63.4 (63.4) | 47.6 (47.6) | 54.5 (54.5) | 0.32-0.34 s |

Engine rounds (ruler-fresh):

| streams | tokens a round | drafts a round | accepted | ms a round | requests |
|---:|---:|---:|---:|---:|---:|
| 1 | 2.224 | 1.839 | 66% | 43.09 | 12 |

### checks

| check | result |
|---|---|
| memory-idle | measured: mac: System-wide memory free percentage: 16%; total = 4096.00M  us |
| structured | pass: 18/18 obey, drafted == plain 12/12; a bad regex -> 400 |
| tools | pass: 5/5 tool cases right |
| sampling | pass: 9/9 seeded replies equal on repeat and undrafted; 0 errors |

### history

| run | plan | status | 1 stream code | 16 streams code | 16 streams first token | suite |
|---|---|---|---:|---:|---:|---|
| 2026-10-27 23:57 | quick | aborted: minimax-m31-mix34-m5 never came up after 1 starts | 63.4 |  |  |  |
| 2026-10-27 23:50 | glm-vision | done |  |  |  | 15/22 |
| 2026-10-27 06:26 | glm-vision | done |  |  |  | 3/6 |
| 2026-10-27 06:09 | quick | done | 61.3 |  |  | 114/114 |
| 2026-10-25 01:49 | dsv41-quality-off | done |  |  |  | 1389/1614 |
| 2026-10-24 19:01 | quick | done | 59.2 |  |  | 114/114 |
| 2026-10-24 18:55 | speed | done | 58.5 |  |  |  |
| 2026-10-24 16:21 | quick | done | 65.1 |  |  | 114/114 |
| 2026-10-24 14:06 | quick | done | 65.1 |  |  | 114/114 |
| 2026-10-24 13:20 | quick | done | 66.1 |  |  | 114/114 |
| 2026-10-24 05:59 | quick | done | 65.2 |  |  | 114/114 |
| 2026-10-24 04:09 | quick | done | 66.6 |  |  | 114/114 |
| 2026-10-23 21:17 | dsv41-quality-off | done |  |  |  | 1393/1614 |
| 2026-10-23 21:01 | mlx-speed | done | 43.3 |  |  |  |
| 2026-10-23 20:52 | speed | done | 65.9 |  |  |  |
| 2026-10-23 20:28 | speed | aborted: minimax-m31-mix34-m5 never came up after 1 starts | 64.3 |  |  |  |

## MiniMax-M3.1-Flash, NVFP4 (15 MoE layers) + 3-bit refit, dense NVFP4, MXFP8 head, 32k context on 2x NVIDIA DGX Spark (GB10, 128 GB unified each), TP=2 over RoCE

Target `minimax-m31-nvfp4mix-dense4-gb10x2`: MiniMax-M3.1-Flash, NVFP4 x 15 layers + 3-bit, dense NVFP4 + MXFP8 head, DSpark drafts, 32k x 2 streams, TensorFold native CUDA, TP=2 on two DGX Sparks. Engine: TensorFold native, CUDA; served as `MiniMax-M3.1-Flash`. Latest: run `20261026-215020-minimax-thinking` (2026-10-26 21:50, plan minimax-thinking, done).

Serving: engine_commit `1d559dd44; 9`; binary_sha256 `09ac4a25886400303603ffa9221dc29816f77b4821d9a612605d67f242b5ae07`; checkpoint_mix `[20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 31, 49, 52, 57, 59] ['qkv', 'o', 'mlp']`; checkpoint_sha256 `b21fdee27b56408db9f77bb2dc22b93224960d419106db758007d00e9cf43711`; server_args `TF_MINIMAX_RANK=0 TF_MINIMAX_WORLD=2 NCCL_SOCKET_IFNAME=enp1s0f1np1 NCCL_IB_HCA=rocep1s0f1`; suite_commit `a7ba7e392d57`

### suite-thinking

| check | passed |
|---|---:|
| gsm8k | 242/250 |

### checks

| check | result |
|---|---|
| thinking | pass: thinking on: 10/10 right, 10/10 with reasoning_content, 0 leaks, 0 errors, 0 cut at 29696 tokens |

### history

| run | plan | status | 1 stream code | 16 streams code | 16 streams first token | suite |
|---|---|---|---:|---:|---:|---|
| 2026-10-26 21:50 | minimax-thinking | done |  |  |  | 242/250 |
| 2026-10-26 21:32 | minimax-thinking | done |  |  |  | 240/250 |
| 2026-10-26 20:00 | minimax-quality-off | done |  |  |  | 940/1114 |
| 2026-10-26 19:27 | quick | done | 44.7 |  |  | 114/114 |
| 2026-10-26 19:10 | speed3 | done | 45.2 |  |  |  |
| 2026-10-26 17:41 | quick | done | 45.6 |  |  | 114/114 |
| 2026-10-26 17:27 | speed | done | 45.8 |  |  |  |
| 2026-10-26 13:39 | quick | done | 43.3 |  |  | 114/114 |
| 2026-10-26 13:17 | speed | done | 43.1 |  |  |  |

## MiniMax-M3.1-Flash, NVFP4 (15 MoE layers) + 3-bit refit, 32k context on 2x NVIDIA DGX Spark (GB10, 128 GB unified each), TP=2 over RoCE

Target `minimax-m31-nvfp4mix-gb10x2`: MiniMax-M3.1-Flash, NVFP4 x 15 layers + 3-bit, DSpark drafts, 32k x 2 streams, TensorFold native CUDA, TP=2 on two DGX Sparks. Engine: TensorFold native, CUDA; served as `MiniMax-M3.1-Flash`. Latest: run `20261026-222738-quick` (2026-10-26 22:27, plan quick, done).

Serving: engine_commit `1d559dd44; 13`; binary_sha256 `67ab85c6e9ba163e87cbdb0dabdcd7e7eda1213453b2536165eab57525306a24`; checkpoint_mix `[20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 31, 49, 52, 57, 59]`; server_args `TF_MINIMAX_RANK=0 TF_MINIMAX_WORLD=2 NCCL_SOCKET_IFNAME=enp1s0f1np1 NCCL_IB_HCA=rocep1s0f1`; suite_commit `277c842a1481`

### ruler-fresh

| streams | prose total (a stream) | code total (a stream) | structured total (a stream) | list total (a stream) | first token |
|---:|---:|---:|---:|---:|---:|
| 1 | 23.0 (23.0) | 40.6 (40.6) | 24.7 (24.7) | 32.2 (32.2) | 0.47-0.51 s |

Engine rounds (ruler-fresh):

| streams | tokens a round | drafts a round | accepted | ms a round | requests |
|---:|---:|---:|---:|---:|---:|
| 1 | 2.698 | 3.526 | 48% | 89.45 | 12 |

### ruler-after

| streams | prose total (a stream) | code total (a stream) | structured total (a stream) | list total (a stream) | first token |
|---:|---:|---:|---:|---:|---:|
| 1 | 22.1 (22.1) | 39.5 (39.5) | 24.7 (24.7) | 31.5 (31.5) | 0.47-0.51 s |

Engine rounds (ruler-after):

| streams | tokens a round | drafts a round | accepted | ms a round | requests |
|---:|---:|---:|---:|---:|---:|
| 1 | 2.713 | 3.771 | 45% | 92.14 | 13 |

### suite

| check | passed |
|---|---:|
| soak | 60/60 |
| drafts | 12/12 |
| concurrent | 12/12 |
| streaming | 4/4 |
| multiturn | 8/8 |
| stop | 3/3 |
| thinking | 10/10 |
| copy | 2/2 |
| max-tokens | 3/3 |

### checks

| check | result |
|---|---|
| memory-idle | measured: head 8.2 GiB available; worker 7.9 GiB available |
| structured | pass: 18/18 obey, drafted == plain 12/12; a bad regex -> 400 |
| tools | pass: 5/5 tool cases right |
| sampling | pass: 9/9 seeded replies equal on repeat and undrafted; 0 errors |
| turns | pass: resumed == again: True; cold (after a restart): True; cached 4096 of 4826; ttft resumed 0.993s, cold 5.132s |
| urls | FAIL: public 400; loopback 400; http 400; unexpected: ['public'] |

### history

| run | plan | status | 1 stream code | 16 streams code | 16 streams first token | suite |
|---|---|---|---:|---:|---:|---|
| 2026-10-26 22:27 | quick | done | 40.6 |  |  | 114/114 |
| 2026-10-26 22:11 | speed | done | 40.9 |  |  |  |
| 2026-10-26 13:22 | quick | done | 40.7 |  |  | 114/114 |
| 2026-10-26 10:51 | speed | done | 40.5 |  |  |  |
| 2026-10-26 06:04 | quick | done | 41.1 |  |  | 114/114 |
| 2026-10-26 05:29 | speed | done | 39.9 |  |  |  |
| 2026-10-26 03:16 | quick | done | 39.9 |  |  | 114/114 |
| 2026-10-26 01:40 | quick | done | 34.3 |  |  | 114/114 |

## Nanbeige4.3-33B, affine 4bit on 1x Apple M5 Ultra (256 GB unified), macOS

Target `nanbeige43-33b-4bit-m5`: Nanbeige4.3-33B MLX affine 4bit (llama_convert.py), TensorFold native Metal (llama) on one M5 Ultra (131072-token window, 2 streams). Engine: TensorFold native, Metal; served as `nanbeige`. Latest: run `20261026-090304-speed` (2026-10-26 09:03, plan speed, done).

Serving: engine_commit `c0243b7e3`; binary_sha256 `70f5a3c2a635a8d9ddd59cf5e751c38c9cf28faf407348046efd60a14716e3a8`; served_model `{"object": "list", "data": [{"id": "nanbeige", "object": "model", "created": 1793023392, "`; chip `Apple M5 Ultra; 274877906944`; suite_commit `277c842a1481`

### ruler-fresh

| streams | prose total (a stream) | code total (a stream) | structured total (a stream) | list total (a stream) | first token |
|---:|---:|---:|---:|---:|---:|
| 1 | 48.5 (48.5) | 47.9 (47.9) | 48.7 (48.7) | 48.6 (48.6) | 0.10-0.12 s |
| 2 | 84.8 (42.4) | 81.3 (40.6) | 84.1 (42.1) | 84.7 (42.4) | 0.16-0.18 s |

Engine rounds (ruler-fresh):

| streams | tokens a round | drafts a round | accepted | ms a round | requests |
|---:|---:|---:|---:|---:|---:|
| 1 | 1.011 | 0.034 | 20% | 20.89 | 12 |
| 2 | 1.022 | 0.05 | 34% | 24.41 | 25 |

### ruler-after

| streams | prose total (a stream) | code total (a stream) | structured total (a stream) | list total (a stream) | first token |
|---:|---:|---:|---:|---:|---:|
| 1 | 48.3 (48.3) | 47.6 (47.6) | 48.4 (48.4) | 48.3 (48.3) | 0.10-0.12 s |

Engine rounds (ruler-after):

| streams | tokens a round | drafts a round | accepted | ms a round | requests |
|---:|---:|---:|---:|---:|---:|
| 1 | 1.02 | 0.045 | 32% | 21.17 | 13 |

### checks

| check | result |
|---|---|
| memory-idle | measured: mac: System-wide memory free percentage: 53%; total = 4096.00M  us |
| turns | pass: resumed == again: True; cold (after a restart): True; cached 5493 of 5649; ttft resumed 0.217s, cold 4.247s |
| memory-busy | measured: mac: System-wide memory free percentage: 53%; total = 4096.00M  us |

### history

| run | plan | status | 1 stream code | 16 streams code | 16 streams first token | suite |
|---|---|---|---:|---:|---:|---|
| 2026-10-26 09:03 | speed | done | 47.9 |  |  |  |
| 2026-10-26 08:49 | quick | done | 48.1 |  |  | 114/114 |

## Nanbeige4.3-33B, affine 8bit on 1x Apple M5 Ultra (256 GB unified), macOS

Target `nanbeige43-33b-8bit-m5`: Nanbeige4.3-33B MLX affine 8bit (llama_convert.py), TensorFold native Metal (llama) on one M5 Ultra (131072-token window, 2 streams). Engine: TensorFold native, Metal; served as `nanbeige`. Latest: run `20261026-082437-speed` (2026-10-26 08:24, plan speed, done).

Serving: engine_commit `fa5b1f989`; binary_sha256 `70f5a3c2a635a8d9ddd59cf5e751c38c9cf28faf407348046efd60a14716e3a8`; served_model `{"object": "list", "data": [{"id": "nanbeige", "object": "model", "created": 1793021086, "`; chip `Apple M5 Ultra; 274877906944`; suite_commit `277c842a1481`

### ruler-fresh

| streams | prose total (a stream) | code total (a stream) | structured total (a stream) | list total (a stream) | first token |
|---:|---:|---:|---:|---:|---:|
| 1 | 28.7 (28.7) | 28.3 (28.3) | 28.8 (28.8) | 28.8 (28.8) | 0.13-0.15 s |
| 2 | 54.1 (27.1) | 52.5 (26.3) | 53.2 (26.6) | 54.0 (27.0) | 0.19-0.23 s |

Engine rounds (ruler-fresh):

| streams | tokens a round | drafts a round | accepted | ms a round | requests |
|---:|---:|---:|---:|---:|---:|
| 1 | 1.005 | 0.017 | 0% | 35.06 | 12 |
| 2 | 1.022 | 0.051 | 34% | 38.25 | 25 |

### ruler-after

| streams | prose total (a stream) | code total (a stream) | structured total (a stream) | list total (a stream) | first token |
|---:|---:|---:|---:|---:|---:|
| 1 | 28.7 (28.7) | 28.3 (28.3) | 28.7 (28.7) | 28.7 (28.7) | 0.13-0.15 s |

Engine rounds (ruler-after):

| streams | tokens a round | drafts a round | accepted | ms a round | requests |
|---:|---:|---:|---:|---:|---:|
| 1 | 1.007 | 0.023 | 10% | 35.19 | 13 |

### checks

| check | result |
|---|---|
| memory-idle | measured: mac: System-wide memory free percentage: 47%; total = 4096.00M  us |
| turns | pass: resumed == again: True; cold (after a restart): True; cached 5493 of 5649; ttft resumed 0.256s, cold 4.461s |
| memory-busy | measured: mac: System-wide memory free percentage: 48%; total = 4096.00M  us |

### history

| run | plan | status | 1 stream code | 16 streams code | 16 streams first token | suite |
|---|---|---|---:|---:|---:|---|
| 2026-10-26 08:24 | speed | done | 28.3 |  |  |  |
| 2026-10-26 08:02 | quick | done | 28.4 |  |  | 114/114 |

## Nanbeige4.3-33B bf16, drafted by Nanbeige4.1-3B bf16 on 1x Apple M5 Ultra (256 GB unified), macOS

Target `nanbeige43-33b-bf16draft-m5`: Nanbeige4.3-33B bf16 with Nanbeige4.1-3B bf16 drafting, TensorFold native Metal (llama) on one M5 Ultra (131072-token window, 2 streams, every stream drafted). Engine: TensorFold native, Metal; served as `nanbeige`. Latest: run `20261029-180246-speed` (2026-10-29 18:02, plan speed, done).

Serving: engine_commit `c3ee3db24`; binary_sha256 `0d5c5c6b34b6267ae99c4d9182b1c71c2e71af9bbfd2e697cbe487398bf0224f`; served_model `{"object": "list", "data": [{"id": "nanbeige", "object": "model", "created": 1793314979, "`; chip `Apple M5 Ultra; 274877906944`; suite_commit `21db9b23f7be`

### ruler-fresh

| streams | prose total (a stream) | code total (a stream) | structured total (a stream) | list total (a stream) | first token |
|---:|---:|---:|---:|---:|---:|
| 1 | 114.0 (114.0) | 98.4 (98.4) | 99.0 (99.0) | 106.9 (106.9) | 0.23-0.26 s |
| 2 | 44.1 (22.0) | 58.8 (29.4) | 54.5 (27.2) | 55.9 (27.9) | 0.34-0.39 s |

Engine rounds (ruler-fresh):

| streams | tokens a round | drafts a round | accepted | ms a round | requests |
|---:|---:|---:|---:|---:|---:|
| 1 | 4.77 | 4.408 | 85% | 45.61 | 12 |
| 2 | 4.507 | 3.934 | 89% | 169.14 | 25 |

### ruler-after

| streams | prose total (a stream) | code total (a stream) | structured total (a stream) | list total (a stream) | first token |
|---:|---:|---:|---:|---:|---:|
| 1 | 114.0 (114.0) | 92.5 (92.5) | 101.8 (101.8) | 101.8 (101.8) | 0.23-0.26 s |

Engine rounds (ruler-after):

| streams | tokens a round | drafts a round | accepted | ms a round | requests |
|---:|---:|---:|---:|---:|---:|
| 1 | 4.737 | 4.337 | 86% | 46.21 | 13 |

### checks

| check | result |
|---|---|
| memory-idle | measured: mac: System-wide memory free percentage: 68%; total = 4096.00M  us |
| turns | pass: resumed == again: True; cold (after a restart): True; cached 5493 of 5649; ttft resumed 0.365s, cold 4.407s |
| memory-busy | measured: mac: System-wide memory free percentage: 67%; total = 4096.00M  us |

### history

| run | plan | status | 1 stream code | 16 streams code | 16 streams first token | suite |
|---|---|---|---:|---:|---:|---|
| 2026-10-29 18:02 | speed | done | 98.4 |  |  |  |
| 2026-10-29 17:37 | quick | done | 81.9 |  |  | 114/114 |
| 2026-10-28 11:59 | speed | done | 108.3 |  |  |  |
| 2026-10-28 11:33 | quick | done | 100.5 |  |  | 114/114 |

## Nanbeige4.3-33B bf16, drafted by Nanbeige4.1-3B 4-bit on 1x Apple M5 Ultra (256 GB unified), macOS

Target `nanbeige43-33b-draft-m5`: Nanbeige4.3-33B bf16 with Nanbeige4.1-3B 4-bit drafting, TensorFold native Metal (llama) on one M5 Ultra (131072-token window, 2 streams). Engine: TensorFold native, Metal; served as `nanbeige`. Latest: run `20261026-121700-speed` (2026-10-26 12:17, plan speed, done).

Serving: engine_commit `e1f447bf3`; binary_sha256 `7d06edafe546ae55db81fedc6936810b80219413aac64c847573b4681f8a4674`; served_model `{"object": "list", "data": [{"id": "nanbeige", "object": "model", "created": 1793035033, "`; chip `Apple M5 Ultra; 274877906944`; suite_commit `277c842a1481`

### ruler-fresh

| streams | prose total (a stream) | code total (a stream) | structured total (a stream) | list total (a stream) | first token |
|---:|---:|---:|---:|---:|---:|
| 1 | 113.5 (113.5) | 111.0 (111.0) | 108.5 (108.5) | 84.9 (84.9) | 0.23-0.26 s |
| 2 | 63.3 (31.6) | 64.3 (32.1) | 63.8 (31.9) | 58.3 (29.2) | 0.35-0.39 s |

Engine rounds (ruler-fresh):

| streams | tokens a round | drafts a round | accepted | ms a round | requests |
|---:|---:|---:|---:|---:|---:|
| 1 | 4.92 | 4.831 | 81% | 47.08 | 12 |
| 2 | 2.716 | 2.116 | 81% | 87.01 | 25 |

### ruler-after

| streams | prose total (a stream) | code total (a stream) | structured total (a stream) | list total (a stream) | first token |
|---:|---:|---:|---:|---:|---:|
| 1 | 110.5 (110.5) | 108.5 (108.5) | 109.3 (109.3) | 90.0 (90.0) | 0.23-0.26 s |

Engine rounds (ruler-after):

| streams | tokens a round | drafts a round | accepted | ms a round | requests |
|---:|---:|---:|---:|---:|---:|
| 1 | 4.847 | 4.736 | 81% | 46.35 | 13 |

### checks

| check | result |
|---|---|
| memory-idle | measured: mac: System-wide memory free percentage: 33%; total = 5120.00M  us |
| turns | pass: resumed == again: True; cold (after a restart): True; cached 5493 of 5649; ttft resumed 0.344s, cold 4.491s |
| memory-busy | measured: mac: System-wide memory free percentage: 32%; total = 5120.00M  us |

### history

| run | plan | status | 1 stream code | 16 streams code | 16 streams first token | suite |
|---|---|---|---:|---:|---:|---|
| 2026-10-26 12:17 | speed | done | 111.0 |  |  |  |
| 2026-10-26 11:52 | quick | done | 108.6 |  |  | 114/114 |
| 2026-10-26 11:21 | quick | done | 102.5 |  |  | 57/60 |

## Nanbeige4.3-33B, bf16 on 1x Apple M5 Ultra (256 GB unified), macOS

Target `nanbeige43-33b-m5`: Nanbeige4.3-33B bf16 as released, TensorFold native Metal (llama) on one M5 Ultra (131072-token window, 2 streams). Engine: TensorFold native, Metal; served as `nanbeige`. Latest: run `20261028-112259-speed` (2026-10-28 11:22, plan speed, done).

Serving: engine_commit `50fe245ac`; binary_sha256 `c3fcf8cacf289aec9ee53f1eae52fda4fab2f1eeda1bf75b61482542dba4b3d1`; served_model `{"object": "list", "data": [{"id": "nanbeige", "object": "model", "created": 1793204587, "`; chip `Apple M5 Ultra; 274877906944`; suite_commit `21db9b23f7be`

### ruler-fresh

| streams | prose total (a stream) | code total (a stream) | structured total (a stream) | list total (a stream) | first token |
|---:|---:|---:|---:|---:|---:|
| 1 | 16.3 (16.3) | 16.2 (16.2) | 16.3 (16.3) | 16.3 (16.3) | 0.23-0.26 s |
| 2 | 31.7 (15.8) | 27.8 (13.9) | 31.4 (15.7) | 31.6 (15.8) | 0.34-0.39 s |

Engine rounds (ruler-fresh):

| streams | tokens a round | drafts a round | accepted | ms a round | requests |
|---:|---:|---:|---:|---:|---:|
| 1 | 1.005 | 0.017 | 0% | 61.7 | 12 |
| 2 | 1.023 | 0.059 | 30% | 66.8 | 25 |

### ruler-after

| streams | prose total (a stream) | code total (a stream) | structured total (a stream) | list total (a stream) | first token |
|---:|---:|---:|---:|---:|---:|
| 1 | 16.3 (16.3) | 16.3 (16.3) | 16.3 (16.3) | 16.3 (16.3) | 0.23-0.26 s |

Engine rounds (ruler-after):

| streams | tokens a round | drafts a round | accepted | ms a round | requests |
|---:|---:|---:|---:|---:|---:|
| 1 | 1.007 | 0.022 | 10% | 61.76 | 13 |

### checks

| check | result |
|---|---|
| memory-idle | measured: mac: System-wide memory free percentage: 71%; total = 4096.00M  us |
| turns | pass: resumed == again: True; cold (after a restart): True; cached 5493 of 5649; ttft resumed 0.346s, cold 4.387s |
| memory-busy | measured: mac: System-wide memory free percentage: 70%; total = 4096.00M  us |

### history

| run | plan | status | 1 stream code | 16 streams code | 16 streams first token | suite |
|---|---|---|---:|---:|---:|---|
| 2026-10-28 11:22 | speed | done | 16.2 |  |  |  |
| 2026-10-28 10:46 | quick | done | 15.5 |  |  | 114/114 |
| 2026-10-26 06:06 | quick | done | 16.2 |  |  | 114/114 |
| 2026-10-26 04:19 | speed | done | 16.3 |  |  |  |
| 2026-10-26 03:43 | quick | done | 16.2 |  |  | 114/114 |
| 2026-10-26 02:07 | quick | aborted: the server died during suite; its result is discarded | 16.3 |  |  |  |

## Nanbeige4.3-33B, MLX 4-bit on 1x Apple M5 Ultra (256 GB unified), macOS

Target `nanbeige43-33b-mlx4-m5`: Nanbeige4.3-33B MLX 4-bit as published (pratikgx/Nanbeige4.3-33B-MLX-4bit), TensorFold native Metal (llama) on one M5 Ultra (131072-token window, 2 streams). Engine: TensorFold native, Metal; served as `nanbeige`. Latest: run `20261027-100550-speed` (2026-10-27 10:05, plan speed, done).

Serving: engine_commit `657ac711c`; binary_sha256 `56fb3ebeaa8facd66a071318c4602df8920f6675171b8a3b093c639695609e9c`; served_model `{"object": "list", "data": [{"id": "nanbeige", "object": "model", "created": 1793113558, "`; chip `Apple M5 Ultra; 274877906944`; suite_commit `a7ba7e392d57`

### ruler-fresh

| streams | prose total (a stream) | code total (a stream) | structured total (a stream) | list total (a stream) | first token |
|---:|---:|---:|---:|---:|---:|
| 1 | 46.7 (46.7) | 46.0 (46.0) | 46.7 (46.7) | 46.7 (46.7) | 0.12-0.13 s |
| 2 | 79.1 (39.6) | 76.5 (38.2) | 78.7 (39.3) | 79.3 (39.7) | 0.18-0.20 s |

Engine rounds (ruler-fresh):

| streams | tokens a round | drafts a round | accepted | ms a round | requests |
|---:|---:|---:|---:|---:|---:|
| 1 | 1.011 | 0.034 | 20% | 21.73 | 12 |
| 2 | 1.02 | 0.042 | 36% | 26.01 | 25 |

### ruler-after

| streams | prose total (a stream) | code total (a stream) | structured total (a stream) | list total (a stream) | first token |
|---:|---:|---:|---:|---:|---:|
| 1 | 46.2 (46.2) | 45.6 (45.6) | 46.3 (46.3) | 46.3 (46.3) | 0.12-0.13 s |

Engine rounds (ruler-after):

| streams | tokens a round | drafts a round | accepted | ms a round | requests |
|---:|---:|---:|---:|---:|---:|
| 1 | 1.012 | 0.034 | 20% | 21.95 | 13 |

### checks

| check | result |
|---|---|
| memory-idle | measured: mac: System-wide memory free percentage: 52%; total = 4096.00M  us |
| turns | pass: resumed == again: True; cold (after a restart): True; cached 5493 of 5649; ttft resumed 0.24s, cold 4.16s |
| memory-busy | measured: mac: System-wide memory free percentage: 52%; total = 4096.00M  us |

### history

| run | plan | status | 1 stream code | 16 streams code | 16 streams first token | suite |
|---|---|---|---:|---:|---:|---|
| 2026-10-27 10:05 | speed | done | 46.0 |  |  |  |
| 2026-10-27 08:05 | quick | done | 45.2 |  |  | 114/114 |

## Nanbeige4.3-33B, MLX 8-bit on 1x Apple M5 Ultra (256 GB unified), macOS

Target `nanbeige43-33b-mlx8-m5`: Nanbeige4.3-33B MLX 8-bit as published (fcmeyer/Nanbeige4.3-33B-MLX-8bit), TensorFold native Metal (llama) on one M5 Ultra (131072-token window, 2 streams). Engine: TensorFold native, Metal; served as `nanbeige`. Latest: run `20261027-103259-quick` (2026-10-27 10:32, plan quick, done).

Serving: engine_commit `657ac711c`; binary_sha256 `56fb3ebeaa8facd66a071318c4602df8920f6675171b8a3b093c639695609e9c`; served_model `{"object": "list", "data": [{"id": "nanbeige", "object": "model", "created": 1793115187, "`; chip `Apple M5 Ultra; 274877906944`; suite_commit `a7ba7e392d57`

### ruler-fresh

| streams | prose total (a stream) | code total (a stream) | structured total (a stream) | list total (a stream) | first token |
|---:|---:|---:|---:|---:|---:|
| 1 | 28.4 (28.4) | 27.9 (27.9) | 28.3 (28.3) | 28.3 (28.3) | 0.15-0.16 s |

Engine rounds (ruler-fresh):

| streams | tokens a round | drafts a round | accepted | ms a round | requests |
|---:|---:|---:|---:|---:|---:|
| 1 | 1.005 | 0.017 | 0% | 35.58 | 12 |

### ruler-after

| streams | prose total (a stream) | code total (a stream) | structured total (a stream) | list total (a stream) | first token |
|---:|---:|---:|---:|---:|---:|
| 1 | 28.3 (28.3) | 27.8 (27.8) | 28.3 (28.3) | 28.3 (28.3) | 0.15-0.16 s |

Engine rounds (ruler-after):

| streams | tokens a round | drafts a round | accepted | ms a round | requests |
|---:|---:|---:|---:|---:|---:|
| 1 | 1.007 | 0.022 | 10% | 35.76 | 13 |

### suite

| check | passed |
|---|---:|
| soak | 60/60 |
| drafts | 12/12 |
| concurrent | 12/12 |
| streaming | 4/4 |
| multiturn | 8/8 |
| stop | 3/3 |
| thinking | 10/10 |
| copy | 2/2 |
| max-tokens | 3/3 |

### checks

| check | result |
|---|---|
| memory-idle | measured: mac: System-wide memory free percentage: 46%; total = 4096.00M  us |
| structured | pass: 18/18 obey, drafted == plain 12/12; a bad regex -> 400 |
| tools | pass: 5/5 tool cases right |
| sampling | pass: 9/9 seeded replies equal on repeat and undrafted; 0 errors |
| turns | pass: resumed == again: True; cold (after a restart): True; cached 5493 of 5649; ttft resumed 0.275s, cold 4.494s |

### history

| run | plan | status | 1 stream code | 16 streams code | 16 streams first token | suite |
|---|---|---|---:|---:|---:|---|
| 2026-10-27 10:32 | quick | done | 27.9 |  |  | 114/114 |
| 2026-10-27 10:13 | speed | done | 27.9 |  |  |  |

## Nanbeige4.3-33B bf16, drafted by Nanbeige4.1-3B MLX 4-bit on 1x Apple M5 Ultra (256 GB unified), macOS

Target `nanbeige43-33b-mlxdraft-m5`: Nanbeige4.3-33B bf16 with Nanbeige4.1-3B MLX 4-bit (mlx-community) drafting, TensorFold native Metal (llama) on one M5 Ultra (131072-token window, 2 streams, every stream drafted). Engine: TensorFold native, Metal; served as `nanbeige`. Latest: run `20261028-051302-quality-off` (2026-10-28 05:13, plan quality-off, running).

Serving: engine_commit `b6524565c`; binary_sha256 `4e72f4d002aaa3097489e932c03819764d0ac957c72034463850ccaf265a0103`; served_model `{"object": "list", "data": [{"id": "nanbeige", "object": "model", "created": 1793182390, "`; chip `Apple M5 Ultra; 274877906944`; suite_commit `21db9b23f7be`

### ruler-fresh

| streams | prose total (a stream) | code total (a stream) | structured total (a stream) | list total (a stream) | first token |
|---:|---:|---:|---:|---:|---:|
| 1 | 116.7 (116.7) | 110.8 (110.8) | 109.5 (109.5) | 101.7 (101.7) | 0.23-0.26 s |

Engine rounds (ruler-fresh):

| streams | tokens a round | drafts a round | accepted | ms a round | requests |
|---:|---:|---:|---:|---:|---:|
| 1 | 4.884 | 4.755 | 81% | 44.53 | 12 |

### history

| run | plan | status | 1 stream code | 16 streams code | 16 streams first token | suite |
|---|---|---|---:|---:|---:|---|
| 2026-10-28 05:13 | quality-off | running | 110.8 |  |  |  |
| 2026-10-28 05:08 | speed | done | 109.9 |  |  |  |
| 2026-10-28 04:44 | quick | done | 110.6 |  |  | 114/114 |
| 2026-10-28 02:31 | quick | done | 94.0 |  |  | 114/114 |
| 2026-10-27 17:34 | quick | done | 106.9 |  |  | 114/114 |
| 2026-10-27 16:06 | quick | done | 113.7 |  |  | 114/114 |
| 2026-10-27 15:46 | quick | running | 109.7 |  |  |  |
| 2026-10-27 11:30 | speed | done | 110.8 |  |  |  |
| 2026-10-27 11:05 | quick | done | 110.9 |  |  | 114/114 |
| 2026-10-27 10:00 | speed | done | 110.9 |  |  |  |
| 2026-10-27 09:36 | quick | done | 113.7 |  |  | 114/114 |

## NVIDIA Nemotron 3.5 Bolt 74B-A9B (24 GB: IQ2_XXS experts, Q8_0, NVFP4 Mamba) + vision on 1x NVIDIA RTX 5090 (32 GB)

Target `nemotron-bolt-5090`: Nemotron 3.5 Bolt 74B-A9B ModelOpt IQ2_XXS/Q8_0/NVFP4, TensorFold native CUDA on one RTX 5090 (262144, two streams, vision, host prompt cache). Engine: TensorFold native, CUDA; served as `nemotron-bolt`. Latest: run `20261015-175621-full` (2026-10-15 17:56, plan full, done).

Serving: recipe_commit `f546a71`; engine_commit `b2ec378d`; served_model `{"object": "list", "data": [{"id": "nemotron-bolt", "object": "model", "created": 17920869`

### ruler-fresh

| streams | prose total (a stream) | code total (a stream) | structured total (a stream) | list total (a stream) | first token |
|---:|---:|---:|---:|---:|---:|
| 1 | 149.7 (149.7) | 149.6 (149.6) | 150.1 (150.1) | 149.7 (149.7) | 0.03-0.03 s |

Engine rounds (ruler-fresh):

| streams | tokens a round | drafts a round | accepted | ms a round | requests |
|---:|---:|---:|---:|---:|---:|
| 1 | 1.011 | 0.0 |  | 6.75 | 217 |

### ruler-after

| streams | prose total (a stream) | code total (a stream) | structured total (a stream) | list total (a stream) | first token |
|---:|---:|---:|---:|---:|---:|
| 1 | 149.3 (149.3) | 149.2 (149.2) | 149.7 (149.7) | 149.3 (149.3) | 0.03-0.03 s |

Engine rounds (ruler-after):

| streams | tokens a round | drafts a round | accepted | ms a round | requests |
|---:|---:|---:|---:|---:|---:|
| 1 | 1.007 | 0.0 |  | 6.74 | 1781 |

### suite

| check | passed |
|---|---:|
| drafts | 12/12 |
| concurrent | 12/12 |
| streaming | 4/4 |
| multiturn | 8/8 |
| stop | 3/3 |
| thinking | 10/10 |
| copy | 2/2 |
| max-tokens | 3/3 |
| tools | 58/60 |
| json | 30/30 |
| ifeval | 120/150 |
| gsm8k | 241/250 |
| mgsm | 190/240 |
| mmlu | 279/342 |
| humaneval | 153/164 |
| repetition | 8/8 |
| long-context | 55/55 |
| vision | 12/12 |
| soak | 60/60 |
| snapshot | 12/12 |

### checks

| check | result |
|---|---|
| memory-idle | measured: gpu: 28716 MiB, 32607 MiB |
| structured | pass: 18/18 obey; a bad regex -> 400 |
| sampling | pass: 9/9 seeded replies equal on repeat; 0 errors |
| turns | pass: resumed == again == cold: True; cached 5832 of 5865; ttft resumed 0.053s, cold 0.134s |
| capacity | pass: 6/6 answered, 0 refused, 0 lost (no reply); a short request after: 200 |

### history

| run | plan | status | 1 stream code | 16 streams code | 16 streams first token | suite |
|---|---|---|---:|---:|---:|---|
| 2026-10-15 17:56 | full | done | 149.6 |  |  | 1272/1437 |
| 2026-10-15 17:33 | full | running | 149.8 |  |  |  |
| 2026-10-15 17:22 | quick | done | 149.8 |  |  | 54/114 |
| 2026-10-15 17:13 | quick | done | 149.6 |  |  | 51/114 |

## Ornith-1.5-122B, 8-bit MLX affine (g64) on 1x Apple M5 Ultra (256 GB unified), macOS

Target `ornith-15-122b-8bit-native-m5`: Ornith-1.5-122B, the publisher's 8-bit MLX affine, TensorFold native Metal on one M5 Ultra. Engine: TensorFold native, Metal; served as `Ornith-1.5-122B`. Latest: run `20261029-050046-mlx-speed` (2026-10-29 05:00, plan mlx-speed, done).

Serving: engine_commit `a410eb56`; binary_sha256 `462b6a0c6d60b2743eb88fdbf0db93a560155a8cf3919ac4f694d1fc9fe156e7`; served_model `{"object": "list", "data": [{"id": "Ornith-1.5-122B", "object": "model", "created": 179326`; chip `Apple M5 Ultra; 274877906944`; suite_commit `21db9b23f7be`

### ruler-streams

| streams | prose total (a stream) | code total (a stream) | structured total (a stream) | list total (a stream) | first token |
|---:|---:|---:|---:|---:|---:|
| 1 | 57.3 (57.3) | 112.1 (112.1) | 91.0 (91.0) | 83.7 (83.7) | 0.08-0.11 s |
| 2 | 116.0 (58.0) | 171.5 (85.7) | 146.5 (73.3) | 202.3 (101.1) | 0.13-0.17 s |
| 4 | 153.8 (38.9) | 239.6 (59.8) | 188.4 (46.9) | 247.4 (62.9) | 0.21-0.28 s |

### checks

| check | result |
|---|---|
| memory-idle | measured: mac: System-wide memory free percentage: 34%; total = 2048.00M  us |

### history

| run | plan | status | 1 stream code | 16 streams code | 16 streams first token | suite |
|---|---|---|---:|---:|---:|---|
| 2026-10-29 05:00 | mlx-speed | done | 112.1 |  |  |  |
| 2026-10-29 02:14 | speed | done | 111.7 |  |  |  |
| 2026-10-29 02:00 | glm-vision | done |  |  |  | 20/22 |
| 2026-10-29 01:52 | quick | done | 112.5 |  |  | 114/114 |

## Ornith-1.5-122B, 4-bit MLX affine (g64) on 1x Apple M5 Ultra (256 GB unified), macOS

Target `ornith-15-122b-m5`: Ornith-1.5-122B, 4-bit MLX affine with images, vllm-mlx on one M5 Ultra. Engine: vllm-mlx 0.6.0 (mlx-vlm 0.7.9, mlx-lm 0.31.3, mlx 0.32.4); served as `Ornith-1.5-122B`. Latest: run `20261020-111724-mlx-speed` (2026-10-20 11:17, plan mlx-speed, done).

Serving: stack `vllm-mlx 0.6.0, mlx-vlm 0.7.9, mlx-lm 0.31.3, mlx 0.32.4`; served_model `{"object":"list","data":[{"id":"Ornith-1.5-122B","object":"model","created":1792513044,"ow`; checkpoint `{'dir': 'Ornith-1.5-122B-MLX-4bit', 'bits': 4, 'group_size': 64, 'mode': 'affine', 'revisi`; chip `Apple M5 Ultra; 274877906944`; suite_commit `277c842a1481`

### ruler-streams

| streams | prose total (a stream) | code total (a stream) | structured total (a stream) | list total (a stream) | first token |
|---:|---:|---:|---:|---:|---:|
| 1 | 66.2 (66.2) | 66.6 (66.6) | 66.4 (66.4) | 66.6 (66.6) | 0.08-0.11 s |
| 2 | 113.4 (56.7) | 113.2 (56.6) | 113.2 (56.6) | 114.0 (57.0) | 0.14-0.19 s |
| 4 | 175.9 (44.0) | 178.1 (44.9) | 177.6 (44.1) | 180.4 (44.9) | 0.25-0.35 s |

### checks

| check | result |
|---|---|
| memory-idle | measured: mac: System-wide memory free percentage: 95%; total = 7168.00M  us |

### history

| run | plan | status | 1 stream code | 16 streams code | 16 streams first token | suite |
|---|---|---|---:|---:|---:|---|
| 2026-10-20 11:17 | mlx-speed | done | 66.6 |  |  |  |

## Ornith-1.5-122B, 4-bit MLX affine (g64) on 1x Apple M5 Ultra (256 GB unified), macOS

Target `ornith-15-122b-native-m5`: Ornith-1.5-122B, 4-bit MLX affine, TensorFold native Metal on one M5 Ultra. Engine: TensorFold native, Metal; served as `Ornith-1.5-122B`. Latest: run `20261029-050010-glm-vision` (2026-10-29 05:00, plan glm-vision, done).

Serving: engine_commit `a410eb56`; binary_sha256 `462b6a0c6d60b2743eb88fdbf0db93a560155a8cf3919ac4f694d1fc9fe156e7`; served_model `{"object": "list", "data": [{"id": "Ornith-1.5-122B", "object": "model", "created": 179326`; chip `Apple M5 Ultra; 274877906944`; suite_commit `21db9b23f7be`

### suite-vision

| check | passed |
|---|---:|
| vision | 4/6 |
| vision-concurrent | 16/16 |

### history

| run | plan | status | 1 stream code | 16 streams code | 16 streams first token | suite |
|---|---|---|---:|---:|---:|---|
| 2026-10-29 05:00 | glm-vision | done |  |  |  | 20/22 |
| 2026-10-29 04:54 | mlx-speed | done | 155.9 |  |  |  |
| 2026-10-29 04:49 | quick | done | 158.0 |  |  | 114/114 |
| 2026-10-26 13:27 | glm-vision | done |  |  |  | 4/6 |
| 2026-10-26 13:19 | glm-vision | done |  |  |  | 20/20 |
| 2026-10-26 13:09 | thinking | done |  |  |  | 244/250 |
| 2026-10-26 12:53 | mlx-speed | done | 157.5 |  |  |  |
| 2026-10-26 12:48 | quick | done | 157.4 |  |  | 114/114 |
| 2026-10-26 12:30 | mlx-speed | done | 157.5 |  |  |  |
| 2026-10-26 12:25 | quick | done | 157.1 |  |  | 114/114 |
| 2026-10-26 11:16 | quick | done | 157.0 |  |  | 114/114 |
| 2026-10-26 11:04 | thinking | done |  |  |  | 244/250 |
| 2026-10-26 10:33 | dsv41-quality-off | done |  |  |  | 1448/1614 |
| 2026-10-26 08:42 | mlx-speed | done | 157.7 |  |  |  |
| 2026-10-26 08:37 | quick | done | 157.5 |  |  | 114/114 |
| 2026-10-26 07:50 | mlx-speed | done | 157.7 |  |  |  |
| 2026-10-26 07:45 | quick | done | 157.8 |  |  | 114/114 |
| 2026-10-26 03:37 | thinking | done |  |  |  | 245/250 |
| 2026-10-26 03:08 | dsv41-quality-off | done |  |  |  | 1427/1614 |
| 2026-10-26 03:02 | mlx-speed | done | 171.3 |  |  |  |
| 2026-10-26 02:57 | quick | done | 171.0 |  |  | 114/114 |
| 2026-10-26 02:54 | quick | running | 169.9 |  |  |  |
| 2026-10-25 22:37 | mlx-speed | done | 172.1 |  |  |  |
| 2026-10-25 22:32 | quick | done | 171.6 |  |  | 114/114 |
| 2026-10-25 21:43 | mlx-speed | done | 171.9 |  |  |  |
| 2026-10-25 21:38 | quick | done | 171.4 |  |  | 114/114 |
| 2026-10-25 18:54 | mlx-speed | done | 171.8 |  |  |  |
| 2026-10-25 18:39 | quick | done | 172.0 |  |  | 114/114 |
| 2026-10-21 02:20 | mlx-speed | done | 174.2 |  |  |  |
| 2026-10-20 16:39 | glm-streams | done | 95.5 | 415.0 | 0.42-0.56 s | 24/24 |
| 2026-10-20 16:34 | glm-streams | done | 157.1 | 410.5 | 0.44-0.59 s | 24/24 |
| 2026-10-20 16:19 | thinking | done |  |  |  | 244/250 |
| 2026-10-20 15:25 | mlx-speed | done | 95.6 |  |  |  |
| 2026-10-20 15:23 | mlx-speed | done | 157.0 |  |  |  |
| 2026-10-20 14:53 | dsv41-quality-off | done |  |  |  | 1444/1614 |
| 2026-10-20 14:16 | mlx-speed | done | 95.4 |  |  |  |
| 2026-10-20 14:15 | mlx-speed | done | 314.3 |  |  |  |
| 2026-10-20 14:01 | mlx-speed | done | 85.0 |  |  |  |
| 2026-10-20 14:00 | mlx-speed | done | 316.2 |  |  |  |
| 2026-10-20 13:39 | mlx-speed | done | 84.8 |  |  |  |
| 2026-10-20 13:36 | mlx-speed | done | 84.1 |  |  |  |
| 2026-10-20 13:31 | mlx-speed | done | 85.3 |  |  |  |
| 2026-10-20 13:29 | mlx-speed | done | 84.2 |  |  |  |
| 2026-10-20 13:19 | mlx-speed | done | 84.6 |  |  |  |
| 2026-10-20 12:56 | mlx-speed | done | 79.3 |  |  |  |
| 2026-10-20 12:49 | mlx-speed | done | 85.1 |  |  |  |

## Ornith-1.5-122B, 4-bit MLX affine (g64), YaRN x4 to 1M context on 1x Apple M5 Ultra (256 GB unified), macOS

Target `ornith-15-122b-yarn1m-native-m5`: Ornith-1.5-122B, 4-bit MLX affine, static YaRN x4 (one 1,048,576-token stream), TensorFold native Metal on one M5 Ultra. Engine: TensorFold native, Metal; served as `Ornith-1.5-122B`. Latest: run `20261026-014405-mlx-speed` (2026-10-26 01:44, plan mlx-speed, done).

Serving: engine_commit `1429b56b`; binary_sha256 `64f5d54183672d8cc018bfb29f8be83b0da65c0e7b9293d9e6dd70203ff87cd5`; served_model `{"object": "list", "data": [{"id": "Ornith-1.5-122B", "object": "model", "created": 179299`; chip `Apple M5 Ultra; 274877906944`; suite_commit `277c842a1481`

### ruler-streams

| streams | prose total (a stream) | code total (a stream) | structured total (a stream) | list total (a stream) | first token |
|---:|---:|---:|---:|---:|---:|
| 1 | 77.7 (77.7) | 160.6 (160.6) | 105.8 (105.8) | 111.3 (111.3) | 0.06-0.08 s |
| 2 | 228.2 (114.1) | 374.0 (187.0) | 265.3 (132.6) | 376.2 (188.1) | 0.71-1.13 s |
| 4 | 447.1 (116.2) | 774.4 (197.4) | 554.8 (138.3) | 871.1 (210.4) | 1.58-3.32 s |

### checks

| check | result |
|---|---|
| memory-idle | measured: mac: System-wide memory free percentage: 48%; total = 3072.00M  us |

### history

| run | plan | status | 1 stream code | 16 streams code | 16 streams first token | suite |
|---|---|---|---:|---:|---:|---|
| 2026-10-26 01:44 | mlx-speed | done | 160.6 |  |  |  |
| 2026-10-26 01:41 | mlx-speed | done | 179.8 |  |  |  |
| 2026-10-26 01:33 | thinking | done |  |  |  | 247/250 |
| 2026-10-26 01:30 | mlx-speed | done | 183.2 |  |  |  |
| 2026-10-26 00:46 | dsv41-quality-off | done |  |  |  | 1426/1614 |
| 2026-10-26 00:42 | mlx-speed | done | 93.5 |  |  |  |
| 2026-10-26 00:40 | mlx-speed | done | 180.8 |  |  |  |
| 2026-10-20 22:24 | thinking | done |  |  |  | 247/250 |
| 2026-10-20 21:42 | dsv41-quality-off | done |  |  |  | 1426/1614 |
| 2026-10-20 21:37 | mlx-speed | done | 95.3 |  |  |  |
| 2026-10-20 21:34 | mlx-speed | done | 193.7 |  |  |  |

## qwen38-27b on q27-base886

Target `q27-base886`: . Engine: ?; served as `qwen38-27b`. Latest: run `20261016-222607-speed` (2026-10-16 22:26, plan speed, done).

Serving: q27-base886 `{"object": "list", "data": [{"id": "qwen38-27b", "object": "model", "created": 1792189591,`

### ruler-fresh

| streams | prose total (a stream) | code total (a stream) | structured total (a stream) | list total (a stream) | first token |
|---:|---:|---:|---:|---:|---:|
| 1 | 150.0 (150.0) | 229.6 (229.6) | 167.6 (167.6) | 184.6 (184.6) | 0.10-0.10 s |

### checks

| check | result |
|---|---|
| memory-idle | measured: q27-base886: 24906 MiB, 32607 MiB |
| memory-busy | measured: q27-base886: 24906 MiB, 32607 MiB |

### history

| run | plan | status | 1 stream code | 16 streams code | 16 streams first token | suite |
|---|---|---|---:|---:|---:|---|
| 2026-10-16 22:26 | speed | done | 229.6 |  |  |  |

## qwen38-27b on q27-stack

Target `q27-stack`: . Engine: ?; served as `qwen38-27b`. Latest: run `20261016-234937-speed` (2026-10-16 23:49, plan speed, done).

Serving: q27-stack `{"object": "list", "data": [{"id": "qwen38-27b", "object": "model", "created": 1792194590,`

### ruler-fresh

| streams | prose total (a stream) | code total (a stream) | structured total (a stream) | list total (a stream) | first token |
|---:|---:|---:|---:|---:|---:|
| 1 | 210.8 (210.8) | 397.9 (397.9) | 268.4 (268.4) | 250.4 (250.4) | 0.10-0.10 s |

### checks

| check | result |
|---|---|
| memory-idle | measured: q27-stack: 24912 MiB, 32607 MiB |
| memory-busy | measured: q27-stack: 24912 MiB, 32607 MiB |

### history

| run | plan | status | 1 stream code | 16 streams code | 16 streams first token | suite |
|---|---|---|---:|---:|---:|---|
| 2026-10-16 23:49 | speed | done | 397.9 |  |  |  |
| 2026-10-16 23:04 | speed | done | 343.2 |  |  |  |
| 2026-10-16 22:37 | speed | done | 334.8 |  |  |  |
| 2026-10-16 22:26 | speed | done | 290.2 |  |  |  |

## qwen38-27b on qwen38-27b-5090-q35line

Target `qwen38-27b-5090-q35line`: . Engine: ?; served as `qwen38-27b`. Latest: run `20261016-212230-speed` (2026-10-16 21:22, plan speed, done).

Serving: engine_commit `3d763bde`; served_model `{"object": "list", "data": [{"id": "qwen38-27b", "object": "model", "created": 1792185803,`

### ruler-fresh

| streams | prose total (a stream) | code total (a stream) | structured total (a stream) | list total (a stream) | first token |
|---:|---:|---:|---:|---:|---:|
| 1 | 149.9 (149.9) | 229.4 (229.4) | 167.4 (167.4) | 184.6 (184.6) | 0.10-0.10 s |

### checks

| check | result |
|---|---|
| memory-idle | measured: gpu: 26486 MiB, 32607 MiB |
| memory-busy | measured: gpu: 26486 MiB, 32607 MiB |

### history

| run | plan | status | 1 stream code | 16 streams code | 16 streams first token | suite |
|---|---|---|---:|---:|---:|---|
| 2026-10-16 21:22 | speed | done | 229.4 |  |  |  |

## qwen38-27b on qwen38-27b-5090-q35speed

Target `qwen38-27b-5090-q35speed`: . Engine: ?; served as `qwen38-27b`. Latest: run `20261019-222616-thinking` (2026-10-19 22:26, plan thinking, done).

Serving: recipe_commit `6f7277d`; engine_commit `29eb2574`; served_model `{"object": "list", "data": [{"id": "qwen38-27b", "object": "model", "created": 1792448776,`

### suite-thinking

| check | passed |
|---|---:|
| gsm8k | 222/250 |

### checks

| check | result |
|---|---|
| thinking | pass: thinking on: 10/10 right, 10/10 with reasoning_content, 0 leaks, 0 errors |

### history

| run | plan | status | 1 stream code | 16 streams code | 16 streams first token | suite |
|---|---|---|---:|---:|---:|---|
| 2026-10-19 22:26 | thinking | done |  |  |  | 222/250 |
| 2026-10-19 21:44 | full | done | 436.8 |  |  | 1137/1273 |
| 2026-10-19 18:52 | speed | done | 450.8 |  |  |  |

## qwen38-27b on qwen38-27b-5090-v111

Target `qwen38-27b-5090-v111`: . Engine: ?; served as `qwen38-27b`. Latest: run `20261019-141223-full` (2026-10-19 14:12, plan full, running).

Serving: recipe_commit `6f7277d`; engine_commit `b10231b9`; served_model `{"object": "list", "data": [{"id": "qwen38-27b", "object": "model", "created": 1792419740,`

### ruler-fresh

| streams | prose total (a stream) | code total (a stream) | structured total (a stream) | list total (a stream) | first token |
|---:|---:|---:|---:|---:|---:|
| 1 | 210.2 (210.2) | 396.6 (396.6) | 265.7 (265.7) | 258.8 (258.8) | 0.10-0.10 s |

### checks

| check | result |
|---|---|
| memory-idle | measured: gpu: 26904 MiB, 32607 MiB |

### history

| run | plan | status | 1 stream code | 16 streams code | 16 streams first token | suite |
|---|---|---|---:|---:|---:|---|
| 2026-10-19 14:12 | full | running | 396.6 |  |  |  |

## Qwen3.8-27B, MLX 4-bit + DFlash2 on 1x NVIDIA RTX 5090 (32 GB)

Target `qwen38-27b-5090`: Qwen3.8-27B MLX 4-bit + DFlash2, TensorFold native CUDA on one RTX 5090 (fp8 KV, 262k, one stream, vision). Engine: TensorFold native, CUDA; served as `qwen38-27b`. Latest: run `20261027-204231-streams` (2026-10-27 20:42, plan streams, done).

Serving: recipe_commit `be63697`; engine_commit `59044397a`; served_model `{"object": "list", "data": [{"id": "qwen38-27b", "object": "model", "created": 1793133763,`; suite_commit `49a346d8899c`

### ruler-streams

| streams | prose total (a stream) | code total (a stream) | structured total (a stream) | list total (a stream) | first token |
|---:|---:|---:|---:|---:|---:|
| 1 | 278.0 (278.0) | 535.5 (535.5) | 352.0 (352.0) | 337.0 (337.0) | 0.06-0.06 s |
| 2 | 445.8 (222.9) | 737.1 (368.6) | 504.3 (252.2) | 737.0 (368.5) | 0.09-0.09 s |
| 4 | 741.9 (173.6) | 1396.5 (297.3) | 839.2 (198.1) | 1217.9 (305.9) | 0.15-0.15 s |

### suite-together

| check | passed |
|---|---:|
| concurrent | 12/12 |
| drafts | 12/12 |

### checks

| check | result |
|---|---|
| memory-idle | measured: gpu: 30914 MiB, 32607 MiB |
| memory-busy | measured: gpu: 31088 MiB, 32607 MiB |

### history

| run | plan | status | 1 stream code | 16 streams code | 16 streams first token | suite |
|---|---|---|---:|---:|---:|---|
| 2026-10-27 20:42 | streams | done | 535.5 |  |  | 24/24 |
| 2026-10-27 20:42 | vision | done |  |  |  | 12/12 |
| 2026-10-27 20:38 | quick | done | 537.8 |  |  | 113/114 |
| 2026-10-27 20:33 | streams | done | 536.9 |  |  | 24/24 |
| 2026-10-27 20:31 | streams | done | 536.6 |  |  | 24/24 |
| 2026-10-27 20:30 | together | done |  |  |  | 24/24 |
| 2026-10-27 20:29 | together | done |  |  |  | 24/24 |
| 2026-10-27 20:28 | together | done |  |  |  | 24/24 |
| 2026-10-27 20:27 | together | done |  |  |  | 24/24 |
| 2026-10-27 20:14 | vision | done |  |  |  | 12/12 |
| 2026-10-27 20:10 | quick | done | 537.7 |  |  | 113/114 |
| 2026-10-26 01:29 | humaneval-penalized | done |  |  |  | 154/164 |
| 2026-10-26 01:28 | humaneval-sampled | done |  |  |  | 153/164 |
| 2026-10-26 01:26 | humaneval-off | done |  |  |  | 152/164 |
| 2026-10-26 00:54 | after-long | done | 538.9 |  |  |  |
| 2026-10-26 00:06 | quality-penalized | done | 539.1 |  |  | 1127/1273 |
| 2026-10-25 23:24 | quality-sampled | done | 537.7 |  |  | 1142/1273 |
| 2026-10-25 22:42 | quality-off | done | 538.0 |  |  | 1143/1273 |
| 2026-10-25 20:16 | streams | done | 537.6 |  |  | 24/24 |
| 2026-10-25 20:14 | streams | done | 537.5 |  |  | 24/24 |
| 2026-10-25 20:13 | together | done |  |  |  | 18/24 |
| 2026-10-25 20:11 | together | done |  |  |  | 24/24 |
| 2026-10-25 20:10 | together | done |  |  |  | 24/24 |
| 2026-10-25 20:09 | together | done |  |  |  | 24/24 |
| 2026-10-25 20:09 | together | done |  |  |  | 20/24 |
| 2026-10-25 20:08 | together | done |  |  |  | 24/24 |
| 2026-10-25 20:05 | streams | done | 538.6 |  |  | 18/24 |
| 2026-10-25 20:04 | streams | done | 538.4 |  |  | 19/24 |
| 2026-10-25 20:03 | streams | done | 539.2 |  |  | 18/24 |
| 2026-10-25 19:53 | quick | done | 538.1 |  |  | 113/114 |
| 2026-10-22 11:50 | humaneval-fresh | done |  |  |  | 152/164 |
| 2026-10-22 11:12 | quality-off | done | 497.1 |  |  | 1143/1273 |
| 2026-10-22 11:10 | after-long | done | 496.1 |  |  |  |
| 2026-10-22 11:07 | after-long | done | 496.1 |  |  |  |
| 2026-10-22 11:03 | quick | done | 497.7 |  |  | 113/114 |
| 2026-10-22 10:30 | after-long | done | 497.6 |  |  |  |
| 2026-10-22 10:26 | after-long | done | 498.2 |  |  |  |
| 2026-10-22 10:11 | quick | done | 496.8 |  |  | 113/114 |
| 2026-10-22 00:34 | quick | done | 497.2 |  |  | 113/114 |
| 2026-10-21 22:53 | quality-off | done | 498.5 |  |  | 1295/1437 |
| 2026-10-21 22:18 | ruler3 | done | 484.8 |  |  |  |
| 2026-10-21 20:50 | quality-off | done | 500.1 |  |  | 1295/1437 |
| 2026-10-21 17:28 | quality-off | done | 485.5 |  |  | 1294/1437 |
| 2026-10-21 16:25 | quick | done | 486.0 |  |  | 113/114 |
| 2026-10-21 08:44 | soak-ab | done | 474.6 |  |  | 60/60 |
| 2026-10-21 08:37 | bisect-mgsm | done | 474.5 |  |  | 214/240 |
| 2026-10-21 08:35 | bisect-soak | done | 440.6 |  |  | 60/60 |
| 2026-10-21 08:34 | bisect-concurrent | done | 475.6 |  |  | 12/12 |
| 2026-10-21 08:21 | bisect-long-context | done | 473.9 |  |  | 55/55 |
| 2026-10-21 08:20 | ruler-restart | done | 476.1 |  |  |  |
| 2026-10-21 08:19 | ruler1 | done | 373.2 |  |  |  |
| 2026-10-21 08:19 | ruler1 | done | 373.7 |  |  |  |
| 2026-10-21 08:18 | humaneval | done |  |  |  | 151/164 |
| 2026-10-21 08:16 | humaneval | done |  |  |  |  |
| 2026-10-21 07:35 | full | done | 478.1 |  |  | 1137/1273 |
| 2026-10-19 22:30 | full | running | 456.9 |  |  |  |
| 2026-10-19 18:53 | speed | done | 458.0 |  |  |  |
| 2026-10-16 21:24 | speed | done | 459.2 |  |  |  |
| 2026-10-16 11:14 | quick | done | 459.0 |  |  | 113/114 |
| 2026-10-14 00:00 | published evidence | published |  |  |  |  |
| 2026-10-13 00:00 | published evidence | published |  |  |  |  |
| 2026-10-12 00:00 | published evidence | published |  |  |  | 1229/1437 |
| 2026-10-12 00:00 | published evidence | published |  |  |  | 1289/1437 |
| 2026-10-12 00:00 | published evidence | published |  |  |  |  |
| 2026-10-12 00:00 | published evidence | published |  |  |  |  |

## Qwen3.8-Flash-Next, MLX 6-bit on 1x Apple M5 Ultra (256 GB unified), macOS

Target `qwen38-flashnext-mlx6bit-m5`: Qwen3.8-Flash-Next MLX 6-bit, TensorFold native on one M5 Ultra. Engine: TensorFold native, Metal; served as `Qwen3.8-Flash-Next-MLX-6bit`. Latest: run `evidence/2026-10-11-suite-rest` (2026-10-11 00:00, plan published evidence, published).

### suite

| check | passed |
|---|---:|
| ifeval | 134/150 |
| gsm8k | 242/250 |
| mgsm | 225/240 |
| mmlu | 282/342 |
| repetition | 8/8 |
| long-context | 55/55 |
| concurrent | 12/12 |
| snapshot | 12/12 |

### history

| run | plan | status | 1 stream code | 16 streams code | 16 streams first token | suite |
|---|---|---|---:|---:|---:|---|
| 2026-10-11 00:00 | published evidence | published |  |  |  | 970/1069 |
| 2026-10-11 00:00 | published evidence | published | 205.9 |  |  | 24/24 |
| 2026-10-11 00:00 | published evidence | published |  |  |  | 157/164 |
| 2026-10-11 00:00 | published evidence | published | 199.8 |  |  |  |
| 2026-10-11 00:00 | published evidence | published |  |  |  | 131/132 |
| 2026-10-11 00:00 | published evidence | published | 206.2 |  |  |  |

## Qwen3.8-Flash-Next, 6-bit with vision on 1x Apple M5 Ultra (256 GB unified), macOS

Target `qwen38-flashnext-vision-m5`: Qwen3.8-Flash-Next 6-bit MTP with images and video, TensorFold native Metal on one M5 Ultra. Engine: TensorFold native, Metal; served as `Qwen3.8-Flash-Next-MLX-6bit`. Latest: run `20261017-120921-fn-speed` (2026-10-17 12:09, plan fn-speed, done).

Serving: engine_commit `394d2e35`; binary_sha256 `43a9c01ac3eee31998def08595f5e4fc6d29819d46799a8ac01b7cdffd72b668`; served_model `{"object": "list", "data": [{"id": "Qwen3.8-Flash-Next-MLX-6bit", "object": "model", "crea`; chip `Apple M5 Ultra; 274877906944`

### ruler-fresh

| streams | prose total (a stream) | code total (a stream) | structured total (a stream) | list total (a stream) | first token |
|---:|---:|---:|---:|---:|---:|
| 1 | 142.4 (142.4) | 209.5 (209.5) | 173.2 (173.2) | 206.5 (206.5) | 0.11-0.13 s |
| 2 | 197.6 (98.8) | 261.9 (130.9) | 221.5 (110.7) | 271.5 (135.8) | 0.17-0.19 s |

### suite

| check | passed |
|---|---:|
| drafts | 12/12 |
| concurrent | 12/12 |

### checks

| check | result |
|---|---|
| structured | pass: 18/18 obey; a bad regex -> 400 |

### history

| run | plan | status | 1 stream code | 16 streams code | 16 streams first token | suite |
|---|---|---|---:|---:|---:|---|
| 2026-10-17 12:09 | fn-speed | done | 209.5 |  |  | 24/24 |
| 2026-10-17 12:06 | fn-speed | done | 209.8 |  |  | 24/24 |
| 2026-10-17 11:34 | fn-1m | done | 197.4 |  |  | 24/24 |
| 2026-10-17 11:31 | fn-media | done | 208.9 |  |  | 24/24 |
| 2026-10-17 08:04 | fn-speed | done | 206.1 |  |  | 24/24 |
| 2026-10-17 08:02 | fn-speed | done | 204.3 |  |  | 24/24 |
| 2026-10-17 05:58 | fn-speed | done | 208.0 |  |  | 24/24 |
| 2026-10-17 01:00 | fn-speed | done | 202.8 |  |  | 24/24 |
| 2026-10-17 00:57 | fn-speed | done | 207.3 |  |  | 24/24 |
| 2026-10-16 19:29 | fn-speed | done | 201.8 |  |  | 24/24 |
| 2026-10-16 19:26 | fn-speed | done | 207.3 |  |  | 24/24 |
| 2026-10-12 00:00 | published evidence | published | 174.1 |  |  |  |
| 2026-10-12 00:00 | published evidence | published | 202.7 |  |  |  |
| 2026-10-12 00:00 | published evidence | published | 176.6 |  |  |  |
| 2026-10-11 00:00 | published evidence | published | 205.6 |  |  | 131/132 |
| 2026-10-11 00:00 | published evidence | published | 178.9 |  |  | 513/544 |

## Qwen3.8-Flash-Next INT4-Mixed (AutoRound) on 2x NVIDIA DGX Spark (GB10, 128 GB unified each), TP=2 over RoCE

Target `qwen38-int4mixed`: Qwen3.8-Flash-Next INT4-Mixed, TensorFold native, TP=2 on two DGX Sparks. Engine: TensorFold native, CUDA; served as `Qwen3.8-Flash-Next-INT4-Mixed`. Latest: run `evidence/2026-10-27-native-v1.1.6` (2026-10-27 00:00, plan published evidence, published).

### ruler

| streams | prose total (a stream) | code total (a stream) | structured total (a stream) | list total (a stream) | first token |
|---:|---:|---:|---:|---:|---:|
| 1 | 78.2 (78.2) | 127.1 (127.1) | 102.5 (102.5) | 130.6 (130.6) | 0.04-0.04 s |
| 4 | 161.1 (40.4) | 257.2 (66.7) | 205.2 (50.9) | 293.5 (69.7) | 0.08-0.10 s |
| 16 | 305.1 (19.0) | 516.3 (31.0) | 393.1 (23.9) | 526.9 (32.0) | 0.46-0.51 s |

### suite

| check | passed |
|---|---:|
| drafts | 12/12 |
| concurrent | 12/12 |
| streaming | 4/4 |
| multiturn | 8/8 |
| stop | 3/3 |
| thinking | 10/10 |
| copy | 2/2 |
| max-tokens | 3/3 |
| tools | 60/60 |
| json | 30/30 |
| ifeval | 130/150 |
| gsm8k | 241/250 |
| mgsm | 219/240 |
| mmlu | 283/342 |
| humaneval | 157/164 |
| repetition | 8/8 |
| long-context | 55/55 |
| vision | 12/12 |
| soak | 60/60 |
| snapshot | 12/12 |

### history

| run | plan | status | 1 stream code | 16 streams code | 16 streams first token | suite |
|---|---|---|---:|---:|---:|---|
| 2026-10-27 00:00 | published evidence | published | 127.1 | 516.3 | 0.46-0.51 s | 1321/1437 |
| 2026-10-17 07:25 | rebase | done | 127.0 | 516.3 | 0.45-0.54 s | 114/114 |
| 2026-10-15 17:13 | full | done | 127.0 | 509.8 | 0.44-0.55 s | 1321/1437 |
| 2026-10-15 00:00 | published evidence | published | 123.4 | 472.9 | 0.52-0.74 s | 1321/1437 |
| 2026-10-15 00:00 | published evidence | published |  |  |  | 1321/1437 |
| 2026-10-11 00:00 | published evidence | published | 120.1 | 507.2 | 0.54-0.62 s | 1321/1437 |
| 2026-10-11 00:00 | published evidence | published | 120.4 | 507.1 | 0.50-0.59 s |  |
| 2026-10-10 09:45 | quick | done | 105.3 |  |  | 54/54 |
| 2026-10-10 00:00 | published evidence | published | 122.0 | 510.3 | 0.40-0.49 s | 114/114 |
| 2026-10-10 00:00 | published evidence | published | 125.9 | 510.9 | 0.44-0.49 s | 1261/1377 |
| 2026-10-10 00:00 | published evidence | published | 125.7 | 506.7 | 0.42-0.49 s | 54/54 |
| 2026-10-10 00:00 | published evidence | published | 106.1 | 506.1 | 0.42-0.51 s | 54/54 |
| 2026-10-10 00:00 | published evidence | published | 110.0 | 511.8 | 0.41-0.55 s | 1261/1377 |
| 2026-10-10 00:00 | published evidence | published | 105.8 | 505.5 | 0.41-0.46 s | 1261/1377 |
| 2026-10-09 00:00 | published evidence | published | 105.2 | 412.2 | 0.78-0.98 s | 1260/1377 |
| 2026-10-09 00:00 | published evidence | published |  |  |  | 1256/1377 |
| 2026-10-08 00:00 | published evidence | published | 107.1 | 519.4 | 0.44-0.56 s |  |
| 2026-10-08 00:00 | published evidence | published | 107.7 | 474.0 | 0.52-0.66 s | 145/145 |
| 2026-10-08 00:00 | published evidence | published | 107.6 | 442.6 | 0.44-0.58 s | 36/36 |
| 2026-10-08 00:00 | published evidence | published | 107.6 | 441.7 | 0.45-0.58 s |  |
| 2026-10-07 00:00 | published evidence | published |  |  |  | 12/12 |

## Spark-X2.6-4B, MLX 8-bit on 1x NVIDIA RTX 4090 (24 GB), Windows

Target `spark-x26-4b-4090`: Spark-X2.6-4B MLX 8-bit, TensorFold native CUDA (spark2_5) on one RTX 4090, Windows (32768-token window, 4 streams). Engine: TensorFold native, CUDA; served as `spark`. Latest: run `20261025-041904-full` (2026-10-25 04:19, plan full, done).

Serving: engine_commit `9d352b66`; binary_sha256 `978f64996b777498553acd0672b167a0730b20c0b46635ac0ceb88ede4ed0b7f`; served_model `{"object": "list", "data": [{"id": "spark", "object": "model", "created": 1792919956, "own`; gpu `NVIDIA GeForce RTX 4090, 616.56`; suite_commit `e91d8816c7e8`

### ruler-fresh

| streams | prose total (a stream) | code total (a stream) | structured total (a stream) | list total (a stream) | first token |
|---:|---:|---:|---:|---:|---:|
| 1 | 145.9 (145.9) | 144.0 (144.0) | 147.3 (147.3) | 146.3 (146.3) | 0.03-0.05 s |
| 4 | 547.6 (137.0) | 547.0 (136.8) | 551.8 (137.5) | 550.1 (137.6) | 0.07-0.07 s |

### ruler-after

| streams | prose total (a stream) | code total (a stream) | structured total (a stream) | list total (a stream) | first token |
|---:|---:|---:|---:|---:|---:|
| 1 | 145.5 (145.5) | 143.8 (143.8) | 147.2 (147.2) | 146.1 (146.1) | 0.04-0.05 s |

### suite

| check | passed |
|---|---:|
| drafts | 12/12 |
| concurrent | 12/12 |
| streaming | 4/4 |
| multiturn | 8/8 |
| stop | 3/3 |
| thinking | 10/10 |
| copy | 2/2 |
| max-tokens | 3/3 |
| tools | 53/60 |
| json | 30/30 |
| ifeval | 117/150 |
| gsm8k | 232/250 |
| mgsm | 175/240 |
| mmlu | 257/342 |
| humaneval | 0/0 |
| repetition | 7/8 |
| long-context | 16/16 |
| vision | 0/12 |
| soak | 60/60 |
| snapshot | 12/12 |

### checks

| check | result |
|---|---|
| memory-idle | measured: gpu: 10674 MiB, 24564 MiB |
| tools | pass: 1/1 tool cases right; not tested (features.structured = false): required, named, named/thinking, named/stream |
| sampling | pass: 9/9 seeded replies equal on repeat and undrafted; 0 errors |
| turns | pass: resumed == again: True; cold (after a restart): True; cached 5568 of 5630; ttft resumed 0.383s, cold 0.885s |

### history

| run | plan | status | 1 stream code | 16 streams code | 16 streams first token | suite |
|---|---|---|---:|---:|---:|---|
| 2026-10-25 04:19 | full | done | 144.0 |  |  | 1013/1234 |
| 2026-10-25 04:00 | full | done | 144.2 |  |  | 997/1218 |

## Spark-X2.6-4B, MLX 8-bit on 1x NVIDIA RTX 5090 (32 GB)

Target `spark-x26-4b-5090`: Spark-X2.6-4B MLX 8-bit, TensorFold native CUDA (main), one RTX 5090, 32k window, 4 streams, no drafter. Engine: TensorFold native, CUDA (main); served as `spark`. Latest: run `20261026-044629-streams` (2026-10-26 04:46, plan streams, done).

Serving: engine_commit `31a864f13`; model `ca74508b40984452`; suite_commit `49a346d8899c`

### ruler-streams

| streams | prose total (a stream) | code total (a stream) | structured total (a stream) | list total (a stream) | first token |
|---:|---:|---:|---:|---:|---:|
| 1 | 199.1 (199.1) | 190.9 (190.9) | 202.7 (202.7) | 203.7 (203.7) | 0.03-0.03 s |
| 2 | 375.0 (187.5) | 376.5 (188.2) | 376.0 (188.0) | 389.1 (194.5) | 0.04-0.04 s |
| 4 | 716.4 (178.9) | 708.9 (178.9) | 725.8 (182.7) | 728.9 (182.2) | 0.06-0.06 s |

### suite-together

| check | passed |
|---|---:|
| concurrent | 12/12 |
| drafts | 12/12 |

### history

| run | plan | status | 1 stream code | 16 streams code | 16 streams first token | suite |
|---|---|---|---:|---:|---:|---|
| 2026-10-26 04:46 | streams | done | 190.9 |  |  | 24/24 |
| 2026-10-26 04:45 | exact | done |  |  |  | 12/12 |
| 2026-10-26 04:42 | speed | done | 191.2 |  |  |  |

## Spark-X2.6-4B, MLX 8-bit on 1x Apple M5 Ultra (256 GB unified), macOS

Target `spark-x26-4b-8bit-m5`: Spark-X2.6-4B MLX affine 8-bit (a lossy conversion of the release), TensorFold native Metal (spark2_5) on one M5 Ultra (262144-token window, 4 streams). Engine: TensorFold native, Metal; served as `spark`. Latest: run `20261025-180037-mlx-speed` (2026-10-25 18:00, plan mlx-speed, done).

Serving: engine_commit `cc840195e`; binary_sha256 `5a20c6f0cb2289384f0deda99840d9acc01d10766beea0cfb1d1de78e938be46`; served_model `{"object": "list", "data": [{"id": "spark", "object": "model", "created": 1792969237, "own`; chip `Apple M5 Ultra; 274877906944`; suite_commit `277c842a1481`

### ruler-streams

| streams | prose total (a stream) | code total (a stream) | structured total (a stream) | list total (a stream) | first token |
|---:|---:|---:|---:|---:|---:|
| 1 | 167.1 (167.1) | 167.0 (167.0) | 166.9 (166.9) | 167.1 (167.1) | 0.03-0.05 s |
| 2 | 267.6 (133.8) | 260.8 (130.4) | 272.0 (136.0) | 265.4 (132.7) | 0.05-0.08 s |
| 4 | 368.3 (92.1) | 354.6 (88.6) | 369.6 (93.3) | 364.3 (90.5) | 0.09-0.13 s |

Engine rounds (ruler-streams):

| streams | tokens a round | drafts a round | accepted | ms a round | requests |
|---:|---:|---:|---:|---:|---:|
| 1 | 1.005 | 0.0 |  | 6.02 | 12 |
| 2 | 1.01 | 0.034 | 15% | 7.58 | 25 |
| 4 | 1.008 | 0.021 | 15% | 11.06 | 50 |

### checks

| check | result |
|---|---|
| memory-idle | measured: mac: System-wide memory free percentage: 93%; total = 3072.00M  us |

### history

| run | plan | status | 1 stream code | 16 streams code | 16 streams first token | suite |
|---|---|---|---:|---:|---:|---|
| 2026-10-25 18:00 | mlx-speed | done | 167.0 |  |  |  |
| 2026-10-25 17:57 | speed | done | 166.6 |  |  |  |
| 2026-10-25 17:54 | quick | done | 167.7 |  |  | 114/114 |

## Spark-X2.6-4B, bf16 on 1x Apple M5 Ultra (256 GB unified), macOS

Target `spark-x26-4b-m5`: Spark-X2.6-4B bf16 as released, TensorFold native Metal (spark2_5) on one M5 Ultra (262144-token window, 4 streams). Engine: TensorFold native, Metal; served as `spark`. Latest: run `20261025-172137-quick` (2026-10-25 17:21, plan quick, done).

Serving: engine_commit `cc840195e`; binary_sha256 `5a20c6f0cb2289384f0deda99840d9acc01d10766beea0cfb1d1de78e938be46`; served_model `{"object": "list", "data": [{"id": "spark", "object": "model", "created": 1792966905, "own`; chip `Apple M5 Ultra; 274877906944`; suite_commit `277c842a1481`

### ruler-fresh

| streams | prose total (a stream) | code total (a stream) | structured total (a stream) | list total (a stream) | first token |
|---:|---:|---:|---:|---:|---:|
| 1 | 106.0 (106.0) | 106.1 (106.1) | 106.1 (106.1) | 106.0 (106.0) | 0.05-0.07 s |

Engine rounds (ruler-fresh):

| streams | tokens a round | drafts a round | accepted | ms a round | requests |
|---:|---:|---:|---:|---:|---:|
| 1 | 1.005 | 0.0 |  | 9.47 | 12 |

### ruler-after

| streams | prose total (a stream) | code total (a stream) | structured total (a stream) | list total (a stream) | first token |
|---:|---:|---:|---:|---:|---:|
| 1 | 105.7 (105.7) | 105.7 (105.7) | 105.5 (105.5) | 105.3 (105.3) | 0.05-0.07 s |

Engine rounds (ruler-after):

| streams | tokens a round | drafts a round | accepted | ms a round | requests |
|---:|---:|---:|---:|---:|---:|
| 1 | 1.005 | 0.0 |  | 9.52 | 13 |

### suite

| check | passed |
|---|---:|
| soak | 60/60 |
| drafts | 12/12 |
| concurrent | 12/12 |
| streaming | 4/4 |
| multiturn | 7/8 |
| stop | 3/3 |
| thinking | 10/10 |
| copy | 2/2 |
| max-tokens | 3/3 |

### checks

| check | result |
|---|---|
| memory-idle | measured: mac: System-wide memory free percentage: 90%; total = 3072.00M  us |
| structured | pass: 18/18 obey, drafted == plain 12/12; a bad regex -> 400 |
| tools | pass: 5/5 tool cases right |
| sampling | pass: 9/9 seeded replies equal on repeat and undrafted; 0 errors |
| turns | pass: resumed == again: True; cold (after a restart): True; cached 5499 of 5624; ttft resumed 0.066s, cold 0.59s |

### history

| run | plan | status | 1 stream code | 16 streams code | 16 streams first token | suite |
|---|---|---|---:|---:|---:|---|
| 2026-10-25 17:21 | quick | done | 106.1 |  |  | 113/114 |
| 2026-10-25 17:04 | mlx-speed | done | 105.3 |  |  |  |
| 2026-10-25 16:22 | speed | done | 106.0 |  |  |  |
| 2026-10-25 16:16 | quick | done | 106.1 |  |  | 113/114 |
| 2026-10-25 15:41 | speed | done | 165.9 |  |  |  |
| 2026-10-25 15:36 | quick | done | 166.5 |  |  | 114/114 |
| 2026-10-25 15:00 | speed | done | 165.9 |  |  |  |
| 2026-10-25 14:55 | quick | done | 166.8 |  |  | 114/114 |

## Step-5-Preview, MLX 2-bit experts (8-bit rest) + MTP on 1x Apple M5 Ultra (256 GB unified), macOS

Target `step5-m5`: Step-5-Preview 2-bit (experts 2/128, rest 8/64, MTP, images), TensorFold native Metal on one M5 Ultra. Engine: TensorFold native, Metal; served as `step5-preview`. Latest: run `20261016-102144-pr903-final` (2026-10-16 10:21, plan pr903-final, done).

Serving: engine_commit `e2bb58db`; binary_sha256 `61059a383f74fd363f17527526fdc7de028fe624d40e59e3238d20e4925bfef5`; served_model `{"object": "list", "data": [{"id": "step5-preview", "object": "model", "created": 17921641`; chip `Apple M5 Ultra; 274877906944`

### ruler-fresh

| streams | prose total (a stream) | code total (a stream) | structured total (a stream) | list total (a stream) | first token |
|---:|---:|---:|---:|---:|---:|
| 1 | 38.5 (38.5) | 50.4 (50.4) | 40.5 (40.5) | 47.9 (47.9) | 0.24-0.28 s |

Engine rounds (ruler-fresh):

| streams | tokens a round | drafts a round | accepted | ms a round | requests |
|---:|---:|---:|---:|---:|---:|
| 1 | 2.381 | 2.072 | 67% | 53.72 | 12 |

### suite

| check | passed |
|---|---:|
| vision | 12/12 |
| drafts | 12/12 |
| concurrent | 12/12 |

### checks

| check | result |
|---|---|
| memory-idle | measured: mac: System-wide memory free percentage: 27%; total = 4096.00M  us |
| turns | pass: resumed == again == cold: True; cached 4514 of 4618; ttft resumed 0.353s, cold 3.21s |

### history

| run | plan | status | 1 stream code | 16 streams code | 16 streams first token | suite |
|---|---|---|---:|---:|---:|---|
| 2026-10-16 10:21 | pr903-final | done | 50.4 |  |  | 36/36 |
| 2026-10-16 09:23 | pr903 | done | 50.4 |  |  | 156/156 |
| 2026-10-15 19:44 | one-stream | done | 50.9 |  |  | 220/232 |
| 2026-10-15 19:28 | quick | done | 50.5 |  |  | 114/114 |
| 2026-10-15 18:52 | quick | done | 50.6 |  |  | 114/114 |
| 2026-10-15 13:43 | one-stream | done | 50.6 |  |  | 220/232 |
| 2026-10-15 12:43 | quick | done | 50.6 |  |  |  |

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

