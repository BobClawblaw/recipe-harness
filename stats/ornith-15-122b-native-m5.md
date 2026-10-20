# Ornith-1.5-122B, 4-bit MLX affine (g64) on 1x Apple M5 Ultra (256 GB unified), macOS

Target `ornith-15-122b-native-m5`: Ornith-1.5-122B, 4-bit MLX affine, TensorFold native Metal on one M5 Ultra. Engine: TensorFold native, Metal. Rendered from `stats/ornith-15-122b-native-m5.json` (17 runs); aggregate tok/s, total (a stream).

## 2026-10-20 16:19: run `20261020-161950-thinking`

Plan thinking, done; served as `Ornith-1.5-122B`.

Serving: engine_commit `30e5dcb4`; binary_sha256 `3e7504db19242321a95555a39a18a51e368405092dbe724d89537d5c14091376`; served_model `{"object": "list", "data": [{"id": "Ornith-1.5-122B", "object": "model", "created": 179253`; chip `Apple M5 Ultra; 274877906944`; suite_commit `291734b3cf5a`

### suite-thinking

| check | passed |
|---|---:|
| gsm8k | 244/250 |

### checks

| check | result |
|---|---|
| thinking | pass: thinking on: 10/10 right, 10/10 with reasoning_content, 0 leaks, 0 errors, 0 cut at 50176 tokens |

## 2026-10-20 15:27: run `20261020-152715-thinking`

Plan thinking, done; served as `Ornith-1.5-122B`.

Serving: engine_commit `30e5dcb4`; binary_sha256 `3e7504db19242321a95555a39a18a51e368405092dbe724d89537d5c14091376`; served_model `{"object": "list", "data": [{"id": "Ornith-1.5-122B", "object": "model", "created": 179252`; chip `Apple M5 Ultra; 274877906944`; suite_commit `277c842a1481`

### checks

| check | result |
|---|---|
| thinking | pass: thinking on: 10/10 right, 10/10 with reasoning_content, 0 leaks, 0 errors, 0 cut at 50176 tokens |

## 2026-10-20 15:25: run `20261020-152513-mlx-speed`

Plan mlx-speed, done; served as `Ornith-1.5-122B`.

Serving: engine_commit `30e5dcb4`; binary_sha256 `3e7504db19242321a95555a39a18a51e368405092dbe724d89537d5c14091376`; served_model `{"object": "list", "data": [{"id": "Ornith-1.5-122B", "object": "model", "created": 179252`; chip `Apple M5 Ultra; 274877906944`; suite_commit `277c842a1481`

### ruler-streams

| streams | prose total (a stream) | code total (a stream) | structured total (a stream) | list total (a stream) | first token |
|---:|---:|---:|---:|---:|---:|
| 1 | 95.7 (95.7) | 95.6 (95.6) | 95.7 (95.7) | 95.6 (95.6) | 0.05-0.07 s |
| 2 | 152.7 (76.4) | 154.7 (77.3) | 154.9 (77.5) | 156.5 (78.3) | 0.08-0.10 s |
| 4 | 232.9 (58.2) | 233.4 (58.4) | 234.1 (58.6) | 240.9 (60.2) | 0.12-0.17 s |

### checks

| check | result |
|---|---|
| memory-idle | measured: mac: System-wide memory free percentage: 66%; total = 4096.00M  us |

## 2026-10-20 15:23: run `20261020-152333-mlx-speed`

Plan mlx-speed, done; served as `Ornith-1.5-122B`.

Serving: engine_commit `30e5dcb4`; binary_sha256 `3e7504db19242321a95555a39a18a51e368405092dbe724d89537d5c14091376`; served_model `{"object": "list", "data": [{"id": "Ornith-1.5-122B", "object": "model", "created": 179252`; chip `Apple M5 Ultra; 274877906944`; suite_commit `277c842a1481`

### ruler-streams

| streams | prose total (a stream) | code total (a stream) | structured total (a stream) | list total (a stream) | first token |
|---:|---:|---:|---:|---:|---:|
| 1 | 93.7 (93.7) | 157.0 (157.0) | 132.9 (132.9) | 149.7 (149.7) | 0.05-0.07 s |
| 2 | 191.5 (95.8) | 274.2 (137.1) | 224.2 (112.1) | 315.2 (157.6) | 0.08-0.11 s |
| 4 | 223.2 (55.2) | 319.2 (80.9) | 282.6 (69.1) | 349.3 (85.7) | 0.13-0.18 s |

### checks

| check | result |
|---|---|
| memory-idle | measured: mac: System-wide memory free percentage: 46%; total = 4096.00M  us |

## 2026-10-20 14:53: run `20261020-145307-dsv41-quality-off`

Plan dsv41-quality-off, done; served as `Ornith-1.5-122B`.

Serving: engine_commit `30e5dcb4`; binary_sha256 `3e7504db19242321a95555a39a18a51e368405092dbe724d89537d5c14091376`; served_model `{"object": "list", "data": [{"id": "Ornith-1.5-122B", "object": "model", "created": 179252`; chip `Apple M5 Ultra; 274877906944`; suite_commit `277c842a1481`

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
| ifeval | 120/150 |
| gsm8k | 245/250 |
| mgsm | 220/240 |
| mmlu | 294/342 |
| math500 | 438/500 |

### checks

| check | result |
|---|---|
| memory-idle | measured: mac: System-wide memory free percentage: 65%; total = 4096.00M  us |

## 2026-10-20 14:29: run `20261020-142950-dsv41-quality-off`

Plan dsv41-quality-off, running; served as `Ornith-1.5-122B`.

