# Spark-X2.6-4B, bf16 on 1x Apple M5 Ultra (256 GB unified), macOS

Target `spark-x26-4b-m5`: Spark-X2.6-4B bf16 as released, TensorFold native Metal (spark2_5) on one M5 Ultra (262144-token window, 4 streams). Engine: TensorFold native, Metal. Rendered from `stats/spark-x26-4b-m5.json` (10 runs); aggregate tok/s, total (a stream).

## 2026-10-25 17:04: run `20261025-170422-mlx-speed`

Plan mlx-speed, done; served as `spark`.

Serving: engine_commit `11f15133e`; binary_sha256 `3ffa026b390096dad439f4fdd1e7ae54aaf9c825fcd009a5ac9c495a4d521f9f`; served_model `{"object": "list", "data": [{"id": "spark", "object": "model", "created": 1792965862, "own`; chip `Apple M5 Ultra; 274877906944`; suite_commit `277c842a1481`

### ruler-streams

| streams | prose total (a stream) | code total (a stream) | structured total (a stream) | list total (a stream) | first token |
|---:|---:|---:|---:|---:|---:|
| 1 | 105.1 (105.1) | 105.3 (105.3) | 105.2 (105.2) | 105.2 (105.2) | 0.05-0.07 s |
| 2 | 187.1 (93.5) | 177.4 (88.7) | 188.3 (94.2) | 186.7 (93.4) | 0.08-0.10 s |
| 4 | 321.5 (80.1) | 296.2 (74.6) | 325.5 (80.9) | 318.0 (78.6) | 0.13-0.17 s |

Engine rounds (ruler-streams):

| streams | tokens a round | drafts a round | accepted | ms a round | requests |
|---:|---:|---:|---:|---:|---:|
| 1 | 1.005 | 0.0 |  | 9.55 | 12 |
| 2 | 1.009 | 0.032 | 15% | 10.92 | 25 |
| 4 | 1.008 | 0.024 | 12% | 12.82 | 50 |

### checks

| check | result |
|---|---|
| memory-idle | measured: mac: System-wide memory free percentage: 90%; total = 3072.00M  us |

## 2026-10-25 16:24: run `20261025-162417-prefill`

Plan prefill, done; served as `spark`.

Serving: engine_commit `878697c64`; binary_sha256 `55a3c50002f212139eeb4c8b79f4a57e0e3d7c8619ad519be7fd215b8c19b6de`; served_model `{"object": "list", "data": [{"id": "spark", "object": "model", "created": 1792963465, "own`; chip `Apple M5 Ultra; 274877906944`; suite_commit `277c842a1481`

### checks

| check | result |
|---|---|
| memory-idle | measured: mac: System-wide memory free percentage: 91%; total = 3072.00M  us |
| prefill-off | measured: 2350 tokens 9437.8 tok/s (0.249 s), 9354 tokens 10940.4 tok/s (0.855 s), 37174 tokens 9058.0 tok/s (4.104 s), 148588 tokens 5002.1 tok/s (29.705 s) |
| prefill-thinking | measured: 2439 tokens 9564.7 tok/s (0.255 s), 9322 tokens 10864.8 tok/s (0.858 s), 37159 tokens 9063.2 tok/s (4.1 s), 148607 tokens 5019.2 tok/s (29.608 s) |
| memory-busy | measured: mac: System-wide memory free percentage: 87%; total = 3072.00M  us |

## 2026-10-25 16:22: run `20261025-162233-speed`

Plan speed, done; served as `spark`.

Serving: engine_commit `878697c64`; binary_sha256 `55a3c50002f212139eeb4c8b79f4a57e0e3d7c8619ad519be7fd215b8c19b6de`; served_model `{"object": "list", "data": [{"id": "spark", "object": "model", "created": 1792963361, "own`; chip `Apple M5 Ultra; 274877906944`; suite_commit `277c842a1481`

### ruler-fresh

| streams | prose total (a stream) | code total (a stream) | structured total (a stream) | list total (a stream) | first token |
|---:|---:|---:|---:|---:|---:|
| 1 | 105.9 (105.9) | 106.0 (106.0) | 105.9 (105.9) | 105.9 (105.9) | 0.05-0.07 s |
| 2 | 188.8 (94.4) | 178.9 (89.5) | 189.8 (94.9) | 188.4 (94.2) | 0.08-0.10 s |

Engine rounds (ruler-fresh):

| streams | tokens a round | drafts a round | accepted | ms a round | requests |
|---:|---:|---:|---:|---:|---:|
| 1 | 1.005 | 0.0 |  | 9.48 | 12 |
| 2 | 1.009 | 0.032 | 15% | 10.82 | 25 |

### ruler-after

