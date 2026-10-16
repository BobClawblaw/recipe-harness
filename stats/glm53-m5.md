# GLM-5.3-Flash, MLX 4-bit on 1x Apple M5 Ultra (256 GB unified), macOS

Target `glm53-m5`: GLM-5.3-Flash MLX 4-bit, TensorFold native on one M5 Ultra Mac (one stream, greedy). Engine: TensorFold native, Metal. Rendered from `stats/glm53-m5.json` (10 runs); aggregate tok/s, total (a stream).

## 2026-10-16 08:23: run `20261016-082326-glm-gate-novision`

Plan glm-gate-novision, done; served as `GLM-5.3-Flash-MLX-4bit`.

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

## 2026-10-16 08:04: run `20261016-080418-glm-gate-novision`

Plan glm-gate-novision, done; served as `GLM-5.3-Flash-MLX-4bit`.

Serving: engine_commit `46a08c18`; binary_sha256 `c040cfbfafa63174bdd6b668e3c23ebaf3afb26c2dcab9516a430790009c5390`

### ruler-fresh

| streams | prose total (a stream) | code total (a stream) | structured total (a stream) | list total (a stream) | first token |
|---:|---:|---:|---:|---:|---:|
| 1 | 77.7 (77.7) | 77.6 (77.6) | 77.8 (77.8) | 77.9 (77.9) | 0.10-0.15 s |

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
| mmlu | 292/342 |

## 2026-10-16 00:35: run `20261016-003511-glm-gate`

Plan glm-gate, done; served as `GLM-5.3-Flash-MLX-4bit`.

Serving: engine_commit `c5304036`; binary_sha256 `507c6fc3b1f9f5a521185d3da00ec3f555c39e20188ba8eefec2547581bb618d`

### ruler-fresh

| streams | prose total (a stream) | code total (a stream) | structured total (a stream) | list total (a stream) | first token |
|---:|---:|---:|---:|---:|---:|
| 1 | 78.0 (78.0) | 78.7 (78.7) | 77.9 (77.9) | 87.0 (87.0) | 0.11-0.15 s |

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
| vision | 12/12 |
| gsm8k | 246/250 |
| mmlu | 290/342 |

## 2026-10-10 00:00: run `evidence/2026-10-10-wiredreads`

Plan published evidence, published; served as `GLM-5.3-Flash-MLX-4bit`.

### ruler-repeat

| streams | prose total (a stream) | code total (a stream) | structured total (a stream) | list total (a stream) | first token |
|---:|---:|---:|---:|---:|---:|
| 1 | 92.4 (92.4) | 103.6 (103.6) | 97.0 (97.0) | 94.9 (94.9) | 0.11-0.15 s |

### ruler

| streams | prose total (a stream) | code total (a stream) | structured total (a stream) | list total (a stream) | first token |
|---:|---:|---:|---:|---:|---:|
| 1 | 90.7 (90.7) | 103.7 (103.7) | 99.1 (99.1) | 41.8 (41.8) | 0.12-0.15 s |

### suite

| check | passed |
|---|---:|
| snapshot | 12/12 |
| drafts | 12/12 |
| concurrent | 12/12 |

## 2026-10-10 00:00: run `evidence/2026-10-10-thinking-on`

Plan published evidence, published; served as `GLM-5.3-Flash-MLX-4bit`.

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
| max-tokens | 0/3 |
| tools | 58/60 |
| json | 30/30 |
| ifeval | 127/150 |
| gsm8k | 248/250 |
| mgsm | 221/240 |
| mmlu | 307/342 |
| repetition | 8/8 |
| long-context | 54/55 |
| vision | 12/12 |
| snapshot | 12/12 |

## 2026-10-10 00:00: run `evidence/2026-10-10-1.0.5-thinking`

Plan published evidence, published; served as `GLM-5.3-Flash-MLX-4bit`.

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
| max-tokens | 0/3 |
| tools | 57/60 |
| json | 30/30 |
| ifeval | 131/150 |
| gsm8k | 248/250 |
| mgsm | 226/240 |
| mmlu | 308/342 |
| repetition | 8/8 |
| long-context | 54/55 |
| vision | 12/12 |
| snapshot | 12/12 |

## 2026-10-10 00:00: run `evidence/2026-10-10-1.0.5`

Plan published evidence, published; served as `GLM-5.3-Flash-MLX-4bit`.

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
| ifeval | 96/150 |
| gsm8k | 246/250 |
| mgsm | 217/240 |
| mmlu | 292/342 |
| repetition | 8/8 |
| long-context | 55/55 |
| vision | 12/12 |
| snapshot | 12/12 |

## 2026-10-09 00:00: run `evidence/2026-10-09-ruler-1.0.4`

Plan published evidence, published; served as `GLM-5.3-Flash-MLX-4bit`.

### ruler

| streams | prose total (a stream) | code total (a stream) | structured total (a stream) | list total (a stream) | first token |
|---:|---:|---:|---:|---:|---:|
| 1 | 93.3 (93.3) | 104.6 (104.6) | 104.2 (104.2) | 89.7 (89.7) | 0.23-0.29 s |

## 2026-10-09 00:00: run `evidence/2026-10-09-quality-1.0.4-part3`

Plan published evidence, published; served as `GLM-5.3-Flash-MLX-4bit`.

### suite

| check | passed |
|---|---:|
| mmlu | 288/342 |
| repetition | 8/8 |
| long-context | 29/29 |
| vision | 12/12 |
| snapshot | 12/12 |

## 2026-10-09 00:00: run `evidence/2026-10-09-quality-1.0.4-long128`

Plan published evidence, published; served as `GLM-5.3-Flash-MLX-4bit`.

### suite

| check | passed |
|---|---:|
| long-context | 42/42 |

