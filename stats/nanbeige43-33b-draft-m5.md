# Nanbeige4.3-33B bf16, drafted by Nanbeige4.1-3B 4-bit on 1x Apple M5 Ultra (256 GB unified), macOS

Target `nanbeige43-33b-draft-m5`: Nanbeige4.3-33B bf16 with Nanbeige4.1-3B 4-bit drafting, TensorFold native Metal (llama) on one M5 Ultra (131072-token window, 2 streams). Engine: TensorFold native, Metal. Rendered from `stats/nanbeige43-33b-draft-m5.json` (4 runs); aggregate tok/s, total (a stream).

## 2026-10-26 12:17: run `20261026-121700-speed`

Plan speed, done; served as `nanbeige`.

Serving: engine_commit `e1f447bf3`; binary_sha256 `7d06edafe546ae55db81fedc6936810b80219413aac64c847573b4681f8a4674`; served_model `{"object": "list", "data": [{"id": "nanbeige", "object": "model", "created": 1793035033, "`; chip `Apple M5 Ultra; 274877906944`; suite_commit `277c842a1481`

### ruler-fresh

| streams | prose total (a stream) | code total (a stream) | structured total (a stream) | list total (a stream) | first token |
|---:|---:|---:|---:|---:|---:|
| 1 | 113.5 (113.5) | 111.0 (111.0) | 108.5 (108.5) | 84.9 (84.9) | 0.23-0.26 s |
| 2 | 63.3 (31.6) | 64.3 (32.1) | 63.8 (31.9) | 58.3 (29.2) | 0.35-0.39 s |

Engine rounds (ruler-fresh):

| streams | tokens a round | drafts a round | accepted | ms a round | requests |
|---:|---:|---:|---:|---:|---:|
| 1 | 4.92 | 4.831 | 81% | 47.08 | 12 |
| 2 | 2.716 | 2.116 | 81% | 87.01 | 25 |

### ruler-after

| streams | prose total (a stream) | code total (a stream) | structured total (a stream) | list total (a stream) | first token |
|---:|---:|---:|---:|---:|---:|
| 1 | 110.5 (110.5) | 108.5 (108.5) | 109.3 (109.3) | 90.0 (90.0) | 0.23-0.26 s |

Engine rounds (ruler-after):

| streams | tokens a round | drafts a round | accepted | ms a round | requests |
|---:|---:|---:|---:|---:|---:|
| 1 | 4.847 | 4.736 | 81% | 46.35 | 13 |

### checks

| check | result |
|---|---|
| memory-idle | measured: mac: System-wide memory free percentage: 33%; total = 5120.00M  us |
| turns | pass: resumed == again: True; cold (after a restart): True; cached 5493 of 5649; ttft resumed 0.344s, cold 4.491s |
| memory-busy | measured: mac: System-wide memory free percentage: 32%; total = 5120.00M  us |

## 2026-10-26 11:52: run `20261026-115252-quick`

Plan quick, done; served as `nanbeige`.

Serving: engine_commit `e1f447bf3`; binary_sha256 `7d06edafe546ae55db81fedc6936810b80219413aac64c847573b4681f8a4674`; served_model `{"object": "list", "data": [{"id": "nanbeige", "object": "model", "created": 1793033585, "`; chip `Apple M5 Ultra; 274877906944`; suite_commit `277c842a1481`

### ruler-fresh

| streams | prose total (a stream) | code total (a stream) | structured total (a stream) | list total (a stream) | first token |
|---:|---:|---:|---:|---:|---:|
| 1 | 113.7 (113.7) | 108.6 (108.6) | 109.6 (109.6) | 100.8 (100.8) | 0.23-0.26 s |

Engine rounds (ruler-fresh):

| streams | tokens a round | drafts a round | accepted | ms a round | requests |
|---:|---:|---:|---:|---:|---:|
| 1 | 4.976 | 4.871 | 81% | 45.99 | 12 |

### ruler-after

