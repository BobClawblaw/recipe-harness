# GLM-5.3-Flash EXL3 4bpw on 2x NVIDIA DGX Spark (GB10, 128 GB unified each), TP=2 over RoCE

Target `glm53-exl3-gb10-port`: GLM-5.3-Flash EXL3 4bpw, main's families/glm with PR 855's port, TP=2 on two DGX Sparks. Engine: TensorFold native, CUDA: families/glm on 1.0.12 (PR 855's port). Rendered from `stats/glm53-exl3-gb10-port.json` (4 runs); aggregate tok/s, total (a stream).

## 2026-10-16 21:38: run `20261016-213802-glm-streams`

Plan glm-streams, done; served as `GLM-5.3-Flash-EXL3`.

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

