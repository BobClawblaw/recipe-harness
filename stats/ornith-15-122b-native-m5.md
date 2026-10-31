# Ornith-1.5-122B, 4-bit MLX affine (g64) on 1x Apple M5 Ultra (256 GB unified), macOS

Target `ornith-15-122b-native-m5`: Ornith-1.5-122B, 4-bit MLX affine, TensorFold native Metal on one M5 Ultra. Engine: TensorFold native, Metal. Rendered from `stats/ornith-15-122b-native-m5.json` (66 runs); aggregate tok/s, total (a stream).

## 2026-10-31 04:51: run `20261031-045144-quick`

Plan quick, done; served as `Ornith-1.5-122B`.

Serving: engine_commit `a410eb56`; binary_sha256 `462b6a0c6d60b2743eb88fdbf0db93a560155a8cf3919ac4f694d1fc9fe156e7`; served_model `{"object": "list", "data": [{"id": "Ornith-1.5-122B", "object": "model", "created": 179344`; chip `Apple M5 Ultra; 274877906944`; suite_commit `21db9b23f7be`

### ruler-fresh

| streams | prose total (a stream) | code total (a stream) | structured total (a stream) | list total (a stream) | first token |
|---:|---:|---:|---:|---:|---:|
| 1 | 94.0 (94.0) | 157.7 (157.7) | 133.3 (133.3) | 150.0 (150.0) | 0.05-0.07 s |

### ruler-after

| streams | prose total (a stream) | code total (a stream) | structured total (a stream) | list total (a stream) | first token |
|---:|---:|---:|---:|---:|---:|
| 1 | 93.8 (93.8) | 157.2 (157.2) | 132.9 (132.9) | 149.6 (149.6) | 0.05-0.07 s |

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
| memory-idle | measured: mac: System-wide memory free percentage: 59%; total = 0.00M  used |
| structured | pass: 18/18 obey, drafted == plain 12/12; a bad regex -> 400 |
| tools | FAIL: 4/5 tool cases right; failed named/thinking (calls ['book_flight', 'book_flight']) |
| sampling | pass: 9/9 seeded replies equal on repeat and undrafted; 0 errors |
| turns | pass: resumed == again: True; cold (after a restart): True; cached 5624 of 5643; ttft resumed 0.067s, cold 2.64s |
| urls | pass: public 200; loopback 400; http 400 |

## 2026-10-31 04:49: run `20261031-044951-glm-vision`

Plan glm-vision, done; served as `Ornith-1.5-122B`.

Serving: engine_commit `078e2247`; binary_sha256 `77350f1c4ffaba29a2faf620a707e3ddd49b2f31442a879f2ccced6eab0f0b98`; served_model `{"object": "list", "data": [{"id": "Ornith-1.5-122B", "object": "model", "created": 179344`; chip `Apple M5 Ultra; 274877906944`; suite_commit `21db9b23f7be`

### suite-vision

| check | passed |
|---|---:|
| vision | 4/6 |
| vision-concurrent | 16/16 |

## 2026-10-31 04:44: run `20261031-044438-quick`

Plan quick, done; served as `Ornith-1.5-122B`.

Serving: engine_commit `078e2247`; binary_sha256 `77350f1c4ffaba29a2faf620a707e3ddd49b2f31442a879f2ccced6eab0f0b98`; served_model `{"object": "list", "data": [{"id": "Ornith-1.5-122B", "object": "model", "created": 179343`; chip `Apple M5 Ultra; 274877906944`; suite_commit `21db9b23f7be`

### ruler-fresh

| streams | prose total (a stream) | code total (a stream) | structured total (a stream) | list total (a stream) | first token |
|---:|---:|---:|---:|---:|---:|
| 1 | 132.5 (132.5) | 189.6 (189.6) | 164.7 (164.7) | 198.7 (198.7) | 0.06-0.07 s |

### ruler-after

| streams | prose total (a stream) | code total (a stream) | structured total (a stream) | list total (a stream) | first token |
|---:|---:|---:|---:|---:|---:|
| 1 | 132.1 (132.1) | 190.3 (190.3) | 163.3 (163.3) | 197.3 (197.3) | 0.05-0.07 s |

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
| memory-idle | measured: mac: System-wide memory free percentage: 59%; total = 0.00M  used |
| structured | pass: 18/18 obey, drafted == plain 12/12; a bad regex -> 400 |
| tools | FAIL: 4/5 tool cases right; failed named/thinking (calls ['book_flight', 'book_flight']) |
| sampling | pass: 9/9 seeded replies equal on repeat and undrafted; 0 errors |
| turns | pass: resumed == again: True; cold (after a restart): True; cached 5625 of 5643; ttft resumed 0.066s, cold 2.652s |
| urls | FAIL: public 400; loopback 400; http 400; unexpected: ['public'] |

## 2026-10-30 07:45: run `20261030-074547-glm-vision`

Plan glm-vision, done; served as `Ornith-1.5-122B`.

Serving: engine_commit `a410eb56`; binary_sha256 `462b6a0c6d60b2743eb88fdbf0db93a560155a8cf3919ac4f694d1fc9fe156e7`; served_model `{"object": "list", "data": [{"id": "Ornith-1.5-122B", "object": "model", "created": 179336`; chip `Apple M5 Ultra; 274877906944`; suite_commit `21db9b23f7be`

### suite-vision

| check | passed |
|---|---:|
| vision | 4/6 |
| vision-concurrent | 16/16 |

## 2026-10-30 07:41: run `20261030-074104-quick`

Plan quick, done; served as `Ornith-1.5-122B`.

Serving: engine_commit `a410eb56`; binary_sha256 `462b6a0c6d60b2743eb88fdbf0db93a560155a8cf3919ac4f694d1fc9fe156e7`; served_model `{"object": "list", "data": [{"id": "Ornith-1.5-122B", "object": "model", "created": 179336`; chip `Apple M5 Ultra; 274877906944`; suite_commit `21db9b23f7be`

### ruler-fresh

| streams | prose total (a stream) | code total (a stream) | structured total (a stream) | list total (a stream) | first token |
|---:|---:|---:|---:|---:|---:|
| 1 | 93.6 (93.6) | 157.1 (157.1) | 132.7 (132.7) | 149.3 (149.3) | 0.05-0.07 s |

### ruler-after

| streams | prose total (a stream) | code total (a stream) | structured total (a stream) | list total (a stream) | first token |
|---:|---:|---:|---:|---:|---:|
| 1 | 92.7 (92.7) | 155.2 (155.2) | 132.5 (132.5) | 149.1 (149.1) | 0.05-0.07 s |

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
| memory-idle | measured: mac: System-wide memory free percentage: 58%; total = 4096.00M  us |
| structured | pass: 18/18 obey, drafted == plain 12/12; a bad regex -> 400 |
| tools | FAIL: 4/5 tool cases right; failed named/thinking (calls ['book_flight', 'book_flight']) |
| sampling | pass: 9/9 seeded replies equal on repeat and undrafted; 0 errors |
| turns | pass: resumed == again: True; cold (padded): True; cached 5624 of 5643; ttft resumed 0.067s, cold 0.059s |
| urls | FAIL: public 400; loopback 400; http 400; unexpected: ['public'] |

## 2026-10-29 05:00: run `20261029-050010-glm-vision`

Plan glm-vision, done; served as `Ornith-1.5-122B`.

Serving: engine_commit `a410eb56`; binary_sha256 `462b6a0c6d60b2743eb88fdbf0db93a560155a8cf3919ac4f694d1fc9fe156e7`; served_model `{"object": "list", "data": [{"id": "Ornith-1.5-122B", "object": "model", "created": 179326`; chip `Apple M5 Ultra; 274877906944`; suite_commit `21db9b23f7be`

### suite-vision

| check | passed |
|---|---:|
| vision | 4/6 |
| vision-concurrent | 16/16 |

## 2026-10-29 04:55: run `20261029-045545-prefill`

Plan prefill, done; served as `Ornith-1.5-122B`.

