# Ornith-1.5-122B, 4-bit MLX affine (g64), YaRN x4 to 1M context on 1x Apple M5 Ultra (256 GB unified), macOS

Target `ornith-15-122b-yarn1m-native-m5`: Ornith-1.5-122B, 4-bit MLX affine, static YaRN x4 (one 1,048,576-token stream), TensorFold native Metal on one M5 Ultra. Engine: TensorFold native, Metal. Rendered from `stats/ornith-15-122b-yarn1m-native-m5.json` (12 runs); aggregate tok/s, total (a stream).

## 2026-10-26 01:44: run `20261026-014405-mlx-speed`

Plan mlx-speed, done; served as `Ornith-1.5-122B`.

Serving: engine_commit `1429b56b`; binary_sha256 `64f5d54183672d8cc018bfb29f8be83b0da65c0e7b9293d9e6dd70203ff87cd5`; served_model `{"object": "list", "data": [{"id": "Ornith-1.5-122B", "object": "model", "created": 179299`; chip `Apple M5 Ultra; 274877906944`; suite_commit `277c842a1481`

### ruler-streams

| streams | prose total (a stream) | code total (a stream) | structured total (a stream) | list total (a stream) | first token |
|---:|---:|---:|---:|---:|---:|
| 1 | 77.7 (77.7) | 160.6 (160.6) | 105.8 (105.8) | 111.3 (111.3) | 0.06-0.08 s |
| 2 | 228.2 (114.1) | 374.0 (187.0) | 265.3 (132.6) | 376.2 (188.1) | 0.71-1.13 s |
| 4 | 447.1 (116.2) | 774.4 (197.4) | 554.8 (138.3) | 871.1 (210.4) | 1.58-3.32 s |

### checks

| check | result |
|---|---|
| memory-idle | measured: mac: System-wide memory free percentage: 48%; total = 3072.00M  us |

## 2026-10-26 01:41: run `20261026-014130-mlx-speed`

Plan mlx-speed, done; served as `Ornith-1.5-122B`.

Serving: engine_commit `f1097d68`; binary_sha256 `5756373d85256437f8c78b0043648b6b801baf4ea208e4c20b63e525ae8cf511`; served_model `{"object": "list", "data": [{"id": "Ornith-1.5-122B", "object": "model", "created": 179299`; chip `Apple M5 Ultra; 274877906944`; suite_commit `277c842a1481`

### ruler-streams

| streams | prose total (a stream) | code total (a stream) | structured total (a stream) | list total (a stream) | first token |
|---:|---:|---:|---:|---:|---:|
| 1 | 85.6 (85.6) | 179.8 (179.8) | 122.5 (122.5) | 129.5 (129.5) | 0.05-0.07 s |
| 2 | 223.9 (112.0) | 349.3 (174.7) | 260.8 (130.4) | 404.6 (202.3) | 0.67-1.14 s |
| 4 | 424.2 (110.1) | 832.7 (213.1) | 597.8 (150.8) | 800.3 (196.3) | 1.93-3.32 s |

### checks

| check | result |
|---|---|
| memory-idle | measured: mac: System-wide memory free percentage: 31%; total = 3072.00M  us |

## 2026-10-26 01:33: run `20261026-013308-thinking`

Plan thinking, done; served as `Ornith-1.5-122B`.

Serving: engine_commit `1429b56b`; binary_sha256 `64f5d54183672d8cc018bfb29f8be83b0da65c0e7b9293d9e6dd70203ff87cd5`; served_model `{"object": "list", "data": [{"id": "Ornith-1.5-122B", "object": "model", "created": 179299`; chip `Apple M5 Ultra; 274877906944`; suite_commit `291734b3cf5a`

### suite-thinking

| check | passed |
|---|---:|
| gsm8k | 247/250 |

### checks

| check | result |
|---|---|
| thinking | pass: thinking on: 10/10 right, 10/10 with reasoning_content, 0 leaks, 0 errors, 0 cut at 50176 tokens |

## 2026-10-26 01:30: run `20261026-013048-mlx-speed`

Plan mlx-speed, done; served as `Ornith-1.5-122B`.

Serving: engine_commit `1429b56b`; binary_sha256 `64f5d54183672d8cc018bfb29f8be83b0da65c0e7b9293d9e6dd70203ff87cd5`; served_model `{"object": "list", "data": [{"id": "Ornith-1.5-122B", "object": "model", "created": 179299`; chip `Apple M5 Ultra; 274877906944`; suite_commit `277c842a1481`

### ruler-streams

