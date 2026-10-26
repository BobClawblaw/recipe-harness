# MiniMax-M3.1-Flash, NVFP4 (15 MoE layers) + 3-bit refit, 32k context on 2x NVIDIA DGX Spark (GB10, 128 GB unified each), TP=2 over RoCE

Target `minimax-m31-nvfp4mix-gb10x2`: MiniMax-M3.1-Flash, NVFP4 x 15 layers + 3-bit, DSpark drafts, 32k x 2 streams, TensorFold native CUDA, TP=2 on two DGX Sparks. Engine: TensorFold native, CUDA. Rendered from `stats/minimax-m31-nvfp4mix-gb10x2.json` (5 runs); aggregate tok/s, total (a stream).

## 2026-10-26 10:51: run `20261026-105149-speed`

Plan speed, done; served as `MiniMax-M3.1-Flash`.

Serving: engine_commit `c1ace3229; 43`; binary_sha256 `a878eb001eda40208d92bcc1cbb95a9315671b948711833f60549afefd27d268`; checkpoint_mix `[20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 31, 49, 52, 57, 59]`; server_args `TF_MINIMAX_RANK=0 TF_MINIMAX_WORLD=2 NCCL_SOCKET_IFNAME=enp1s0f1np1 NCCL_IB_HCA=rocep1s0f1`; suite_commit `277c842a1481`

### ruler-fresh

| streams | prose total (a stream) | code total (a stream) | structured total (a stream) | list total (a stream) | first token |
|---:|---:|---:|---:|---:|---:|
| 1 | 23.0 (23.0) | 40.5 (40.5) | 24.8 (24.8) | 32.0 (32.0) | 0.47-0.51 s |
| 2 | 29.8 (14.9) | 49.3 (24.7) | 32.6 (16.3) | 53.9 (27.0) | 0.81-0.86 s |

Engine rounds (ruler-fresh):

| streams | tokens a round | drafts a round | accepted | ms a round | requests |
|---:|---:|---:|---:|---:|---:|
| 1 | 2.703 | 3.484 | 49% | 89.87 | 12 |
| 2 | 2.441 | 2.36 | 61% | 117.94 | 25 |

### ruler-after

| streams | prose total (a stream) | code total (a stream) | structured total (a stream) | list total (a stream) | first token |
|---:|---:|---:|---:|---:|---:|
| 1 | 22.5 (22.5) | 39.9 (39.9) | 25.1 (25.1) | 32.1 (32.1) | 0.47-0.50 s |

Engine rounds (ruler-after):

| streams | tokens a round | drafts a round | accepted | ms a round | requests |
|---:|---:|---:|---:|---:|---:|
| 1 | 2.718 | 3.704 | 46% | 90.87 | 13 |

### checks

| check | result |
|---|---|
| memory-idle | measured: head 8.2 GiB available; worker 7.5 GiB available |
| turns | pass: resumed == again: True; cold (after a restart): True; cached 4096 of 4826; ttft resumed 0.999s, cold 5.088s |
| memory-busy | measured: head 8.0 GiB available; worker 7.8 GiB available |

## 2026-10-26 06:04: run `20261026-060449-quick`

Plan quick, done; served as `MiniMax-M3.1-Flash`.

Serving: engine_commit `c1ace3229; 43`; binary_sha256 `a878eb001eda40208d92bcc1cbb95a9315671b948711833f60549afefd27d268`; checkpoint_mix `[20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 31, 49, 52, 57, 59]`; server_args `TF_MINIMAX_RANK=0 TF_MINIMAX_WORLD=2 NCCL_SOCKET_IFNAME=enp1s0f1np1 NCCL_IB_HCA=rocep1s0f1`; suite_commit `fatal: not a git repository (or any of the parent directories): .git`

### ruler-fresh

| streams | prose total (a stream) | code total (a stream) | structured total (a stream) | list total (a stream) | first token |
|---:|---:|---:|---:|---:|---:|
| 1 | 23.6 (23.6) | 41.1 (41.1) | 25.0 (25.0) | 32.6 (32.6) | 0.47-0.50 s |

Engine rounds (ruler-fresh):