Serving: engine_commit `a410eb56`; binary_sha256 `462b6a0c6d60b2743eb88fdbf0db93a560155a8cf3919ac4f694d1fc9fe156e7`; served_model `{"object": "list", "data": [{"id": "Ornith-1.5-122B", "object": "model", "created": 179326`; chip `Apple M5 Ultra; 274877906944`; suite_commit `21db9b23f7be`

### checks

| check | result |
|---|---|
| memory-idle | measured: mac: System-wide memory free percentage: 58%; total = 2048.00M  us |
| prefill-off | measured: 2233 tokens 2432.5 tok/s (0.918 s), 8782 tokens 2477.3 tok/s (3.545 s), 35063 tokens 2151.9 tok/s (16.294 s), 139919 tokens 1328.4 tok/s (105.331 s) |
| prefill-thinking | measured: 2211 tokens 2195.6 tok/s (1.007 s), 8750 tokens 2465.5 tok/s (3.549 s), 34964 tokens 2146.7 tok/s (16.287 s), 139826 tokens 1324.8 tok/s (105.546 s) |
| memory-busy | measured: mac: System-wide memory free percentage: 56%; total = 2048.00M  us |

## 2026-10-29 04:54: run `20261029-045414-mlx-speed`

Plan mlx-speed, done; served as `Ornith-1.5-122B`.

Serving: engine_commit `a410eb56`; binary_sha256 `462b6a0c6d60b2743eb88fdbf0db93a560155a8cf3919ac4f694d1fc9fe156e7`; served_model `{"object": "list", "data": [{"id": "Ornith-1.5-122B", "object": "model", "created": 179326`; chip `Apple M5 Ultra; 274877906944`; suite_commit `21db9b23f7be`

### ruler-streams

| streams | prose total (a stream) | code total (a stream) | structured total (a stream) | list total (a stream) | first token |
|---:|---:|---:|---:|---:|---:|
| 1 | 93.2 (93.2) | 155.9 (155.9) | 132.6 (132.6) | 149.2 (149.2) | 0.05-0.07 s |
| 2 | 192.5 (96.3) | 265.6 (132.8) | 220.5 (110.2) | 298.3 (149.2) | 0.09-0.15 s |
| 4 | 230.2 (57.0) | 315.0 (79.2) | 280.3 (70.3) | 349.3 (86.2) | 0.13-0.17 s |

### checks

| check | result |
|---|---|
| memory-idle | measured: mac: System-wide memory free percentage: 48%; total = 2048.00M  us |

## 2026-10-29 04:49: run `20261029-044908-quick`

Plan quick, done; served as `Ornith-1.5-122B`.

Serving: engine_commit `a410eb56`; binary_sha256 `462b6a0c6d60b2743eb88fdbf0db93a560155a8cf3919ac4f694d1fc9fe156e7`; served_model `{"object": "list", "data": [{"id": "Ornith-1.5-122B", "object": "model", "created": 179326`; chip `Apple M5 Ultra; 274877906944`; suite_commit `21db9b23f7be`

### ruler-fresh

| streams | prose total (a stream) | code total (a stream) | structured total (a stream) | list total (a stream) | first token |
|---:|---:|---:|---:|---:|---:|
| 1 | 94.2 (94.2) | 158.0 (158.0) | 133.5 (133.5) | 150.3 (150.3) | 0.05-0.07 s |

### ruler-after

| streams | prose total (a stream) | code total (a stream) | structured total (a stream) | list total (a stream) | first token |
|---:|---:|---:|---:|---:|---:|
| 1 | 94.0 (94.0) | 157.7 (157.7) | 133.2 (133.2) | 150.2 (150.2) | 0.05-0.07 s |

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
| memory-idle | measured: mac: System-wide memory free percentage: 59%; total = 2048.00M  us |
| structured | pass: 18/18 obey, drafted == plain 12/12; a bad regex -> 400 |
| tools | FAIL: 4/5 tool cases right; failed named/thinking (calls ['book_flight', 'book_flight']) |
| sampling | pass: 9/9 seeded replies equal on repeat and undrafted; 0 errors |
| turns | pass: resumed == again: True; cold (after a restart): True; cached 5624 of 5643; ttft resumed 0.067s, cold 2.635s |
| urls | FAIL: public 400; loopback 400; http 400; unexpected: ['public'] |

## 2026-10-26 13:27: run `20261026-132723-glm-vision`

Plan glm-vision, done; served as `Ornith-1.5-122B`.

Serving: engine_commit `6e841053`; binary_sha256 `fce62b559adc7b4d1edf158767240f3e6f76fcf2681d5c308aa9f6ce8d659d3f`; served_model `{"object": "list", "data": [{"id": "Ornith-1.5-122B", "object": "model", "created": 179303`; chip `Apple M5 Ultra; 274877906944`; suite_commit `a7ba7e392d57`

### suite-vision

| check | passed |
|---|---:|
| vision | 4/6 |
| vision-concurrent | 0/0 |

## 2026-10-26 13:19: run `20261026-131919-glm-vision`

Plan glm-vision, done; served as `Ornith-1.5-122B`.

Serving: engine_commit `6e841053`; binary_sha256 `fce62b559adc7b4d1edf158767240f3e6f76fcf2681d5c308aa9f6ce8d659d3f`; served_model `{"object": "list", "data": [{"id": "Ornith-1.5-122B", "object": "model", "created": 179303`; chip `Apple M5 Ultra; 274877906944`; suite_commit `a7ba7e392d57`

### suite-vision

| check | passed |
|---|---:|
| vision | 4/4 |
| vision-concurrent | 16/16 |

## 2026-10-26 13:09: run `20261026-130938-thinking`

Plan thinking, done; served as `Ornith-1.5-122B`.

Serving: engine_commit `6e841053`; binary_sha256 `fce62b559adc7b4d1edf158767240f3e6f76fcf2681d5c308aa9f6ce8d659d3f`; served_model `{"object": "list", "data": [{"id": "Ornith-1.5-122B", "object": "model", "created": 179303`; chip `Apple M5 Ultra; 274877906944`; suite_commit `277c842a1481-dirty`

### suite-thinking

| check | passed |
|---|---:|
| gsm8k | 244/250 |

### checks

| check | result |
|---|---|
| thinking | pass: thinking on: 10/10 right, 10/10 with reasoning_content, 0 leaks, 0 errors, 0 cut at 50176 tokens |

## 2026-10-26 12:54: run `20261026-125443-prefill`

Plan prefill, done; served as `Ornith-1.5-122B`.

Serving: engine_commit `6e841053`; binary_sha256 `fce62b559adc7b4d1edf158767240f3e6f76fcf2681d5c308aa9f6ce8d659d3f`; served_model `{"object": "list", "data": [{"id": "Ornith-1.5-122B", "object": "model", "created": 179303`; chip `Apple M5 Ultra; 274877906944`; suite_commit `277c842a1481`

### checks

| check | result |
|---|---|
| memory-idle | measured: mac: System-wide memory free percentage: 40%; total = 5120.00M  us |
| prefill-off | measured: 2208 tokens 2506.2 tok/s (0.881 s), 8799 tokens 2486.3 tok/s (3.539 s), 34991 tokens 2164.6 tok/s (16.165 s), 139556 tokens 1338.7 tok/s (104.25 s) |
| prefill-thinking | measured: 2229 tokens 2178.9 tok/s (1.023 s), 8755 tokens 2468.3 tok/s (3.547 s), 35010 tokens 2155.9 tok/s (16.239 s), 139767 tokens 1333.6 tok/s (104.804 s) |
| memory-busy | measured: mac: System-wide memory free percentage: 40%; total = 5120.00M  us |

## 2026-10-26 12:53: run `20261026-125312-mlx-speed`

Plan mlx-speed, done; served as `Ornith-1.5-122B`.

