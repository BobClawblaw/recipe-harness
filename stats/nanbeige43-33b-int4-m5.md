# Nanbeige4.3-33B-INT4, int4 g32 (QAT) on 1x Apple M5 Ultra (256 GB unified), macOS

Target `nanbeige43-33b-int4-m5`: Nanbeige4.3-33B-INT4 as released (QAT int4 g32), TensorFold native Metal (llama) on one M5 Ultra (131072-token window, 2 streams). Engine: TensorFold native, Metal. Rendered from `stats/nanbeige43-33b-int4-m5.json` (6 runs); aggregate tok/s, total (a stream).

## 2026-10-31 14:07: run `20261031-140754-prefill-64k`

Plan prefill-64k, done; served as `nanbeige`.

Serving: engine_commit `a110eeee6`; binary_sha256 `e06dd8097c8bf9a9e6b8ec006c1d516182bf034c8c60ccd4fcb1048833a93741`; served_model `{"object": "list", "data": [{"id": "nanbeige", "object": "model", "created": 1793473682, "`; chip `Apple M5 Ultra; 274877906944`; suite_commit `21db9b23f7be`

### checks

| check | result |
|---|---|
| memory-idle | measured: mac: System-wide memory free percentage: 85%; total = 1024.00M  us |
| prefill-off | measured: 2109 tokens 1184.8 tok/s (1.78 s), 8254 tokens 1256.9 tok/s (6.567 s), 32829 tokens 1040.5 tok/s (31.55 s), 61501 tokens 846.0 tok/s (72.698 s) |
| prefill-thinking | measured: 2107 tokens 1178.4 tok/s (1.788 s), 8249 tokens 1235.1 tok/s (6.679 s), 32824 tokens 1024.6 tok/s (32.035 s), 61498 tokens 816.7 tok/s (75.302 s) |
| memory-busy | measured: mac: System-wide memory free percentage: 81%; total = 1024.00M  us |

## 2026-10-31 14:03: run `20261031-140344-speed`

Plan speed, done; served as `nanbeige`.

Serving: engine_commit `a110eeee6`; binary_sha256 `e06dd8097c8bf9a9e6b8ec006c1d516182bf034c8c60ccd4fcb1048833a93741`; served_model `{"object": "list", "data": [{"id": "nanbeige", "object": "model", "created": 1793473432, "`; chip `Apple M5 Ultra; 274877906944`; suite_commit `21db9b23f7be`

### ruler-fresh

| streams | prose total (a stream) | code total (a stream) | structured total (a stream) | list total (a stream) | first token |
|---:|---:|---:|---:|---:|---:|
| 1 | 42.8 (42.8) | 42.0 (42.0) | 42.9 (42.9) | 41.4 (41.4) | 0.27-0.30 s |
| 2 | 74.6 (37.3) | 53.4 (26.7) | 66.6 (33.3) | 74.7 (37.4) | 0.41-0.45 s |

Engine rounds (ruler-fresh):

| streams | tokens a round | drafts a round | accepted | ms a round | requests |
|---:|---:|---:|---:|---:|---:|
| 1 | 1.005 | 0.017 | 0% | 23.75 | 12 |
| 2 | 1.023 | 0.059 | 30% | 30.38 | 25 |

### ruler-after

| streams | prose total (a stream) | code total (a stream) | structured total (a stream) | list total (a stream) | first token |
|---:|---:|---:|---:|---:|---:|
| 1 | 43.0 (43.0) | 42.1 (42.1) | 43.0 (43.0) | 43.0 (43.0) | 0.27-0.30 s |

Engine rounds (ruler-after):

| streams | tokens a round | drafts a round | accepted | ms a round | requests |
|---:|---:|---:|---:|---:|---:|
| 1 | 1.01 | 0.023 | 23% | 23.61 | 13 |

### checks

| check | result |
|---|---|
| memory-idle | measured: mac: System-wide memory free percentage: 85%; total = 1024.00M  us |
| turns | pass: resumed == again: True; cold (after a restart): True; cached 5493 of 5649; ttft resumed 0.392s, cold 4.584s |
| memory-busy | measured: mac: System-wide memory free percentage: 86%; total = 1024.00M  us |

