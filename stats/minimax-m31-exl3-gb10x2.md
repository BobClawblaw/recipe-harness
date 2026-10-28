# MiniMax-M3.1-Flash, EXL3 3.06 bpw (Mia-AiLab EAQ v1), 32k context on 2x NVIDIA DGX Spark (GB10, 128 GB unified each), TP=2 over RoCE

Target `minimax-m31-exl3-gb10x2`: MiniMax-M3.1-Flash, Mia-AiLab EXL3 3.06 bpw as published, DSpark drafts, 32k x 2 streams, TensorFold native CUDA, TP=2 on two DGX Sparks. Engine: TensorFold native, CUDA. Rendered from `stats/minimax-m31-exl3-gb10x2.json` (5 runs); aggregate tok/s, total (a stream).

## 2026-10-28 03:40: run `20261028-034040-quick`

Plan quick, done; served as `MiniMax-M3.1-Flash`.

Serving: engine_commit `aad9d2b8a; 0`; binary_sha256 `c23f2266dc7647101818eb9680c25ca75fc8704d13152c39e4ecf29a2dffacf5`; checkpoint_revision `Mia-AiLab/MiniMax-M3.1-Flash-EXL3-EAQ-v1-3.06-bpw c33e7a6619f0f12ac99098e07ec5e56acb7eeda9`; server_args `TF_MINIMAX_RANK=0 TF_MINIMAX_WORLD=2 NCCL_SOCKET_IFNAME=enp1s0f1np1 NCCL_IB_HCA=rocep1s0f1`; suite_commit `277c842a1481`

### ruler-fresh

| streams | prose total (a stream) | code total (a stream) | structured total (a stream) | list total (a stream) | first token |
|---:|---:|---:|---:|---:|---:|
| 1 | 24.6 (24.6) | 39.6 (39.6) | 29.7 (29.7) | 30.3 (30.3) | 0.59-0.64 s |

Engine rounds (ruler-fresh):

| streams | tokens a round | drafts a round | accepted | ms a round | requests |
|---:|---:|---:|---:|---:|---:|
| 1 | 2.708 | 3.41 | 50% | 87.21 | 12 |

### ruler-after

| streams | prose total (a stream) | code total (a stream) | structured total (a stream) | list total (a stream) | first token |
|---:|---:|---:|---:|---:|---:|
| 1 | 24.4 (24.4) | 38.8 (38.8) | 28.9 (28.9) | 30.4 (30.4) | 0.59-0.64 s |

Engine rounds (ruler-after):

| streams | tokens a round | drafts a round | accepted | ms a round | requests |
|---:|---:|---:|---:|---:|---:|
| 1 | 2.658 | 3.238 | 51% | 86.77 | 13 |

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
| memory-idle | measured: head 27.1 GiB available; worker 26.0 GiB available |
| structured | pass: 18/18 obey, drafted == plain 12/12; a bad regex -> 400 |
| tools | pass: 5/5 tool cases right |
| sampling | pass: 9/9 seeded replies equal on repeat and undrafted; 0 errors |
| turns | pass: resumed == again: True; cold (after a restart): True; cached 4096 of 4725; ttft resumed 1.623s, cold 10.031s |
| urls | FAIL: public 400; loopback 400; http 400; unexpected: ['public'] |

## 2026-10-28 03:26: run `20261028-032641-speed`

Plan speed, done; served as `MiniMax-M3.1-Flash`.

Serving: engine_commit `aad9d2b8a; 1`; binary_sha256 `c23f2266dc7647101818eb9680c25ca75fc8704d13152c39e4ecf29a2dffacf5`; checkpoint_revision `Mia-AiLab/MiniMax-M3.1-Flash-EXL3-EAQ-v1-3.06-bpw c33e7a6619f0f12ac99098e07ec5e56acb7eeda9`; server_args `TF_MINIMAX_RANK=0 TF_MINIMAX_WORLD=2 NCCL_SOCKET_IFNAME=enp1s0f1np1 NCCL_IB_HCA=rocep1s0f1`; suite_commit `277c842a1481`