| streams | tokens a round | drafts a round | accepted | ms a round | requests |
|---:|---:|---:|---:|---:|---:|
| 1 | 2.74 | 3.627 | 48% | 89.66 | 12 |

### ruler-after

| streams | prose total (a stream) | code total (a stream) | structured total (a stream) | list total (a stream) | first token |
|---:|---:|---:|---:|---:|---:|
| 1 | 22.5 (22.5) | 23.6 (23.6) | 24.8 (24.8) | 32.4 (32.4) | 0.47-0.60 s |

Engine rounds (ruler-after):

| streams | tokens a round | drafts a round | accepted | ms a round | requests |
|---:|---:|---:|---:|---:|---:|
| 1 | 2.737 | 3.595 | 48% | 106.1 | 14 |

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
| memory-idle | measured: head 8.6 GiB available; worker 7.5 GiB available |
| structured | pass: 18/18 obey, drafted == plain 12/12; a bad regex -> 400 |
| tools | pass: 5/5 tool cases right |
| sampling | pass: 9/9 seeded replies equal on repeat and undrafted; 0 errors |
| turns | pass: resumed == again: True; cold (after a restart): True; cached 4096 of 4826; ttft resumed 0.998s, cold 5.568s |
| urls | FAIL: public 400; loopback 400; http 400; unexpected: ['public'] |

## 2026-10-26 05:29: run `20261026-052920-speed`

Plan speed, done; served as `MiniMax-M3.1-Flash`.

Serving: engine_commit `c1ace3229; 42`; binary_sha256 `6ed0a104385c755482a082ce19272ba3a2bb3c5294ce06e1050223ff31f8d0a8`; checkpoint_mix `[20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 31, 49, 52, 57, 59]`; server_args `TF_MINIMAX_RANK=0 TF_MINIMAX_WORLD=2 NCCL_SOCKET_IFNAME=enp1s0f1np1 NCCL_IB_HCA=rocep1s0f1`; suite_commit `fatal: not a git repository (or any of the parent directories): .git`

### ruler-fresh

| streams | prose total (a stream) | code total (a stream) | structured total (a stream) | list total (a stream) | first token |
|---:|---:|---:|---:|---:|---:|
| 1 | 23.3 (23.3) | 39.9 (39.9) | 25.1 (25.1) | 32.3 (32.3) | 0.47-0.50 s |
| 2 | 29.8 (14.9) | 48.1 (24.0) | 32.0 (16.0) | 51.3 (25.6) | 0.83-0.88 s |

Engine rounds (ruler-fresh):

| streams | tokens a round | drafts a round | accepted | ms a round | requests |
|---:|---:|---:|---:|---:|---:|
| 1 | 2.672 | 3.338 | 50% | 88.66 | 12 |
| 2 | 2.46 | 2.426 | 60% | 122.07 | 25 |

### ruler-after

| streams | prose total (a stream) | code total (a stream) | structured total (a stream) | list total (a stream) | first token |
|---:|---:|---:|---:|---:|---:|
| 1 | 23.0 (23.0) | 39.7 (39.7) | 24.4 (24.4) | 32.3 (32.3) | 0.47-0.51 s |

Engine rounds (ruler-after):

| streams | tokens a round | drafts a round | accepted | ms a round | requests |
|---:|---:|---:|---:|---:|---:|
| 1 | 2.713 | 3.593 | 47% | 90.85 | 13 |

### checks

| check | result |
|---|---|
| memory-idle | measured: head 8.6 GiB available; worker 7.6 GiB available |
| turns | pass: resumed == again: True; cold (after a restart): True; cached 4096 of 4826; ttft resumed 0.991s, cold 5.134s |
| memory-busy | measured: head 8.2 GiB available; worker 7.8 GiB available |

## 2026-10-26 03:16: run `20261026-031654-quick`

Plan quick, done; served as `MiniMax-M3.1-Flash`.

Serving: engine_commit `c1ace3229; 42`; binary_sha256 `80854ab00a430f47236528857049ae49cd3b56d5e9257af3721358262eaf99e8`; checkpoint_mix `[20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 31, 49, 52, 57, 59]`; server_args `TF_MINIMAX_RANK=0 TF_MINIMAX_WORLD=2 NCCL_SOCKET_IFNAME=enp1s0f1np1 NCCL_IB_HCA=rocep1s0f1`; suite_commit `fatal: not a git repository (or any of the parent directories): .git`