Serving: engine_commit `6e841053`; binary_sha256 `fce62b559adc7b4d1edf158767240f3e6f76fcf2681d5c308aa9f6ce8d659d3f`; served_model `{"object": "list", "data": [{"id": "Ornith-1.5-122B", "object": "model", "created": 179303`; chip `Apple M5 Ultra; 274877906944`; suite_commit `277c842a1481`

### ruler-streams

| streams | prose total (a stream) | code total (a stream) | structured total (a stream) | list total (a stream) | first token |
|---:|---:|---:|---:|---:|---:|
| 1 | 93.8 (93.8) | 157.5 (157.5) | 132.8 (132.8) | 149.5 (149.5) | 0.05-0.07 s |
| 2 | 195.3 (97.6) | 267.3 (133.6) | 236.0 (118.0) | 318.0 (159.0) | 0.08-0.11 s |
| 4 | 234.0 (57.6) | 317.6 (79.4) | 286.2 (71.6) | 369.6 (89.4) | 0.13-0.17 s |

### checks

| check | result |
|---|---|
| memory-idle | measured: mac: System-wide memory free percentage: 39%; total = 5120.00M  us |

## 2026-10-26 12:48: run `20261026-124829-quick`

Plan quick, done; served as `Ornith-1.5-122B`.

Serving: engine_commit `6e841053`; binary_sha256 `fce62b559adc7b4d1edf158767240f3e6f76fcf2681d5c308aa9f6ce8d659d3f`; served_model `{"object": "list", "data": [{"id": "Ornith-1.5-122B", "object": "model", "created": 179303`; chip `Apple M5 Ultra; 274877906944`; suite_commit `277c842a1481`

### ruler-fresh

| streams | prose total (a stream) | code total (a stream) | structured total (a stream) | list total (a stream) | first token |
|---:|---:|---:|---:|---:|---:|
| 1 | 93.8 (93.8) | 157.4 (157.4) | 133.0 (133.0) | 149.8 (149.8) | 0.05-0.07 s |

### ruler-after

| streams | prose total (a stream) | code total (a stream) | structured total (a stream) | list total (a stream) | first token |
|---:|---:|---:|---:|---:|---:|
| 1 | 93.8 (93.8) | 157.5 (157.5) | 133.1 (133.1) | 149.8 (149.8) | 0.05-0.07 s |

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
| memory-idle | measured: mac: System-wide memory free percentage: 59%; total = 5120.00M  us |
| structured | pass: 18/18 obey, drafted == plain 12/12; a bad regex -> 400 |
| tools | FAIL: 4/5 tool cases right; failed named/thinking (calls ['book_flight', 'book_flight']) |
| sampling | pass: 9/9 seeded replies equal on repeat and undrafted; 0 errors |
| turns | pass: resumed == again: True; cold (padded): True; cached 5624 of 5643; ttft resumed 0.067s, cold 0.059s |
| urls | FAIL: public 400; loopback 400; http 400; unexpected: ['public'] |

## 2026-10-26 12:31: run `20261026-123146-prefill`

Plan prefill, done; served as `Ornith-1.5-122B`.

Serving: engine_commit `8aeabea0`; binary_sha256 `bfbce86bf5a12ae5726af95abb8d5544b6e804be0cf0dfa6c5e31fb33658c8c9`; served_model `{"object": "list", "data": [{"id": "Ornith-1.5-122B", "object": "model", "created": 179303`; chip `Apple M5 Ultra; 274877906944`; suite_commit `277c842a1481`

### checks

| check | result |
|---|---|
| memory-idle | measured: mac: System-wide memory free percentage: 39%; total = 5120.00M  us |
| prefill-off | measured: 2210 tokens 2514.2 tok/s (0.879 s), 8772 tokens 2483.6 tok/s (3.532 s), 35011 tokens 2164.1 tok/s (16.178 s), 139759 tokens 1335.9 tok/s (104.617 s) |
| prefill-thinking | measured: 2238 tokens 2158.1 tok/s (1.037 s), 8782 tokens 2459.3 tok/s (3.571 s), 35044 tokens 2146.0 tok/s (16.33 s), 139961 tokens 1321.6 tok/s (105.906 s) |
| memory-busy | measured: mac: System-wide memory free percentage: 47%; total = 5120.00M  us |

## 2026-10-26 12:30: run `20261026-123015-mlx-speed`

Plan mlx-speed, done; served as `Ornith-1.5-122B`.

Serving: engine_commit `8aeabea0`; binary_sha256 `bfbce86bf5a12ae5726af95abb8d5544b6e804be0cf0dfa6c5e31fb33658c8c9`; served_model `{"object": "list", "data": [{"id": "Ornith-1.5-122B", "object": "model", "created": 179303`; chip `Apple M5 Ultra; 274877906944`; suite_commit `277c842a1481`

### ruler-streams

| streams | prose total (a stream) | code total (a stream) | structured total (a stream) | list total (a stream) | first token |
|---:|---:|---:|---:|---:|---:|
| 1 | 93.9 (93.9) | 157.5 (157.5) | 133.1 (133.1) | 149.2 (149.2) | 0.05-0.07 s |
| 2 | 193.2 (96.6) | 276.7 (138.3) | 235.9 (118.0) | 306.2 (153.1) | 0.08-0.11 s |
| 4 | 234.0 (58.1) | 316.7 (79.2) | 284.1 (71.1) | 354.1 (85.5) | 0.13-0.17 s |

### checks

| check | result |
|---|---|
| memory-idle | measured: mac: System-wide memory free percentage: 49%; total = 5120.00M  us |

## 2026-10-26 12:25: run `20261026-122532-quick`

Plan quick, done; served as `Ornith-1.5-122B`.

Serving: engine_commit `8aeabea0`; binary_sha256 `bfbce86bf5a12ae5726af95abb8d5544b6e804be0cf0dfa6c5e31fb33658c8c9`; served_model `{"object": "list", "data": [{"id": "Ornith-1.5-122B", "object": "model", "created": 179303`; chip `Apple M5 Ultra; 274877906944`; suite_commit `277c842a1481`

### ruler-fresh

| streams | prose total (a stream) | code total (a stream) | structured total (a stream) | list total (a stream) | first token |
|---:|---:|---:|---:|---:|---:|
| 1 | 93.8 (93.8) | 157.1 (157.1) | 132.4 (132.4) | 149.1 (149.1) | 0.05-0.07 s |

### ruler-after

| streams | prose total (a stream) | code total (a stream) | structured total (a stream) | list total (a stream) | first token |
|---:|---:|---:|---:|---:|---:|
| 1 | 93.2 (93.2) | 157.0 (157.0) | 132.6 (132.6) | 149.5 (149.5) | 0.05-0.07 s |

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
| memory-idle | measured: mac: System-wide memory free percentage: 57%; total = 5120.00M  us |
| structured | pass: 18/18 obey, drafted == plain 12/12; a bad regex -> 400 |
| tools | FAIL: 4/5 tool cases right; failed named/thinking (calls ['book_flight', 'book_flight']) |
| sampling | pass: 9/9 seeded replies equal on repeat and undrafted; 0 errors |
| turns | pass: resumed == again: True; cold (padded): True; cached 5624 of 5643; ttft resumed 0.067s, cold 0.059s |
| urls | FAIL: public 400; loopback 400; http 400; unexpected: ['public'] |

## 2026-10-26 11:16: run `20261026-111607-quick`

Plan quick, done; served as `Ornith-1.5-122B`.

Serving: engine_commit `aa472b6d`; binary_sha256 `8eb45a8cf11ea8e120af8fdd8e48bdd2ce973545026bbef778de57916cec7522`; served_model `{"object": "list", "data": [{"id": "Ornith-1.5-122B", "object": "model", "created": 179303`; chip `Apple M5 Ultra; 274877906944`; suite_commit `277c842a1481`

### ruler-fresh

| streams | prose total (a stream) | code total (a stream) | structured total (a stream) | list total (a stream) | first token |
|---:|---:|---:|---:|---:|---:|
| 1 | 93.5 (93.5) | 157.0 (157.0) | 132.8 (132.8) | 149.2 (149.2) | 0.05-0.07 s |

