# GLM-5.3-Flash EXL3 4bpw on 2x NVIDIA DGX Spark (GB10, 128 GB unified each), TP=2 over RoCE

Target `glm53-exl3-gb10-port`: GLM-5.3-Flash EXL3 4bpw, main's families/glm with PR 855's port, TP=2 on two DGX Sparks. Engine: TensorFold native, CUDA: families/glm on 1.0.12 (PR 855's port). Rendered from `stats/glm53-exl3-gb10-port.json` (3 runs); aggregate tok/s, total (a stream).

## 2026-10-16 21:24: run `20261016-212421-glm-vision`

Plan glm-vision, done; served as `GLM-5.3-Flash-EXL3`.

Serving: binary `2b666cc74334abec`

### suite-vision

| check | passed |
|---|---:|
| vision | 6/6 |
| vision-concurrent | 16/16 |

## 2026-10-16 21:03: run `20261016-210300-glm-vision`

Plan glm-vision, done; served as `GLM-5.3-Flash-EXL3`.

Serving: binary `2b666cc74334abec`

### suite-vision

| check | passed |
|---|---:|
| vision | 4/6 |
| vision-concurrent | 0/0 |

## 2026-10-16 18:10: run `20261016-181039-glm-quality`

Plan glm-quality, done; served as `GLM-5.3-Flash-EXL3`.

Serving: binary `8c2034ce295aaf9c`

### ruler-fresh

| streams | prose total (a stream) | code total (a stream) | structured total (a stream) | list total (a stream) | first token |
|---:|---:|---:|---:|---:|---:|
| 1 | 27.8 (27.8) | 38.2 (38.2) | 33.2 (33.2) | 30.6 (30.6) | 0.18-0.24 s |

### checks

| check | result |
|---|---|
| memory-idle | measured: head 22.6 GiB available |
| thinking | pass: thinking on: 10/10 right, 10/10 with reasoning_content, 0 leaks, 0 errors |