Serving: engine_commit `0d37dcb2`; binary_sha256 `3e7504db19242321a95555a39a18a51e368405092dbe724d89537d5c14091376`; served_model `{"object": "list", "data": [{"id": "Ornith-1.5-122B", "object": "model", "created": 179252`; chip `Apple M5 Ultra; 274877906944`; suite_commit `277c842a1481`

### checks

| check | result |
|---|---|
| memory-idle | measured: mac: System-wide memory free percentage: 65%; total = 5120.00M  us |

## 2026-10-20 14:16: run `20261020-141648-mlx-speed`

Plan mlx-speed, done; served as `Ornith-1.5-122B`.

Serving: engine_commit `0d37dcb2`; binary_sha256 `3e7504db19242321a95555a39a18a51e368405092dbe724d89537d5c14091376`; served_model `{"object": "list", "data": [{"id": "Ornith-1.5-122B", "object": "model", "created": 179252`; chip `Apple M5 Ultra; 274877906944`; suite_commit `277c842a1481`

### ruler-streams

| streams | prose total (a stream) | code total (a stream) | structured total (a stream) | list total (a stream) | first token |
|---:|---:|---:|---:|---:|---:|
| 1 | 95.6 (95.6) | 95.4 (95.4) | 95.1 (95.1) | 95.5 (95.5) | 0.05-0.07 s |
| 2 | 152.9 (76.5) | 159.9 (79.9) | 167.7 (83.8) | 156.4 (78.2) | 0.07-0.10 s |
| 4 | 234.0 (58.4) | 240.1 (59.9) | 253.3 (64.7) | 241.6 (60.4) | 0.12-0.17 s |

### checks

| check | result |
|---|---|
| memory-idle | measured: mac: System-wide memory free percentage: 66%; total = 5120.00M  us |

## 2026-10-20 14:15: run `20261020-141514-mlx-speed`

Plan mlx-speed, done; served as `Ornith-1.5-122B`.

Serving: engine_commit `0d37dcb2`; binary_sha256 `3e7504db19242321a95555a39a18a51e368405092dbe724d89537d5c14091376`; served_model `{"object": "list", "data": [{"id": "Ornith-1.5-122B", "object": "model", "created": 179252`; chip `Apple M5 Ultra; 274877906944`; suite_commit `277c842a1481`

### ruler-streams

| streams | prose total (a stream) | code total (a stream) | structured total (a stream) | list total (a stream) | first token |
|---:|---:|---:|---:|---:|---:|
| 1 | 89.7 (89.7) | 314.3 (314.3) | 151.1 (151.1) | 177.6 (177.6) | 0.05-0.07 s |
| 2 | 169.9 (84.9) | 285.0 (142.5) | 246.4 (123.2) | 282.2 (141.1) | 0.08-0.10 s |
| 4 | 204.5 (51.0) | 357.4 (82.8) | 361.4 (85.0) | 389.7 (91.5) | 0.13-0.17 s |

### checks

| check | result |
|---|---|
| memory-idle | measured: mac: System-wide memory free percentage: 66%; total = 5120.00M  us |

## 2026-10-20 14:01: run `20261020-140142-mlx-speed`

Plan mlx-speed, done; served as `Ornith-1.5-122B`.

Serving: engine_commit `e077860c`; binary_sha256 `5866da0e156bce5092010f65f97137b222ed3653bd4e2a8cd98dd9572ee499c2`; served_model `{"object": "list", "data": [{"id": "Ornith-1.5-122B", "object": "model", "created": 179252`; chip `Apple M5 Ultra; 274877906944`; suite_commit `277c842a1481`

### ruler-streams

| streams | prose total (a stream) | code total (a stream) | structured total (a stream) | list total (a stream) | first token |
|---:|---:|---:|---:|---:|---:|
| 1 | 85.2 (85.2) | 85.0 (85.0) | 85.2 (85.2) | 85.2 (85.2) | 0.05-0.07 s |
| 2 | 139.1 (69.6) | 145.1 (72.6) | 151.7 (75.8) | 141.9 (71.0) | 0.07-0.10 s |
| 4 | 218.1 (54.4) | 223.1 (55.9) | 237.5 (60.9) | 226.9 (56.8) | 0.12-0.16 s |

### checks

| check | result |
|---|---|
| memory-idle | measured: mac: System-wide memory free percentage: 66%; total = 5120.00M  us |

## 2026-10-20 14:00: run `20261020-140007-mlx-speed`

Plan mlx-speed, done; served as `Ornith-1.5-122B`.

Serving: engine_commit `e077860c`; binary_sha256 `5866da0e156bce5092010f65f97137b222ed3653bd4e2a8cd98dd9572ee499c2`; served_model `{"object": "list", "data": [{"id": "Ornith-1.5-122B", "object": "model", "created": 179252`; chip `Apple M5 Ultra; 274877906944`; suite_commit `277c842a1481`

### ruler-streams

| streams | prose total (a stream) | code total (a stream) | structured total (a stream) | list total (a stream) | first token |
|---:|---:|---:|---:|---:|---:|
| 1 | 85.5 (85.5) | 316.2 (316.2) | 158.2 (158.2) | 177.4 (177.4) | 0.05-0.07 s |
| 2 | 154.2 (77.1) | 272.2 (136.1) | 239.2 (119.6) | 267.0 (133.5) | 0.08-0.11 s |
| 4 | 205.0 (50.8) | 366.7 (82.1) | 379.7 (86.6) | 382.1 (93.1) | 0.13-0.17 s |

### checks

| check | result |
|---|---|
| memory-idle | measured: mac: System-wide memory free percentage: 65%; total = 5120.00M  us |

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

