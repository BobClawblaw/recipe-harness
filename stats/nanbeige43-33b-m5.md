# Nanbeige4.3-33B, bf16 on 1x Apple M5 Ultra (256 GB unified), macOS

Target `nanbeige43-33b-m5`: Nanbeige4.3-33B bf16 as released, TensorFold native Metal (llama) on one M5 Ultra (131072-token window, 2 streams). Engine: TensorFold native, Metal. Rendered from `stats/nanbeige43-33b-m5.json` (6 runs); aggregate tok/s, total (a stream).

## 2026-10-26 04:31: run `20261026-043132-prefill-64k`

Plan prefill-64k, done; served as `nanbeige`.

Serving: engine_commit `490b6b9a5`; binary_sha256 `f2a9ddfd933ba5b60c5921180b31faeca58b8ac826e09b78911e49d0ef7342a0`; served_model `{"object": "list", "data": [{"id": "nanbeige", "object": "model", "created": 1793007100, "`; chip `Apple M5 Ultra; 274877906944`; suite_commit `277c842a1481`

### checks

| check | result |
|---|---|
| memory-idle | measured: mac: System-wide memory free percentage: 33%; total = 5120.00M  us |
| prefill-off | measured: 2109 tokens 1259.1 tok/s (1.675 s), 8254 tokens 1313.1 tok/s (6.286 s), 32827 tokens 1074.3 tok/s (30.557 s), 61502 tokens 866.3 tok/s (70.991 s) |
| prefill-thinking | measured: 2106 tokens 1250.6 tok/s (1.684 s), 8248 tokens 1310.2 tok/s (6.295 s), 32825 tokens 1053.5 tok/s (31.157 s), 61496 tokens 837.3 tok/s (73.442 s) |
| memory-busy | measured: mac: System-wide memory free percentage: 25%; total = 5120.00M  us |

## 2026-10-26 04:28: run `20261026-042844-prefill`

Plan prefill, done; served as `nanbeige`.

Serving: engine_commit `490b6b9a5`; binary_sha256 `f2a9ddfd933ba5b60c5921180b31faeca58b8ac826e09b78911e49d0ef7342a0`; served_model `{"object": "list", "data": [{"id": "nanbeige", "object": "model", "created": 1793006932, "`; chip `Apple M5 Ultra; 274877906944`; suite_commit `277c842a1481`

### checks

| check | result |
|---|---|
| memory-idle | measured: mac: System-wide memory free percentage: 33%; total = 5120.00M  us |
| prefill-off | FAIL: 2109 tokens 1264.4 tok/s (1.668 s), 8254 tokens 1312.5 tok/s (6.289 s), 32831 tokens 1074.9 tok/s (30.544 s); not cold or failed: ['131072'] |
| prefill-thinking | FAIL: 2104 tokens 1267.5 tok/s (1.66 s), 8251 tokens 1310.5 tok/s (6.296 s), 32826 tokens 1073.0 tok/s (30.594 s); not cold or failed: ['131072'] |
| memory-busy | measured: mac: System-wide memory free percentage: 33%; total = 5120.00M  us |

## 2026-10-26 04:19: run `20261026-041934-speed`

Plan speed, done; served as `nanbeige`.

Serving: engine_commit `490b6b9a5`; binary_sha256 `f2a9ddfd933ba5b60c5921180b31faeca58b8ac826e09b78911e49d0ef7342a0`; served_model `{"object": "list", "data": [{"id": "nanbeige", "object": "model", "created": 1793006382, "`; chip `Apple M5 Ultra; 274877906944`; suite_commit `277c842a1481`

### ruler-fresh

| streams | prose total (a stream) | code total (a stream) | structured total (a stream) | list total (a stream) | first token |
|---:|---:|---:|---:|---:|---:|
| 1 | 16.4 (16.4) | 16.3 (16.3) | 16.4 (16.4) | 16.4 (16.4) | 0.23-0.26 s |
| 2 | 31.8 (15.9) | 28.0 (14.0) | 31.7 (15.8) | 31.7 (15.8) | 0.34-0.38 s |

Engine rounds (ruler-fresh):

| streams | tokens a round | drafts a round | accepted | ms a round | requests |
|---:|---:|---:|---:|---:|---:|
| 1 | 1.005 | 0.017 | 0% | 61.35 | 12 |
| 2 | 1.023 | 0.059 | 30% | 66.44 | 25 |

### ruler-after

| streams | prose total (a stream) | code total (a stream) | structured total (a stream) | list total (a stream) | first token |
|---:|---:|---:|---:|---:|---:|
| 1 | 16.4 (16.4) | 16.3 (16.3) | 16.4 (16.4) | 16.4 (16.4) | 0.23-0.26 s |

Engine rounds (ruler-after):

| streams | tokens a round | drafts a round | accepted | ms a round | requests |
|---:|---:|---:|---:|---:|---:|
| 1 | 1.007 | 0.022 | 10% | 61.52 | 13 |

### checks