| streams | prose total (a stream) | code total (a stream) | structured total (a stream) | list total (a stream) | first token |
|---:|---:|---:|---:|---:|---:|
| 1 | 105.9 (105.9) | 106.0 (106.0) | 106.0 (106.0) | 105.9 (105.9) | 0.05-0.07 s |

Engine rounds (ruler-after):

| streams | tokens a round | drafts a round | accepted | ms a round | requests |
|---:|---:|---:|---:|---:|---:|
| 1 | 1.005 | 0.0 |  | 9.48 | 13 |

### checks

| check | result |
|---|---|
| memory-idle | measured: mac: System-wide memory free percentage: 91%; total = 3072.00M  us |
| turns | pass: resumed == again: True; cold (after a restart): True; cached 5499 of 5624; ttft resumed 0.065s, cold 0.581s |
| memory-busy | measured: mac: System-wide memory free percentage: 91%; total = 3072.00M  us |

## 2026-10-25 16:16: run `20261025-161656-quick`

Plan quick, done; served as `spark`.

Serving: engine_commit `878697c64`; binary_sha256 `55a3c50002f212139eeb4c8b79f4a57e0e3d7c8619ad519be7fd215b8c19b6de`; served_model `{"object": "list", "data": [{"id": "spark", "object": "model", "created": 1792963024, "own`; chip `Apple M5 Ultra; 274877906944`; suite_commit `277c842a1481`

### ruler-fresh

| streams | prose total (a stream) | code total (a stream) | structured total (a stream) | list total (a stream) | first token |
|---:|---:|---:|---:|---:|---:|
| 1 | 106.1 (106.1) | 106.1 (106.1) | 106.1 (106.1) | 105.9 (105.9) | 0.05-0.07 s |

Engine rounds (ruler-fresh):

| streams | tokens a round | drafts a round | accepted | ms a round | requests |
|---:|---:|---:|---:|---:|---:|
| 1 | 1.005 | 0.0 |  | 9.47 | 12 |

### ruler-after

| streams | prose total (a stream) | code total (a stream) | structured total (a stream) | list total (a stream) | first token |
|---:|---:|---:|---:|---:|---:|
| 1 | 105.8 (105.8) | 105.9 (105.9) | 105.8 (105.8) | 105.7 (105.7) | 0.05-0.07 s |

Engine rounds (ruler-after):

| streams | tokens a round | drafts a round | accepted | ms a round | requests |
|---:|---:|---:|---:|---:|---:|
| 1 | 1.005 | 0.0 |  | 9.5 | 13 |

### suite

| check | passed |
|---|---:|
| soak | 60/60 |
| drafts | 12/12 |
| concurrent | 12/12 |
| streaming | 4/4 |
| multiturn | 7/8 |
| stop | 3/3 |
| thinking | 10/10 |
| copy | 2/2 |
| max-tokens | 3/3 |

### checks

| check | result |
|---|---|
| memory-idle | measured: mac: System-wide memory free percentage: 91%; total = 3072.00M  us |
| structured | pass: 18/18 obey, drafted == plain 12/12; a bad regex -> 400 |
| tools | pass: 5/5 tool cases right |
| sampling | pass: 9/9 seeded replies equal on repeat and undrafted; 0 errors |
| turns | pass: resumed == again: True; cold (after a restart): True; cached 5499 of 5624; ttft resumed 0.065s, cold 0.59s |

## 2026-10-25 15:42: run `20261025-154240-prefill`

Plan prefill, done; served as `spark`.

Serving: engine_commit `3f1b46d75`; binary_sha256 `7329bbc598ee57cda498147953fd3f20b257d77e89948000486fa36654f89932`; served_model `{"object": "list", "data": [{"id": "spark", "object": "model", "created": 1792960968, "own`; chip `Apple M5 Ultra; 274877906944`; suite_commit `277c842a1481`

### checks

| check | result |
|---|---|
| memory-idle | measured: mac: System-wide memory free percentage: 93%; total = 3072.00M  us |
| prefill-off | measured: 2401 tokens 8222.6 tok/s (0.292 s), 9339 tokens 9246.5 tok/s (1.01 s), 37128 tokens 7730.2 tok/s (4.803 s), 148569 tokens 4533.7 tok/s (32.77 s) |
| prefill-thinking | measured: 2412 tokens 8583.6 tok/s (0.281 s), 9393 tokens 9263.3 tok/s (1.014 s), 37255 tokens 7746.9 tok/s (4.809 s), 148530 tokens 4525.6 tok/s (32.82 s) |
| memory-busy | measured: mac: System-wide memory free percentage: 88%; total = 3072.00M  us |

## 2026-10-25 15:41: run `20261025-154128-speed`

Plan speed, done; served as `spark`.

Serving: engine_commit `3f1b46d75`; binary_sha256 `7329bbc598ee57cda498147953fd3f20b257d77e89948000486fa36654f89932`; served_model `{"object": "list", "data": [{"id": "spark", "object": "model", "created": 1792960896, "own`; chip `Apple M5 Ultra; 274877906944`; suite_commit `277c842a1481`

