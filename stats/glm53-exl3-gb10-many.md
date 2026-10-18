# GLM-5.3-Flash EXL3 4bpw on 2x NVIDIA DGX Spark (GB10, 128 GB unified each), TP=2 over RoCE

Target `glm53-exl3-gb10-many`: #1014 merged onto TensorFold main 76aafcf2: batched prompts (prefill_many) with DFlash2's feed and the hold fix, GLM-5.3-Flash EXL3 4bpw, TP=2. Engine: TensorFold native, CUDA: families/glm (many). Rendered from `stats/glm53-exl3-gb10-many.json` (2 runs); aggregate tok/s, total (a stream).

## 2026-10-18 14:29: run `20261018-142953-glm-quality`

Plan glm-quality, done; served as `GLM-5.3-Flash-EXL3`.

Serving: binary `07ab411ad6bef70e`

### ruler-fresh

| streams | prose total (a stream) | code total (a stream) | structured total (a stream) | list total (a stream) | first token |
|---:|---:|---:|---:|---:|---:|
| 1 | 42.2 (42.2) | 60.1 (60.1) | 57.2 (57.2) | 57.7 (57.7) | 0.17-0.22 s |

### suite

| check | passed |
|---|---:|
| drafts | 12/12 |
| streaming | 4/4 |
| multiturn | 8/8 |
| stop | 3/3 |
| thinking | 10/10 |
| copy | 1/2 |
| max-tokens | 3/3 |
| tools | 58/60 |
| json | 27/30 |
| ifeval | 100/150 |
| gsm8k | 241/250 |
| mgsm | 223/240 |
| mmlu | 293/342 |
| math500 | 433/500 |
| gpqa | 125/198 |
| humaneval | 151/164 |
| repetition | 7/8 |
| long-context | 0/0 |
| vision | 6/6 |
| chartqa | 151/200 |
| docvqa | 63/200 |
| concurrent | 12/12 |
| vision-concurrent | 16/16 |

### suite-thinking

| check | passed |
|---|---:|
| gsm8k | 248/250 |
| ifeval | 100/150 |

### checks

| check | result |
|---|---|
| memory-idle | measured: head 28.4 GiB available |
| thinking | pass: thinking on: 10/10 right, 10/10 with reasoning_content, 0 leaks, 0 errors |

## 2026-10-18 13:40: run `20261018-134056-glm-qual1014`

Plan glm-qual1014, done; served as `GLM-5.3-Flash-EXL3`.

Serving: binary `07ab411ad6bef70e`

### ruler-c1-16

| streams | prose total (a stream) | code total (a stream) | structured total (a stream) | list total (a stream) | first token |
|---:|---:|---:|---:|---:|---:|
| 1 | 42.5 (42.4) | 67.8 (68.3) | 56.2 (55.7) | 56.0 (53.7) | 0.17-0.23 s |

### ruler-streams

| streams | prose total (a stream) | code total (a stream) | structured total (a stream) | list total (a stream) | first token |
|---:|---:|---:|---:|---:|---:|
| 8 | 92.8 (11.7) | 132.9 (16.1) | 125.3 (15.6) | 144.5 (17.1) | 0.83-1.06 s |
| 16 | 118.0 (7.3) | 134.1 (8.1) | 146.4 (9.2) | 158.9 (9.6) | 1.35-1.67 s |

### suite

| check | passed |
|---|---:|
| concurrent | 12/12 |
| drafts | 12/12 |

