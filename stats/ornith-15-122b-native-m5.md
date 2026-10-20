# Ornith-1.5-122B, 4-bit MLX affine (g64) on 1x Apple M5 Ultra (256 GB unified), macOS

Target `ornith-15-122b-native-m5`: Ornith-1.5-122B, 4-bit MLX affine, TensorFold native Metal on one M5 Ultra. Engine: TensorFold native, Metal. Rendered from `stats/ornith-15-122b-native-m5.json` (7 runs); aggregate tok/s, total (a stream).

## 2026-10-20 13:39: run `20261020-133912-mlx-speed`

Plan mlx-speed, done; served as `Ornith-1.5-122B`.

Serving: engine_commit `32dad79b`; binary_sha256 `5dcb999c71614342b4d9056e76ec2d00befb6d581f6961bcc088d5a7cd2a3bd1`; served_model `{"object": "list", "data": [{"id": "Ornith-1.5-122B", "object": "model", "created": 179252`; chip `Apple M5 Ultra; 274877906944`; suite_commit `277c842a1481`

### ruler-streams

| streams | prose total (a stream) | code total (a stream) | structured total (a stream) | list total (a stream) | first token |
|---:|---:|---:|---:|---:|---:|
| 1 | 85.0 (85.0) | 84.8 (84.8) | 84.6 (84.6) | 84.9 (84.9) | 0.05-0.07 s |
| 2 | 139.2 (69.6) | 143.6 (71.8) | 146.2 (73.1) | 141.7 (70.8) | 0.07-0.10 s |
| 4 | 218.7 (54.5) | 223.6 (56.1) | 238.1 (61.0) | 227.3 (56.8) | 0.12-0.16 s |

### checks

| check | result |
|---|---|
| memory-idle | measured: mac: System-wide memory free percentage: 66%; total = 5120.00M  us |

## 2026-10-20 13:36: run `20261020-133658-mlx-speed`

Plan mlx-speed, done; served as `Ornith-1.5-122B`.

Serving: engine_commit `32dad79b`; binary_sha256 `5dcb999c71614342b4d9056e76ec2d00befb6d581f6961bcc088d5a7cd2a3bd1`; served_model `{"object": "list", "data": [{"id": "Ornith-1.5-122B", "object": "model", "created": 179252`; chip `Apple M5 Ultra; 274877906944`; suite_commit `277c842a1481`

### ruler-streams

| streams | prose total (a stream) | code total (a stream) | structured total (a stream) | list total (a stream) | first token |
|---:|---:|---:|---:|---:|---:|
| 1 | 42.6 (42.6) | 84.1 (84.1) | 70.5 (70.5) | 71.4 (71.4) | 0.05-0.07 s |
| 2 | 155.1 (77.6) | 252.2 (126.1) | 165.3 (82.6) | 246.5 (123.2) | 0.08-0.10 s |
| 4 | 194.5 (48.3) | 363.7 (82.7) | 329.6 (69.6) | 322.7 (80.2) | 0.13-0.17 s |

### checks

| check | result |
|---|---|
| memory-idle | measured: mac: System-wide memory free percentage: 65%; total = 5120.00M  us |

## 2026-10-20 13:31: run `20261020-133150-mlx-speed`

Plan mlx-speed, done; served as `Ornith-1.5-122B`.

Serving: engine_commit `4acc699a`; binary_sha256 `45468c73e693884f05ce1e4221cdbd89e645907d7daaf814425c35a09de3c4d4`; served_model `{"object": "list", "data": [{"id": "Ornith-1.5-122B", "object": "model", "created": 179252`; chip `Apple M5 Ultra; 274877906944`; suite_commit `277c842a1481`

### ruler-streams

| streams | prose total (a stream) | code total (a stream) | structured total (a stream) | list total (a stream) | first token |
|---:|---:|---:|---:|---:|---:|
| 1 | 85.4 (85.4) | 85.3 (85.3) | 85.3 (85.3) | 85.3 (85.3) | 0.05-0.07 s |
| 2 | 139.7 (69.9) | 144.9 (72.4) | 151.4 (75.7) | 142.7 (71.4) | 0.07-0.10 s |
| 4 | 219.0 (54.6) | 224.7 (56.0) | 236.5 (61.4) | 227.3 (56.9) | 0.12-0.16 s |

### checks

| check | result |
|---|---|
| memory-idle | measured: mac: System-wide memory free percentage: 67%; total = 5120.00M  us |

## 2026-10-20 13:29: run `20261020-132936-mlx-speed`

Plan mlx-speed, done; served as `Ornith-1.5-122B`.

Serving: engine_commit `4acc699a`; binary_sha256 `45468c73e693884f05ce1e4221cdbd89e645907d7daaf814425c35a09de3c4d4`; served_model `{"object": "list", "data": [{"id": "Ornith-1.5-122B", "object": "model", "created": 179252`; chip `Apple M5 Ultra; 274877906944`; suite_commit `277c842a1481`

