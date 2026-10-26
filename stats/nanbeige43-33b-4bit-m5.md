# Nanbeige4.3-33B, affine 4bit on 1x Apple M5 Ultra (256 GB unified), macOS

Target `nanbeige43-33b-4bit-m5`: Nanbeige4.3-33B MLX affine 4bit (llama_convert.py), TensorFold native Metal (llama) on one M5 Ultra (131072-token window, 2 streams). Engine: TensorFold native, Metal. Rendered from `stats/nanbeige43-33b-4bit-m5.json` (3 runs); aggregate tok/s, total (a stream).

## 2026-10-26 09:06: run `20261026-090633-prefill-64k`

Plan prefill-64k, done; served as `nanbeige`.

Serving: engine_commit `c0243b7e3`; binary_sha256 `70f5a3c2a635a8d9ddd59cf5e751c38c9cf28faf407348046efd60a14716e3a8`; served_model `{"object": "list", "data": [{"id": "nanbeige", "object": "model", "created": 1793023602, "`; chip `Apple M5 Ultra; 274877906944`; suite_commit `277c842a1481`

### checks

| check | result |
|---|---|
| memory-idle | measured: mac: System-wide memory free percentage: 53%; total = 4096.00M  us |
| prefill-off | measured: 2109 tokens 1344.2 tok/s (1.569 s), 8253 tokens 1312.3 tok/s (6.289 s), 32831 tokens 1043.6 tok/s (31.459 s), 61500 tokens 836.2 tok/s (73.544 s) |
| prefill-thinking | measured: 2106 tokens 1357.8 tok/s (1.551 s), 8247 tokens 1292.0 tok/s (6.383 s), 32824 tokens 1016.1 tok/s (32.303 s), 61498 tokens 788.1 tok/s (78.034 s) |
| memory-busy | measured: mac: System-wide memory free percentage: 46%; total = 4096.00M  us |

## 2026-10-26 09:03: run `20261026-090304-speed`

Plan speed, done; served as `nanbeige`.

Serving: engine_commit `c0243b7e3`; binary_sha256 `70f5a3c2a635a8d9ddd59cf5e751c38c9cf28faf407348046efd60a14716e3a8`; served_model `{"object": "list", "data": [{"id": "nanbeige", "object": "model", "created": 1793023392, "`; chip `Apple M5 Ultra; 274877906944`; suite_commit `277c842a1481`

### ruler-fresh

| streams | prose total (a stream) | code total (a stream) | structured total (a stream) | list total (a stream) | first token |
|---:|---:|---:|---:|---:|---:|
| 1 | 48.5 (48.5) | 47.9 (47.9) | 48.7 (48.7) | 48.6 (48.6) | 0.10-0.12 s |
| 2 | 84.8 (42.4) | 81.3 (40.6) | 84.1 (42.1) | 84.7 (42.4) | 0.16-0.18 s |

Engine rounds (ruler-fresh):

| streams | tokens a round | drafts a round | accepted | ms a round | requests |
|---:|---:|---:|---:|---:|---:|
| 1 | 1.011 | 0.034 | 20% | 20.89 | 12 |
| 2 | 1.022 | 0.05 | 34% | 24.41 | 25 |

### ruler-after

| streams | prose total (a stream) | code total (a stream) | structured total (a stream) | list total (a stream) | first token |
|---:|---:|---:|---:|---:|---:|
| 1 | 48.3 (48.3) | 47.6 (47.6) | 48.4 (48.4) | 48.3 (48.3) | 0.10-0.12 s |

Engine rounds (ruler-after):

| streams | tokens a round | drafts a round | accepted | ms a round | requests |
|---:|---:|---:|---:|---:|---:|
| 1 | 1.02 | 0.045 | 32% | 21.17 | 13 |

### checks

| check | result |
|---|---|
| memory-idle | measured: mac: System-wide memory free percentage: 53%; total = 4096.00M  us |
| turns | pass: resumed == again: True; cold (after a restart): True; cached 5493 of 5649; ttft resumed 0.217s, cold 4.247s |
| memory-busy | measured: mac: System-wide memory free percentage: 53%; total = 4096.00M  us |

## 2026-10-26 08:49: run `20261026-084932-quick`

Plan quick, done; served as `nanbeige`.

Serving: engine_commit `c0243b7e3`; binary_sha256 `70f5a3c2a635a8d9ddd59cf5e751c38c9cf28faf407348046efd60a14716e3a8`; served_model `{"object": "list", "data": [{"id": "nanbeige", "object": "model", "created": 1793022580, "`; chip `Apple M5 Ultra; 274877906944`; suite_commit `277c842a1481`

### ruler-fresh

| streams | prose total (a stream) | code total (a stream) | structured total (a stream) | list total (a stream) | first token |
|---:|---:|---:|---:|---:|---:|
| 1 | 48.8 (48.8) | 48.1 (48.1) | 48.8 (48.8) | 48.8 (48.8) | 0.10-0.12 s |

Engine rounds (ruler-fresh):

| streams | tokens a round | drafts a round | accepted | ms a round | requests |
|---:|---:|---:|---:|---:|---:|
| 1 | 1.011 | 0.034 | 20% | 20.8 | 12 |

### ruler-after

| streams | prose total (a stream) | code total (a stream) | structured total (a stream) | list total (a stream) | first token |
|---:|---:|---:|---:|---:|---:|
| 1 | 48.7 (48.7) | 48.0 (48.0) | 48.7 (48.7) | 48.7 (48.7) | 0.10-0.12 s |

Engine rounds (ruler-after):

| streams | tokens a round | drafts a round | accepted | ms a round | requests |
|---:|---:|---:|---:|---:|---:|
| 1 | 1.02 | 0.045 | 32% | 21.01 | 13 |

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
| memory-idle | measured: mac: System-wide memory free percentage: 54%; total = 4096.00M  us |
| structured | pass: 18/18 obey, drafted == plain 12/12; a bad regex -> 400 |
| tools | pass: 5/5 tool cases right |
| sampling | pass: 9/9 seeded replies equal on repeat and undrafted; 0 errors |
| turns | pass: resumed == again: True; cold (after a restart): True; cached 5493 of 5649; ttft resumed 0.219s, cold 4.137s |

