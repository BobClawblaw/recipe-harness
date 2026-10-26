# Nanbeige4.3-33B, affine 8bit on 1x Apple M5 Ultra (256 GB unified), macOS

Target `nanbeige43-33b-8bit-m5`: Nanbeige4.3-33B MLX affine 8bit (llama_convert.py), TensorFold native Metal (llama) on one M5 Ultra (131072-token window, 2 streams). Engine: TensorFold native, Metal. Rendered from `stats/nanbeige43-33b-8bit-m5.json` (3 runs); aggregate tok/s, total (a stream).

## 2026-10-26 08:30: run `20261026-083001-prefill-64k`

Plan prefill-64k, done; served as `nanbeige`.

Serving: engine_commit `fa5b1f989`; binary_sha256 `70f5a3c2a635a8d9ddd59cf5e751c38c9cf28faf407348046efd60a14716e3a8`; served_model `{"object": "list", "data": [{"id": "nanbeige", "object": "model", "created": 1793021409, "`; chip `Apple M5 Ultra; 274877906944`; suite_commit `277c842a1481`

### checks

| check | result |
|---|---|
| memory-idle | measured: mac: System-wide memory free percentage: 47%; total = 4096.00M  us |
| prefill-off | measured: 2107 tokens 1268.5 tok/s (1.661 s), 8253 tokens 1254.1 tok/s (6.581 s), 32828 tokens 1009.4 tok/s (32.521 s), 61499 tokens 814.9 tok/s (75.465 s) |
| prefill-thinking | measured: 2106 tokens 1249.1 tok/s (1.686 s), 8248 tokens 1208.1 tok/s (6.827 s), 32824 tokens 957.4 tok/s (34.286 s), 61497 tokens 758.7 tok/s (81.055 s) |
| memory-busy | measured: mac: System-wide memory free percentage: 43%; total = 4096.00M  us |

## 2026-10-26 08:24: run `20261026-082437-speed`

Plan speed, done; served as `nanbeige`.

Serving: engine_commit `fa5b1f989`; binary_sha256 `70f5a3c2a635a8d9ddd59cf5e751c38c9cf28faf407348046efd60a14716e3a8`; served_model `{"object": "list", "data": [{"id": "nanbeige", "object": "model", "created": 1793021086, "`; chip `Apple M5 Ultra; 274877906944`; suite_commit `277c842a1481`

### ruler-fresh

| streams | prose total (a stream) | code total (a stream) | structured total (a stream) | list total (a stream) | first token |
|---:|---:|---:|---:|---:|---:|
| 1 | 28.7 (28.7) | 28.3 (28.3) | 28.8 (28.8) | 28.8 (28.8) | 0.13-0.15 s |
| 2 | 54.1 (27.1) | 52.5 (26.3) | 53.2 (26.6) | 54.0 (27.0) | 0.19-0.23 s |

Engine rounds (ruler-fresh):

| streams | tokens a round | drafts a round | accepted | ms a round | requests |
|---:|---:|---:|---:|---:|---:|
| 1 | 1.005 | 0.017 | 0% | 35.06 | 12 |
| 2 | 1.022 | 0.051 | 34% | 38.25 | 25 |

### ruler-after

| streams | prose total (a stream) | code total (a stream) | structured total (a stream) | list total (a stream) | first token |
|---:|---:|---:|---:|---:|---:|
| 1 | 28.7 (28.7) | 28.3 (28.3) | 28.7 (28.7) | 28.7 (28.7) | 0.13-0.15 s |

Engine rounds (ruler-after):

| streams | tokens a round | drafts a round | accepted | ms a round | requests |
|---:|---:|---:|---:|---:|---:|
| 1 | 1.007 | 0.023 | 10% | 35.19 | 13 |

### checks

| check | result |
|---|---|
| memory-idle | measured: mac: System-wide memory free percentage: 47%; total = 4096.00M  us |
| turns | pass: resumed == again: True; cold (after a restart): True; cached 5493 of 5649; ttft resumed 0.256s, cold 4.461s |
| memory-busy | measured: mac: System-wide memory free percentage: 48%; total = 4096.00M  us |

## 2026-10-26 08:02: run `20261026-080253-quick`

Plan quick, done; served as `nanbeige`.

Serving: engine_commit `fa5b1f989`; binary_sha256 `70f5a3c2a635a8d9ddd59cf5e751c38c9cf28faf407348046efd60a14716e3a8`; served_model `{"object": "list", "data": [{"id": "nanbeige", "object": "model", "created": 1793019781, "`; chip `Apple M5 Ultra; 274877906944`; suite_commit `277c842a1481`

### ruler-fresh

| streams | prose total (a stream) | code total (a stream) | structured total (a stream) | list total (a stream) | first token |
|---:|---:|---:|---:|---:|---:|
| 1 | 28.9 (28.9) | 28.4 (28.4) | 28.9 (28.9) | 28.9 (28.9) | 0.13-0.15 s |

Engine rounds (ruler-fresh):

| streams | tokens a round | drafts a round | accepted | ms a round | requests |
|---:|---:|---:|---:|---:|---:|
| 1 | 1.005 | 0.017 | 0% | 34.92 | 12 |

### ruler-after

| streams | prose total (a stream) | code total (a stream) | structured total (a stream) | list total (a stream) | first token |
|---:|---:|---:|---:|---:|---:|
| 1 | 28.8 (28.8) | 28.4 (28.4) | 28.9 (28.9) | 28.8 (28.8) | 0.13-0.15 s |

Engine rounds (ruler-after):

| streams | tokens a round | drafts a round | accepted | ms a round | requests |
|---:|---:|---:|---:|---:|---:|
| 1 | 1.007 | 0.023 | 10% | 35.06 | 13 |

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
| memory-idle | measured: mac: System-wide memory free percentage: 47%; total = 5120.00M  us |
| structured | pass: 18/18 obey, drafted == plain 12/12; a bad regex -> 400 |
| tools | pass: 5/5 tool cases right |
| sampling | pass: 9/9 seeded replies equal on repeat and undrafted; 0 errors |
| turns | pass: resumed == again: True; cold (after a restart): True; cached 5493 of 5649; ttft resumed 0.257s, cold 4.489s |