### ruler-streams

| streams | prose total (a stream) | code total (a stream) | structured total (a stream) | list total (a stream) | first token |
|---:|---:|---:|---:|---:|---:|
| 1 | 42.6 (42.6) | 84.2 (84.2) | 70.4 (70.4) | 71.3 (71.3) | 0.05-0.07 s |
| 2 | 155.2 (77.6) | 248.6 (124.3) | 166.1 (83.0) | 242.1 (121.1) | 0.08-0.10 s |
| 4 | 190.3 (47.9) | 359.2 (82.2) | 323.3 (70.3) | 296.7 (74.0) | 0.13-0.17 s |

### checks

| check | result |
|---|---|
| memory-idle | measured: mac: System-wide memory free percentage: 66%; total = 5120.00M  us |

## 2026-10-20 13:19: run `20261020-131953-mlx-speed`

Plan mlx-speed, done; served as `Ornith-1.5-122B`.

Serving: engine_commit `b117a8bc`; binary_sha256 `1afd91325cd437f1b113cdfe152a66d9e87b454ead77e21e0d80428ff36417a7`; served_model `{"object": "list", "data": [{"id": "Ornith-1.5-122B", "object": "model", "created": 179252`; chip `Apple M5 Ultra; 274877906944`; suite_commit `277c842a1481`

### ruler-streams

| streams | prose total (a stream) | code total (a stream) | structured total (a stream) | list total (a stream) | first token |
|---:|---:|---:|---:|---:|---:|
| 1 | 40.5 (40.5) | 84.6 (84.6) | 70.3 (70.3) | 68.4 (68.4) | 0.05-0.07 s |
| 2 | 149.9 (75.0) | 263.6 (131.8) | 159.7 (79.9) | 259.3 (129.6) | 0.08-0.10 s |
| 4 | 197.5 (47.9) | 353.0 (80.5) | 323.9 (69.7) | 333.0 (82.4) | 0.12-0.17 s |

### checks

| check | result |
|---|---|
| memory-idle | measured: mac: System-wide memory free percentage: 40%; total = 5120.00M  us |

## 2026-10-20 12:56: run `20261020-125604-mlx-speed`

Plan mlx-speed, done; served as `Ornith-1.5-122B`.

Serving: engine_commit `b117a8bc`; binary_sha256 `01878b3c9d69c23fae1de11b26ad547c9a21a0824c50016fe83fbd0405ba3713`; served_model `{"object": "list", "data": [{"id": "Ornith-1.5-122B", "object": "model", "created": 179251`; chip `Apple M5 Ultra; 274877906944`; suite_commit `277c842a1481`

### ruler-streams

| streams | prose total (a stream) | code total (a stream) | structured total (a stream) | list total (a stream) | first token |
|---:|---:|---:|---:|---:|---:|
| 1 | 40.4 (40.4) | 79.3 (79.3) | 71.4 (71.4) | 71.8 (71.8) | 0.05-0.07 s |
| 2 | 152.1 (76.0) | 281.8 (140.9) | 164.6 (82.3) | 250.7 (125.4) | 0.08-0.11 s |
| 4 | 197.3 (48.3) | 408.0 (99.6) | 322.4 (69.1) | 331.1 (81.7) | 0.13-0.18 s |

### checks

| check | result |
|---|---|
| memory-idle | measured: mac: System-wide memory free percentage: 68%; total = 4096.00M  us |

## 2026-10-20 12:49: run `20261020-124945-mlx-speed`

Plan mlx-speed, done; served as `Ornith-1.5-122B`.

Serving: engine_commit `b117a8bc`; binary_sha256 `00b1b365240971356da3bf4a84f646d0f748e34f6b29f865226a7651ee903241`; served_model `{"object": "list", "data": [{"id": "Ornith-1.5-122B", "object": "model", "created": 179251`; chip `Apple M5 Ultra; 274877906944`; suite_commit `277c842a1481`

### ruler-streams

| streams | prose total (a stream) | code total (a stream) | structured total (a stream) | list total (a stream) | first token |
|---:|---:|---:|---:|---:|---:|
| 1 | 85.0 (85.0) | 85.1 (85.1) | 85.3 (85.3) | 85.1 (85.1) | 0.05-0.07 s |
| 2 | 143.4 (71.7) | 144.7 (72.3) | 143.3 (71.6) | 142.5 (71.3) | 0.07-0.10 s |
| 4 | 219.4 (55.2) | 221.4 (55.4) | 237.1 (56.2) | 225.0 (56.2) | 0.12-0.16 s |

### checks

| check | result |
|---|---|
| memory-idle | measured: mac: System-wide memory free percentage: 66%; total = 4096.00M  us |