### ruler-after

| streams | prose total (a stream) | code total (a stream) | structured total (a stream) | list total (a stream) | first token |
|---:|---:|---:|---:|---:|---:|
| 1 | 93.7 (93.7) | 157.1 (157.1) | 132.5 (132.5) | 149.2 (149.2) | 0.05-0.07 s |

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
| memory-idle | measured: mac: System-wide memory free percentage: 59%; total = 4096.00M  us |
| structured | pass: 18/18 obey, drafted == plain 12/12; a bad regex -> 400 |
| tools | FAIL: 4/5 tool cases right; failed named/thinking (calls ['book_flight', 'book_flight']) |
| sampling | pass: 9/9 seeded replies equal on repeat and undrafted; 0 errors |
| turns | pass: resumed == again: True; cold (padded): True; cached 5624 of 5643; ttft resumed 0.068s, cold 0.059s |
| urls | FAIL: public 400; loopback 400; http 400; unexpected: ['public'] |

## 2026-10-26 11:04: run `20261026-110423-thinking`

Plan thinking, done; served as `Ornith-1.5-122B`.

Serving: engine_commit `aa472b6d`; binary_sha256 `d8c410ee9547a1cabb211f2169003e3a46b0f2ff75576753d12c90a6c4eec40b`; served_model `{"object": "list", "data": [{"id": "Ornith-1.5-122B", "object": "model", "created": 179303`; chip `Apple M5 Ultra; 274877906944`; suite_commit `291734b3cf5a`

### suite-thinking

| check | passed |
|---|---:|
| gsm8k | 244/250 |

### checks

| check | result |
|---|---|
| thinking | pass: thinking on: 10/10 right, 10/10 with reasoning_content, 0 leaks, 0 errors, 0 cut at 50176 tokens |

## 2026-10-26 11:02: run `20261026-110250-thinking`

Plan thinking, done; served as `Ornith-1.5-122B`.

Serving: engine_commit `aa472b6d`; binary_sha256 `d8c410ee9547a1cabb211f2169003e3a46b0f2ff75576753d12c90a6c4eec40b`; served_model `{"object": "list", "data": [{"id": "Ornith-1.5-122B", "object": "model", "created": 179303`; chip `Apple M5 Ultra; 274877906944`; suite_commit `277c842a1481`

### checks

| check | result |
|---|---|
| thinking | pass: thinking on: 10/10 right, 10/10 with reasoning_content, 0 leaks, 0 errors, 0 cut at 50176 tokens |

## 2026-10-26 10:33: run `20261026-103314-dsv41-quality-off`

Plan dsv41-quality-off, done; served as `Ornith-1.5-122B`.

Serving: engine_commit `aa472b6d`; binary_sha256 `d8c410ee9547a1cabb211f2169003e3a46b0f2ff75576753d12c90a6c4eec40b`; served_model `{"object": "list", "data": [{"id": "Ornith-1.5-122B", "object": "model", "created": 179302`; chip `Apple M5 Ultra; 274877906944`; suite_commit `277c842a1481`

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
| mmlu | 298/342 |
| math500 | 438/500 |

### checks

| check | result |
|---|---|
| memory-idle | measured: mac: System-wide memory free percentage: 59%; total = 4096.00M  us |

## 2026-10-26 08:43: run `20261026-084338-prefill`

Plan prefill, done; served as `Ornith-1.5-122B`.

Serving: engine_commit `aa472b6d`; binary_sha256 `d8c410ee9547a1cabb211f2169003e3a46b0f2ff75576753d12c90a6c4eec40b`; served_model `{"object": "list", "data": [{"id": "Ornith-1.5-122B", "object": "model", "created": 179302`; chip `Apple M5 Ultra; 274877906944`; suite_commit `277c842a1481`

### checks

| check | result |
|---|---|
| memory-idle | measured: mac: System-wide memory free percentage: 40%; total = 4096.00M  us |
| prefill-off | measured: 2214 tokens 2498.9 tok/s (0.886 s), 8802 tokens 2482.2 tok/s (3.546 s), 35029 tokens 2158.6 tok/s (16.228 s), 139877 tokens 1334.3 tok/s (104.831 s) |
| prefill-thinking | measured: 2203 tokens 2157.7 tok/s (1.021 s), 8756 tokens 2462.3 tok/s (3.556 s), 34992 tokens 2131.7 tok/s (16.415 s), 139747 tokens 1332.9 tok/s (104.848 s) |
| memory-busy | measured: mac: System-wide memory free percentage: 42%; total = 4096.00M  us |

## 2026-10-26 08:42: run `20261026-084207-mlx-speed`

Plan mlx-speed, done; served as `Ornith-1.5-122B`.

Serving: engine_commit `aa472b6d`; binary_sha256 `d8c410ee9547a1cabb211f2169003e3a46b0f2ff75576753d12c90a6c4eec40b`; served_model `{"object": "list", "data": [{"id": "Ornith-1.5-122B", "object": "model", "created": 179302`; chip `Apple M5 Ultra; 274877906944`; suite_commit `277c842a1481`

### ruler-streams

| streams | prose total (a stream) | code total (a stream) | structured total (a stream) | list total (a stream) | first token |
|---:|---:|---:|---:|---:|---:|
| 1 | 94.1 (94.1) | 157.7 (157.7) | 132.9 (132.9) | 149.8 (149.8) | 0.05-0.07 s |
| 2 | 191.6 (95.8) | 263.2 (131.6) | 230.7 (115.3) | 317.3 (158.7) | 0.08-0.11 s |
| 4 | 232.4 (57.8) | 314.0 (78.6) | 290.5 (71.4) | 349.5 (85.1) | 0.13-0.17 s |

### checks

| check | result |
|---|---|
| memory-idle | measured: mac: System-wide memory free percentage: 39%; total = 4096.00M  us |

## 2026-10-26 08:37: run `20261026-083724-quick`

Plan quick, done; served as `Ornith-1.5-122B`.

Serving: engine_commit `aa472b6d`; binary_sha256 `d8c410ee9547a1cabb211f2169003e3a46b0f2ff75576753d12c90a6c4eec40b`; served_model `{"object": "list", "data": [{"id": "Ornith-1.5-122B", "object": "model", "created": 179302`; chip `Apple M5 Ultra; 274877906944`; suite_commit `277c842a1481`

### ruler-fresh

| streams | prose total (a stream) | code total (a stream) | structured total (a stream) | list total (a stream) | first token |
|---:|---:|---:|---:|---:|---:|
| 1 | 93.8 (93.8) | 157.5 (157.5) | 133.2 (133.2) | 150.0 (150.0) | 0.05-0.07 s |

### ruler-after

| streams | prose total (a stream) | code total (a stream) | structured total (a stream) | list total (a stream) | first token |
|---:|---:|---:|---:|---:|---:|
| 1 | 93.9 (93.9) | 157.6 (157.6) | 133.1 (133.1) | 149.3 (149.3) | 0.05-0.07 s |

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
| memory-idle | measured: mac: System-wide memory free percentage: 59%; total = 4096.00M  us |
| structured | pass: 18/18 obey, drafted == plain 12/12; a bad regex -> 400 |
| tools | FAIL: 4/5 tool cases right; failed named/thinking (calls ['book_flight', 'book_flight']) |
| sampling | pass: 9/9 seeded replies equal on repeat and undrafted; 0 errors |
| turns | pass: resumed == again: True; cold (padded): True; cached 5624 of 5643; ttft resumed 0.068s, cold 0.058s |
| urls | FAIL: public 400; loopback 400; http 400; unexpected: ['public'] |

## 2026-10-26 07:51: run `20261026-075154-prefill`

Plan prefill, done; served as `Ornith-1.5-122B`.

Serving: engine_commit `0f033773`; binary_sha256 `c0d214542ba34896cd2a6bc348fa2867af4ab56287b22c210838c361b0b32a65`; served_model `{"object": "list", "data": [{"id": "Ornith-1.5-122B", "object": "model", "created": 179301`; chip `Apple M5 Ultra; 274877906944`; suite_commit `277c842a1481`

