# Ornith-1.5-122B, 8-bit MLX affine (g64) on 1x Apple M5 Ultra (256 GB unified), macOS

Target `ornith-15-122b-8bit-native-m5`: Ornith-1.5-122B, the publisher's 8-bit MLX affine, TensorFold native Metal on one M5 Ultra. Engine: TensorFold native, Metal. Rendered from `stats/ornith-15-122b-8bit-native-m5.json` (11 runs); aggregate tok/s, total (a stream).

## 2026-10-31 06:09: run `20261031-060947-mlx-speed`

Plan mlx-speed, done; served as `Ornith-1.5-122B`.

Serving: engine_commit `a410eb56`; binary_sha256 `462b6a0c6d60b2743eb88fdbf0db93a560155a8cf3919ac4f694d1fc9fe156e7`; served_model `{"object": "list", "data": [{"id": "Ornith-1.5-122B", "object": "model", "created": 179344`; chip `Apple M5 Ultra; 274877906944`; suite_commit `21db9b23f7be`

### ruler-streams

| streams | prose total (a stream) | code total (a stream) | structured total (a stream) | list total (a stream) | first token |
|---:|---:|---:|---:|---:|---:|
| 1 | 57.0 (57.0) | 111.1 (111.1) | 90.6 (90.6) | 82.8 (82.8) | 0.08-0.11 s |
| 2 | 116.0 (58.0) | 170.3 (85.2) | 143.4 (71.7) | 199.7 (99.8) | 0.12-0.16 s |
| 4 | 148.1 (37.3) | 231.5 (58.0) | 185.7 (46.9) | 242.8 (62.0) | 0.19-0.27 s |

### checks

| check | result |
|---|---|
| memory-idle | measured: mac: System-wide memory free percentage: 34%; total = 1024.00M  us |

## 2026-10-31 06:03: run `20261031-060351-prefill`

Plan prefill, done; served as `Ornith-1.5-122B`.

Serving: engine_commit `a410eb56`; binary_sha256 `462b6a0c6d60b2743eb88fdbf0db93a560155a8cf3919ac4f694d1fc9fe156e7`; served_model `{"object": "list", "data": [{"id": "Ornith-1.5-122B", "object": "model", "created": 179344`; chip `Apple M5 Ultra; 274877906944`; suite_commit `21db9b23f7be`

### checks

| check | result |
|---|---|
| memory-idle | measured: mac: System-wide memory free percentage: 36%; total = 1024.00M  us |
| prefill-off | measured: 2209 tokens 1685.0 tok/s (1.311 s), 8786 tokens 1730.2 tok/s (5.078 s), 35053 tokens 1463.0 tok/s (23.96 s), 139834 tokens 1003.7 tok/s (139.322 s) |
| prefill-thinking | measured: 2252 tokens 1651.0 tok/s (1.364 s), 8749 tokens 1730.8 tok/s (5.055 s), 35046 tokens 1512.4 tok/s (23.172 s), 139912 tokens 1037.4 tok/s (134.87 s) |
| memory-busy | measured: mac: System-wide memory free percentage: 34%; total = 1024.00M  us |

## 2026-10-31 05:38: run `20261031-053847-glm-vision`

Plan glm-vision, done; served as `Ornith-1.5-122B`.

Serving: engine_commit `078e2247`; binary_sha256 `77350f1c4ffaba29a2faf620a707e3ddd49b2f31442a879f2ccced6eab0f0b98`; served_model `{"object": "list", "data": [{"id": "Ornith-1.5-122B", "object": "model", "created": 179344`; chip `Apple M5 Ultra; 274877906944`; suite_commit `21db9b23f7be`

### suite-vision

| check | passed |
|---|---:|
| vision | 4/6 |
| vision-concurrent | 16/16 |

## 2026-10-31 05:32: run `20261031-053210-prefill`

Plan prefill, done; served as `Ornith-1.5-122B`.

Serving: engine_commit `078e2247`; binary_sha256 `77350f1c4ffaba29a2faf620a707e3ddd49b2f31442a879f2ccced6eab0f0b98`; served_model `{"object": "list", "data": [{"id": "Ornith-1.5-122B", "object": "model", "created": 179344`; chip `Apple M5 Ultra; 274877906944`; suite_commit `21db9b23f7be`

### checks

| check | result |
|---|---|
| memory-idle | measured: mac: System-wide memory free percentage: 35%; total = 1024.00M  us |
| prefill-off | measured: 2231 tokens 1245.0 tok/s (1.792 s), 8751 tokens 1450.8 tok/s (6.032 s), 34940 tokens 1442.7 tok/s (24.219 s), 139630 tokens 988.4 tok/s (141.264 s) |
| prefill-thinking | measured: 2210 tokens 1655.4 tok/s (1.335 s), 8749 tokens 1432.4 tok/s (6.108 s), 35045 tokens 1428.8 tok/s (24.527 s), 139990 tokens 967.5 tok/s (144.693 s) |
| memory-busy | measured: mac: System-wide memory free percentage: 33%; total = 1024.00M  us |