| streams | prose total (a stream) | code total (a stream) | structured total (a stream) | list total (a stream) | first token |
|---:|---:|---:|---:|---:|---:|
| 1 | 81.8 (81.8) | 183.2 (183.2) | 119.1 (119.1) | 125.4 (125.4) | 0.05-0.07 s |
| 2 | 211.2 (105.6) | 344.9 (172.5) | 282.4 (141.2) | 387.4 (193.7) | 0.52-1.08 s |
| 4 | 422.3 (108.1) | 843.4 (215.9) | 561.7 (143.7) | 797.5 (200.7) | 1.73-3.46 s |

### checks

| check | result |
|---|---|
| memory-idle | measured: mac: System-wide memory free percentage: 48%; total = 3072.00M  us |

## 2026-10-26 01:29: run `20261026-012919-thinking`

Plan thinking, done; served as `Ornith-1.5-122B`.

Serving: engine_commit `1429b56b`; binary_sha256 `64f5d54183672d8cc018bfb29f8be83b0da65c0e7b9293d9e6dd70203ff87cd5`; served_model `{"object": "list", "data": [{"id": "Ornith-1.5-122B", "object": "model", "created": 179299`; chip `Apple M5 Ultra; 274877906944`; suite_commit `277c842a1481`

### checks

| check | result |
|---|---|
| thinking | pass: thinking on: 10/10 right, 10/10 with reasoning_content, 0 leaks, 0 errors, 0 cut at 50176 tokens |

## 2026-10-26 00:46: run `20261026-004634-dsv41-quality-off`

Plan dsv41-quality-off, done; served as `Ornith-1.5-122B`.

Serving: engine_commit `1429b56b`; binary_sha256 `64f5d54183672d8cc018bfb29f8be83b0da65c0e7b9293d9e6dd70203ff87cd5`; served_model `{"object": "list", "data": [{"id": "Ornith-1.5-122B", "object": "model", "created": 179299`; chip `Apple M5 Ultra; 274877906944`; suite_commit `277c842a1481`

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
| ifeval | 116/150 |
| gsm8k | 245/250 |
| mgsm | 215/240 |
| mmlu | 294/342 |
| math500 | 428/500 |

### checks

| check | result |
|---|---|
| memory-idle | measured: mac: System-wide memory free percentage: 47%; total = 3072.00M  us |

## 2026-10-26 00:42: run `20261026-004241-mlx-speed`

Plan mlx-speed, done; served as `Ornith-1.5-122B`.

Serving: engine_commit `1429b56b`; binary_sha256 `64f5d54183672d8cc018bfb29f8be83b0da65c0e7b9293d9e6dd70203ff87cd5`; served_model `{"object": "list", "data": [{"id": "Ornith-1.5-122B", "object": "model", "created": 179299`; chip `Apple M5 Ultra; 274877906944`; suite_commit `277c842a1481`

### ruler-streams

| streams | prose total (a stream) | code total (a stream) | structured total (a stream) | list total (a stream) | first token |
|---:|---:|---:|---:|---:|---:|
| 1 | 93.5 (93.5) | 93.5 (93.5) | 93.6 (93.6) | 93.7 (93.7) | 0.05-0.07 s |
| 2 | 187.3 (93.7) | 187.0 (93.5) | 186.6 (93.3) | 187.4 (93.7) | 1.02-1.45 s |
| 4 | 342.3 (88.1) | 331.7 (84.5) | 363.4 (92.3) | 373.2 (93.4) | 3.04-4.92 s |

### checks

| check | result |
|---|---|
| memory-idle | measured: mac: System-wide memory free percentage: 48%; total = 3072.00M  us |

## 2026-10-26 00:40: run `20261026-004002-mlx-speed`

Plan mlx-speed, done; served as `Ornith-1.5-122B`.

Serving: engine_commit `1429b56b`; binary_sha256 `64f5d54183672d8cc018bfb29f8be83b0da65c0e7b9293d9e6dd70203ff87cd5`; served_model `{"object": "list", "data": [{"id": "Ornith-1.5-122B", "object": "model", "created": 179299`; chip `Apple M5 Ultra; 274877906944`; suite_commit `277c842a1481`

### ruler-streams

| streams | prose total (a stream) | code total (a stream) | structured total (a stream) | list total (a stream) | first token |
|---:|---:|---:|---:|---:|---:|
| 1 | 86.4 (86.4) | 180.8 (180.8) | 115.6 (115.6) | 117.1 (117.1) | 0.06-0.07 s |
| 2 | 225.6 (112.8) | 359.0 (179.5) | 282.5 (141.3) | 382.4 (191.2) | 0.52-1.01 s |
| 4 | 451.9 (116.5) | 828.2 (204.6) | 593.7 (149.7) | 868.7 (213.9) | 1.75-3.19 s |

