# MiniMax-M3.1-Flash, MLX mixed 3-bit (mix256k), 256k context on 1x Apple M5 Ultra (256 GB unified), macOS

Target `minimax-m31-mix256k-m5`: MiniMax-M3.1-Flash, MLX mixed 3-bit (mix256k), 256k context, TensorFold native Metal on one M5 Ultra. Engine: TensorFold native, Metal. Rendered from `stats/minimax-m31-mix256k-m5.json` (5 runs); aggregate tok/s, total (a stream).

## 2026-10-24 03:42: run `20261024-034251-mlx-speed`

Plan mlx-speed, done; served as `MiniMax-M3.1-Flash`.

Serving: engine_commit `39746b53e`; binary_sha256 `d56e474b3cef52e1cdaf7383f9fb415098b778f688850572dbae187b27a728df`; served_model `{"object": "list", "data": [{"id": "MiniMax-M3.1-Flash", "object": "model", "created": 179`; chip `Apple M5 Ultra; 274877906944`; suite_commit `277c842a1481`

### ruler-streams

| streams | prose total (a stream) | code total (a stream) | structured total (a stream) | list total (a stream) | first token |
|---:|---:|---:|---:|---:|---:|
| 1 | 44.1 (44.1) | 44.0 (44.0) | 44.0 (44.0) | 44.1 (44.1) | 0.32-0.34 s |
| 2 | 63.3 (31.7) | 62.8 (31.4) | 64.1 (32.0) | 63.6 (31.8) | 0.48-0.51 s |
| 4 | 126.3 (31.6) | 125.6 (31.4) | 126.3 (30.9) | 126.6 (31.7) | 3.40-4.81 s |

Engine rounds (ruler-streams):

| streams | tokens a round | drafts a round | accepted | ms a round | requests |
|---:|---:|---:|---:|---:|---:|
| 1 | 1.004 | 0.0 |  | 22.8 | 12 |
| 2 | 1.004 | 0.0 |  | 31.66 | 25 |
| 4 | 1.004 | 0.0 |  | 31.99 | 50 |

### checks

| check | result |
|---|---|
| memory-idle | measured: mac: System-wide memory free percentage: 96%; total = 4096.00M  us |

## 2026-10-24 03:33: run `20261024-033319-prefill`

Plan prefill, done; served as `MiniMax-M3.1-Flash`.

Serving: engine_commit `39746b53e`; binary_sha256 `d56e474b3cef52e1cdaf7383f9fb415098b778f688850572dbae187b27a728df`; served_model `{"object": "list", "data": [{"id": "MiniMax-M3.1-Flash", "object": "model", "created": 179`; chip `Apple M5 Ultra; 274877906944`; suite_commit `277c842a1481`

### checks

| check | result |
|---|---|
| memory-idle | measured: mac: System-wide memory free percentage: 96%; total = 4096.00M  us |
| prefill-off | measured: 2261 tokens 579.7 tok/s (3.9 s), 8402 tokens 1205.6 tok/s (6.969 s), 32980 tokens 1020.4 tok/s (32.321 s), 131282 tokens 702.7 tok/s (186.829 s) |
| prefill-thinking | measured: 2259 tokens 1172.3 tok/s (1.927 s), 8407 tokens 1194.0 tok/s (7.041 s), 32979 tokens 1025.0 tok/s (32.176 s), 131283 tokens 699.8 tok/s (187.603 s) |
| memory-busy | measured: mac: System-wide memory free percentage: 19%; total = 4096.00M  us |

## 2026-10-24 00:46: run `20261024-004651-dsv41-quality-off`

Plan dsv41-quality-off, done; served as `MiniMax-M3.1-Flash`.

Serving: engine_commit `39746b53e`; binary_sha256 `d56e474b3cef52e1cdaf7383f9fb415098b778f688850572dbae187b27a728df`; served_model `{"object": "list", "data": [{"id": "MiniMax-M3.1-Flash", "object": "model", "created": 179`; chip `Apple M5 Ultra; 274877906944`; suite_commit `277c842a1481`

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
| tools | 55/60 |
| json | 30/30 |
| ifeval | 86/150 |
| gsm8k | 244/250 |
| mgsm | 210/240 |
| mmlu | 280/342 |
| math500 | 454/500 |

### checks

| check | result |
|---|---|
| memory-idle | measured: mac: System-wide memory free percentage: 22%; total = 4096.00M  us |

## 2026-10-24 00:45: run `20261024-004535-structured`

Plan structured, done; served as `MiniMax-M3.1-Flash`.

Serving: engine_commit `39746b53e`; binary_sha256 `d56e474b3cef52e1cdaf7383f9fb415098b778f688850572dbae187b27a728df`; served_model `{"object": "list", "data": [{"id": "MiniMax-M3.1-Flash", "object": "model", "created": 179`; chip `Apple M5 Ultra; 274877906944`; suite_commit `277c842a1481`

### checks

| check | result |
|---|---|
| structured | pass: 18/18 obey, drafted == plain 12/12; a bad regex -> 400 |
| tools | pass: 5/5 tool cases right |

## 2026-10-24 00:39: run `20261024-003948-speed`

Plan speed, done; served as `MiniMax-M3.1-Flash`.

Serving: engine_commit `39746b53e`; binary_sha256 `d56e474b3cef52e1cdaf7383f9fb415098b778f688850572dbae187b27a728df`; served_model `{"object": "list", "data": [{"id": "MiniMax-M3.1-Flash", "object": "model", "created": 179`; chip `Apple M5 Ultra; 274877906944`; suite_commit `277c842a1481`

### ruler-fresh

| streams | prose total (a stream) | code total (a stream) | structured total (a stream) | list total (a stream) | first token |
|---:|---:|---:|---:|---:|---:|
| 1 | 42.8 (42.8) | 57.9 (57.9) | 48.7 (48.7) | 47.9 (47.9) | 0.31-0.33 s |
| 2 | 52.2 (26.1) | 65.5 (32.8) | 58.1 (29.0) | 74.7 (37.3) | 0.47-0.50 s |

Engine rounds (ruler-fresh):

| streams | tokens a round | drafts a round | accepted | ms a round | requests |
|---:|---:|---:|---:|---:|---:|
| 1 | 2.085 | 1.666 | 65% | 42.25 | 12 |
| 2 | 2.161 | 1.528 | 76% | 69.01 | 25 |

### ruler-after

| streams | prose total (a stream) | code total (a stream) | structured total (a stream) | list total (a stream) | first token |
|---:|---:|---:|---:|---:|---:|
| 1 | 42.2 (42.2) | 58.1 (58.1) | 48.6 (48.6) | 47.8 (47.8) | 0.31-0.33 s |

Engine rounds (ruler-after):

| streams | tokens a round | drafts a round | accepted | ms a round | requests |
|---:|---:|---:|---:|---:|---:|
| 1 | 2.14 | 1.759 | 64% | 43.48 | 13 |

### checks

| check | result |
|---|---|
| memory-idle | measured: mac: System-wide memory free percentage: 22%; total = 4096.00M  us |
| turns | pass: resumed == again: True; cold (after a restart): True; cached 4685 of 4826; ttft resumed 0.309s, cold 6.217s |
| memory-busy | measured: mac: System-wide memory free percentage: 22%; total = 4096.00M  us |