### checks

| check | result |
|---|---|
| memory-idle | measured: mac: System-wide memory free percentage: 41%; total = 5120.00M  us |
| prefill-off | measured: 2220 tokens 2528.5 tok/s (0.878 s), 8771 tokens 2487.5 tok/s (3.526 s), 35001 tokens 2169.4 tok/s (16.134 s), 139894 tokens 1339.9 tok/s (104.41 s) |
| prefill-thinking | measured: 2231 tokens 2139.0 tok/s (1.043 s), 8759 tokens 2470.8 tok/s (3.545 s), 34893 tokens 2158.4 tok/s (16.166 s), 139857 tokens 1333.4 tok/s (104.885 s) |
| memory-busy | measured: mac: System-wide memory free percentage: 49%; total = 5120.00M  us |

## 2026-10-26 07:50: run `20261026-075024-mlx-speed`

Plan mlx-speed, done; served as `Ornith-1.5-122B`.

Serving: engine_commit `0f033773`; binary_sha256 `c0d214542ba34896cd2a6bc348fa2867af4ab56287b22c210838c361b0b32a65`; served_model `{"object": "list", "data": [{"id": "Ornith-1.5-122B", "object": "model", "created": 179301`; chip `Apple M5 Ultra; 274877906944`; suite_commit `277c842a1481`

### ruler-streams

| streams | prose total (a stream) | code total (a stream) | structured total (a stream) | list total (a stream) | first token |
|---:|---:|---:|---:|---:|---:|
| 1 | 94.1 (94.1) | 157.7 (157.7) | 133.3 (133.3) | 150.3 (150.3) | 0.05-0.07 s |
| 2 | 193.6 (96.8) | 270.3 (135.2) | 236.3 (118.2) | 317.8 (158.9) | 0.08-0.11 s |
| 4 | 237.3 (58.5) | 317.3 (79.2) | 294.7 (73.8) | 364.0 (89.1) | 0.13-0.17 s |

### checks

| check | result |
|---|---|
| memory-idle | measured: mac: System-wide memory free percentage: 39%; total = 5120.00M  us |

## 2026-10-26 07:45: run `20261026-074542-quick`

Plan quick, done; served as `Ornith-1.5-122B`.

Serving: engine_commit `0f033773`; binary_sha256 `c0d214542ba34896cd2a6bc348fa2867af4ab56287b22c210838c361b0b32a65`; served_model `{"object": "list", "data": [{"id": "Ornith-1.5-122B", "object": "model", "created": 179301`; chip `Apple M5 Ultra; 274877906944`; suite_commit `277c842a1481`

### ruler-fresh

| streams | prose total (a stream) | code total (a stream) | structured total (a stream) | list total (a stream) | first token |
|---:|---:|---:|---:|---:|---:|
| 1 | 94.1 (94.1) | 157.8 (157.8) | 133.4 (133.4) | 150.3 (150.3) | 0.05-0.07 s |

### ruler-after

| streams | prose total (a stream) | code total (a stream) | structured total (a stream) | list total (a stream) | first token |
|---:|---:|---:|---:|---:|---:|
| 1 | 94.1 (94.1) | 157.7 (157.7) | 133.3 (133.3) | 150.1 (150.1) | 0.05-0.07 s |

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
| memory-idle | measured: mac: System-wide memory free percentage: 58%; total = 5120.00M  us |
| structured | pass: 18/18 obey, drafted == plain 12/12; a bad regex -> 400 |
| tools | FAIL: 4/5 tool cases right; failed named/thinking (calls ['book_flight', 'book_flight']) |
| sampling | pass: 9/9 seeded replies equal on repeat and undrafted; 0 errors |
| turns | pass: resumed == again: True; cold (padded): True; cached 5624 of 5643; ttft resumed 0.067s, cold 0.059s |
| urls | FAIL: public 400; loopback 400; http 400; unexpected: ['public'] |

## 2026-10-26 03:37: run `20261026-033758-thinking`

Plan thinking, done; served as `Ornith-1.5-122B`.

Serving: engine_commit `1429b56b`; binary_sha256 `64f5d54183672d8cc018bfb29f8be83b0da65c0e7b9293d9e6dd70203ff87cd5`; served_model `{"object": "list", "data": [{"id": "Ornith-1.5-122B", "object": "model", "created": 179300`; chip `Apple M5 Ultra; 274877906944`; suite_commit `291734b3cf5a`

### suite-thinking

| check | passed |
|---|---:|
| gsm8k | 245/250 |

### checks

| check | result |
|---|---|
| thinking | pass: thinking on: 10/10 right, 10/10 with reasoning_content, 0 leaks, 0 errors, 0 cut at 50176 tokens |

## 2026-10-26 03:08: run `20261026-030806-dsv41-quality-off`

Plan dsv41-quality-off, done; served as `Ornith-1.5-122B`.

Serving: engine_commit `1429b56b`; binary_sha256 `64f5d54183672d8cc018bfb29f8be83b0da65c0e7b9293d9e6dd70203ff87cd5`; served_model `{"object": "list", "data": [{"id": "Ornith-1.5-122B", "object": "model", "created": 179300`; chip `Apple M5 Ultra; 274877906944`; suite_commit `277c842a1481`

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
| ifeval | 114/150 |
| gsm8k | 241/250 |
| mgsm | 212/240 |
| mmlu | 300/342 |
| math500 | 432/500 |

### checks

| check | result |
|---|---|
| memory-idle | measured: mac: System-wide memory free percentage: 30%; total = 6144.00M  us |

## 2026-10-26 03:04: run `20261026-030425-prefill`

Plan prefill, done; served as `Ornith-1.5-122B`.

Serving: engine_commit `1429b56b`; binary_sha256 `64f5d54183672d8cc018bfb29f8be83b0da65c0e7b9293d9e6dd70203ff87cd5`; served_model `{"object": "list", "data": [{"id": "Ornith-1.5-122B", "object": "model", "created": 179300`; chip `Apple M5 Ultra; 274877906944`; suite_commit `277c842a1481`

### checks

| check | result |
|---|---|
| memory-idle | measured: mac: System-wide memory free percentage: 30%; total = 6144.00M  us |
| prefill-off | measured: 2254 tokens 3247.8 tok/s (0.694 s), 8762 tokens 3162.0 tok/s (2.771 s), 35024 tokens 2660.0 tok/s (13.167 s), 139831 tokens 1500.7 tok/s (93.178 s) |
| prefill-thinking | measured: 2207 tokens 2728.1 tok/s (0.809 s), 8797 tokens 3128.4 tok/s (2.812 s), 35011 tokens 2647.9 tok/s (13.222 s), 139782 tokens 1495.3 tok/s (93.479 s) |
| memory-busy | measured: mac: System-wide memory free percentage: 32%; total = 6144.00M  us |

## 2026-10-26 03:02: run `20261026-030256-mlx-speed`

Plan mlx-speed, done; served as `Ornith-1.5-122B`.

Serving: engine_commit `1429b56b`; binary_sha256 `64f5d54183672d8cc018bfb29f8be83b0da65c0e7b9293d9e6dd70203ff87cd5`; served_model `{"object": "list", "data": [{"id": "Ornith-1.5-122B", "object": "model", "created": 179300`; chip `Apple M5 Ultra; 274877906944`; suite_commit `277c842a1481`

### ruler-streams

| streams | prose total (a stream) | code total (a stream) | structured total (a stream) | list total (a stream) | first token |
|---:|---:|---:|---:|---:|---:|
| 1 | 92.8 (92.8) | 171.3 (171.3) | 122.5 (122.5) | 154.7 (154.7) | 0.05-0.07 s |
| 2 | 180.7 (90.3) | 295.5 (147.7) | 229.9 (114.9) | 319.6 (159.8) | 0.08-0.10 s |
| 4 | 215.0 (54.2) | 346.3 (88.9) | 277.7 (69.7) | 360.9 (87.6) | 0.13-0.16 s |