## 2026-10-31 05:29: run `20261031-052945-mlx-speed`

Plan mlx-speed, done; served as `Ornith-1.5-122B`.

Serving: engine_commit `078e2247`; binary_sha256 `77350f1c4ffaba29a2faf620a707e3ddd49b2f31442a879f2ccced6eab0f0b98`; served_model `{"object": "list", "data": [{"id": "Ornith-1.5-122B", "object": "model", "created": 179344`; chip `Apple M5 Ultra; 274877906944`; suite_commit `21db9b23f7be`

### ruler-streams

| streams | prose total (a stream) | code total (a stream) | structured total (a stream) | list total (a stream) | first token |
|---:|---:|---:|---:|---:|---:|
| 1 | 79.5 (79.5) | 138.2 (138.2) | 119.2 (119.2) | 103.6 (103.6) | 0.08-0.11 s |
| 2 | 114.0 (57.0) | 168.7 (84.4) | 139.4 (69.7) | 185.6 (92.8) | 0.12-0.17 s |
| 4 | 145.4 (36.0) | 229.0 (53.2) | 171.6 (44.1) | 216.3 (52.1) | 0.21-0.28 s |

### checks

| check | result |
|---|---|
| memory-idle | measured: mac: System-wide memory free percentage: 26%; total = 1024.00M  us |

## 2026-10-31 05:21: run `20261031-052126-quick`

Plan quick, done; served as `Ornith-1.5-122B`.

Serving: engine_commit `078e2247`; binary_sha256 `77350f1c4ffaba29a2faf620a707e3ddd49b2f31442a879f2ccced6eab0f0b98`; served_model `{"object": "list", "data": [{"id": "Ornith-1.5-122B", "object": "model", "created": 179344`; chip `Apple M5 Ultra; 274877906944`; suite_commit `21db9b23f7be`

### ruler-fresh

| streams | prose total (a stream) | code total (a stream) | structured total (a stream) | list total (a stream) | first token |
|---:|---:|---:|---:|---:|---:|
| 1 | 80.3 (80.3) | 134.3 (134.3) | 115.2 (115.2) | 108.1 (108.1) | 0.09-0.11 s |

### ruler-after

| streams | prose total (a stream) | code total (a stream) | structured total (a stream) | list total (a stream) | first token |
|---:|---:|---:|---:|---:|---:|
| 1 | 79.2 (79.2) | 132.9 (132.9) | 114.4 (114.4) | 107.7 (107.7) | 0.08-0.11 s |

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
| memory-idle | measured: mac: System-wide memory free percentage: 35%; total = 1024.00M  us |
| structured | pass: 18/18 obey, drafted == plain 12/12; a bad regex -> 400 |
| tools | pass: 5/5 tool cases right |
| sampling | pass: 9/9 seeded replies equal on repeat and undrafted; 0 errors |
| turns | pass: resumed == again: True; cold (after a restart): True; cached 5593 of 5610; ttft resumed 0.07s, cold 3.866s |
| urls | pass: public 200; loopback 400; http 400 |

## 2026-10-29 05:00: run `20261029-050046-mlx-speed`

Plan mlx-speed, done; served as `Ornith-1.5-122B`.

Serving: engine_commit `a410eb56`; binary_sha256 `462b6a0c6d60b2743eb88fdbf0db93a560155a8cf3919ac4f694d1fc9fe156e7`; served_model `{"object": "list", "data": [{"id": "Ornith-1.5-122B", "object": "model", "created": 179326`; chip `Apple M5 Ultra; 274877906944`; suite_commit `21db9b23f7be`

### ruler-streams

| streams | prose total (a stream) | code total (a stream) | structured total (a stream) | list total (a stream) | first token |
|---:|---:|---:|---:|---:|---:|
| 1 | 57.3 (57.3) | 112.1 (112.1) | 91.0 (91.0) | 83.7 (83.7) | 0.08-0.11 s |
| 2 | 116.0 (58.0) | 171.5 (85.7) | 146.5 (73.3) | 202.3 (101.1) | 0.13-0.17 s |
| 4 | 153.8 (38.9) | 239.6 (59.8) | 188.4 (46.9) | 247.4 (62.9) | 0.21-0.28 s |

### checks

| check | result |
|---|---|
| memory-idle | measured: mac: System-wide memory free percentage: 34%; total = 2048.00M  us |

## 2026-10-29 02:14: run `20261029-021417-speed`

Plan speed, done; served as `Ornith-1.5-122B`.

Serving: engine_commit `a410eb56`; binary_sha256 `462b6a0c6d60b2743eb88fdbf0db93a560155a8cf3919ac4f694d1fc9fe156e7`; served_model `{"object": "list", "data": [{"id": "Ornith-1.5-122B", "object": "model", "created": 179325`; chip `Apple M5 Ultra; 274877906944`; suite_commit `21db9b23f7be`

