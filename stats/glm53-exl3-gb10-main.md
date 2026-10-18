# GLM-5.3-Flash EXL3 4bpw on 2x NVIDIA DGX Spark (GB10, 128 GB unified each), TP=2 over RoCE

Target `glm53-exl3-gb10-main`: TensorFold main 76aafcf2 (with #855, #979, #984, #995 merged): GLM-5.3-Flash EXL3 4bpw, DFlash2, 16 streams, TP=2 on two DGX Sparks. Engine: TensorFold native, CUDA: families/glm (main). Rendered from `stats/glm53-exl3-gb10-main.json` (1 runs); aggregate tok/s, total (a stream).

## 2026-10-18 13:12: run `20261018-131205-glm-qual1014`

Plan glm-qual1014, done; served as `GLM-5.3-Flash-EXL3`.

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