### checks

| check | result |
|---|---|
| memory-idle | measured: mac: System-wide memory free percentage: 30%; total = 6144.00M  us |

## 2026-10-26 02:57: run `20261026-025716-quick`

Plan quick, done; served as `Ornith-1.5-122B`.

Serving: engine_commit `1429b56b`; binary_sha256 `64f5d54183672d8cc018bfb29f8be83b0da65c0e7b9293d9e6dd70203ff87cd5`; served_model `{"object": "list", "data": [{"id": "Ornith-1.5-122B", "object": "model", "created": 179300`; chip `Apple M5 Ultra; 274877906944`; suite_commit `277c842a1481`

### ruler-fresh

| streams | prose total (a stream) | code total (a stream) | structured total (a stream) | list total (a stream) | first token |
|---:|---:|---:|---:|---:|---:|
| 1 | 92.7 (92.7) | 171.0 (171.0) | 122.2 (122.2) | 154.5 (154.5) | 0.05-0.07 s |

### ruler-after

| streams | prose total (a stream) | code total (a stream) | structured total (a stream) | list total (a stream) | first token |
|---:|---:|---:|---:|---:|---:|
| 1 | 92.5 (92.5) | 171.0 (171.0) | 121.8 (121.8) | 153.9 (153.9) | 0.05-0.06 s |

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
| memory-idle | measured: mac: System-wide memory free percentage: 56%; total = 3072.00M  us |
| structured | pass: 18/18 obey, drafted == plain 12/12; a bad regex -> 400 |
| tools | FAIL: 4/5 tool cases right; failed named/thinking (finish length) |
| sampling | pass: 9/9 seeded replies equal on repeat and undrafted; 0 errors |
| turns | pass: resumed == again: True; cold (padded): True; cached 5624 of 5643; ttft resumed 0.065s, cold 0.058s |
| urls | FAIL: public 400; loopback 400; http 400; unexpected: ['public'] |

## 2026-10-26 02:54: run `20261026-025426-quick`

Plan quick, running; served as `Ornith-1.5-122B`.

Serving: engine_commit `1429b56b`; binary_sha256 `64f5d54183672d8cc018bfb29f8be83b0da65c0e7b9293d9e6dd70203ff87cd5`; served_model `{"object": "list", "data": [{"id": "Ornith-1.5-122B", "object": "model", "created": 179300`; chip `Apple M5 Ultra; 274877906944`; suite_commit `277c842a1481`

### ruler-fresh

| streams | prose total (a stream) | code total (a stream) | structured total (a stream) | list total (a stream) | first token |
|---:|---:|---:|---:|---:|---:|
| 1 | 92.2 (92.2) | 169.9 (169.9) | 121.4 (121.4) | 153.6 (153.6) | 0.05-0.07 s |

### ruler-after

| streams | prose total (a stream) | code total (a stream) | structured total (a stream) | list total (a stream) | first token |
|---:|---:|---:|---:|---:|---:|
| 1 | 92.8 (92.8) | 171.2 (171.2) | 122.3 (122.3) | 154.8 (154.8) | 0.05-0.06 s |

### checks

| check | result |
|---|---|
| memory-idle | measured: mac: System-wide memory free percentage: 57%; total = 3072.00M  us |
| structured | pass: 18/18 obey, drafted == plain 12/12; a bad regex -> 400 |
| tools | FAIL: 4/5 tool cases right; failed named/thinking (finish length) |
| sampling | pass: 9/9 seeded replies equal on repeat and undrafted; 0 errors |
| turns | pass: resumed == again: True; cold (padded): True; cached 5624 of 5643; ttft resumed 0.067s, cold 0.058s |
| urls | FAIL: public 400; loopback 400; http 400; unexpected: ['public'] |

## 2026-10-25 22:37: run `20261025-223735-mlx-speed`

Plan mlx-speed, done; served as `Ornith-1.5-122B`.

Serving: engine_commit `1429b56b`; binary_sha256 `64f5d54183672d8cc018bfb29f8be83b0da65c0e7b9293d9e6dd70203ff87cd5`; served_model `{"object": "list", "data": [{"id": "Ornith-1.5-122B", "object": "model", "created": 179298`; chip `Apple M5 Ultra; 274877906944`; suite_commit `277c842a1481`

### ruler-streams

| streams | prose total (a stream) | code total (a stream) | structured total (a stream) | list total (a stream) | first token |
|---:|---:|---:|---:|---:|---:|
| 1 | 93.2 (93.2) | 172.1 (172.1) | 122.8 (122.8) | 155.2 (155.2) | 0.05-0.06 s |
| 2 | 184.3 (92.1) | 289.8 (144.9) | 226.1 (113.1) | 311.2 (155.6) | 0.08-0.10 s |
| 4 | 347.7 (86.0) | 605.6 (159.9) | 451.6 (109.6) | 652.1 (173.4) | 0.73-1.48 s |

### checks

| check | result |
|---|---|
| memory-idle | measured: mac: System-wide memory free percentage: 43%; total = 3072.00M  us |

## 2026-10-25 22:32: run `20261025-223222-quick`

Plan quick, done; served as `Ornith-1.5-122B`.

Serving: engine_commit `1429b56b`; binary_sha256 `64f5d54183672d8cc018bfb29f8be83b0da65c0e7b9293d9e6dd70203ff87cd5`; served_model `{"object": "list", "data": [{"id": "Ornith-1.5-122B", "object": "model", "created": 179298`; chip `Apple M5 Ultra; 274877906944`; suite_commit `277c842a1481`

### ruler-fresh

| streams | prose total (a stream) | code total (a stream) | structured total (a stream) | list total (a stream) | first token |
|---:|---:|---:|---:|---:|---:|
| 1 | 93.1 (93.1) | 171.6 (171.6) | 122.5 (122.5) | 155.2 (155.2) | 0.05-0.06 s |

### ruler-after

| streams | prose total (a stream) | code total (a stream) | structured total (a stream) | list total (a stream) | first token |
|---:|---:|---:|---:|---:|---:|
| 1 | 93.1 (93.1) | 171.7 (171.7) | 122.5 (122.5) | 155.2 (155.2) | 0.05-0.06 s |

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
| memory-idle | measured: mac: System-wide memory free percentage: 58%; total = 3072.00M  us |
| structured | pass: 18/18 obey, drafted == plain 12/12; a bad regex -> 400 |
| tools | FAIL: 4/5 tool cases right; failed named/thinking (finish length) |
| sampling | pass: 9/9 seeded replies equal on repeat and undrafted; 0 errors |
| turns | FAIL: resumed == again: True; cold (after a restart): False; cached 5624 of 5643; ttft resumed 0.065s, cold 2.126s |
| urls | FAIL: public 400; loopback 400; http 400; unexpected: ['public'] |

## 2026-10-25 22:28: run `20261025-222829-prefill`

Plan prefill, done; served as `Ornith-1.5-122B`.

Serving: engine_commit `1429b56b`; binary_sha256 `64f5d54183672d8cc018bfb29f8be83b0da65c0e7b9293d9e6dd70203ff87cd5`; served_model `{"object": "list", "data": [{"id": "Ornith-1.5-122B", "object": "model", "created": 179298`; chip `Apple M5 Ultra; 274877906944`; suite_commit `277c842a1481`

### checks

| check | result |
|---|---|
| memory-idle | measured: mac: System-wide memory free percentage: 58%; total = 3072.00M  us |
| prefill-off | measured: 2199 tokens 3210.2 tok/s (0.685 s), 8766 tokens 3188.8 tok/s (2.749 s), 34975 tokens 2676.2 tok/s (13.069 s), 139884 tokens 1508.4 tok/s (92.734 s) |
| prefill-thinking | measured: 2214 tokens 2753.7 tok/s (0.804 s), 8757 tokens 3132.0 tok/s (2.796 s), 34975 tokens 2662.3 tok/s (13.137 s), 139952 tokens 1501.5 tok/s (93.211 s) |
| memory-busy | measured: mac: System-wide memory free percentage: 47%; total = 3072.00M  us |