| streams | prose total (a stream) | code total (a stream) | structured total (a stream) | list total (a stream) | first token |
|---:|---:|---:|---:|---:|---:|
| 1 | 113.7 (113.7) | 110.9 (110.9) | 111.6 (111.6) | 98.7 (98.7) | 0.23-0.26 s |

Engine rounds (ruler-after):

| streams | tokens a round | drafts a round | accepted | ms a round | requests |
|---:|---:|---:|---:|---:|---:|
| 1 | 4.77 | 4.602 | 82% | 43.88 | 13 |

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
| memory-idle | measured: mac: System-wide memory free percentage: 32%; total = 6144.00M  us |
| structured | pass: 18/18 obey, drafted == plain 12/12; a bad regex -> 400 |
| tools | pass: 5/5 tool cases right |
| sampling | pass: 9/9 seeded replies equal on repeat and undrafted; 0 errors |
| turns | pass: resumed == again: True; cold (after a restart): True; cached 5493 of 5649; ttft resumed 0.345s, cold 4.438s |

## 2026-10-26 11:44: run `20261026-114400-speed`

Plan speed, running; served as `nanbeige`.

Serving: engine_commit `e1f447bf3`; binary_sha256 `5311c6484055f2103acd54fc1173c1d156255f7ab259a732ed71ff34a10e04f5`; served_model `{"object": "list", "data": [{"id": "nanbeige", "object": "model", "created": 1793033083, "`; chip `Apple M5 Ultra; 274877906944`; suite_commit `277c842a1481`

### checks

| check | result |
|---|---|
| memory-idle | measured: mac: System-wide memory free percentage: 68%; total = 7168.00M  us |

## 2026-10-26 11:21: run `20261026-112114-quick`

Plan quick, done; served as `nanbeige`.

Serving: engine_commit `e1f447bf3`; binary_sha256 `5311c6484055f2103acd54fc1173c1d156255f7ab259a732ed71ff34a10e04f5`; served_model `{"object": "list", "data": [{"id": "nanbeige", "object": "model", "created": 1793031707, "`; chip `Apple M5 Ultra; 274877906944`; suite_commit `277c842a1481`

### ruler-fresh

| streams | prose total (a stream) | code total (a stream) | structured total (a stream) | list total (a stream) | first token |
|---:|---:|---:|---:|---:|---:|
| 1 | 110.4 (110.4) | 102.5 (102.5) | 101.8 (101.8) | 102.0 (102.0) | 0.23-0.26 s |

Engine rounds (ruler-fresh):

| streams | tokens a round | drafts a round | accepted | ms a round | requests |
|---:|---:|---:|---:|---:|---:|
| 1 | 4.669 | 4.472 | 82% | 44.82 | 12 |

### ruler-after

| streams | prose total (a stream) | code total (a stream) | structured total (a stream) | list total (a stream) | first token |
|---:|---:|---:|---:|---:|---:|
| 1 | 116.7 (116.7) | 110.9 (110.9) | 99.3 (99.3) | 41.4 (41.4) | 0.23-0.26 s |

Engine rounds (ruler-after):

| streams | tokens a round | drafts a round | accepted | ms a round | requests |
|---:|---:|---:|---:|---:|---:|
| 1 | 4.252 | 3.888 | 83% | 46.17 | 13 |

### suite

| check | passed |
|---|---:|
| soak | 57/60 |
| drafts | 0/0 |
| concurrent | 0/0 |
| behaviour | 0/0 |

### checks

| check | result |
|---|---|
| memory-idle | measured: mac: System-wide memory free percentage: 12%; total = 5120.00M  us |
| structured | pass: 18/18 obey, drafted == plain 12/12; a bad regex -> 400 |
| tools | pass: 5/5 tool cases right |
| sampling | pass: 9/9 seeded replies equal on repeat and undrafted; 0 errors |
| turns | pass: resumed == again: True; cold (after a restart): True; cached 5493 of 5649; ttft resumed 0.363s, cold 4.436s |