## 2026-10-31 13:44: run `20261031-134414-quick`

Plan quick, done; served as `nanbeige`.

Serving: engine_commit `a110eeee6`; binary_sha256 `e06dd8097c8bf9a9e6b8ec006c1d516182bf034c8c60ccd4fcb1048833a93741`; served_model `{"object": "list", "data": [{"id": "nanbeige", "object": "model", "created": 1793472262, "`; chip `Apple M5 Ultra; 274877906944`; suite_commit `21db9b23f7be`

### ruler-fresh

| streams | prose total (a stream) | code total (a stream) | structured total (a stream) | list total (a stream) | first token |
|---:|---:|---:|---:|---:|---:|
| 1 | 39.9 (39.9) | 42.0 (42.0) | 42.9 (42.9) | 42.8 (42.8) | 0.27-0.30 s |

Engine rounds (ruler-fresh):

| streams | tokens a round | drafts a round | accepted | ms a round | requests |
|---:|---:|---:|---:|---:|---:|
| 1 | 1.005 | 0.017 | 0% | 23.98 | 12 |

### ruler-after

| streams | prose total (a stream) | code total (a stream) | structured total (a stream) | list total (a stream) | first token |
|---:|---:|---:|---:|---:|---:|
| 1 | 43.0 (43.0) | 22.3 (22.3) | 9.9 (9.9) | 18.8 (18.8) | 0.27-0.81 s |

Engine rounds (ruler-after):

| streams | tokens a round | drafts a round | accepted | ms a round | requests |
|---:|---:|---:|---:|---:|---:|
| 1 | 1.01 | 0.023 | 23% | 42.99 | 13 |

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
| memory-idle | measured: mac: System-wide memory free percentage: 86%; total = 1024.00M  us |
| structured | pass: 18/18 obey, drafted == plain 12/12; a bad regex -> 400 |
| tools | pass: 5/5 tool cases right |
| sampling | pass: 9/9 seeded replies equal on repeat and undrafted; 0 errors |
| turns | pass: resumed == again: True; cold (after a restart): True; cached 5493 of 5649; ttft resumed 0.381s, cold 4.704s |

## 2026-10-31 11:53: run `20261031-115302-prefill-64k`

Plan prefill-64k, done; served as `nanbeige`.

Serving: engine_commit `eb8ce29dd`; binary_sha256 `286415df04c2c00bf96cd2abab78b14c3b44ed97da85d6990a877cd94d6c51a5`; served_model `{"object": "list", "data": [{"id": "nanbeige", "object": "model", "created": 1793465590, "`; chip `Apple M5 Ultra; 274877906944`; suite_commit `21db9b23f7be`

### checks

| check | result |
|---|---|
| memory-idle | measured: mac: System-wide memory free percentage: 85%; total = 1024.00M  us |
| prefill-off | measured: 2110 tokens 1154.3 tok/s (1.828 s), 8253 tokens 1167.2 tok/s (7.071 s), 32828 tokens 929.3 tok/s (35.327 s), 61502 tokens 770.1 tok/s (79.863 s) |
| prefill-thinking | measured: 2104 tokens 1001.9 tok/s (2.1 s), 8250 tokens 985.9 tok/s (8.368 s), 32824 tokens 835.0 tok/s (39.31 s), 61499 tokens 736.7 tok/s (83.484 s) |
| memory-busy | measured: mac: System-wide memory free percentage: 77%; total = 1024.00M  us |

## 2026-10-31 11:48: run `20261031-114848-speed`

Plan speed, done; served as `nanbeige`.

Serving: engine_commit `eb8ce29dd`; binary_sha256 `286415df04c2c00bf96cd2abab78b14c3b44ed97da85d6990a877cd94d6c51a5`; served_model `{"object": "list", "data": [{"id": "nanbeige", "object": "model", "created": 1793465336, "`; chip `Apple M5 Ultra; 274877906944`; suite_commit `21db9b23f7be`