## 2026-10-25 21:46: run `20261025-214639-prefill`

Plan prefill, done; served as `Ornith-1.5-122B`.

Serving: engine_commit `f1097d68`; binary_sha256 `5756373d85256437f8c78b0043648b6b801baf4ea208e4c20b63e525ae8cf511`; served_model `{"object": "list", "data": [{"id": "Ornith-1.5-122B", "object": "model", "created": 179298`; chip `Apple M5 Ultra; 274877906944`; suite_commit `277c842a1481`

### checks

| check | result |
|---|---|
| memory-idle | measured: mac: System-wide memory free percentage: 51%; total = 3072.00M  us |
| prefill-off | measured: 2241 tokens 2441.2 tok/s (0.918 s), 8794 tokens 2504.7 tok/s (3.511 s), 35003 tokens 2170.6 tok/s (16.126 s), 139802 tokens 1340.8 tok/s (104.267 s) |
| prefill-thinking | measured: 2247 tokens 2213.8 tok/s (1.015 s), 8791 tokens 2479.8 tok/s (3.545 s), 35020 tokens 2163.7 tok/s (16.185 s), 139764 tokens 1340.3 tok/s (104.281 s) |
| memory-busy | measured: mac: System-wide memory free percentage: 49%; total = 3072.00M  us |

## 2026-10-25 21:43: run `20261025-214343-mlx-speed`

Plan mlx-speed, done; served as `Ornith-1.5-122B`.

Serving: engine_commit `b2bdb481`; binary_sha256 `77d056a5892a8f6648953256cb2b81eccdd3f2eac93f3d352d382b114776174f`; served_model `{"object": "list", "data": [{"id": "Ornith-1.5-122B", "object": "model", "created": 179298`; chip `Apple M5 Ultra; 274877906944`; suite_commit `277c842a1481`

### ruler-streams

| streams | prose total (a stream) | code total (a stream) | structured total (a stream) | list total (a stream) | first token |
|---:|---:|---:|---:|---:|---:|
| 1 | 93.2 (93.2) | 171.9 (171.9) | 122.6 (122.6) | 155.4 (155.4) | 0.05-0.07 s |
| 2 | 184.9 (92.5) | 287.6 (143.8) | 228.3 (114.2) | 311.6 (155.8) | 0.08-0.10 s |
| 4 | 344.4 (86.2) | 586.4 (147.1) | 453.7 (111.8) | 642.4 (160.3) | 0.74-1.48 s |

### checks

| check | result |
|---|---|
| memory-idle | measured: mac: System-wide memory free percentage: 31%; total = 3072.00M  us |

## 2026-10-25 21:38: run `20261025-213830-quick`

Plan quick, done; served as `Ornith-1.5-122B`.

Serving: engine_commit `b2bdb481`; binary_sha256 `77d056a5892a8f6648953256cb2b81eccdd3f2eac93f3d352d382b114776174f`; served_model `{"object": "list", "data": [{"id": "Ornith-1.5-122B", "object": "model", "created": 179298`; chip `Apple M5 Ultra; 274877906944`; suite_commit `277c842a1481`

### ruler-fresh

| streams | prose total (a stream) | code total (a stream) | structured total (a stream) | list total (a stream) | first token |
|---:|---:|---:|---:|---:|---:|
| 1 | 93.0 (93.0) | 171.4 (171.4) | 122.3 (122.3) | 154.9 (154.9) | 0.05-0.07 s |

### ruler-after

| streams | prose total (a stream) | code total (a stream) | structured total (a stream) | list total (a stream) | first token |
|---:|---:|---:|---:|---:|---:|
| 1 | 93.2 (93.2) | 171.8 (171.8) | 122.7 (122.7) | 155.3 (155.3) | 0.05-0.07 s |

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
| memory-idle | measured: mac: System-wide memory free percentage: 48%; total = 3072.00M  us |
| structured | pass: 18/18 obey, drafted == plain 12/12; a bad regex -> 400 |
| tools | FAIL: 4/5 tool cases right; failed named/thinking (finish length) |
| sampling | pass: 9/9 seeded replies equal on repeat and undrafted; 0 errors |
| turns | FAIL: resumed == again: True; cold (after a restart): False; cached 5624 of 5643; ttft resumed 0.069s, cold 2.118s |
| urls | FAIL: public 400; loopback 400; http 400; unexpected: ['public'] |

## 2026-10-25 21:34: run `20261025-213438-prefill`

Plan prefill, done; served as `Ornith-1.5-122B`.

Serving: engine_commit `b2bdb481`; binary_sha256 `77d056a5892a8f6648953256cb2b81eccdd3f2eac93f3d352d382b114776174f`; served_model `{"object": "list", "data": [{"id": "Ornith-1.5-122B", "object": "model", "created": 179298`; chip `Apple M5 Ultra; 274877906944`; suite_commit `277c842a1481`

### checks

| check | result |
|---|---|
| memory-idle | measured: mac: System-wide memory free percentage: 48%; total = 3072.00M  us |
| prefill-off | measured: 2224 tokens 3150.1 tok/s (0.706 s), 8779 tokens 3191.2 tok/s (2.751 s), 35078 tokens 2692.3 tok/s (13.029 s), 139782 tokens 1515.4 tok/s (92.24 s) |
| prefill-thinking | measured: 2212 tokens 2466.0 tok/s (0.897 s), 8771 tokens 3133.6 tok/s (2.799 s), 34926 tokens 2678.6 tok/s (13.039 s), 139852 tokens 1506.1 tok/s (92.855 s) |
| memory-busy | measured: mac: System-wide memory free percentage: 45%; total = 3072.00M  us |

## 2026-10-25 18:54: run `20261025-185408-mlx-speed`

Plan mlx-speed, done; served as `Ornith-1.5-122B`.

Serving: engine_commit `f1097d68`; binary_sha256 `5756373d85256437f8c78b0043648b6b801baf4ea208e4c20b63e525ae8cf511`; served_model `{"object": "list", "data": [{"id": "Ornith-1.5-122B", "object": "model", "created": 179297`; chip `Apple M5 Ultra; 274877906944`; suite_commit `277c842a1481`

### ruler-streams

| streams | prose total (a stream) | code total (a stream) | structured total (a stream) | list total (a stream) | first token |
|---:|---:|---:|---:|---:|---:|
| 1 | 93.2 (93.2) | 171.8 (171.8) | 122.7 (122.7) | 155.3 (155.3) | 0.05-0.07 s |
| 2 | 178.3 (89.2) | 301.1 (150.5) | 223.5 (111.7) | 318.9 (159.4) | 0.08-0.10 s |
| 4 | 343.0 (85.5) | 658.0 (172.9) | 454.9 (110.6) | 649.0 (163.1) | 0.70-1.53 s |

### checks

| check | result |
|---|---|
| memory-idle | measured: mac: System-wide memory free percentage: 51%; total = 3072.00M  us |

## 2026-10-25 18:46: run `20261025-184622-ab-tools-turns`

Plan ab-tools-turns, done; served as `Ornith-1.5-122B`.

Serving: engine_commit `f1097d68`; binary_sha256 `5756373d85256437f8c78b0043648b6b801baf4ea208e4c20b63e525ae8cf511`; served_model `{"object": "list", "data": [{"id": "Ornith-1.5-122B", "object": "model", "created": 179297`; chip `Apple M5 Ultra; 274877906944`; suite_commit `277c842a1481`

### checks

| check | result |
|---|---|
| tools | FAIL: 4/5 tool cases right; failed named/thinking (finish length) |
| turns | FAIL: resumed == again: True; cold (after a restart): False; cached 5624 of 5643; ttft resumed 0.069s, cold 2.628s |

## 2026-10-25 18:45: run `20261025-184542-ab-tools-turns`