### ruler-fresh

| streams | prose total (a stream) | code total (a stream) | structured total (a stream) | list total (a stream) | first token |
|---:|---:|---:|---:|---:|---:|
| 1 | 57.4 (57.4) | 111.7 (111.7) | 91.0 (91.0) | 83.0 (83.0) | 0.08-0.11 s |
| 2 | 117.1 (58.6) | 172.0 (86.0) | 148.9 (74.4) | 204.0 (102.0) | 0.13-0.17 s |

### ruler-after

| streams | prose total (a stream) | code total (a stream) | structured total (a stream) | list total (a stream) | first token |
|---:|---:|---:|---:|---:|---:|
| 1 | 57.6 (57.6) | 112.2 (112.2) | 91.4 (91.4) | 83.7 (83.7) | 0.08-0.11 s |

### checks

| check | result |
|---|---|
| memory-idle | measured: mac: System-wide memory free percentage: 35%; total = 2048.00M  us |
| turns | pass: resumed == again: True; cold (after a restart): True; cached 5592 of 5610; ttft resumed 0.095s, cold 3.872s |
| memory-busy | measured: mac: System-wide memory free percentage: 35%; total = 2048.00M  us |

## 2026-10-29 02:00: run `20261029-020057-prefill`

Plan prefill, done; served as `Ornith-1.5-122B`.

Serving: engine_commit `a410eb56`; binary_sha256 `462b6a0c6d60b2743eb88fdbf0db93a560155a8cf3919ac4f694d1fc9fe156e7`; served_model `{"object": "list", "data": [{"id": "Ornith-1.5-122B", "object": "model", "created": 179325`; chip `Apple M5 Ultra; 274877906944`; suite_commit `21db9b23f7be`

### checks

| check | result |
|---|---|
| memory-idle | measured: mac: System-wide memory free percentage: 35%; total = 2048.00M  us |
| prefill-off | measured: 2217 tokens 1642.2 tok/s (1.35 s), 8788 tokens 1727.9 tok/s (5.086 s), 34927 tokens 1572.6 tok/s (22.21 s), 139834 tokens 1078.1 tok/s (129.7 s) |
| prefill-thinking | measured: 2206 tokens 1640.1 tok/s (1.345 s), 8768 tokens 1726.3 tok/s (5.079 s), 35050 tokens 1560.4 tok/s (22.462 s), 139777 tokens 1051.4 tok/s (132.941 s) |
| memory-busy | measured: mac: System-wide memory free percentage: 34%; total = 2048.00M  us |

## 2026-10-29 02:00: run `20261029-020027-glm-vision`

Plan glm-vision, done; served as `Ornith-1.5-122B`.

Serving: engine_commit `a410eb56`; binary_sha256 `462b6a0c6d60b2743eb88fdbf0db93a560155a8cf3919ac4f694d1fc9fe156e7`; served_model `{"object": "list", "data": [{"id": "Ornith-1.5-122B", "object": "model", "created": 179325`; chip `Apple M5 Ultra; 274877906944`; suite_commit `21db9b23f7be`

### suite-vision

| check | passed |
|---|---:|
| vision | 4/6 |
| vision-concurrent | 16/16 |

## 2026-10-29 01:52: run `20261029-015221-quick`

Plan quick, done; served as `Ornith-1.5-122B`.

Serving: engine_commit `a410eb56`; binary_sha256 `462b6a0c6d60b2743eb88fdbf0db93a560155a8cf3919ac4f694d1fc9fe156e7`; served_model `{"object": "list", "data": [{"id": "Ornith-1.5-122B", "object": "model", "created": 179325`; chip `Apple M5 Ultra; 274877906944`; suite_commit `21db9b23f7be`

### ruler-fresh

| streams | prose total (a stream) | code total (a stream) | structured total (a stream) | list total (a stream) | first token |
|---:|---:|---:|---:|---:|---:|
| 1 | 57.8 (57.8) | 112.5 (112.5) | 91.6 (91.6) | 83.9 (83.9) | 0.08-0.11 s |

### ruler-after

| streams | prose total (a stream) | code total (a stream) | structured total (a stream) | list total (a stream) | first token |
|---:|---:|---:|---:|---:|---:|
| 1 | 57.4 (57.4) | 112.3 (112.3) | 91.5 (91.5) | 83.7 (83.7) | 0.08-0.11 s |

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
| memory-idle | measured: mac: System-wide memory free percentage: 36%; total = 2048.00M  us |
| structured | pass: 18/18 obey, drafted == plain 12/12; a bad regex -> 400 |
| tools | pass: 5/5 tool cases right |
| sampling | pass: 9/9 seeded replies equal on repeat and undrafted; 0 errors |
| turns | pass: resumed == again: True; cold (after a restart): True; cached 5592 of 5610; ttft resumed 0.086s, cold 3.864s |
| urls | FAIL: public 400; loopback 400; http 400; unexpected: ['public'] |

