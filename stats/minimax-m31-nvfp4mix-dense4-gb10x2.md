# MiniMax-M3.1-Flash, NVFP4 (15 MoE layers) + 3-bit refit, dense NVFP4, MXFP8 head, 32k context on 2x NVIDIA DGX Spark (GB10, 128 GB unified each), TP=2 over RoCE

Target `minimax-m31-nvfp4mix-dense4-gb10x2`: MiniMax-M3.1-Flash, NVFP4 x 15 layers + 3-bit, dense NVFP4 + MXFP8 head, DSpark drafts, 32k x 2 streams, TensorFold native CUDA, TP=2 on two DGX Sparks. Engine: TensorFold native, CUDA. Rendered from `stats/minimax-m31-nvfp4mix-dense4-gb10x2.json` (10 runs); aggregate tok/s, total (a stream).

## 2026-10-26 21:50: run `20261026-215020-minimax-thinking`

Plan minimax-thinking, done; served as `MiniMax-M3.1-Flash`.

Serving: engine_commit `1d559dd44; 9`; binary_sha256 `09ac4a25886400303603ffa9221dc29816f77b4821d9a612605d67f242b5ae07`; checkpoint_mix `[20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 31, 49, 52, 57, 59] ['qkv', 'o', 'mlp']`; checkpoint_sha256 `b21fdee27b56408db9f77bb2dc22b93224960d419106db758007d00e9cf43711`; server_args `TF_MINIMAX_RANK=0 TF_MINIMAX_WORLD=2 NCCL_SOCKET_IFNAME=enp1s0f1np1 NCCL_IB_HCA=rocep1s0f1`; suite_commit `a7ba7e392d57`

### suite-thinking

| check | passed |
|---|---:|
| gsm8k | 242/250 |

### checks

| check | result |
|---|---|
| thinking | pass: thinking on: 10/10 right, 10/10 with reasoning_content, 0 leaks, 0 errors, 0 cut at 29696 tokens |

## 2026-10-26 21:32: run `20261026-213259-minimax-thinking`

Plan minimax-thinking, done; served as `MiniMax-M3.1-Flash`.

Serving: engine_commit `1d559dd44; 9`; binary_sha256 `09ac4a25886400303603ffa9221dc29816f77b4821d9a612605d67f242b5ae07`; checkpoint_mix `[20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 31, 49, 52, 57, 59] ['qkv', 'o', 'mlp']`; checkpoint_sha256 `b21fdee27b56408db9f77bb2dc22b93224960d419106db758007d00e9cf43711`; server_args `TF_MINIMAX_RANK=0 TF_MINIMAX_WORLD=2 NCCL_SOCKET_IFNAME=enp1s0f1np1 NCCL_IB_HCA=rocep1s0f1`; suite_commit `277c842a1481`

### suite-thinking

| check | passed |
|---|---:|
| gsm8k | 240/250 |

### checks

| check | result |
|---|---|
| thinking | pass: thinking on: 10/10 right, 10/10 with reasoning_content, 0 leaks, 0 errors, 0 cut at 29696 tokens |

## 2026-10-26 21:31: run `20261026-213139-minimax-thinking`

Plan minimax-thinking, done; served as `MiniMax-M3.1-Flash`.

Serving: engine_commit `1d559dd44; 9`; binary_sha256 `09ac4a25886400303603ffa9221dc29816f77b4821d9a612605d67f242b5ae07`; checkpoint_mix `[20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 31, 49, 52, 57, 59] ['qkv', 'o', 'mlp']`; checkpoint_sha256 `b21fdee27b56408db9f77bb2dc22b93224960d419106db758007d00e9cf43711`; server_args `TF_MINIMAX_RANK=0 TF_MINIMAX_WORLD=2 NCCL_SOCKET_IFNAME=enp1s0f1np1 NCCL_IB_HCA=rocep1s0f1`; suite_commit `277c842a1481`

### checks

| check | result |
|---|---|
| thinking | pass: thinking on: 10/10 right, 10/10 with reasoning_content, 0 leaks, 0 errors, 0 cut at 29696 tokens |

## 2026-10-26 20:00: run `20261026-200035-minimax-quality-off`

Plan minimax-quality-off, done; served as `MiniMax-M3.1-Flash`.