### ruler-fresh

| streams | prose total (a stream) | code total (a stream) | structured total (a stream) | list total (a stream) | first token |
|---:|---:|---:|---:|---:|---:|
| 1 | 165.9 (165.9) | 165.9 (165.9) | 165.5 (165.5) | 165.9 (165.9) | 0.04-0.05 s |
| 2 | 264.2 (132.1) | 258.0 (129.0) | 268.4 (134.2) | 262.6 (131.3) | 0.05-0.08 s |

Engine rounds (ruler-fresh):

| streams | tokens a round | drafts a round | accepted | ms a round | requests |
|---:|---:|---:|---:|---:|---:|
| 1 | 1.005 | 0.0 |  | 6.06 | 12 |
| 2 | 1.01 | 0.033 | 15% | 7.67 | 26 |

### ruler-after

| streams | prose total (a stream) | code total (a stream) | structured total (a stream) | list total (a stream) | first token |
|---:|---:|---:|---:|---:|---:|
| 1 | 165.3 (165.3) | 165.5 (165.5) | 165.5 (165.5) | 165.4 (165.4) | 0.04-0.05 s |

Engine rounds (ruler-after):

| streams | tokens a round | drafts a round | accepted | ms a round | requests |
|---:|---:|---:|---:|---:|---:|
| 1 | 1.005 | 0.006 | 7% | 6.08 | 13 |

### checks

| check | result |
|---|---|
| memory-idle | measured: mac: System-wide memory free percentage: 92%; total = 3072.00M  us |
| turns | pass: resumed == again: True; cold (after a restart): True; cached 5499 of 5630; ttft resumed 0.049s, cold 0.639s |
| memory-busy | measured: mac: System-wide memory free percentage: 92%; total = 3072.00M  us |

## 2026-10-25 15:36: run `20261025-153648-quick`

Plan quick, done; served as `spark`.

Serving: engine_commit `3f1b46d75`; binary_sha256 `7329bbc598ee57cda498147953fd3f20b257d77e89948000486fa36654f89932`; served_model `{"object": "list", "data": [{"id": "spark", "object": "model", "created": 1792960617, "own`; chip `Apple M5 Ultra; 274877906944`; suite_commit `277c842a1481`

### ruler-fresh

| streams | prose total (a stream) | code total (a stream) | structured total (a stream) | list total (a stream) | first token |
|---:|---:|---:|---:|---:|---:|
| 1 | 166.4 (166.4) | 166.5 (166.5) | 166.7 (166.7) | 166.6 (166.6) | 0.04-0.05 s |

Engine rounds (ruler-fresh):

| streams | tokens a round | drafts a round | accepted | ms a round | requests |
|---:|---:|---:|---:|---:|---:|
| 1 | 1.005 | 0.0 |  | 6.03 | 12 |

### ruler-after

| streams | prose total (a stream) | code total (a stream) | structured total (a stream) | list total (a stream) | first token |
|---:|---:|---:|---:|---:|---:|
| 1 | 166.0 (166.0) | 165.9 (165.9) | 165.1 (165.1) | 164.8 (164.8) | 0.04-0.06 s |

Engine rounds (ruler-after):

| streams | tokens a round | drafts a round | accepted | ms a round | requests |
|---:|---:|---:|---:|---:|---:|
| 1 | 1.005 | 0.006 | 7% | 6.08 | 13 |

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
| memory-idle | measured: mac: System-wide memory free percentage: 93%; total = 3072.00M  us |
| structured | pass: 18/18 obey, drafted == plain 12/12; a bad regex -> 400 |
| tools | pass: 5/5 tool cases right |
| sampling | pass: 9/9 seeded replies equal on repeat and undrafted; 0 errors |
| turns | pass: resumed == again: True; cold (after a restart): True; cached 5499 of 5630; ttft resumed 0.052s, cold 0.648s |

## 2026-10-25 15:02: run `20261025-150200-prefill`

Plan prefill, done; served as `spark`.

Serving: engine_commit `4d8a4a2b5`; binary_sha256 `758ad67887cd9adda5d419b04e2ce864cf5278d097d256df9f3b719fd91bdd8f`; served_model `{"object": "list", "data": [{"id": "spark", "object": "model", "created": 1792958528, "own`; chip `Apple M5 Ultra; 274877906944`; suite_commit `277c842a1481`

### checks

