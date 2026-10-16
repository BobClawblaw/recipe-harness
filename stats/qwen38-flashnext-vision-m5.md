# Qwen3.8-Flash-Next, 6-bit with vision on 1x Apple M5 Ultra (256 GB unified), macOS

Target `qwen38-flashnext-vision-m5`: Qwen3.8-Flash-Next 6-bit with image input, TensorFold native on one M5 Ultra. Engine: TensorFold native, Metal. Rendered from `stats/qwen38-flashnext-vision-m5.json` (5 runs); aggregate tok/s, total (a stream).

## 2026-10-12 00:00: run `evidence/2026-10-12-parallel8`

Plan published evidence, published; served as `Qwen3.8-Flash-Next-6bit`.

### ruler

| streams | prose total (a stream) | code total (a stream) | structured total (a stream) | list total (a stream) | first token |
|---:|---:|---:|---:|---:|---:|
| 1 | 127.7 (127.7) | 174.1 (174.1) | 147.8 (147.8) | 175.4 (175.4) | 0.16-0.17 s |
| 4 | 210.2 (52.9) | 303.3 (76.3) | 249.2 (61.1) | 316.9 (77.8) | 0.37-0.40 s |
| 8 | 271.5 (34.1) | 330.0 (40.8) | 292.5 (36.5) | 339.3 (41.7) | 0.76-0.84 s |

## 2026-10-12 00:00: run `evidence/2026-10-12-lane-parity`

Plan published evidence, published; served as `Qwen3.8-Flash-Next-6bit`.

### ruler_trial

| streams | prose total (a stream) | code total (a stream) | structured total (a stream) | list total (a stream) | first token |
|---:|---:|---:|---:|---:|---:|
| 1 | 141.6 (141.6) | 202.7 (202.7) | 169.1 (169.1) | 191.5 (191.5) | 0.12-0.20 s |
| 4 | 244.7 (60.9) | 325.4 (80.9) | 277.4 (68.6) | 327.2 (83.3) | 0.41-0.44 s |

## 2026-10-12 00:00: run `evidence/2026-10-12-262k-cache`

Plan published evidence, published; served as `Qwen3.8-Flash-Next-6bit`.

### ruler

| streams | prose total (a stream) | code total (a stream) | structured total (a stream) | list total (a stream) | first token |
|---:|---:|---:|---:|---:|---:|
| 1 | 129.3 (129.3) | 176.6 (176.6) | 149.8 (149.8) | 177.4 (177.4) | 0.19-0.20 s |
| 4 | 209.5 (52.6) | 309.6 (78.3) | 245.9 (60.7) | 321.5 (78.4) | 0.39-0.41 s |

## 2026-10-11 00:00: run `evidence/2026-10-11-launchd`

Plan published evidence, published; served as `Qwen3.8-Flash-Next-6bit`.

### ruler-1user

| streams | prose total (a stream) | code total (a stream) | structured total (a stream) | list total (a stream) | first token |
|---:|---:|---:|---:|---:|---:|
| 1 | 144.6 (144.6) | 205.6 (205.6) | 172.6 (172.6) | 194.7 (194.7) | 0.10-0.20 s |

### suite

| check | passed |
|---|---:|
| drafts | 12/12 |
| streaming | 4/4 |
| multiturn | 8/8 |
| stop | 3/3 |
| thinking | 10/10 |
| copy | 2/2 |
| max-tokens | 3/3 |
| tools | 59/60 |
| json | 30/30 |

## 2026-10-11 00:00: run `evidence/2026-10-11-1m-parallel4`

Plan published evidence, published; served as `Qwen3.8-Flash-Next-6bit`.

### ruler

| streams | prose total (a stream) | code total (a stream) | structured total (a stream) | list total (a stream) | first token |
|---:|---:|---:|---:|---:|---:|
| 1 | 131.3 (131.3) | 178.9 (178.9) | 160.2 (160.2) | 183.9 (183.9) | 0.12-0.16 s |
| 4 | 211.0 (52.0) | 311.5 (77.0) | 259.8 (64.7) | 317.6 (78.8) | 0.36-0.42 s |

### suite

| check | passed |
|---|---:|
| drafts | 12/12 |
| streaming | 4/4 |
| multiturn | 8/8 |
| stop | 3/3 |
| thinking | 10/10 |
| copy | 2/2 |
| max-tokens | 3/3 |
| tools | 56/60 |
| json | 30/30 |
| ifeval | 132/150 |
| gsm8k | 241/250 |
| concurrent | 12/12 |