Serving: engine_commit `1d559dd44; 8`; binary_sha256 `09ac4a25886400303603ffa9221dc29816f77b4821d9a612605d67f242b5ae07`; checkpoint_mix `[20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 31, 49, 52, 57, 59] ['qkv', 'o', 'mlp']`; checkpoint_sha256 `b21fdee27b56408db9f77bb2dc22b93224960d419106db758007d00e9cf43711`; server_args `TF_MINIMAX_RANK=0 TF_MINIMAX_WORLD=2 NCCL_SOCKET_IFNAME=enp1s0f1np1 NCCL_IB_HCA=rocep1s0f1`; suite_commit `277c842a1481`

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
| tools | 57/60 |
| json | 30/30 |
| ifeval | 93/150 |
| gsm8k | 242/250 |
| mgsm | 196/240 |
| mmlu | 280/342 |

### checks

| check | result |
|---|---|
| memory-idle | measured: head 10.1 GiB available; worker 9.7 GiB available |

## 2026-10-26 19:27: run `20261026-192739-quick`

Plan quick, done; served as `MiniMax-M3.1-Flash`.

Serving: engine_commit `1d559dd44; 8`; binary_sha256 `09ac4a25886400303603ffa9221dc29816f77b4821d9a612605d67f242b5ae07`; checkpoint_mix `[20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 31, 49, 52, 57, 59] ['qkv', 'o', 'mlp']`; checkpoint_sha256 `b21fdee27b56408db9f77bb2dc22b93224960d419106db758007d00e9cf43711`; server_args `TF_MINIMAX_RANK=0 TF_MINIMAX_WORLD=2 NCCL_SOCKET_IFNAME=enp1s0f1np1 NCCL_IB_HCA=rocep1s0f1`; suite_commit `277c842a1481`

### ruler-fresh

| streams | prose total (a stream) | code total (a stream) | structured total (a stream) | list total (a stream) | first token |
|---:|---:|---:|---:|---:|---:|
| 1 | 26.9 (26.9) | 44.7 (44.7) | 32.7 (32.7) | 36.8 (36.8) | 0.47-0.50 s |

Engine rounds (ruler-fresh):

| streams | tokens a round | drafts a round | accepted | ms a round | requests |
|---:|---:|---:|---:|---:|---:|
| 1 | 2.462 | 2.758 | 53% | 69.74 | 12 |

### ruler-after

| streams | prose total (a stream) | code total (a stream) | structured total (a stream) | list total (a stream) | first token |
|---:|---:|---:|---:|---:|---:|
| 1 | 27.0 (27.0) | 45.8 (45.8) | 33.0 (33.0) | 36.4 (36.4) | 0.47-0.50 s |

Engine rounds (ruler-after):

| streams | tokens a round | drafts a round | accepted | ms a round | requests |
|---:|---:|---:|---:|---:|---:|
| 1 | 2.569 | 3.068 | 51% | 72.25 | 13 |

### suite

| check | passed |
|---|---:|
| soak | 60/60 |
| drafts | 12/12 |
| concurrent | 12/12 |
| streaming | 4/4 |
| multiturn | 8/8 |
| stop | 3/3 |
| thinking | 10/10 |
| copy | 2/2 |
| max-tokens | 3/3 |

### checks

| check | result |
|---|---|
| memory-idle | measured: head 11.5 GiB available; worker 10.3 GiB available |
| structured | pass: 18/18 obey, drafted == plain 12/12; a bad regex -> 400 |
| tools | pass: 5/5 tool cases right |
| sampling | pass: 9/9 seeded replies equal on repeat and undrafted; 0 errors |
| turns | pass: resumed == again: True; cold (after a restart): True; cached 4096 of 4826; ttft resumed 0.977s, cold 4.918s |
| urls | FAIL: public 400; loopback 400; http 400; unexpected: ['public'] |

## 2026-10-26 19:10: run `20261026-191004-speed3`

Plan speed3, done; served as `MiniMax-M3.1-Flash`.

