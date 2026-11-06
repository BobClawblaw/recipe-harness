# ricursiveAI Ripple-65B-Preview (bf16) on 1x Apple M5 Ultra (256 GB unified), macOS

Target `ripple-65b-m5`: ricursiveAI Ripple-65B-Preview, bf16 release, TensorFold native Metal on one M5 Ultra. Engine: TensorFold native, Metal. Rendered from `stats/ripple-65b-m5.json` (4 runs); aggregate tok/s, total (a stream).

## 2026-11-06 04:51: run `20261106-045115-speed`

Plan speed, done; served as `ripple`.

Serving: engine_commit `b7ff7854f`; binary_sha256 `40cade17c2254999237c082761470cdf70982a6a02e5ec3658fdb6fe9bc17016`; served_model `{"object": "list", "data": [{"id": "ripple", "object": "model", "created": 1793962340, "ow`; chip `Apple M5 Ultra; 274877906944`; suite_commit `21db9b23f7be`

### ruler-fresh

| streams | prose total (a stream) | code total (a stream) | structured total (a stream) | list total (a stream) | first token |
|---:|---:|---:|---:|---:|---:|
| 1 | 6.4 (6.4) | 6.4 (6.4) | 6.4 (6.4) | 6.4 (6.4) | 0.52-1.20 s |
| 2 | 13.6 (6.8) | 13.6 (6.8) | 13.4 (6.7) | 13.7 (6.9) | 0.79-1.78 s |

Engine rounds (ruler-fresh):

| streams | tokens a round | drafts a round | accepted | ms a round | requests |
|---:|---:|---:|---:|---:|---:|
| 1 | 1.007 | 0.0 |  | 157.24 | 12 |
| 2 | 1.007 | 0.01 | 8% | 148.42 | 25 |

### ruler-after

| streams | prose total (a stream) | code total (a stream) | structured total (a stream) | list total (a stream) | first token |
|---:|---:|---:|---:|---:|---:|
| 1 | 6.4 (6.4) | 6.4 (6.4) | 6.5 (6.5) | 6.4 (6.4) | 0.52-1.18 s |

Engine rounds (ruler-after):

| streams | tokens a round | drafts a round | accepted | ms a round | requests |
|---:|---:|---:|---:|---:|---:|
| 1 | 1.007 | 0.0 |  | 156.64 | 13 |

### checks

| check | result |
|---|---|
| memory-idle | measured: mac: System-wide memory free percentage: 27%; total = 6144.00M  us |
| turns | pass: resumed == again: True; cold (after a restart): True; cached 4513 of 4597; ttft resumed 0.626s, cold 7.541s |
| memory-busy | measured: mac: System-wide memory free percentage: 25%; total = 6144.00M  us |

## 2026-11-05 03:12: run `20261105-031234-prefill`

Plan prefill, done; served as `ripple`.

Serving: engine_commit `98743a975`; binary_sha256 `cf15bebca5c5f0bd89ff4f9a1ffad672c7bc3ebecbfdcd869a286ebbaf6794ea`; served_model `{"object": "list", "data": [{"id": "ripple", "object": "model", "created": 1793869979, "ow`; chip `Apple M5 Ultra; 274877906944`; suite_commit `21db9b23f7be`

### checks

| check | result |
|---|---|
| memory-idle | measured: mac: System-wide memory free percentage: 42%; total = 6144.00M  us |
| prefill-off | FAIL: ; not cold or failed: ['2048', '8192', '32768', '131072'] |
| prefill-thinking | measured: 2206 tokens 518.6 tok/s (4.254 s), 8830 tokens 596.1 tok/s (14.812 s), 34931 tokens 586.4 tok/s (59.567 s), 139870 tokens 459.0 tok/s (304.719 s) |
| memory-busy | measured: mac: System-wide memory free percentage: 38%; total = 6144.00M  us |

## 2026-11-05 02:52: run `20261105-025221-speed`

Plan speed, done; served as `ripple`.

Serving: engine_commit `98743a975`; binary_sha256 `cf15bebca5c5f0bd89ff4f9a1ffad672c7bc3ebecbfdcd869a286ebbaf6794ea`; served_model `{"object": "list", "data": [{"id": "ripple", "object": "model", "created": 1793868767, "ow`; chip `Apple M5 Ultra; 274877906944`; suite_commit `21db9b23f7be`

