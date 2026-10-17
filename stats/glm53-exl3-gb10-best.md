# GLM-5.3-Flash EXL3 4bpw on 2x NVIDIA DGX Spark (GB10, 128 GB unified each), TP=2 over RoCE

Target `glm53-exl3-gb10-best`: GLM-5.3-Flash EXL3 4bpw, families/glm with 4-bit dense / 8-bit head, DFlash2 and 16 streams (PRs 855+979+984 and packing), TP=2 on two DGX Sparks. Engine: TensorFold native, CUDA: families/glm, packed linears (4/8), DFlash2, 16 streams. Rendered from `stats/glm53-exl3-gb10-best.json` (1 runs); aggregate tok/s, total (a stream).

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

