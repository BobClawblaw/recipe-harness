# Recursive Flint 40B-A2.5B, MLX INT4 (g64) on 1x Apple M5 Ultra (256 GB unified), macOS

Target `flint-40b-native-m5`: Recursive Flint 40B-A2.5B, MLX INT4 (g64), TensorFold native Metal on one M5 Ultra. Engine: TensorFold native, Metal. Rendered from `stats/flint-40b-native-m5.json` (4 runs); aggregate tok/s, total (a stream).

## 2026-10-21 17:23: run `20261021-172342-speed`

Plan speed, done; served as `flint`.

Serving: engine_commit `8491096c`; binary_sha256 `7bbe2fa3fe4bb1708e023c2a0ee586a933558ca3f32273fcdfa811bb7d53a4b7`; served_model `{"object": "list", "data": [{"id": "flint", "object": "model", "created": 1792621430, "own`; chip `Apple M5 Ultra; 274877906944`; suite_commit `277c842a1481`

### ruler-fresh

| streams | prose total (a stream) | code total (a stream) | structured total (a stream) | list total (a stream) | first token |
|---:|---:|---:|---:|---:|---:|
| 1 | 136.4 (136.4) | 132.7 (132.7) | 142.6 (142.6) | 132.9 (132.9) | 0.03-0.05 s |
| 2 | 182.8 (91.4) | 179.1 (89.5) | 193.3 (96.7) | 178.1 (89.1) | 0.04-0.07 s |

Engine rounds (ruler-fresh):

| streams | tokens a round | drafts a round | accepted | ms a round | requests |
|---:|---:|---:|---:|---:|---:|
| 1 | 1.048 | 0.092 | 48% | 7.7 | 12 |
| 2 | 1.051 | 0.116 | 41% | 11.47 | 25 |

### ruler-after

| streams | prose total (a stream) | code total (a stream) | structured total (a stream) | list total (a stream) | first token |
|---:|---:|---:|---:|---:|---:|
| 1 | 135.7 (135.7) | 131.8 (131.8) | 142.5 (142.5) | 132.2 (132.2) | 0.03-0.05 s |

Engine rounds (ruler-after):

| streams | tokens a round | drafts a round | accepted | ms a round | requests |
|---:|---:|---:|---:|---:|---:|
| 1 | 1.048 | 0.096 | 46% | 7.73 | 13 |

### checks

| check | result |
|---|---|
| memory-idle | measured: mac: System-wide memory free percentage: 87%; total = 3072.00M  us |
| turns | pass: resumed == again: True; cold (after a restart): True; cached 4507 of 4627; ttft resumed 0.073s, cold 0.912s |
| memory-busy | measured: mac: System-wide memory free percentage: 87%; total = 3072.00M  us |

## 2026-10-21 17:10: run `20261021-171056-prefill`

Plan prefill, done; served as `flint`.

Serving: engine_commit `97ce2ef3`; binary_sha256 `c19c2847652def0f298490541cd6bf2dbb0f0379aaf19ec9b20adcc6441d9152`; served_model `{"object": "list", "data": [{"id": "flint", "object": "model", "created": 1792620664, "own`; chip `Apple M5 Ultra; 274877906944`; suite_commit `277c842a1481`

### checks

| check | result |
|---|---|
| memory-idle | measured: mac: System-wide memory free percentage: 87%; total = 3072.00M  us |
| prefill-off | measured: 2067 tokens 5327.3 tok/s (0.388 s), 8213 tokens 5508.4 tok/s (1.491 s), 32791 tokens 4766.1 tok/s (6.88 s), 131092 tokens 2930.2 tok/s (44.739 s) |
| prefill-thinking | measured: 2068 tokens 5209.1 tok/s (0.397 s), 8211 tokens 5474.0 tok/s (1.5 s), 32791 tokens 4730.4 tok/s (6.932 s), 131095 tokens 2930.3 tok/s (44.737 s) |
| memory-busy | measured: mac: System-wide memory free percentage: 84%; total = 3072.00M  us |

## 2026-10-21 17:08: run `20261021-170851-structured`

Plan structured, done; served as `flint`.

Serving: engine_commit `97ce2ef3`; binary_sha256 `c19c2847652def0f298490541cd6bf2dbb0f0379aaf19ec9b20adcc6441d9152`; served_model `{"object": "list", "data": [{"id": "flint", "object": "model", "created": 1792620531, "own`; chip `Apple M5 Ultra; 274877906944`; suite_commit `277c842a1481`

### checks

| check | result |
|---|---|
| structured | pass: 18/18 obey, drafted == plain 12/12; a bad regex -> 400 |
| tools | pass: 5/5 tool cases right |

## 2026-10-21 17:06: run `20261021-170658-mlx-speed`

Plan mlx-speed, done; served as `flint`.

Serving: engine_commit `97ce2ef3`; binary_sha256 `c19c2847652def0f298490541cd6bf2dbb0f0379aaf19ec9b20adcc6441d9152`; served_model `{"object": "list", "data": [{"id": "flint", "object": "model", "created": 1792620418, "own`; chip `Apple M5 Ultra; 274877906944`; suite_commit `277c842a1481`

### ruler-streams

| streams | prose total (a stream) | code total (a stream) | structured total (a stream) | list total (a stream) | first token |
|---:|---:|---:|---:|---:|---:|
| 1 | 135.4 (135.4) | 131.3 (131.3) | 143.4 (143.4) | 131.9 (131.9) | 0.03-0.05 s |
| 2 | 182.4 (91.2) | 181.0 (90.5) | 193.2 (96.6) | 178.8 (89.4) | 0.04-0.07 s |
| 4 | 230.3 (57.6) | 227.6 (56.9) | 237.0 (59.2) | 229.2 (57.1) | 0.07-0.12 s |

Engine rounds (ruler-streams):

| streams | tokens a round | drafts a round | accepted | ms a round | requests |
|---:|---:|---:|---:|---:|---:|
| 1 | 1.048 | 0.092 | 48% | 7.73 | 12 |
| 2 | 1.051 | 0.116 | 41% | 11.44 | 25 |
| 4 | 1.055 | 0.128 | 40% | 18.28 | 50 |

### checks

| check | result |
|---|---|
| memory-idle | measured: mac: System-wide memory free percentage: 87%; total = 3072.00M  us |

