# GLM-5.3-Flash EXL3 4bpw on 2x NVIDIA DGX Spark (GB10, 128 GB unified each), TP=2 over RoCE

Target `glm53-exl3-gb10-port16`: GLM-5.3-Flash EXL3 4bpw, families/glm with 4096-row index rings, --parallel 16, TP=2 on two DGX Sparks. Engine: TensorFold native, CUDA: families/glm + index rings (16 streams at 40960). Rendered from `stats/glm53-exl3-gb10-port16.json` (1 runs); aggregate tok/s, total (a stream).

## 2026-10-17 05:56: run `20261017-055626-glm-streams`

Plan glm-streams, done; served as `GLM-5.3-Flash-EXL3`.

Serving: binary `44e0c91b7c5589f4`

### ruler-streams

| streams | prose total (a stream) | code total (a stream) | structured total (a stream) | list total (a stream) | first token |
|---:|---:|---:|---:|---:|---:|
| 1 | 28.3 (28.3) | 39.0 (39.0) | 34.0 (34.0) | 31.3 (31.3) | 0.18-0.23 s |
| 4 | 52.5 (13.1) | 67.8 (16.8) | 66.6 (16.5) | 67.2 (16.8) | 0.65-0.79 s |
| 8 | 66.6 (8.4) | 87.0 (10.9) | 83.9 (10.6) | 85.2 (10.5) | 1.39-1.65 s |
| 16 | 68.3 (4.2) | 90.8 (5.6) | 88.3 (5.4) | 89.3 (5.5) | 3.20-3.67 s |

### suite-together

| check | passed |
|---|---:|
| concurrent | 12/12 |
| drafts | 12/12 |

