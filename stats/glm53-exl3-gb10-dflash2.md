# GLM-5.3-Flash EXL3 4bpw on 2x NVIDIA DGX Spark (GB10, 128 GB unified each), TP=2 over RoCE

Target `glm53-exl3-gb10-dflash2`: GLM-5.3-Flash EXL3 4bpw, families/glm with DFlash2 drafts (--drafter, 4-bit), TP=2 on two DGX Sparks. Engine: TensorFold native, CUDA: families/glm + DFlash2 (incoai/GLM-5.3-Flash-DFlash2, opt-in). Rendered from `stats/glm53-exl3-gb10-dflash2.json` (1 runs); aggregate tok/s, total (a stream).

## 2026-10-17 00:32: run `20261017-003221-glm-streams8`

Plan glm-streams8, done; served as `GLM-5.3-Flash-EXL3`.

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