| check | result |
|---|---|
| memory-idle | measured: mac: System-wide memory free percentage: 33%; total = 5120.00M  us |
| turns | pass: resumed == again: True; cold (after a restart): True; cached 5493 of 5649; ttft resumed 0.348s, cold 4.539s |
| memory-busy | measured: mac: System-wide memory free percentage: 32%; total = 5120.00M  us |

## 2026-10-26 03:43: run `20261026-034316-quick`

Plan quick, done; served as `nanbeige`.

Serving: engine_commit `490b6b9a5`; binary_sha256 `f2a9ddfd933ba5b60c5921180b31faeca58b8ac826e09b78911e49d0ef7342a0`; served_model `{"object": "list", "data": [{"id": "nanbeige", "object": "model", "created": 1793004209, "`; chip `Apple M5 Ultra; 274877906944`; suite_commit `277c842a1481`

### ruler-fresh

| streams | prose total (a stream) | code total (a stream) | structured total (a stream) | list total (a stream) | first token |
|---:|---:|---:|---:|---:|---:|
| 1 | 16.3 (16.3) | 16.2 (16.2) | 16.3 (16.3) | 16.3 (16.3) | 0.23-0.26 s |

Engine rounds (ruler-fresh):

| streams | tokens a round | drafts a round | accepted | ms a round | requests |
|---:|---:|---:|---:|---:|---:|
| 1 | 1.005 | 0.017 | 0% | 61.6 | 12 |

### ruler-after

| streams | prose total (a stream) | code total (a stream) | structured total (a stream) | list total (a stream) | first token |
|---:|---:|---:|---:|---:|---:|
| 1 | 16.4 (16.4) | 16.3 (16.3) | 16.4 (16.4) | 16.3 (16.3) | 0.23-0.26 s |

Engine rounds (ruler-after):

| streams | tokens a round | drafts a round | accepted | ms a round | requests |
|---:|---:|---:|---:|---:|---:|
| 1 | 1.007 | 0.022 | 10% | 61.66 | 13 |

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
| memory-idle | measured: mac: System-wide memory free percentage: 33%; total = 6144.00M  us |
| structured | pass: 18/18 obey, drafted == plain 12/12; a bad regex -> 400 |
| tools | pass: 5/5 tool cases right |
| sampling | pass: 9/9 seeded replies equal on repeat and undrafted; 0 errors |
| turns | pass: resumed == again: True; cold (after a restart): True; cached 5493 of 5649; ttft resumed 0.343s, cold 4.512s |

## 2026-10-26 02:59: run `20261026-025918-quick`

Plan quick, running; served as `nanbeige`.

Serving: engine_commit `490b6b9a5`; binary_sha256 `f2a9ddfd933ba5b60c5921180b31faeca58b8ac826e09b78911e49d0ef7342a0`; served_model `{"object": "list", "data": [{"id": "nanbeige", "object": "model", "created": 1793001621, "`; chip `Apple M5 Ultra; 274877906944`; suite_commit `277c842a1481`

### checks

| check | result |
|---|---|
| memory-idle | measured: mac: System-wide memory free percentage: 9%; total = 6144.00M  use |

## 2026-10-26 02:07: run `20261026-020710-quick`

Plan quick, aborted: the server died during suite; its result is discarded; served as `nanbeige`.

Serving: engine_commit `e38574b0f`; binary_sha256 `9a1329719d3273bfe23de3f5494bcfd369af8beb1d12bc5c2aafec20d849226a`; served_model `{"object": "list", "data": [{"id": "nanbeige", "object": "model", "created": 1792998438, "`; chip `Apple M5 Ultra; 274877906944`; suite_commit `277c842a1481`

### ruler-fresh

| streams | prose total (a stream) | code total (a stream) | structured total (a stream) | list total (a stream) | first token |
|---:|---:|---:|---:|---:|---:|
| 1 | 16.4 (16.4) | 16.3 (16.3) | 16.3 (16.3) | 16.4 (16.4) | 0.23-0.26 s |

Engine rounds (ruler-fresh):

| streams | tokens a round | drafts a round | accepted | ms a round | requests |
|---:|---:|---:|---:|---:|---:|
| 1 | 1.005 | 0.017 | 0% | 61.48 | 12 |

### ruler-after

| streams | prose total (a stream) | code total (a stream) | structured total (a stream) | list total (a stream) | first token |
|---:|---:|---:|---:|---:|---:|
| 1 | 16.4 (16.4) | 16.3 (16.3) | 16.4 (16.4) | 16.4 (16.4) | 0.23-0.26 s |

Engine rounds (ruler-after):

| streams | tokens a round | drafts a round | accepted | ms a round | requests |
|---:|---:|---:|---:|---:|---:|
| 1 | 1.007 | 0.022 | 10% | 61.59 | 13 |

### checks

| check | result |
|---|---|
| memory-idle | measured: mac: System-wide memory free percentage: 31%; total = 3072.00M  us |
| structured | pass: 18/18 obey, drafted == plain 12/12; a bad regex -> 400 |
| tools | pass: 5/5 tool cases right |
| sampling | pass: 9/9 seeded replies equal on repeat and undrafted; 0 errors |
| turns | pass: resumed == again: True; cold (after a restart): True; cached 5493 of 5649; ttft resumed 0.355s, cold 4.376s |