### checks

| check | result |
|---|---|
| memory-idle | measured: mac: System-wide memory free percentage: 40%; total = 3072.00M  us |

## 2026-10-20 22:24: run `20261020-222403-thinking`

Plan thinking, done; served as `Ornith-1.5-122B`.

Serving: engine_commit `5ec491c8`; binary_sha256 `a3737c2d0060755f43a9fe9c09b90fa0993eb1b0eed53a43c9ee9bd36391f76d`; served_model `{"object": "list", "data": [{"id": "Ornith-1.5-122B", "object": "model", "created": 179255`; chip `Apple M5 Ultra; 274877906944`; suite_commit `291734b3cf5a`

### suite-thinking

| check | passed |
|---|---:|
| gsm8k | 247/250 |

### checks

| check | result |
|---|---|
| thinking | pass: thinking on: 10/10 right, 10/10 with reasoning_content, 0 leaks, 0 errors, 0 cut at 50176 tokens |

## 2026-10-20 21:42: run `20261020-214200-dsv41-quality-off`

Plan dsv41-quality-off, done; served as `Ornith-1.5-122B`.

Serving: engine_commit `5ec491c8`; binary_sha256 `a3737c2d0060755f43a9fe9c09b90fa0993eb1b0eed53a43c9ee9bd36391f76d`; served_model `{"object": "list", "data": [{"id": "Ornith-1.5-122B", "object": "model", "created": 179255`; chip `Apple M5 Ultra; 274877906944`; suite_commit `277c842a1481`

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
| ifeval | 116/150 |
| gsm8k | 245/250 |
| mgsm | 215/240 |
| mmlu | 294/342 |
| math500 | 428/500 |

### checks

| check | result |
|---|---|
| memory-idle | measured: mac: System-wide memory free percentage: 58%; total = 4096.00M  us |

## 2026-10-20 21:37: run `20261020-213756-mlx-speed`

Plan mlx-speed, done; served as `Ornith-1.5-122B`.

Serving: engine_commit `5ec491c8`; binary_sha256 `a3737c2d0060755f43a9fe9c09b90fa0993eb1b0eed53a43c9ee9bd36391f76d`; served_model `{"object": "list", "data": [{"id": "Ornith-1.5-122B", "object": "model", "created": 179255`; chip `Apple M5 Ultra; 274877906944`; suite_commit `277c842a1481`

### ruler-streams

| streams | prose total (a stream) | code total (a stream) | structured total (a stream) | list total (a stream) | first token |
|---:|---:|---:|---:|---:|---:|
| 1 | 95.3 (95.3) | 95.3 (95.3) | 95.1 (95.1) | 95.2 (95.2) | 0.05-0.07 s |
| 2 | 190.5 (95.3) | 190.4 (95.2) | 190.3 (95.2) | 190.4 (95.2) | 1.11-1.43 s |
| 4 | 381.7 (95.4) | 380.6 (95.1) | 380.4 (95.1) | 380.5 (95.1) | 3.09-4.17 s |

### checks

| check | result |
|---|---|
| memory-idle | measured: mac: System-wide memory free percentage: 59%; total = 4096.00M  us |

## 2026-10-20 21:34: run `20261020-213454-mlx-speed`

Plan mlx-speed, done; served as `Ornith-1.5-122B`.

Serving: engine_commit `5ec491c8`; binary_sha256 `a3737c2d0060755f43a9fe9c09b90fa0993eb1b0eed53a43c9ee9bd36391f76d`; served_model `{"object": "list", "data": [{"id": "Ornith-1.5-122B", "object": "model", "created": 179255`; chip `Apple M5 Ultra; 274877906944`; suite_commit `277c842a1481`

### ruler-streams

| streams | prose total (a stream) | code total (a stream) | structured total (a stream) | list total (a stream) | first token |
|---:|---:|---:|---:|---:|---:|
| 1 | 92.4 (92.4) | 193.7 (193.7) | 123.8 (123.8) | 130.0 (130.0) | 0.05-0.07 s |
| 2 | 234.4 (117.2) | 376.7 (188.3) | 296.2 (148.1) | 407.1 (203.6) | 0.65-1.10 s |
| 4 | 474.3 (121.2) | 862.6 (213.4) | 616.5 (156.3) | 900.3 (220.8) | 1.53-3.09 s |

### checks

| check | result |
|---|---|
| memory-idle | measured: mac: System-wide memory free percentage: 50%; total = 4096.00M  us |