| check | result |
|---|---|
| memory-idle | measured: mac: System-wide memory free percentage: 92%; total = 4096.00M  us |
| prefill-off | measured: 2362 tokens 8201.4 tok/s (0.288 s), 9269 tokens 9241.3 tok/s (1.003 s), 37121 tokens 7752.9 tok/s (4.788 s), 148552 tokens 4511.7 tok/s (32.926 s) |
| prefill-thinking | measured: 2433 tokens 8597.2 tok/s (0.283 s), 9318 tokens 9244.0 tok/s (1.008 s), 37214 tokens 7730.4 tok/s (4.814 s), 148534 tokens 4535.4 tok/s (32.75 s) |
| memory-busy | measured: mac: System-wide memory free percentage: 88%; total = 3072.00M  us |

## 2026-10-25 15:00: run `20261025-150048-speed`

Plan speed, done; served as `spark`.

Serving: engine_commit `4d8a4a2b5`; binary_sha256 `758ad67887cd9adda5d419b04e2ce864cf5278d097d256df9f3b719fd91bdd8f`; served_model `{"object": "list", "data": [{"id": "spark", "object": "model", "created": 1792958456, "own`; chip `Apple M5 Ultra; 274877906944`; suite_commit `277c842a1481`

### ruler-fresh

| streams | prose total (a stream) | code total (a stream) | structured total (a stream) | list total (a stream) | first token |
|---:|---:|---:|---:|---:|---:|
| 1 | 166.1 (166.1) | 165.9 (165.9) | 165.6 (165.6) | 166.0 (166.0) | 0.03-0.05 s |
| 2 | 265.3 (132.6) | 257.6 (128.8) | 268.1 (134.1) | 262.4 (131.2) | 0.05-0.08 s |

Engine rounds (ruler-fresh):

| streams | tokens a round | drafts a round | accepted | ms a round | requests |
|---:|---:|---:|---:|---:|---:|
| 1 | 1.005 | 0.0 |  | 6.06 | 12 |
| 2 | 1.01 | 0.034 | 15% | 7.67 | 25 |

### ruler-after

| streams | prose total (a stream) | code total (a stream) | structured total (a stream) | list total (a stream) | first token |
|---:|---:|---:|---:|---:|---:|
| 1 | 166.2 (166.2) | 165.8 (165.8) | 166.0 (166.0) | 165.6 (165.6) | 0.04-0.05 s |

Engine rounds (ruler-after):

| streams | tokens a round | drafts a round | accepted | ms a round | requests |
|---:|---:|---:|---:|---:|---:|
| 1 | 1.005 | 0.006 | 7% | 6.06 | 13 |

### checks

| check | result |
|---|---|
| memory-idle | measured: mac: System-wide memory free percentage: 92%; total = 4096.00M  us |
| turns | pass: resumed == again: True; cold (after a restart): True; cached 5499 of 5630; ttft resumed 0.051s, cold 0.649s |
| memory-busy | measured: mac: System-wide memory free percentage: 92%; total = 4096.00M  us |

## 2026-10-25 14:55: run `20261025-145506-quick`

Plan quick, done; served as `spark`.

Serving: engine_commit `4d8a4a2b5`; binary_sha256 `758ad67887cd9adda5d419b04e2ce864cf5278d097d256df9f3b719fd91bdd8f`; served_model `{"object": "list", "data": [{"id": "spark", "object": "model", "created": 1792958114, "own`; chip `Apple M5 Ultra; 274877906944`; suite_commit `277c842a1481`

### ruler-fresh

| streams | prose total (a stream) | code total (a stream) | structured total (a stream) | list total (a stream) | first token |
|---:|---:|---:|---:|---:|---:|
| 1 | 166.4 (166.4) | 166.8 (166.8) | 166.6 (166.6) | 166.6 (166.6) | 0.04-0.05 s |

Engine rounds (ruler-fresh):

| streams | tokens a round | drafts a round | accepted | ms a round | requests |
|---:|---:|---:|---:|---:|---:|
| 1 | 1.005 | 0.0 |  | 6.03 | 12 |

### ruler-after

| streams | prose total (a stream) | code total (a stream) | structured total (a stream) | list total (a stream) | first token |
|---:|---:|---:|---:|---:|---:|
| 1 | 166.4 (166.4) | 166.7 (166.7) | 166.4 (166.4) | 166.3 (166.3) | 0.04-0.05 s |

Engine rounds (ruler-after):

| streams | tokens a round | drafts a round | accepted | ms a round | requests |
|---:|---:|---:|---:|---:|---:|
| 1 | 1.005 | 0.006 | 7% | 6.04 | 13 |

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
| memory-idle | measured: mac: System-wide memory free percentage: 92%; total = 4096.00M  us |
| structured | pass: 18/18 obey, drafted == plain 12/12; a bad regex -> 400 |
| tools | pass: 5/5 tool cases right |
| sampling | pass: 9/9 seeded replies equal on repeat and undrafted; 0 errors |
| turns | pass: resumed == again: True; cold (after a restart): True; cached 5499 of 5630; ttft resumed 0.05s, cold 0.648s |