Serving: engine_commit `1d559dd44; 8`; binary_sha256 `09ac4a25886400303603ffa9221dc29816f77b4821d9a612605d67f242b5ae07`; checkpoint_mix `[20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 31, 49, 52, 57, 59] ['qkv', 'o', 'mlp']`; checkpoint_sha256 `b21fdee27b56408db9f77bb2dc22b93224960d419106db758007d00e9cf43711`; server_args `TF_MINIMAX_RANK=0 TF_MINIMAX_WORLD=2 NCCL_SOCKET_IFNAME=enp1s0f1np1 NCCL_IB_HCA=rocep1s0f1`; suite_commit `277c842a1481`

### ruler-fresh

| streams | prose total (a stream) | code total (a stream) | structured total (a stream) | list total (a stream) | first token |
|---:|---:|---:|---:|---:|---:|
| 1 | 27.0 (27.0) | 45.2 (45.2) | 32.7 (32.7) | 36.5 (36.5) | 0.47-0.50 s |
| 2 | 36.5 (18.3) | 57.6 (28.8) | 41.6 (20.8) | 65.0 (32.5) | 0.81-0.85 s |
| 3 | 42.5 (14.1) | 61.5 (20.7) | 46.4 (15.8) | 75.0 (25.8) | 1.14-1.20 s |

Engine rounds (ruler-fresh):

| streams | tokens a round | drafts a round | accepted | ms a round | requests |
|---:|---:|---:|---:|---:|---:|
| 1 | 2.49 | 2.857 | 52% | 70.46 | 12 |
| 2 | 2.205 | 1.907 | 63% | 87.88 | 25 |
| 3 | 2.36 | 2.304 | 59% | 123.6 | 37 |

### ruler-after

| streams | prose total (a stream) | code total (a stream) | structured total (a stream) | list total (a stream) | first token |
|---:|---:|---:|---:|---:|---:|
| 1 | 27.4 (27.4) | 46.1 (46.1) | 33.1 (33.1) | 36.5 (36.5) | 0.47-0.50 s |

Engine rounds (ruler-after):

| streams | tokens a round | drafts a round | accepted | ms a round | requests |
|---:|---:|---:|---:|---:|---:|
| 1 | 2.61 | 3.132 | 51% | 72.96 | 13 |

### checks

| check | result |
|---|---|
| memory-idle | measured: head 11.3 GiB available; worker 10.6 GiB available |
| turns | pass: resumed == again: True; cold (after a restart): True; cached 4096 of 4826; ttft resumed 0.965s, cold 4.909s |
| memory-busy | measured: head 11.1 GiB available; worker 10.7 GiB available |

## 2026-10-26 17:41: run `20261026-174151-quick`

Plan quick, done; served as `MiniMax-M3.1-Flash`.

Serving: engine_commit `1d559dd44; 8`; binary_sha256 `fe6ddb669b5761e8988cb859fa09f6c0653a257cfb08fe878e099920326f5857`; checkpoint_mix `[20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 31, 49, 52, 57, 59] decoder projections NVFP4 (e2`; checkpoint_sha256 `c64e38460ff741f77c22877c3c184e20d923cad938c32534695be37e92c8a02e`; server_args `TF_MINIMAX_RANK=0 TF_MINIMAX_WORLD=2 NCCL_SOCKET_IFNAME=enp1s0f1np1 NCCL_IB_HCA=rocep1s0f1`; suite_commit `277c842a1481`

### ruler-fresh

| streams | prose total (a stream) | code total (a stream) | structured total (a stream) | list total (a stream) | first token |
|---:|---:|---:|---:|---:|---:|
| 1 | 27.2 (27.2) | 45.6 (45.6) | 32.4 (32.4) | 36.8 (36.8) | 0.47-0.50 s |

Engine rounds (ruler-fresh):

| streams | tokens a round | drafts a round | accepted | ms a round | requests |
|---:|---:|---:|---:|---:|---:|
| 1 | 2.486 | 2.807 | 52% | 70.0 | 12 |

### ruler-after

| streams | prose total (a stream) | code total (a stream) | structured total (a stream) | list total (a stream) | first token |
|---:|---:|---:|---:|---:|---:|
| 1 | 26.9 (26.9) | 46.5 (46.5) | 32.3 (32.3) | 36.6 (36.6) | 0.47-0.50 s |

Engine rounds (ruler-after):

| streams | tokens a round | drafts a round | accepted | ms a round | requests |
|---:|---:|---:|---:|---:|---:|
| 1 | 2.581 | 3.115 | 50% | 72.57 | 13 |