### ruler-fresh

| streams | prose total (a stream) | code total (a stream) | structured total (a stream) | list total (a stream) | first token |
|---:|---:|---:|---:|---:|---:|
| 1 | 5.8 (5.8) | 5.0 (5.0) | 4.9 (4.9) | 5.0 (5.0) | 0.51-1.30 s |
| 2 | 11.5 (5.8) | 11.0 (5.5) | 10.5 (5.2) | 11.8 (5.9) | 0.86-1.81 s |

Engine rounds (ruler-fresh):

| streams | tokens a round | drafts a round | accepted | ms a round | requests |
|---:|---:|---:|---:|---:|---:|
| 1 | 1.007 | 0.0 |  | 194.68 | 12 |
| 2 | 1.007 | 0.01 | 8% | 179.58 | 25 |

### ruler-after

| streams | prose total (a stream) | code total (a stream) | structured total (a stream) | list total (a stream) | first token |
|---:|---:|---:|---:|---:|---:|
| 1 | 5.8 (5.8) | 4.4 (4.4) | 4.9 (4.9) | 5.3 (5.3) | 0.52-1.19 s |

Engine rounds (ruler-after):

| streams | tokens a round | drafts a round | accepted | ms a round | requests |
|---:|---:|---:|---:|---:|---:|
| 1 | 1.007 | 0.0 |  | 197.23 | 13 |

### checks

| check | result |
|---|---|
| memory-idle | measured: mac: System-wide memory free percentage: 42%; total = 6144.00M  us |
| turns | pass: resumed == again: True; cold (after a restart): True; cached 4513 of 4597; ttft resumed 0.587s, cold 7.535s |
| memory-busy | measured: mac: System-wide memory free percentage: 42%; total = 6144.00M  us |

## 2026-11-04 16:37: run `20261104-163709-quick`

Plan quick, running; served as `ripple`.

Serving: engine_commit `256414900`; binary_sha256 `85fe8ccf0afd7c3353d0e01cfc052fe953b866e0b9932aa619e44ee9d28aea26`; served_model `{"object": "list", "data": [{"id": "ripple", "object": "model", "created": 1793831854, "ow`; chip `Apple M5 Ultra; 274877906944`; suite_commit `21db9b23f7be`

### ruler-fresh

| streams | prose total (a stream) | code total (a stream) | structured total (a stream) | list total (a stream) | first token |
|---:|---:|---:|---:|---:|---:|
| 1 | 6.4 (6.4) | 6.5 (6.5) | 6.3 (6.3) | 6.2 (6.2) | 0.52-1.19 s |

Engine rounds (ruler-fresh):

| streams | tokens a round | drafts a round | accepted | ms a round | requests |
|---:|---:|---:|---:|---:|---:|
| 1 | 1.007 | 0.0 |  | 158.48 | 12 |

### ruler-after

| streams | prose total (a stream) | code total (a stream) | structured total (a stream) | list total (a stream) | first token |
|---:|---:|---:|---:|---:|---:|
| 1 | 6.5 (6.5) | 6.4 (6.4) | 6.1 (6.1) | 6.3 (6.3) | 0.51-1.18 s |

Engine rounds (ruler-after):

| streams | tokens a round | drafts a round | accepted | ms a round | requests |
|---:|---:|---:|---:|---:|---:|
| 1 | 1.007 | 0.0 |  | 159.51 | 13 |

### checks

| check | result |
|---|---|
| memory-idle | measured: mac: System-wide memory free percentage: 41%; total = 6144.00M  us |
| structured | pass: 18/18 obey, drafted == plain 12/12; a bad regex -> 400 |
| tools | pass: 5/5 tool cases right |
| sampling | pass: 9/9 seeded replies equal on repeat and undrafted; 0 errors |
| turns | pass: resumed == again: True; cold (after a restart): True; cached 4513 of 4597; ttft resumed 0.596s, cold 7.582s |
| urls | FAIL: public 400; loopback 400; http 400; unexpected: ['public'] |