### ruler-fresh

| streams | prose total (a stream) | code total (a stream) | structured total (a stream) | list total (a stream) | first token |
|---:|---:|---:|---:|---:|---:|
| 1 | 24.3 (24.3) | 38.5 (38.5) | 29.5 (29.5) | 30.3 (30.3) | 0.59-0.64 s |
| 2 | 33.3 (16.7) | 49.0 (24.5) | 39.4 (19.7) | 55.3 (27.7) | 0.99-1.06 s |

Engine rounds (ruler-fresh):

| streams | tokens a round | drafts a round | accepted | ms a round | requests |
|---:|---:|---:|---:|---:|---:|
| 1 | 2.667 | 3.348 | 50% | 87.02 | 12 |
| 2 | 2.508 | 2.599 | 58% | 113.35 | 25 |

### ruler-after

| streams | prose total (a stream) | code total (a stream) | structured total (a stream) | list total (a stream) | first token |
|---:|---:|---:|---:|---:|---:|
| 1 | 24.6 (24.6) | 39.5 (39.5) | 29.4 (29.4) | 30.3 (30.3) | 0.60-0.64 s |

Engine rounds (ruler-after):

| streams | tokens a round | drafts a round | accepted | ms a round | requests |
|---:|---:|---:|---:|---:|---:|
| 1 | 2.696 | 3.378 | 50% | 87.1 | 13 |

### checks

| check | result |
|---|---|
| memory-idle | measured: head 26.8 GiB available; worker 26.4 GiB available |
| turns | pass: resumed == again: True; cold (after a restart): True; cached 4096 of 4725; ttft resumed 1.613s, cold 9.999s |
| memory-busy | measured: head 26.6 GiB available; worker 26.5 GiB available |

## 2026-10-28 02:59: run `20261028-025952-glm-vision`

Plan glm-vision, done; served as `MiniMax-M3.1-Flash`.

Serving: engine_commit `6183c5306; 51`; binary_sha256 `adfa426690e44f3ecf85a2397c525295c9182346c9a1f8434e6079e10156340d`; checkpoint_revision `Mia-AiLab/MiniMax-M3.1-Flash-EXL3-EAQ-v1-3.06-bpw c33e7a6619f0f12ac99098e07ec5e56acb7eeda9`; server_args `TF_MINIMAX_RANK=0 TF_MINIMAX_WORLD=2 NCCL_SOCKET_IFNAME=enp1s0f1np1 NCCL_IB_HCA=rocep1s0f1`; suite_commit `277c842a1481`

### suite-vision

| check | passed |
|---|---:|
| vision | 3/6 |
| vision-concurrent | 0/0 |

## 2026-10-28 02:31: run `20261028-023138-quick`

Plan quick, done; served as `MiniMax-M3.1-Flash`.

Serving: engine_commit `6183c5306; 51`; binary_sha256 `adfa426690e44f3ecf85a2397c525295c9182346c9a1f8434e6079e10156340d`; checkpoint_revision `Mia-AiLab/MiniMax-M3.1-Flash-EXL3-EAQ-v1-3.06-bpw c33e7a6619f0f12ac99098e07ec5e56acb7eeda9`; server_args `TF_MINIMAX_RANK=0 TF_MINIMAX_WORLD=2 NCCL_SOCKET_IFNAME=enp1s0f1np1 NCCL_IB_HCA=rocep1s0f1`; suite_commit `277c842a1481`

### ruler-fresh

| streams | prose total (a stream) | code total (a stream) | structured total (a stream) | list total (a stream) | first token |
|---:|---:|---:|---:|---:|---:|
| 1 | 24.3 (24.3) | 38.1 (38.1) | 29.0 (29.0) | 30.1 (30.1) | 0.60-0.65 s |