### suite

| check | passed |
|---|---:|
| soak | 60/60 |
| drafts | 12/12 |
| concurrent | 12/12 |
| streaming | 4/4 |
| multiturn | 8/8 |
| stop | 3/3 |
| thinking | 10/10 |
| copy | 2/2 |
| max-tokens | 3/3 |

### checks

| check | result |
|---|---|
| memory-idle | measured: head 11.5 GiB available; worker 10.3 GiB available |
| structured | pass: 18/18 obey, drafted == plain 12/12; a bad regex -> 400 |
| tools | pass: 5/5 tool cases right |
| sampling | pass: 9/9 seeded replies equal on repeat and undrafted; 0 errors |
| turns | pass: resumed == again: True; cold (after a restart): True; cached 4096 of 4826; ttft resumed 0.966s, cold 4.916s |
| urls | FAIL: public 400; loopback 400; http 400; unexpected: ['public'] |

## 2026-10-26 17:27: run `20261026-172719-speed`

Plan speed, done; served as `MiniMax-M3.1-Flash`.

Serving: engine_commit `1d559dd44; 8`; binary_sha256 `fe6ddb669b5761e8988cb859fa09f6c0653a257cfb08fe878e099920326f5857`; checkpoint_mix `[20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 31, 49, 52, 57, 59] decoder projections NVFP4 (e2`; checkpoint_sha256 `c64e38460ff741f77c22877c3c184e20d923cad938c32534695be37e92c8a02e`; server_args `TF_MINIMAX_RANK=0 TF_MINIMAX_WORLD=2 NCCL_SOCKET_IFNAME=enp1s0f1np1 NCCL_IB_HCA=rocep1s0f1`; suite_commit `277c842a1481`

### ruler-fresh

| streams | prose total (a stream) | code total (a stream) | structured total (a stream) | list total (a stream) | first token |
|---:|---:|---:|---:|---:|---:|
| 1 | 27.0 (27.0) | 45.8 (45.8) | 32.8 (32.8) | 36.7 (36.7) | 0.47-0.50 s |
| 2 | 35.7 (17.8) | 55.3 (27.7) | 39.7 (19.8) | 62.0 (31.0) | 0.80-0.85 s |

Engine rounds (ruler-fresh):

| streams | tokens a round | drafts a round | accepted | ms a round | requests |
|---:|---:|---:|---:|---:|---:|
| 1 | 2.445 | 2.679 | 54% | 68.74 | 12 |
| 2 | 2.355 | 2.151 | 63% | 97.78 | 25 |

### ruler-after

| streams | prose total (a stream) | code total (a stream) | structured total (a stream) | list total (a stream) | first token |
|---:|---:|---:|---:|---:|---:|
| 1 | 27.3 (27.3) | 45.4 (45.4) | 32.7 (32.7) | 36.7 (36.7) | 0.47-0.50 s |

Engine rounds (ruler-after):

| streams | tokens a round | drafts a round | accepted | ms a round | requests |
|---:|---:|---:|---:|---:|---:|
| 1 | 2.591 | 3.13 | 50% | 72.93 | 13 |

### checks

| check | result |
|---|---|
| memory-idle | measured: head 11.6 GiB available; worker 10.2 GiB available |
| turns | pass: resumed == again: True; cold (after a restart): True; cached 4096 of 4826; ttft resumed 0.968s, cold 4.901s |
| memory-busy | measured: head 11.1 GiB available; worker 10.7 GiB available |

## 2026-10-26 13:39: run `20261026-133903-quick`

Plan quick, done; served as `MiniMax-M3.1-Flash`.

Serving: engine_commit `1d559dd44; 5`; binary_sha256 `bafbdcc852a5a0c5d6eeed3a73da0762941e9eab95202b840acdb2dbf82451df`; checkpoint_mix `[20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 31, 49, 52, 57, 59]`; server_args `TF_MINIMAX_RANK=0 TF_MINIMAX_WORLD=2 NCCL_SOCKET_IFNAME=enp1s0f1np1 NCCL_IB_HCA=rocep1s0f1`; suite_commit `277c842a1481`

### ruler-fresh