### ruler-fresh

| streams | prose total (a stream) | code total (a stream) | structured total (a stream) | list total (a stream) | first token |
|---:|---:|---:|---:|---:|---:|
| 1 | 22.0 (22.0) | 39.9 (39.9) | 24.1 (24.1) | 29.1 (29.1) | 0.50-0.52 s |

Engine rounds (ruler-fresh):

| streams | tokens a round | drafts a round | accepted | ms a round | requests |
|---:|---:|---:|---:|---:|---:|
| 1 | 2.625 | 3.122 | 52% | 91.28 | 12 |

### ruler-after

| streams | prose total (a stream) | code total (a stream) | structured total (a stream) | list total (a stream) | first token |
|---:|---:|---:|---:|---:|---:|
| 1 | 22.1 (22.1) | 40.8 (40.8) | 24.1 (24.1) | 29.5 (29.5) | 0.49-0.51 s |

Engine rounds (ruler-after):

| streams | tokens a round | drafts a round | accepted | ms a round | requests |
|---:|---:|---:|---:|---:|---:|
| 1 | 2.64 | 3.073 | 53% | 90.57 | 13 |

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
| memory-idle | measured: head 8.0 GiB available; worker 7.8 GiB available |
| structured | pass: 18/18 obey, drafted == plain 12/12; a bad regex -> 400 |
| tools | pass: 5/5 tool cases right |
| sampling | pass: 9/9 seeded replies equal on repeat and undrafted; 0 errors |
| turns | pass: resumed == again: True; cold (after a restart): True; cached 4096 of 4826; ttft resumed 1.035s, cold 5.28s |
| urls | FAIL: public 400; loopback 400; http 400; unexpected: ['public'] |

## 2026-10-26 01:40: run `20261026-014038-quick`

Plan quick, done; served as `MiniMax-M3.1-Flash`.

Serving: engine_commit `c1ace3229; 32`; binary_sha256 `8e34323b0d535f97d1981829addd83500fc2c33a4f74ac430b8d55afb284abfa`; checkpoint_mix `[20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 31, 49, 52, 57, 59]`; server_args `TF_MINIMAX_RANK=0 TF_MINIMAX_WORLD=2 NCCL_SOCKET_IFNAME=enp1s0f1np1 NCCL_IB_HCA=rocep1s0f1`; suite_commit `fatal: not a git repository (or any of the parent directories): .git`

### ruler-fresh

| streams | prose total (a stream) | code total (a stream) | structured total (a stream) | list total (a stream) | first token |
|---:|---:|---:|---:|---:|---:|
| 1 | 22.3 (22.3) | 34.3 (34.3) | 23.8 (23.8) | 25.4 (25.4) | 0.48-0.51 s |

Engine rounds (ruler-fresh):

| streams | tokens a round | drafts a round | accepted | ms a round | requests |
|---:|---:|---:|---:|---:|---:|
| 1 | 2.104 | 1.518 | 72% | 79.59 | 12 |

### ruler-after

| streams | prose total (a stream) | code total (a stream) | structured total (a stream) | list total (a stream) | first token |
|---:|---:|---:|---:|---:|---:|
| 1 | 22.3 (22.3) | 34.5 (34.5) | 23.7 (23.7) | 25.4 (25.4) | 0.48-0.52 s |

Engine rounds (ruler-after):

| streams | tokens a round | drafts a round | accepted | ms a round | requests |
|---:|---:|---:|---:|---:|---:|
| 1 | 2.093 | 1.528 | 71% | 79.05 | 13 |

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
| memory-idle | measured: head 8.2 GiB available; worker 7.5 GiB available |
| structured | pass: 18/18 obey, drafted == plain 12/12; a bad regex -> 400 |
| tools | pass: 5/5 tool cases right |
| sampling | pass: 9/9 seeded replies equal on repeat and undrafted; 0 errors |
| turns | pass: resumed == again: True; cold (after a restart): True; cached 4096 of 4826; ttft resumed 1.013s, cold 5.241s |
| urls | FAIL: public 400; loopback 400; http 400; unexpected: ['public'] |