Engine rounds (ruler-fresh):

| streams | tokens a round | drafts a round | accepted | ms a round | requests |
|---:|---:|---:|---:|---:|---:|
| 1 | 2.615 | 3.208 | 50% | 86.17 | 12 |

### ruler-after

| streams | prose total (a stream) | code total (a stream) | structured total (a stream) | list total (a stream) | first token |
|---:|---:|---:|---:|---:|---:|
| 1 | 24.3 (24.3) | 38.3 (38.3) | 27.6 (27.6) | 29.8 (29.8) | 0.60-0.65 s |

Engine rounds (ruler-after):

| streams | tokens a round | drafts a round | accepted | ms a round | requests |
|---:|---:|---:|---:|---:|---:|
| 1 | 2.649 | 3.301 | 50% | 88.32 | 13 |

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
| memory-idle | measured: head 26.6 GiB available; worker 26.0 GiB available |
| structured | pass: 18/18 obey, drafted == plain 12/12; a bad regex -> 400 |
| tools | pass: 5/5 tool cases right |
| sampling | pass: 9/9 seeded replies equal on repeat and undrafted; 0 errors |
| turns | pass: resumed == again: True; cold (after a restart): True; cached 4096 of 4725; ttft resumed 1.623s, cold 10.105s |
| urls | FAIL: public 400; loopback 400; http 400; unexpected: ['public'] |

## 2026-10-28 02:16: run `20261028-021628-speed`

Plan speed, done; served as `MiniMax-M3.1-Flash`.

Serving: engine_commit `6183c5306; 51`; binary_sha256 `adfa426690e44f3ecf85a2397c525295c9182346c9a1f8434e6079e10156340d`; checkpoint_revision `Mia-AiLab/MiniMax-M3.1-Flash-EXL3-EAQ-v1-3.06-bpw c33e7a6619f0f12ac99098e07ec5e56acb7eeda9`; server_args `TF_MINIMAX_RANK=0 TF_MINIMAX_WORLD=2 NCCL_SOCKET_IFNAME=enp1s0f1np1 NCCL_IB_HCA=rocep1s0f1`; suite_commit `277c842a1481`

### ruler-fresh

| streams | prose total (a stream) | code total (a stream) | structured total (a stream) | list total (a stream) | first token |
|---:|---:|---:|---:|---:|---:|
| 1 | 24.4 (24.4) | 39.2 (39.2) | 29.7 (29.7) | 30.1 (30.1) | 0.60-0.65 s |
| 2 | 31.0 (15.5) | 44.9 (22.5) | 35.7 (17.9) | 52.0 (26.0) | 1.01-1.15 s |

Engine rounds (ruler-fresh):

| streams | tokens a round | drafts a round | accepted | ms a round | requests |
|---:|---:|---:|---:|---:|---:|
| 1 | 2.652 | 3.26 | 51% | 85.96 | 12 |
| 2 | 2.557 | 2.709 | 57% | 124.95 | 25 |

### ruler-after

| streams | prose total (a stream) | code total (a stream) | structured total (a stream) | list total (a stream) | first token |
|---:|---:|---:|---:|---:|---:|
| 1 | 24.3 (24.3) | 39.4 (39.4) | 29.2 (29.2) | 30.4 (30.4) | 0.60-0.65 s |

Engine rounds (ruler-after):

| streams | tokens a round | drafts a round | accepted | ms a round | requests |
|---:|---:|---:|---:|---:|---:|
| 1 | 2.649 | 3.211 | 51% | 85.97 | 13 |

### checks

| check | result |
|---|---|
| memory-idle | measured: head 26.6 GiB available; worker 26.7 GiB available |
| turns | pass: resumed == again: True; cold (after a restart): True; cached 4096 of 4725; ttft resumed 1.635s, cold 10.104s |
| memory-busy | measured: head 26.1 GiB available; worker 26.5 GiB available |