Plan ab-tools-turns, done; served as `Ornith-1.5-122B`.

Serving: engine_commit `9328aff8`; binary_sha256 `84c070e7e0f693348614f6d435c69024c7e5d0c2e86734eafa7c9472dbcf426b`; served_model `{"object": "list", "data": [{"id": "Ornith-1.5-122B", "object": "model", "created": 179297`; chip `Apple M5 Ultra; 274877906944`; suite_commit `277c842a1481`

### checks

| check | result |
|---|---|
| tools | FAIL: 4/5 tool cases right; failed named/thinking (calls ['book_flight', 'book_flight', 'book_flight', 'book_flight', 'book_flight', 'book_flight', 'book_flight', 'book_flight', 'book_flight', 'book_flight', 'book_flight', 'book_flight', 'book_flight', 'book_flight', 'book_flight', 'book_flight', 'book_flight', 'book_flight', 'book_flight', 'book_flight', 'book_flight', 'book_flight', 'book_flight', 'book_flight', 'book_flight', 'book_flight', 'book_flight', 'book_flight', 'book_flight', 'book_flight']) |
| turns | FAIL: resumed == again: True; cold (after a restart): False; cached 5624 of 5643; ttft resumed 0.059s, cold 3.189s |

## 2026-10-25 18:39: run `20261025-183902-quick`

Plan quick, done; served as `Ornith-1.5-122B`.

Serving: engine_commit `f1097d68`; binary_sha256 `5756373d85256437f8c78b0043648b6b801baf4ea208e4c20b63e525ae8cf511`; served_model `{"object": "list", "data": [{"id": "Ornith-1.5-122B", "object": "model", "created": 179297`; chip `Apple M5 Ultra; 274877906944`; suite_commit `277c842a1481`

### ruler-fresh

| streams | prose total (a stream) | code total (a stream) | structured total (a stream) | list total (a stream) | first token |
|---:|---:|---:|---:|---:|---:|
| 1 | 93.3 (93.3) | 172.0 (172.0) | 122.8 (122.8) | 155.5 (155.5) | 0.05-0.07 s |

### ruler-after

| streams | prose total (a stream) | code total (a stream) | structured total (a stream) | list total (a stream) | first token |
|---:|---:|---:|---:|---:|---:|
| 1 | 93.2 (93.2) | 171.5 (171.5) | 122.4 (122.4) | 155.1 (155.1) | 0.05-0.07 s |

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
| memory-idle | measured: mac: System-wide memory free percentage: 51%; total = 3072.00M  us |
| structured | pass: 18/18 obey, drafted == plain 12/12; a bad regex -> 400 |
| tools | FAIL: 4/5 tool cases right; failed named/thinking (finish length) |
| sampling | pass: 9/9 seeded replies equal on repeat and undrafted; 0 errors |
| turns | FAIL: resumed == again: True; cold (after a restart): False; cached 5624 of 5643; ttft resumed 0.068s, cold 2.621s |
| urls | FAIL: public 400; loopback 400; http 400; unexpected: ['public'] |

## 2026-10-21 02:20: run `20261021-022004-mlx-speed`

Plan mlx-speed, done; served as `Ornith-1.5-122B`.

Serving: engine_commit `9328aff8`; binary_sha256 `84c070e7e0f693348614f6d435c69024c7e5d0c2e86734eafa7c9472dbcf426b`; served_model `{"object": "list", "data": [{"id": "Ornith-1.5-122B", "object": "model", "created": 179256`; chip `Apple M5 Ultra; 274877906944`; suite_commit `277c842a1481`

### ruler-streams

| streams | prose total (a stream) | code total (a stream) | structured total (a stream) | list total (a stream) | first token |
|---:|---:|---:|---:|---:|---:|
| 1 | 94.4 (94.4) | 174.2 (174.2) | 126.6 (126.6) | 155.1 (155.1) | 0.05-0.07 s |
| 2 | 193.6 (96.8) | 270.8 (135.4) | 216.8 (108.4) | 321.8 (160.9) | 0.08-0.11 s |
| 4 | 232.6 (57.2) | 328.7 (81.5) | 279.5 (67.9) | 386.3 (99.8) | 0.13-0.17 s |

### checks

| check | result |
|---|---|
| memory-idle | measured: mac: System-wide memory free percentage: 64%; total = 4096.00M  us |

## 2026-10-20 16:39: run `20261020-163959-glm-streams`

Plan glm-streams, done; served as `Ornith-1.5-122B`.

Serving: engine_commit `30e5dcb4`; binary_sha256 `0fb4b69774aebdf3db411bc9865bab9ae80c80817085baf0c1dadd8eef5dc5e3`; served_model `{"object": "list", "data": [{"id": "Ornith-1.5-122B", "object": "model", "created": 179253`; chip `Apple M5 Ultra; 274877906944`; suite_commit `277c842a1481`

### ruler-streams

| streams | prose total (a stream) | code total (a stream) | structured total (a stream) | list total (a stream) | first token |
|---:|---:|---:|---:|---:|---:|
| 1 | 95.3 (95.3) | 95.5 (95.5) | 95.4 (95.4) | 95.5 (95.5) | 0.05-0.07 s |
| 4 | 227.1 (56.8) | 232.7 (58.1) | 233.5 (58.4) | 240.2 (60.0) | 0.12-0.17 s |
| 8 | 315.0 (39.4) | 322.5 (40.2) | 327.2 (40.6) | 338.6 (42.5) | 0.22-0.30 s |
| 16 | 404.5 (25.3) | 415.0 (26.0) | 414.9 (26.0) | 437.5 (27.5) | 0.42-0.56 s |

### suite-together

| check | passed |
|---|---:|
| concurrent | 12/12 |
| drafts | 12/12 |

## 2026-10-20 16:34: run `20261020-163412-glm-streams`

Plan glm-streams, done; served as `Ornith-1.5-122B`.

Serving: engine_commit `30e5dcb4`; binary_sha256 `0fb4b69774aebdf3db411bc9865bab9ae80c80817085baf0c1dadd8eef5dc5e3`; served_model `{"object": "list", "data": [{"id": "Ornith-1.5-122B", "object": "model", "created": 179253`; chip `Apple M5 Ultra; 274877906944`; suite_commit `277c842a1481`

### ruler-streams

| streams | prose total (a stream) | code total (a stream) | structured total (a stream) | list total (a stream) | first token |
|---:|---:|---:|---:|---:|---:|
| 1 | 93.8 (93.8) | 157.1 (157.1) | 132.6 (132.6) | 149.5 (149.5) | 0.05-0.07 s |
| 4 | 239.4 (58.6) | 326.0 (81.4) | 282.6 (70.2) | 391.0 (102.7) | 0.13-0.18 s |
| 8 | 231.8 (28.9) | 357.8 (44.3) | 302.7 (38.0) | 385.1 (46.3) | 0.24-0.32 s |
| 16 | 355.6 (21.2) | 410.5 (23.2) | 373.1 (21.9) | 422.1 (23.6) | 0.44-0.59 s |

### suite-together

| check | passed |
|---|---:|
| concurrent | 12/12 |
| drafts | 12/12 |

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

## 2026-10-20 15:40: run `20261020-154044-ornith-thinking`

Plan ornith-thinking, running; served as `Ornith-1.5-122B`.

Serving: engine_commit `30e5dcb4`; binary_sha256 `3e7504db19242321a95555a39a18a51e368405092dbe724d89537d5c14091376`; served_model `{"object": "list", "data": [{"id": "Ornith-1.5-122B", "object": "model", "created": 179252`; chip `Apple M5 Ultra; 274877906944`; suite_commit `277c842a1481`

### checks

| check | result |
|---|---|
| memory-idle | measured: mac: System-wide memory free percentage: 47%; total = 4096.00M  us |
| thinking | pass: thinking on: 10/10 right, 10/10 with reasoning_content, 0 leaks, 0 errors, 0 cut at 8192 tokens |

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

