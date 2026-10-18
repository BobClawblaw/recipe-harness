# GLM-5.3-Flash EXL3 4bpw on 2x NVIDIA DGX Spark (GB10, 128 GB unified each), TP=2 over RoCE

Target `glm53-exl3-gb10-many-mtp`: #1014 merged onto TensorFold main 76aafcf2, MTP head only (no --drafter), GLM-5.3-Flash EXL3 4bpw, TP=2. Engine: TensorFold native, CUDA: families/glm (many-mtp). Rendered from `stats/glm53-exl3-gb10-many-mtp.json` (1 runs); aggregate tok/s, total (a stream).

## 2026-10-18 14:04: run `20261018-140413-glm-qual1014`

Plan glm-qual1014, done; served as `GLM-5.3-Flash-EXL3`.

Serving: binary `07ab411ad6bef70e`

### ruler-c1-16

| streams | prose total (a stream) | code total (a stream) | structured total (a stream) | list total (a stream) | first token |
|---:|---:|---:|---:|---:|---:|
| 1 | 42.6 (42.3) | 52.8 (52.8) | 50.3 (50.1) | 49.0 (49.0) | 0.17-0.22 s |

### ruler-streams

| streams | prose total (a stream) | code total (a stream) | structured total (a stream) | list total (a stream) | first token |
|---:|---:|---:|---:|---:|---:|
| 8 | 74.7 (9.3) | 95.8 (11.9) | 102.3 (12.8) | 106.8 (13.3) | 0.82-1.02 s |
| 16 | 106.7 (6.7) | 118.6 (7.2) | 133.1 (8.3) | 138.6 (8.5) | 1.28-1.58 s |

### suite

| check | passed |
|---|---:|
| concurrent | 12/12 |
| drafts | 12/12 |