| streams | prose total (a stream) | code total (a stream) | structured total (a stream) | list total (a stream) | first token |
|---:|---:|---:|---:|---:|---:|
| 1 | 27.9 (27.9) | 43.3 (43.3) | 29.8 (29.8) | 37.1 (37.1) | 0.47-0.50 s |

Engine rounds (ruler-fresh):

| streams | tokens a round | drafts a round | accepted | ms a round | requests |
|---:|---:|---:|---:|---:|---:|
| 1 | 2.428 | 2.843 | 50% | 70.28 | 12 |

### ruler-after

| streams | prose total (a stream) | code total (a stream) | structured total (a stream) | list total (a stream) | first token |
|---:|---:|---:|---:|---:|---:|
| 1 | 27.9 (27.9) | 42.2 (42.2) | 29.2 (29.2) | 36.8 (36.8) | 0.47-0.50 s |

Engine rounds (ruler-after):

| streams | tokens a round | drafts a round | accepted | ms a round | requests |
|---:|---:|---:|---:|---:|---:|
| 1 | 2.524 | 3.179 | 48% | 74.13 | 13 |

### suite

| check | passed |
|---|---:|
| soak | 60/60 |
| drafts | 12/12 |
| concurrent | 12/12 |
| streaming | 4/4 |
| multiturn | 8/8 |
| stop | 3/3 |
| thinking | 10/10 |
| copy | 2/2 |
| max-tokens | 3/3 |

### checks

| check | result |
|---|---|
| memory-idle | measured: head 11.3 GiB available; worker 10.2 GiB available |
| structured | pass: 18/18 obey, drafted == plain 12/12; a bad regex -> 400 |
| tools | pass: 5/5 tool cases right |
| sampling | pass: 9/9 seeded replies equal on repeat and undrafted; 0 errors |
| turns | pass: resumed == again: True; cold (after a restart): True; cached 4096 of 4826; ttft resumed 0.965s, cold 4.888s |
| urls | FAIL: public 400; loopback 400; http 400; unexpected: ['public'] |

## 2026-10-26 13:17: run `20261026-131729-speed`

Plan speed, done; served as `MiniMax-M3.1-Flash`.

Serving: engine_commit `1d559dd44; 5`; binary_sha256 `bafbdcc852a5a0c5d6eeed3a73da0762941e9eab95202b840acdb2dbf82451df`; checkpoint_mix `[20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 31, 49, 52, 57, 59]`; server_args `TF_MINIMAX_RANK=0 TF_MINIMAX_WORLD=2 NCCL_SOCKET_IFNAME=enp1s0f1np1 NCCL_IB_HCA=rocep1s0f1`; suite_commit `277c842a1481`

### ruler-fresh

| streams | prose total (a stream) | code total (a stream) | structured total (a stream) | list total (a stream) | first token |
|---:|---:|---:|---:|---:|---:|
| 1 | 27.7 (27.7) | 43.1 (43.1) | 29.7 (29.7) | 36.8 (36.8) | 0.47-0.50 s |
| 2 | 36.6 (18.3) | 53.5 (26.7) | 36.4 (18.2) | 62.5 (31.3) | 0.80-0.84 s |

Engine rounds (ruler-fresh):

| streams | tokens a round | drafts a round | accepted | ms a round | requests |
|---:|---:|---:|---:|---:|---:|
| 1 | 2.407 | 2.811 | 50% | 70.16 | 12 |
| 2 | 2.228 | 2.042 | 60% | 94.29 | 25 |

### ruler-after

| streams | prose total (a stream) | code total (a stream) | structured total (a stream) | list total (a stream) | first token |
|---:|---:|---:|---:|---:|---:|
| 1 | 28.0 (28.0) | 43.0 (43.0) | 29.3 (29.3) | 37.1 (37.1) | 0.47-0.50 s |

Engine rounds (ruler-after):

| streams | tokens a round | drafts a round | accepted | ms a round | requests |
|---:|---:|---:|---:|---:|---:|
| 1 | 2.528 | 3.184 | 48% | 73.59 | 13 |

### checks

| check | result |
|---|---|
| memory-idle | measured: head 11.3 GiB available; worker 10.1 GiB available |
| turns | pass: resumed == again: True; cold (after a restart): True; cached 4096 of 4826; ttft resumed 0.968s, cold 4.911s |
| memory-busy | measured: head 10.8 GiB available; worker 10.6 GiB available |

