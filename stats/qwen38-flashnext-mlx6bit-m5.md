# Qwen3.8-Flash-Next, MLX 6-bit on 1x Apple M5 Ultra (256 GB unified), macOS

Target `qwen38-flashnext-mlx6bit-m5`: Qwen3.8-Flash-Next MLX 6-bit, TensorFold native on one M5 Ultra. Engine: TensorFold native, Metal. Rendered from `stats/qwen38-flashnext-mlx6bit-m5.json` (6 runs); aggregate tok/s, total (a stream).

## 2026-10-11 00:00: run `evidence/2026-10-11-suite-rest`

Plan published evidence, published; served as `Qwen3.8-Flash-Next-MLX-6bit`.

### suite

| check | passed |
|---|---:|
| ifeval | 134/150 |
| gsm8k | 242/250 |
| mgsm | 225/240 |
| mmlu | 282/342 |
| repetition | 8/8 |
| long-context | 55/55 |
| concurrent | 12/12 |
| snapshot | 12/12 |

## 2026-10-11 00:00: run `evidence/2026-10-11-pr606-parallel`

Plan published evidence, published; served as `Qwen3.8-Flash-Next-MLX-6bit`.

### ruler-parallel1

| streams | prose total (a stream) | code total (a stream) | structured total (a stream) | list total (a stream) | first token |
|---:|---:|---:|---:|---:|---:|
| 1 | 144.6 (144.6) | 205.9 (205.9) | 172.3 (172.3) | 194.4 (194.4) | 0.09-0.16 s |
| 4 | 566.1 (142.0) | 815.7 (205.8) | 672.6 (169.3) | 854.3 (213.4) | 1.63-3.07 s |

### ruler-parallel4-256k

| streams | prose total (a stream) | code total (a stream) | structured total (a stream) | list total (a stream) | first token |
|---:|---:|---:|---:|---:|---:|
| 1 | 129.6 (129.6) | 177.3 (177.3) | 150.2 (150.2) | 180.0 (180.0) | 0.18-0.23 s |
| 4 | 212.1 (51.9) | 313.2 (76.9) | 247.9 (60.9) | 306.5 (76.5) | 0.38-0.41 s |

### ruler-parallel4

| streams | prose total (a stream) | code total (a stream) | structured total (a stream) | list total (a stream) | first token |
|---:|---:|---:|---:|---:|---:|
| 1 | 131.0 (131.0) | 180.0 (180.0) | 152.7 (152.7) | 183.3 (183.3) | 0.12-0.18 s |
| 4 | 213.8 (52.8) | 321.8 (80.7) | 254.2 (64.4) | 314.8 (78.6) | 0.33-0.36 s |

### suite-concurrent

| check | passed |
|---|---:|
| concurrent | 12/12 |
| drafts | 12/12 |

### suite-concurrent-256k

| check | passed |
|---|---:|
| concurrent | 12/12 |
| drafts | 12/12 |

## 2026-10-11 00:00: run `evidence/2026-10-11-humaneval`

Plan published evidence, published; served as `Qwen3.8-Flash-Next-MLX-6bit`.

### suite

| check | passed |
|---|---:|
| humaneval | 157/164 |

## 2026-10-11 00:00: run `evidence/2026-10-11-fz-kernels`

Plan published evidence, published; served as `Qwen3.8-Flash-Next-MLX-6bit`.

### ruler-1user-fz

| streams | prose total (a stream) | code total (a stream) | structured total (a stream) | list total (a stream) | first token |
|---:|---:|---:|---:|---:|---:|
| 1 | 137.7 (137.7) | 199.8 (199.8) | 165.2 (165.2) | 187.3 (187.3) | 0.10-0.18 s |

## 2026-10-11 00:00: run `evidence/2026-10-11-first-suite`

Plan published evidence, published; served as `Qwen3.8-Flash-Next-MLX-6bit`.

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

## 2026-10-11 00:00: run `evidence/2026-10-11-first-ruler`

Plan published evidence, published; served as `Qwen3.8-Flash-Next-MLX-6bit`.

### ruler-1user

| streams | prose total (a stream) | code total (a stream) | structured total (a stream) | list total (a stream) | first token |
|---:|---:|---:|---:|---:|---:|
| 1 | 144.5 (144.5) | 206.2 (206.2) | 172.3 (172.3) | 194.3 (194.3) | 0.10-0.20 s |