### ruler-fresh

| streams | prose total (a stream) | code total (a stream) | structured total (a stream) | list total (a stream) | first token |
|---:|---:|---:|---:|---:|---:|
| 1 | 42.9 (42.9) | 41.4 (41.4) | 41.3 (41.3) | 41.4 (41.4) | 0.27-0.30 s |
| 2 | 74.7 (37.3) | 52.6 (26.3) | 73.8 (36.9) | 74.5 (37.3) | 0.41-0.46 s |

Engine rounds (ruler-fresh):

| streams | tokens a round | drafts a round | accepted | ms a round | requests |
|---:|---:|---:|---:|---:|---:|
| 1 | 1.005 | 0.017 | 0% | 24.05 | 12 |
| 2 | 1.023 | 0.059 | 30% | 29.69 | 25 |

### ruler-after

| streams | prose total (a stream) | code total (a stream) | structured total (a stream) | list total (a stream) | first token |
|---:|---:|---:|---:|---:|---:|
| 1 | 42.8 (42.8) | 41.7 (41.7) | 41.1 (41.1) | 41.2 (41.2) | 0.27-0.31 s |

Engine rounds (ruler-after):

| streams | tokens a round | drafts a round | accepted | ms a round | requests |
|---:|---:|---:|---:|---:|---:|
| 1 | 1.01 | 0.023 | 23% | 24.23 | 13 |

### checks

| check | result |
|---|---|
| memory-idle | measured: mac: System-wide memory free percentage: 85%; total = 1024.00M  us |
| turns | pass: resumed == again: True; cold (after a restart): True; cached 5493 of 5649; ttft resumed 0.398s, cold 4.623s |
| memory-busy | measured: mac: System-wide memory free percentage: 85%; total = 1024.00M  us |

## 2026-10-31 11:03: run `20261031-110349-quick`

Plan quick, done; served as `nanbeige`.

Serving: engine_commit `eb8ce29dd`; binary_sha256 `286415df04c2c00bf96cd2abab78b14c3b44ed97da85d6990a877cd94d6c51a5`; served_model `{"object": "list", "data": [{"id": "nanbeige", "object": "model", "created": 1793462638, "`; chip `Apple M5 Ultra; 274877906944`; suite_commit `21db9b23f7be`

### ruler-fresh

| streams | prose total (a stream) | code total (a stream) | structured total (a stream) | list total (a stream) | first token |
|---:|---:|---:|---:|---:|---:|
| 1 | 40.9 (40.9) | 40.8 (40.8) | 42.8 (42.8) | 41.5 (41.5) | 0.27-0.31 s |

Engine rounds (ruler-fresh):

| streams | tokens a round | drafts a round | accepted | ms a round | requests |
|---:|---:|---:|---:|---:|---:|
| 1 | 1.005 | 0.017 | 0% | 24.2 | 12 |

### ruler-after

| streams | prose total (a stream) | code total (a stream) | structured total (a stream) | list total (a stream) | first token |
|---:|---:|---:|---:|---:|---:|
| 1 | 40.0 (40.0) | 39.5 (39.5) | 42.0 (42.0) | 41.0 (41.0) | 0.28-0.32 s |

Engine rounds (ruler-after):

| streams | tokens a round | drafts a round | accepted | ms a round | requests |
|---:|---:|---:|---:|---:|---:|
| 1 | 1.01 | 0.023 | 23% | 24.86 | 13 |

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
| memory-idle | measured: mac: System-wide memory free percentage: 85%; total = 1024.00M  us |
| structured | pass: 18/18 obey, drafted == plain 12/12; a bad regex -> 400 |
| tools | pass: 5/5 tool cases right |
| sampling | pass: 9/9 seeded replies equal on repeat and undrafted; 0 errors |
| turns | pass: resumed == again: True; cold (after a restart): True; cached 5493 of 5649; ttft resumed 0.531s, cold 5.76s |

