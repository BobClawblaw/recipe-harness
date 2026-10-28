# Nanbeige4.3-33B bf16, drafted by Nanbeige4.1-3B bf16 on 1x Apple M5 Ultra (256 GB unified), macOS

Target `nanbeige43-33b-bf16draft-m5`: Nanbeige4.3-33B bf16 with Nanbeige4.1-3B bf16 drafting, TensorFold native Metal (llama) on one M5 Ultra (131072-token window, 2 streams, every stream drafted). Engine: TensorFold native, Metal. Rendered from `stats/nanbeige43-33b-bf16draft-m5.json` (3 runs); aggregate tok/s, total (a stream).

## 2026-10-28 12:03: run `20261028-120335-prefill`

Plan prefill, done; served as `nanbeige`.

Serving: engine_commit `50fe245ac`; binary_sha256 `c3fcf8cacf289aec9ee53f1eae52fda4fab2f1eeda1bf75b61482542dba4b3d1`; served_model `{"object": "list", "data": [{"id": "nanbeige", "object": "model", "created": 1793207029, "`; chip `Apple M5 Ultra; 274877906944`; suite_commit `21db9b23f7be`

### checks

| check | result |
|---|---|
| memory-idle | measured: mac: System-wide memory free percentage: 68%; total = 4096.00M  us |
| prefill-off | FAIL: 2110 tokens 1199.5 tok/s (1.759 s), 8250 tokens 1253.0 tok/s (6.584 s), 32827 tokens 1020.7 tok/s (32.162 s); not cold or failed: ['131072'] |
| prefill-thinking | FAIL: 2106 tokens 1217.3 tok/s (1.73 s), 8248 tokens 1252.9 tok/s (6.583 s), 32822 tokens 1053.9 tok/s (31.144 s); not cold or failed: ['131072'] |
| memory-busy | measured: mac: System-wide memory free percentage: 65%; total = 4096.00M  us |

## 2026-10-28 11:59: run `20261028-115919-speed`

Plan speed, done; served as `nanbeige`.

Serving: engine_commit `50fe245ac`; binary_sha256 `c3fcf8cacf289aec9ee53f1eae52fda4fab2f1eeda1bf75b61482542dba4b3d1`; served_model `{"object": "list", "data": [{"id": "nanbeige", "object": "model", "created": 1793206767, "`; chip `Apple M5 Ultra; 274877906944`; suite_commit `21db9b23f7be`

### ruler-fresh

| streams | prose total (a stream) | code total (a stream) | structured total (a stream) | list total (a stream) | first token |
|---:|---:|---:|---:|---:|---:|
| 1 | 113.9 (113.9) | 108.3 (108.3) | 98.6 (98.6) | 98.9 (98.9) | 0.23-0.26 s |
| 2 | 44.6 (22.3) | 59.0 (29.5) | 54.4 (27.2) | 55.9 (27.9) | 0.35-0.39 s |

Engine rounds (ruler-fresh):

| streams | tokens a round | drafts a round | accepted | ms a round | requests |
|---:|---:|---:|---:|---:|---:|
| 1 | 4.875 | 4.511 | 85% | 46.47 | 12 |
| 2 | 4.54 | 3.981 | 88% | 169.8 | 25 |

### ruler-after

| streams | prose total (a stream) | code total (a stream) | structured total (a stream) | list total (a stream) | first token |
|---:|---:|---:|---:|---:|---:|
| 1 | 113.7 (113.7) | 100.2 (100.2) | 101.9 (101.9) | 94.9 (94.9) | 0.23-0.26 s |

Engine rounds (ruler-after):

| streams | tokens a round | drafts a round | accepted | ms a round | requests |
|---:|---:|---:|---:|---:|---:|
| 1 | 4.865 | 4.472 | 86% | 47.38 | 13 |

### checks

| check | result |
|---|---|
| memory-idle | measured: mac: System-wide memory free percentage: 68%; total = 4096.00M  us |
| turns | pass: resumed == again: True; cold (after a restart): True; cached 5493 of 5649; ttft resumed 0.362s, cold 4.444s |
| memory-busy | measured: mac: System-wide memory free percentage: 68%; total = 4096.00M  us |

## 2026-10-28 11:33: run `20261028-113348-quick`

Plan quick, done; served as `nanbeige`.

Serving: engine_commit `50fe245ac`; binary_sha256 `c3fcf8cacf289aec9ee53f1eae52fda4fab2f1eeda1bf75b61482542dba4b3d1`; served_model `{"object": "list", "data": [{"id": "nanbeige", "object": "model", "created": 1793205241, "`; chip `Apple M5 Ultra; 274877906944`; suite_commit `21db9b23f7be`

### ruler-fresh

| streams | prose total (a stream) | code total (a stream) | structured total (a stream) | list total (a stream) | first token |
|---:|---:|---:|---:|---:|---:|
| 1 | 114.0 (114.0) | 100.5 (100.5) | 101.6 (101.6) | 102.0 (102.0) | 0.23-0.26 s |

Engine rounds (ruler-fresh):

| streams | tokens a round | drafts a round | accepted | ms a round | requests |
|---:|---:|---:|---:|---:|---:|
| 1 | 4.804 | 4.449 | 85% | 45.96 | 12 |

### ruler-after

| streams | prose total (a stream) | code total (a stream) | structured total (a stream) | list total (a stream) | first token |
|---:|---:|---:|---:|---:|---:|
| 1 | 111.1 (111.1) | 108.2 (108.2) | 99.1 (99.1) | 102.1 (102.1) | 0.23-0.26 s |

Engine rounds (ruler-after):

| streams | tokens a round | drafts a round | accepted | ms a round | requests |
|---:|---:|---:|---:|---:|---:|
| 1 | 4.704 | 4.31 | 85% | 44.75 | 13 |

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
| memory-idle | measured: mac: System-wide memory free percentage: 68%; total = 4096.00M  us |
| structured | pass: 18/18 obey, drafted == plain 12/12; a bad regex -> 400 |
| tools | pass: 5/5 tool cases right |
| sampling | pass: 9/9 seeded replies equal on repeat and undrafted; 0 errors |
| turns | pass: resumed == again: True; cold (after a restart): True; cached 5493 of 5649; ttft resumed 0.36s, cold 4.411s |

