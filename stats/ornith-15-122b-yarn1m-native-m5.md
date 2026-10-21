# Ornith-1.5-122B, 4-bit MLX affine (g64), YaRN x4 to 1M context on 1x Apple M5 Ultra (256 GB unified), macOS

Target `ornith-15-122b-yarn1m-native-m5`: Ornith-1.5-122B, 4-bit MLX affine, static YaRN x4 (one 1,048,576-token stream), TensorFold native Metal on one M5 Ultra. Engine: TensorFold native, Metal. Rendered from `stats/ornith-15-122b-yarn1m-native-m5.json` (4 runs); aggregate tok/s, total (a stream).

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

