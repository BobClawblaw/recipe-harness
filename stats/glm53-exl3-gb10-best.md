# GLM-5.3-Flash EXL3 4bpw on 2x NVIDIA DGX Spark (GB10, 128 GB unified each), TP=2 over RoCE

Target `glm53-exl3-gb10-best`: GLM-5.3-Flash EXL3 4bpw, families/glm with 4-bit dense / 8-bit head, DFlash2 and 16 streams (PRs 855+979+984 and packing), TP=2 on two DGX Sparks. Engine: TensorFold native, CUDA: families/glm, packed linears (4/8, bf16 freed), DFlash2, 16 streams, prompts whole. Rendered from `stats/glm53-exl3-gb10-best.json` (3 runs); aggregate tok/s, total (a stream).

## 2026-10-17 14:38: run `20261017-143856-glm-streams`

Plan glm-streams, done; served as `GLM-5.3-Flash-EXL3`.

Serving: binary `cf50867102a60c38`

### ruler-streams

| streams | prose total (a stream) | code total (a stream) | structured total (a stream) | list total (a stream) | first token |
|---:|---:|---:|---:|---:|---:|
| 1 | 43.0 (43.0) | 68.7 (68.7) | 57.1 (57.1) | 48.6 (48.6) | 0.15-0.21 s |
| 4 | 71.9 (18.0) | 105.5 (26.3) | 95.7 (23.6) | 100.1 (25.1) | 0.47-0.62 s |
| 8 | 88.4 (11.0) | 115.3 (14.5) | 118.4 (14.1) | 114.2 (13.9) | 0.91-1.17 s |
| 16 | 109.9 (6.9) | 123.7 (7.5) | 125.6 (7.7) | 132.1 (8.2) | 1.77-2.24 s |

### suite-together

| check | passed |
|---|---:|
| concurrent | 12/12 |
| drafts | 12/12 |

## 2026-10-17 12:40: run `20261017-124058-glm-streams`

Plan glm-streams, done; served as `GLM-5.3-Flash-EXL3`.

Serving: binary `4365ec1e194e8409`

### ruler-streams

| streams | prose total (a stream) | code total (a stream) | structured total (a stream) | list total (a stream) | first token |
|---:|---:|---:|---:|---:|---:|
| 1 | 43.6 (43.6) | 69.4 (69.4) | 58.2 (58.2) | 49.2 (49.2) | 0.15-0.21 s |
| 4 | 75.2 (18.8) | 107.6 (26.7) | 96.9 (24.0) | 101.2 (25.4) | 0.54-0.71 s |
| 8 | 94.5 (11.9) | 129.9 (16.2) | 118.5 (14.9) | 123.7 (15.1) | 1.14-1.45 s |
| 16 | 110.2 (6.8) | 125.0 (7.6) | 139.5 (8.5) | 145.8 (9.1) | 2.55-3.17 s |

### suite-together

| check | passed |
|---|---:|
| concurrent | 12/12 |
| drafts | 12/12 |

## 2026-10-17 11:31: run `20261017-113151-glm-streams`

Plan glm-streams, done; served as `GLM-5.3-Flash-EXL3`.

Serving: binary `2a4bf00a83937d14`

### ruler-streams

| streams | prose total (a stream) | code total (a stream) | structured total (a stream) | list total (a stream) | first token |
|---:|---:|---:|---:|---:|---:|
| 1 | 43.8 (43.8) | 69.8 (69.8) | 58.3 (58.3) | 49.3 (49.3) | 0.15-0.21 s |
| 4 | 75.5 (18.9) | 108.3 (27.2) | 97.2 (24.0) | 101.8 (26.0) | 0.55-0.70 s |
| 8 | 94.8 (11.8) | 129.9 (16.3) | 119.2 (14.9) | 124.5 (15.4) | 1.13-1.45 s |
| 16 | 113.4 (7.1) | 136.4 (8.4) | 140.1 (8.6) | 146.8 (9.0) | 2.55-3.14 s |

### suite-together

| check | passed |
|---|---:|
| concurrent | 12/12 |
| drafts | 12/12 |

