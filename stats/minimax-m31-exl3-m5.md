# MiniMax-M3.1-Flash, EXL3 3.06 bpw (Mia-AiLab EAQ v1), 256k context on 1x Apple M5 Ultra (256 GB unified), macOS

Target `minimax-m31-exl3-m5`: MiniMax-M3.1-Flash, EXL3 3.06 bpw (Mia-AiLab EAQ v1), 256k context, TensorFold native Metal on one M5 Ultra. Engine: TensorFold native, Metal. Rendered from `stats/minimax-m31-exl3-m5.json` (33 runs); aggregate tok/s, total (a stream).

## 2026-10-29 18:24: run `20261029-182420-minimax-math500`

Plan minimax-math500, done; served as `MiniMax-M3.1-Flash`.

Serving: engine_commit `af3573193`; binary_sha256 `90f54df38bb95056e4520d4d5a2b7c6baec75bcad6190711b9bdedbc813cdb8c`; served_model `{"object": "list", "data": [{"id": "MiniMax-M3.1-Flash", "object": "model", "created": 179`; chip `Apple M5 Ultra; 274877906944`; suite_commit `21db9b23f7be`

### suite

| check | passed |
|---|---:|
| math500 | 422/500 |

### checks

| check | result |
|---|---|
| memory-idle | measured: mac: System-wide memory free percentage: 32%; total = 4096.00M  us |

## 2026-10-29 18:23: run `20261029-182313-glm-vision`

Plan glm-vision, done; served as `MiniMax-M3.1-Flash`.

Serving: engine_commit `af3573193`; binary_sha256 `90f54df38bb95056e4520d4d5a2b7c6baec75bcad6190711b9bdedbc813cdb8c`; served_model `{"object": "list", "data": [{"id": "MiniMax-M3.1-Flash", "object": "model", "created": 179`; chip `Apple M5 Ultra; 274877906944`; suite_commit `21db9b23f7be`

### suite-vision

| check | passed |
|---|---:|
| vision | 3/6 |
| vision-concurrent | 12/16 |

## 2026-10-29 15:57: run `20261029-155719-glm-vision`

Plan glm-vision, done; served as `MiniMax-M3.1-Flash`.

Serving: engine_commit `af3573193`; binary_sha256 `90f54df38bb95056e4520d4d5a2b7c6baec75bcad6190711b9bdedbc813cdb8c`; served_model `{"object": "list", "data": [{"id": "MiniMax-M3.1-Flash", "object": "model", "created": 179`; chip `Apple M5 Ultra; 274877906944`; suite_commit `21db9b23f7be`

### suite-vision

| check | passed |
|---|---:|
| vision | 3/6 |
| vision-concurrent | 12/16 |

## 2026-10-29 15:25: run `20261029-152530-speed`

Plan speed, done; served as `MiniMax-M3.1-Flash`.

Serving: engine_commit `4e9fe87f5`; binary_sha256 `3536f1a7cbfcca045fda8654186a106ca4a46929195281d134df742de8be8af8`; served_model `{"object": "list", "data": [{"id": "MiniMax-M3.1-Flash", "object": "model", "created": 179`; chip `Apple M5 Ultra; 274877906944`; suite_commit `21db9b23f7be`

### ruler-fresh

| streams | prose total (a stream) | code total (a stream) | structured total (a stream) | list total (a stream) | first token |
|---:|---:|---:|---:|---:|---:|
| 1 | 32.1 (32.1) | 33.6 (33.6) | 31.3 (31.3) | 31.6 (31.6) | 1.46-1.54 s |
| 2 | 29.9 (14.9) | 38.6 (19.3) | 31.0 (15.5) | 44.8 (22.4) | 2.19-2.33 s |

Engine rounds (ruler-fresh):

| streams | tokens a round | drafts a round | accepted | ms a round | requests |
|---:|---:|---:|---:|---:|---:|
| 1 | 1.359 | 0.513 | 69% | 42.28 | 12 |
| 2 | 1.669 | 0.959 | 69% | 92.59 | 25 |

### ruler-after

| streams | prose total (a stream) | code total (a stream) | structured total (a stream) | list total (a stream) | first token |
|---:|---:|---:|---:|---:|---:|
| 1 | 31.8 (31.8) | 34.0 (34.0) | 31.2 (31.2) | 32.0 (32.0) | 1.46-1.54 s |

Engine rounds (ruler-after):

| streams | tokens a round | drafts a round | accepted | ms a round | requests |
|---:|---:|---:|---:|---:|---:|
| 1 | 1.364 | 0.522 | 69% | 42.29 | 13 |

### checks

| check | result |
|---|---|
| memory-idle | measured: mac: System-wide memory free percentage: 31%; total = 5120.00M  us |
| turns | pass: resumed == again: True; cold (after a restart): True; cached 4645 of 4725; ttft resumed 1.247s, cold 12.216s |
| memory-busy | measured: mac: System-wide memory free percentage: 31%; total = 5120.00M  us |

## 2026-10-29 15:12: run `20261029-151235-prefill`

Plan prefill, done; served as `MiniMax-M3.1-Flash`.

Serving: engine_commit `4e9fe87f5`; binary_sha256 `3536f1a7cbfcca045fda8654186a106ca4a46929195281d134df742de8be8af8`; served_model `{"object": "list", "data": [{"id": "MiniMax-M3.1-Flash", "object": "model", "created": 179`; chip `Apple M5 Ultra; 274877906944`; suite_commit `21db9b23f7be`

### checks

| check | result |
|---|---|
| memory-idle | measured: mac: System-wide memory free percentage: 31%; total = 5120.00M  us |
| prefill-off | measured: 2219 tokens 422.6 tok/s (5.251 s), 8364 tokens 465.0 tok/s (17.989 s), 32941 tokens 484.6 tok/s (67.973 s), 131244 tokens 477.9 tok/s (274.614 s) |
| prefill-thinking | measured: 2217 tokens 419.8 tok/s (5.281 s), 8362 tokens 462.8 tok/s (18.068 s), 32938 tokens 483.6 tok/s (68.117 s), 131241 tokens 484.5 tok/s (270.897 s) |
| memory-busy | measured: mac: System-wide memory free percentage: 25%; total = 5120.00M  us |

## 2026-10-29 15:04: run `20261029-150422-speed`

Plan speed, done; served as `MiniMax-M3.1-Flash`.

Serving: engine_commit `4e9fe87f5`; binary_sha256 `3536f1a7cbfcca045fda8654186a106ca4a46929195281d134df742de8be8af8`; served_model `{"object": "list", "data": [{"id": "MiniMax-M3.1-Flash", "object": "model", "created": 179`; chip `Apple M5 Ultra; 274877906944`; suite_commit `21db9b23f7be`

### ruler-fresh

| streams | prose total (a stream) | code total (a stream) | structured total (a stream) | list total (a stream) | first token |
|---:|---:|---:|---:|---:|---:|
| 1 | 33.6 (33.6) | 33.5 (33.5) | 33.6 (33.6) | 33.6 (33.6) | 1.51-1.59 s |
| 2 | 31.4 (15.7) | 31.2 (15.6) | 31.3 (15.7) | 30.4 (15.2) | 2.26-2.40 s |

Engine rounds (ruler-fresh):

| streams | tokens a round | drafts a round | accepted | ms a round | requests |
|---:|---:|---:|---:|---:|---:|
| 1 | 1.005 | 0.0 |  | 29.93 | 12 |
| 2 | 1.005 | 0.0 |  | 64.68 | 25 |

### ruler-after

| streams | prose total (a stream) | code total (a stream) | structured total (a stream) | list total (a stream) | first token |
|---:|---:|---:|---:|---:|---:|
| 1 | 33.5 (33.5) | 33.5 (33.5) | 33.6 (33.6) | 33.6 (33.6) | 1.51-1.59 s |

Engine rounds (ruler-after):

| streams | tokens a round | drafts a round | accepted | ms a round | requests |
|---:|---:|---:|---:|---:|---:|
| 1 | 1.005 | 0.0 |  | 29.96 | 13 |

### checks

| check | result |
|---|---|
| memory-idle | measured: mac: System-wide memory free percentage: 31%; total = 5120.00M  us |
| turns | pass: resumed == again: True; cold (after a restart): True; cached 4645 of 4725; ttft resumed 1.287s, cold 11.729s |
| memory-busy | measured: mac: System-wide memory free percentage: 31%; total = 5120.00M  us |

## 2026-10-29 15:03: run `20261029-150312-glm-vision`

Plan glm-vision, done; served as `MiniMax-M3.1-Flash`.

Serving: engine_commit `4e9fe87f5`; binary_sha256 `3536f1a7cbfcca045fda8654186a106ca4a46929195281d134df742de8be8af8`; served_model `{"object": "list", "data": [{"id": "MiniMax-M3.1-Flash", "object": "model", "created": 179`; chip `Apple M5 Ultra; 274877906944`; suite_commit `21db9b23f7be`

### suite-vision

| check | passed |
|---|---:|
| vision | 3/6 |
| vision-concurrent | 12/16 |

## 2026-10-29 14:44: run `20261029-144407-quick`

Plan quick, done; served as `MiniMax-M3.1-Flash`.

Serving: engine_commit `4e9fe87f5`; binary_sha256 `3536f1a7cbfcca045fda8654186a106ca4a46929195281d134df742de8be8af8`; served_model `{"object": "list", "data": [{"id": "MiniMax-M3.1-Flash", "object": "model", "created": 179`; chip `Apple M5 Ultra; 274877906944`; suite_commit `21db9b23f7be`

### ruler-fresh

| streams | prose total (a stream) | code total (a stream) | structured total (a stream) | list total (a stream) | first token |
|---:|---:|---:|---:|---:|---:|
| 1 | 34.6 (34.6) | 34.6 (34.6) | 34.6 (34.6) | 34.6 (34.6) | 1.46-1.54 s |

Engine rounds (ruler-fresh):

| streams | tokens a round | drafts a round | accepted | ms a round | requests |
|---:|---:|---:|---:|---:|---:|
| 1 | 1.005 | 0.0 |  | 29.01 | 12 |

### ruler-after

| streams | prose total (a stream) | code total (a stream) | structured total (a stream) | list total (a stream) | first token |
|---:|---:|---:|---:|---:|---:|
| 1 | 34.5 (34.5) | 34.5 (34.5) | 34.6 (34.6) | 34.6 (34.6) | 1.46-1.55 s |

Engine rounds (ruler-after):

| streams | tokens a round | drafts a round | accepted | ms a round | requests |
|---:|---:|---:|---:|---:|---:|
| 1 | 1.005 | 0.0 |  | 29.09 | 13 |

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
| memory-idle | measured: mac: System-wide memory free percentage: 31%; total = 5120.00M  us |
| structured | pass: 18/18 obey, drafted == plain 12/12; a bad regex -> 400 |
| tools | pass: 5/5 tool cases right |
| sampling | pass: 9/9 seeded replies equal on repeat and undrafted; 0 errors |
| turns | pass: resumed == again: True; cold (after a restart): True; cached 4645 of 4725; ttft resumed 1.262s, cold 11.511s |
| urls | FAIL: public 400; loopback 400; http 400; unexpected: ['public'] |

## 2026-10-29 13:49: run `20261029-134912-speed`

Plan speed, done; served as `MiniMax-M3.1-Flash`.

Serving: engine_commit `af3573193`; binary_sha256 `f23babaf9b934985f1895b469eb673d02dec58626a836c27f481a9ad4a495011`; served_model `{"object": "list", "data": [{"id": "MiniMax-M3.1-Flash", "object": "model", "created": 179`; chip `Apple M5 Ultra; 274877906944`; suite_commit `21db9b23f7be`

### ruler-fresh

| streams | prose total (a stream) | code total (a stream) | structured total (a stream) | list total (a stream) | first token |
|---:|---:|---:|---:|---:|---:|
| 1 | 29.6 (29.6) | 40.1 (40.1) | 31.4 (31.4) | 32.2 (32.2) | 1.49-1.57 s |
| 2 | 37.0 (18.5) | 38.1 (19.0) | 34.1 (17.1) | 41.5 (20.7) | 2.24-2.36 s |

Engine rounds (ruler-fresh):

| streams | tokens a round | drafts a round | accepted | ms a round | requests |
|---:|---:|---:|---:|---:|---:|
| 1 | 1.817 | 1.271 | 64% | 54.5 | 12 |
| 2 | 1.612 | 0.827 | 74% | 85.6 | 25 |

### ruler-after

| streams | prose total (a stream) | code total (a stream) | structured total (a stream) | list total (a stream) | first token |
|---:|---:|---:|---:|---:|---:|
| 1 | 28.2 (28.2) | 40.1 (40.1) | 31.1 (31.1) | 32.4 (32.4) | 1.49-1.57 s |

Engine rounds (ruler-after):

| streams | tokens a round | drafts a round | accepted | ms a round | requests |
|---:|---:|---:|---:|---:|---:|
| 1 | 1.88 | 1.381 | 63% | 56.99 | 13 |

### checks

| check | result |
|---|---|
| memory-idle | measured: mac: System-wide memory free percentage: 33%; total = 5120.00M  us |
| turns | pass: resumed == again: True; cold (after a restart): True; cached 4645 of 4725; ttft resumed 1.276s, cold 11.685s |
| memory-busy | measured: mac: System-wide memory free percentage: 31%; total = 5120.00M  us |

## 2026-10-29 13:36: run `20261029-133649-prefill`

Plan prefill, done; served as `MiniMax-M3.1-Flash`.

Serving: engine_commit `af3573193`; binary_sha256 `f23babaf9b934985f1895b469eb673d02dec58626a836c27f481a9ad4a495011`; served_model `{"object": "list", "data": [{"id": "MiniMax-M3.1-Flash", "object": "model", "created": 179`; chip `Apple M5 Ultra; 274877906944`; suite_commit `21db9b23f7be`

### checks

| check | result |
|---|---|
| memory-idle | measured: mac: System-wide memory free percentage: 34%; total = 5120.00M  us |
| prefill-off | measured: 2219 tokens 442.0 tok/s (5.02 s), 8362 tokens 486.8 tok/s (17.178 s), 32938 tokens 509.0 tok/s (64.708 s), 131243 tokens 503.6 tok/s (260.596 s) |
| prefill-thinking | measured: 2217 tokens 438.9 tok/s (5.051 s), 8361 tokens 487.9 tok/s (17.138 s), 32938 tokens 507.9 tok/s (64.854 s), 131241 tokens 503.3 tok/s (260.771 s) |
| memory-busy | measured: mac: System-wide memory free percentage: 27%; total = 5120.00M  us |

## 2026-10-29 13:29: run `20261029-132917-speed`

Plan speed, done; served as `MiniMax-M3.1-Flash`.

Serving: engine_commit `af3573193`; binary_sha256 `f23babaf9b934985f1895b469eb673d02dec58626a836c27f481a9ad4a495011`; served_model `{"object": "list", "data": [{"id": "MiniMax-M3.1-Flash", "object": "model", "created": 179`; chip `Apple M5 Ultra; 274877906944`; suite_commit `21db9b23f7be`

### ruler-fresh

| streams | prose total (a stream) | code total (a stream) | structured total (a stream) | list total (a stream) | first token |
|---:|---:|---:|---:|---:|---:|
| 1 | 33.4 (33.4) | 33.4 (33.4) | 33.5 (33.5) | 33.5 (33.5) | 1.45-1.54 s |
| 2 | 43.3 (21.7) | 43.1 (21.6) | 42.1 (21.1) | 42.2 (21.1) | 2.18-2.31 s |

Engine rounds (ruler-fresh):

| streams | tokens a round | drafts a round | accepted | ms a round | requests |
|---:|---:|---:|---:|---:|---:|
| 1 | 1.005 | 0.0 |  | 30.05 | 12 |
| 2 | 1.005 | 0.0 |  | 47.07 | 25 |

### ruler-after

| streams | prose total (a stream) | code total (a stream) | structured total (a stream) | list total (a stream) | first token |
|---:|---:|---:|---:|---:|---:|
| 1 | 33.4 (33.4) | 33.3 (33.3) | 33.4 (33.4) | 33.4 (33.4) | 1.46-1.54 s |

Engine rounds (ruler-after):

| streams | tokens a round | drafts a round | accepted | ms a round | requests |
|---:|---:|---:|---:|---:|---:|
| 1 | 1.005 | 0.0 |  | 30.11 | 13 |

### checks

| check | result |
|---|---|
| memory-idle | measured: mac: System-wide memory free percentage: 33%; total = 5120.00M  us |
| turns | pass: resumed == again: True; cold (after a restart): True; cached 4645 of 4725; ttft resumed 1.256s, cold 11.218s |
| memory-busy | measured: mac: System-wide memory free percentage: 34%; total = 5120.00M  us |

## 2026-10-29 13:28: run `20261029-132810-glm-vision`

Plan glm-vision, done; served as `MiniMax-M3.1-Flash`.

Serving: engine_commit `af3573193`; binary_sha256 `f23babaf9b934985f1895b469eb673d02dec58626a836c27f481a9ad4a495011`; served_model `{"object": "list", "data": [{"id": "MiniMax-M3.1-Flash", "object": "model", "created": 179`; chip `Apple M5 Ultra; 274877906944`; suite_commit `21db9b23f7be`

### suite-vision

| check | passed |
|---|---:|
| vision | 3/6 |
| vision-concurrent | 12/16 |

## 2026-10-29 13:09: run `20261029-130901-quick`

Plan quick, done; served as `MiniMax-M3.1-Flash`.

Serving: engine_commit `af3573193`; binary_sha256 `f23babaf9b934985f1895b469eb673d02dec58626a836c27f481a9ad4a495011`; served_model `{"object": "list", "data": [{"id": "MiniMax-M3.1-Flash", "object": "model", "created": 179`; chip `Apple M5 Ultra; 274877906944`; suite_commit `21db9b23f7be`

### ruler-fresh

| streams | prose total (a stream) | code total (a stream) | structured total (a stream) | list total (a stream) | first token |
|---:|---:|---:|---:|---:|---:|
| 1 | 33.3 (33.3) | 33.3 (33.3) | 33.3 (33.3) | 33.3 (33.3) | 1.47-1.56 s |

Engine rounds (ruler-fresh):

| streams | tokens a round | drafts a round | accepted | ms a round | requests |
|---:|---:|---:|---:|---:|---:|
| 1 | 1.005 | 0.0 |  | 30.19 | 12 |

### ruler-after

| streams | prose total (a stream) | code total (a stream) | structured total (a stream) | list total (a stream) | first token |
|---:|---:|---:|---:|---:|---:|
| 1 | 33.4 (33.4) | 33.3 (33.3) | 33.4 (33.4) | 33.4 (33.4) | 1.47-1.55 s |

Engine rounds (ruler-after):

| streams | tokens a round | drafts a round | accepted | ms a round | requests |
|---:|---:|---:|---:|---:|---:|
| 1 | 1.005 | 0.0 |  | 30.11 | 13 |

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
| memory-idle | measured: mac: System-wide memory free percentage: 33%; total = 5120.00M  us |
| structured | pass: 18/18 obey, drafted == plain 12/12; a bad regex -> 400 |
| tools | pass: 5/5 tool cases right |
| sampling | pass: 9/9 seeded replies equal on repeat and undrafted; 0 errors |
| turns | pass: resumed == again: True; cold (after a restart): True; cached 4645 of 4725; ttft resumed 1.264s, cold 11.406s |
| urls | FAIL: public 400; loopback 400; http 400; unexpected: ['public'] |

## 2026-10-29 12:23: run `20261029-122304-speed`

Plan speed, done; served as `MiniMax-M3.1-Flash`.

Serving: engine_commit `c11fb68d6`; binary_sha256 `e69565c1afabb1fc3c717a69f5a18992e6fde1d5139e6b7cddb153b05243d026`; served_model `{"object": "list", "data": [{"id": "MiniMax-M3.1-Flash", "object": "model", "created": 179`; chip `Apple M5 Ultra; 274877906944`; suite_commit `21db9b23f7be`

### ruler-fresh

| streams | prose total (a stream) | code total (a stream) | structured total (a stream) | list total (a stream) | first token |
|---:|---:|---:|---:|---:|---:|
| 1 | 29.8 (29.8) | 39.6 (39.6) | 30.8 (30.8) | 32.0 (32.0) | 1.50-1.58 s |
| 2 | 37.7 (18.9) | 37.7 (18.8) | 33.7 (16.9) | 43.1 (21.5) | 2.25-2.38 s |

Engine rounds (ruler-fresh):

| streams | tokens a round | drafts a round | accepted | ms a round | requests |
|---:|---:|---:|---:|---:|---:|
| 1 | 1.711 | 1.078 | 65% | 51.76 | 12 |
| 2 | 1.568 | 0.754 | 75% | 82.38 | 25 |

### ruler-after

| streams | prose total (a stream) | code total (a stream) | structured total (a stream) | list total (a stream) | first token |
|---:|---:|---:|---:|---:|---:|
| 1 | 29.7 (29.7) | 39.5 (39.5) | 30.7 (30.7) | 32.6 (32.6) | 1.50-1.59 s |

Engine rounds (ruler-after):

| streams | tokens a round | drafts a round | accepted | ms a round | requests |
|---:|---:|---:|---:|---:|---:|
| 1 | 1.672 | 1.004 | 66% | 50.45 | 13 |

### checks

| check | result |
|---|---|
| memory-idle | measured: mac: System-wide memory free percentage: 32%; total = 5120.00M  us |
| turns | pass: resumed == again: True; cold (after a restart): True; cached 4645 of 4725; ttft resumed 1.288s, cold 11.895s |
| memory-busy | measured: mac: System-wide memory free percentage: 31%; total = 5120.00M  us |

## 2026-10-29 12:10: run `20261029-121020-prefill`

Plan prefill, done; served as `MiniMax-M3.1-Flash`.

Serving: engine_commit `c11fb68d6`; binary_sha256 `e69565c1afabb1fc3c717a69f5a18992e6fde1d5139e6b7cddb153b05243d026`; served_model `{"object": "list", "data": [{"id": "MiniMax-M3.1-Flash", "object": "model", "created": 179`; chip `Apple M5 Ultra; 274877906944`; suite_commit `21db9b23f7be`

### checks

| check | result |
|---|---|
| memory-idle | measured: mac: System-wide memory free percentage: 33%; total = 5120.00M  us |
| prefill-off | measured: 2218 tokens 413.7 tok/s (5.361 s), 8361 tokens 452.0 tok/s (18.499 s), 32944 tokens 494.5 tok/s (66.627 s), 131242 tokens 484.0 tok/s (271.187 s) |
| prefill-thinking | measured: 2218 tokens 429.4 tok/s (5.165 s), 8364 tokens 474.6 tok/s (17.625 s), 32937 tokens 499.4 tok/s (65.948 s), 131242 tokens 492.2 tok/s (266.664 s) |
| memory-busy | measured: mac: System-wide memory free percentage: 27%; total = 5120.00M  us |

## 2026-10-29 12:02: run `20261029-120233-speed`

Plan speed, done; served as `MiniMax-M3.1-Flash`.

Serving: engine_commit `c11fb68d6`; binary_sha256 `e69565c1afabb1fc3c717a69f5a18992e6fde1d5139e6b7cddb153b05243d026`; served_model `{"object": "list", "data": [{"id": "MiniMax-M3.1-Flash", "object": "model", "created": 179`; chip `Apple M5 Ultra; 274877906944`; suite_commit `21db9b23f7be`

### ruler-fresh

| streams | prose total (a stream) | code total (a stream) | structured total (a stream) | list total (a stream) | first token |
|---:|---:|---:|---:|---:|---:|
| 1 | 32.6 (32.6) | 32.6 (32.6) | 32.7 (32.7) | 32.7 (32.7) | 1.50-1.59 s |
| 2 | 42.3 (21.1) | 42.2 (21.1) | 41.4 (20.7) | 39.7 (19.9) | 2.25-2.37 s |

Engine rounds (ruler-fresh):

| streams | tokens a round | drafts a round | accepted | ms a round | requests |
|---:|---:|---:|---:|---:|---:|
| 1 | 1.005 | 0.0 |  | 30.77 | 12 |
| 2 | 1.005 | 0.0 |  | 48.54 | 25 |

### ruler-after

| streams | prose total (a stream) | code total (a stream) | structured total (a stream) | list total (a stream) | first token |
|---:|---:|---:|---:|---:|---:|
| 1 | 31.3 (31.3) | 31.3 (31.3) | 31.3 (31.3) | 31.3 (31.3) | 1.54-1.63 s |

Engine rounds (ruler-after):

| streams | tokens a round | drafts a round | accepted | ms a round | requests |
|---:|---:|---:|---:|---:|---:|
| 1 | 1.005 | 0.0 |  | 32.12 | 13 |

### checks

| check | result |
|---|---|
| memory-idle | measured: mac: System-wide memory free percentage: 33%; total = 5120.00M  us |
| turns | pass: resumed == again: True; cold (after a restart): True; cached 4645 of 4725; ttft resumed 1.322s, cold 12.03s |
| memory-busy | measured: mac: System-wide memory free percentage: 33%; total = 5120.00M  us |

## 2026-10-29 12:01: run `20261029-120125-glm-vision`

Plan glm-vision, done; served as `MiniMax-M3.1-Flash`.

Serving: engine_commit `c11fb68d6`; binary_sha256 `e69565c1afabb1fc3c717a69f5a18992e6fde1d5139e6b7cddb153b05243d026`; served_model `{"object": "list", "data": [{"id": "MiniMax-M3.1-Flash", "object": "model", "created": 179`; chip `Apple M5 Ultra; 274877906944`; suite_commit `21db9b23f7be`

### suite-vision

| check | passed |
|---|---:|
| vision | 3/6 |
| vision-concurrent | 12/16 |

## 2026-10-29 11:42: run `20261029-114201-quick`

Plan quick, done; served as `MiniMax-M3.1-Flash`.

Serving: engine_commit `c11fb68d6`; binary_sha256 `e69565c1afabb1fc3c717a69f5a18992e6fde1d5139e6b7cddb153b05243d026`; served_model `{"object": "list", "data": [{"id": "MiniMax-M3.1-Flash", "object": "model", "created": 179`; chip `Apple M5 Ultra; 274877906944`; suite_commit `21db9b23f7be`

### ruler-fresh

| streams | prose total (a stream) | code total (a stream) | structured total (a stream) | list total (a stream) | first token |
|---:|---:|---:|---:|---:|---:|
| 1 | 32.9 (32.9) | 33.0 (33.0) | 33.1 (33.1) | 33.0 (33.0) | 1.47-1.55 s |

Engine rounds (ruler-fresh):

| streams | tokens a round | drafts a round | accepted | ms a round | requests |
|---:|---:|---:|---:|---:|---:|
| 1 | 1.005 | 0.0 |  | 30.45 | 12 |

### ruler-after

| streams | prose total (a stream) | code total (a stream) | structured total (a stream) | list total (a stream) | first token |
|---:|---:|---:|---:|---:|---:|
| 1 | 33.0 (33.0) | 32.9 (32.9) | 33.0 (33.0) | 32.9 (32.9) | 1.48-1.56 s |

Engine rounds (ruler-after):

| streams | tokens a round | drafts a round | accepted | ms a round | requests |
|---:|---:|---:|---:|---:|---:|
| 1 | 1.005 | 0.0 |  | 30.52 | 13 |

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
| memory-idle | measured: mac: System-wide memory free percentage: 33%; total = 5120.00M  us |
| structured | pass: 18/18 obey, drafted == plain 12/12; a bad regex -> 400 |
| tools | pass: 5/5 tool cases right |
| sampling | pass: 9/9 seeded replies equal on repeat and undrafted; 0 errors |
| turns | pass: resumed == again: True; cold (after a restart): True; cached 4645 of 4725; ttft resumed 1.258s, cold 11.535s |
| urls | FAIL: public 400; loopback 400; http 400; unexpected: ['public'] |

## 2026-10-29 10:36: run `20261029-103629-speed`

Plan speed, done; served as `MiniMax-M3.1-Flash`.

Serving: engine_commit `cf0d6b4f5`; binary_sha256 `46e1d8341e2426ee967979586977ce3aa18bf9c744a4ff89f1e363c6af3dc343`; served_model `{"object": "list", "data": [{"id": "MiniMax-M3.1-Flash", "object": "model", "created": 179`; chip `Apple M5 Ultra; 274877906944`; suite_commit `21db9b23f7be`

### ruler-fresh

| streams | prose total (a stream) | code total (a stream) | structured total (a stream) | list total (a stream) | first token |
|---:|---:|---:|---:|---:|---:|
| 1 | 22.8 (22.8) | 25.6 (25.6) | 21.7 (21.7) | 23.1 (23.1) | 1.50-1.59 s |
| 2 | 28.5 (14.3) | 27.0 (13.5) | 26.4 (13.2) | 29.3 (14.6) | 2.24-2.37 s |

Engine rounds (ruler-fresh):

| streams | tokens a round | drafts a round | accepted | ms a round | requests |
|---:|---:|---:|---:|---:|---:|
| 1 | 1.478 | 0.602 | 78% | 63.42 | 12 |
| 2 | 1.493 | 0.612 | 80% | 107.42 | 25 |

### ruler-after

| streams | prose total (a stream) | code total (a stream) | structured total (a stream) | list total (a stream) | first token |
|---:|---:|---:|---:|---:|---:|
| 1 | 23.0 (23.0) | 25.8 (25.8) | 21.7 (21.7) | 23.1 (23.1) | 1.50-1.58 s |

Engine rounds (ruler-after):

| streams | tokens a round | drafts a round | accepted | ms a round | requests |
|---:|---:|---:|---:|---:|---:|
| 1 | 1.503 | 0.631 | 78% | 64.21 | 13 |

### checks

| check | result |
|---|---|
| memory-idle | measured: mac: System-wide memory free percentage: 31%; total = 5120.00M  us |
| turns | pass: resumed == again: True; cold (after a restart): True; cached 4645 of 4725; ttft resumed 1.28s, cold 11.696s |
| memory-busy | measured: mac: System-wide memory free percentage: 31%; total = 5120.00M  us |

## 2026-10-29 10:21: run `20261029-102139-prefill`

Plan prefill, done; served as `MiniMax-M3.1-Flash`.

Serving: engine_commit `cf0d6b4f5`; binary_sha256 `46e1d8341e2426ee967979586977ce3aa18bf9c744a4ff89f1e363c6af3dc343`; served_model `{"object": "list", "data": [{"id": "MiniMax-M3.1-Flash", "object": "model", "created": 179`; chip `Apple M5 Ultra; 274877906944`; suite_commit `21db9b23f7be`

### checks

| check | result |
|---|---|
| memory-idle | measured: mac: System-wide memory free percentage: 33%; total = 5120.00M  us |
| prefill-off | measured: 2220 tokens 430.1 tok/s (5.162 s), 8363 tokens 475.5 tok/s (17.587 s), 32940 tokens 499.2 tok/s (65.989 s), 131241 tokens 490.7 tok/s (267.458 s) |
| prefill-thinking | measured: 2218 tokens 427.1 tok/s (5.193 s), 8362 tokens 467.5 tok/s (17.885 s), 32939 tokens 493.5 tok/s (66.75 s), 131242 tokens 491.9 tok/s (266.823 s) |
| memory-busy | measured: mac: System-wide memory free percentage: 26%; total = 5120.00M  us |

## 2026-10-29 10:12: run `20261029-101230-speed`

Plan speed, done; served as `MiniMax-M3.1-Flash`.

Serving: engine_commit `cf0d6b4f5`; binary_sha256 `46e1d8341e2426ee967979586977ce3aa18bf9c744a4ff89f1e363c6af3dc343`; served_model `{"object": "list", "data": [{"id": "MiniMax-M3.1-Flash", "object": "model", "created": 179`; chip `Apple M5 Ultra; 274877906944`; suite_commit `21db9b23f7be`

### ruler-fresh

| streams | prose total (a stream) | code total (a stream) | structured total (a stream) | list total (a stream) | first token |
|---:|---:|---:|---:|---:|---:|
| 1 | 25.4 (25.4) | 25.3 (25.3) | 25.3 (25.3) | 25.4 (25.4) | 1.48-1.58 s |
| 2 | 30.1 (15.1) | 30.0 (15.0) | 29.7 (14.8) | 29.1 (14.5) | 2.23-2.35 s |

Engine rounds (ruler-fresh):

| streams | tokens a round | drafts a round | accepted | ms a round | requests |
|---:|---:|---:|---:|---:|---:|
| 1 | 1.005 | 0.0 |  | 39.6 | 12 |
| 2 | 1.005 | 0.0 |  | 67.64 | 25 |

### ruler-after

| streams | prose total (a stream) | code total (a stream) | structured total (a stream) | list total (a stream) | first token |
|---:|---:|---:|---:|---:|---:|
| 1 | 25.4 (25.4) | 25.4 (25.4) | 25.4 (25.4) | 25.5 (25.5) | 1.49-1.57 s |

Engine rounds (ruler-after):

| streams | tokens a round | drafts a round | accepted | ms a round | requests |
|---:|---:|---:|---:|---:|---:|
| 1 | 1.005 | 0.0 |  | 39.52 | 13 |

### checks

| check | result |
|---|---|
| memory-idle | measured: mac: System-wide memory free percentage: 32%; total = 5120.00M  us |
| turns | pass: resumed == again: True; cold (after a restart): True; cached 4645 of 4725; ttft resumed 1.277s, cold 11.428s |
| memory-busy | measured: mac: System-wide memory free percentage: 33%; total = 5120.00M  us |

## 2026-10-29 10:11: run `20261029-101117-glm-vision`

Plan glm-vision, done; served as `MiniMax-M3.1-Flash`.

Serving: engine_commit `cf0d6b4f5`; binary_sha256 `46e1d8341e2426ee967979586977ce3aa18bf9c744a4ff89f1e363c6af3dc343`; served_model `{"object": "list", "data": [{"id": "MiniMax-M3.1-Flash", "object": "model", "created": 179`; chip `Apple M5 Ultra; 274877906944`; suite_commit `21db9b23f7be`

### suite-vision

| check | passed |
|---|---:|
| vision | 3/6 |
| vision-concurrent | 12/16 |

## 2026-10-29 09:48: run `20261029-094854-quick`

Plan quick, done; served as `MiniMax-M3.1-Flash`.

Serving: engine_commit `cf0d6b4f5`; binary_sha256 `46e1d8341e2426ee967979586977ce3aa18bf9c744a4ff89f1e363c6af3dc343`; served_model `{"object": "list", "data": [{"id": "MiniMax-M3.1-Flash", "object": "model", "created": 179`; chip `Apple M5 Ultra; 274877906944`; suite_commit `21db9b23f7be`

### ruler-fresh

| streams | prose total (a stream) | code total (a stream) | structured total (a stream) | list total (a stream) | first token |
|---:|---:|---:|---:|---:|---:|
| 1 | 25.5 (25.5) | 25.5 (25.5) | 25.5 (25.5) | 25.5 (25.5) | 1.49-1.57 s |

Engine rounds (ruler-fresh):

| streams | tokens a round | drafts a round | accepted | ms a round | requests |
|---:|---:|---:|---:|---:|---:|
| 1 | 1.005 | 0.0 |  | 39.39 | 12 |

### ruler-after

| streams | prose total (a stream) | code total (a stream) | structured total (a stream) | list total (a stream) | first token |
|---:|---:|---:|---:|---:|---:|
| 1 | 25.4 (25.4) | 25.4 (25.4) | 25.4 (25.4) | 25.4 (25.4) | 1.49-1.58 s |

Engine rounds (ruler-after):

| streams | tokens a round | drafts a round | accepted | ms a round | requests |
|---:|---:|---:|---:|---:|---:|
| 1 | 1.005 | 0.0 |  | 39.58 | 13 |

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
| memory-idle | measured: mac: System-wide memory free percentage: 32%; total = 5120.00M  us |
| structured | pass: 18/18 obey, drafted == plain 12/12; a bad regex -> 400 |
| tools | pass: 5/5 tool cases right |
| sampling | pass: 9/9 seeded replies equal on repeat and undrafted; 0 errors |
| turns | pass: resumed == again: True; cold (after a restart): True; cached 4645 of 4725; ttft resumed 1.27s, cold 11.469s |
| urls | FAIL: public 400; loopback 400; http 400; unexpected: ['public'] |

## 2026-10-29 08:50: run `20261029-085020-speed`

Plan speed, done; served as `MiniMax-M3.1-Flash`.

Serving: engine_commit `ac35cd022`; binary_sha256 `4b73bfa0dda82843ef2c27099e9ed883d9ab4dd8de31f6d7c42026f2bdc1bc1b`; served_model `{"object": "list", "data": [{"id": "MiniMax-M3.1-Flash", "object": "model", "created": 179`; chip `Apple M5 Ultra; 274877906944`; suite_commit `21db9b23f7be`

### ruler-fresh

| streams | prose total (a stream) | code total (a stream) | structured total (a stream) | list total (a stream) | first token |
|---:|---:|---:|---:|---:|---:|
| 1 | 17.9 (17.9) | 20.0 (20.0) | 17.7 (17.7) | 18.5 (18.5) | 1.52-1.62 s |
| 2 | 22.9 (11.4) | 21.3 (10.7) | 21.8 (10.9) | 23.6 (11.8) | 2.28-2.41 s |

Engine rounds (ruler-fresh):

| streams | tokens a round | drafts a round | accepted | ms a round | requests |
|---:|---:|---:|---:|---:|---:|
| 1 | 1.461 | 0.609 | 75% | 78.76 | 12 |
| 2 | 1.388 | 0.447 | 86% | 123.91 | 25 |

### ruler-after

| streams | prose total (a stream) | code total (a stream) | structured total (a stream) | list total (a stream) | first token |
|---:|---:|---:|---:|---:|---:|
| 1 | 17.6 (17.6) | 19.8 (19.8) | 17.7 (17.7) | 18.8 (18.8) | 1.51-1.60 s |

Engine rounds (ruler-after):

| streams | tokens a round | drafts a round | accepted | ms a round | requests |
|---:|---:|---:|---:|---:|---:|
| 1 | 1.415 | 0.555 | 74% | 76.5 | 13 |

### checks

| check | result |
|---|---|
| memory-idle | measured: mac: System-wide memory free percentage: 31%; total = 5120.00M  us |
| turns | pass: resumed == again: True; cold (after a restart): True; cached 4645 of 4725; ttft resumed 1.299s, cold 12.206s |
| memory-busy | measured: mac: System-wide memory free percentage: 30%; total = 5120.00M  us |

## 2026-10-29 08:23: run `20261029-082303-quick`

Plan quick, done; served as `MiniMax-M3.1-Flash`.

Serving: engine_commit `ac35cd022`; binary_sha256 `4b73bfa0dda82843ef2c27099e9ed883d9ab4dd8de31f6d7c42026f2bdc1bc1b`; served_model `{"object": "list", "data": [{"id": "MiniMax-M3.1-Flash", "object": "model", "created": 179`; chip `Apple M5 Ultra; 274877906944`; suite_commit `21db9b23f7be`

### ruler-fresh

| streams | prose total (a stream) | code total (a stream) | structured total (a stream) | list total (a stream) | first token |
|---:|---:|---:|---:|---:|---:|
| 1 | 18.6 (18.6) | 20.1 (20.1) | 17.7 (17.7) | 18.8 (18.8) | 1.52-1.61 s |

Engine rounds (ruler-fresh):

| streams | tokens a round | drafts a round | accepted | ms a round | requests |
|---:|---:|---:|---:|---:|---:|
| 1 | 1.376 | 0.477 | 78% | 73.27 | 12 |

### ruler-after

| streams | prose total (a stream) | code total (a stream) | structured total (a stream) | list total (a stream) | first token |
|---:|---:|---:|---:|---:|---:|
| 1 | 18.6 (18.6) | 20.3 (20.3) | 17.8 (17.8) | 18.6 (18.6) | 1.52-1.61 s |

Engine rounds (ruler-after):

| streams | tokens a round | drafts a round | accepted | ms a round | requests |
|---:|---:|---:|---:|---:|---:|
| 1 | 1.409 | 0.528 | 77% | 74.82 | 13 |

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
| memory-idle | measured: mac: System-wide memory free percentage: 29%; total = 7168.00M  us |
| structured | pass: 18/18 obey, drafted == plain 12/12; a bad regex -> 400 |
| tools | pass: 5/5 tool cases right |
| sampling | pass: 9/9 seeded replies equal on repeat and undrafted; 0 errors |
| turns | pass: resumed == again: True; cold (after a restart): True; cached 4645 of 4725; ttft resumed 1.289s, cold 11.913s |
| urls | FAIL: public 400; loopback 400; http 400; unexpected: ['public'] |

## 2026-10-29 08:02: run `20261029-080202-prefill`

Plan prefill, done; served as `MiniMax-M3.1-Flash`.

Serving: engine_commit `dbcb9d791`; binary_sha256 `42ea5cbbab682611357ddc6b7a865150a1a88f410ea9e7777c834587236bcd5e`; served_model `{"object": "list", "data": [{"id": "MiniMax-M3.1-Flash", "object": "model", "created": 179`; chip `Apple M5 Ultra; 274877906944`; suite_commit `21db9b23f7be`

### checks

| check | result |
|---|---|
| memory-idle | measured: mac: System-wide memory free percentage: 32%; total = 4096.00M  us |
| prefill-off | measured: 2217 tokens 434.0 tok/s (5.108 s), 8362 tokens 485.5 tok/s (17.222 s), 32943 tokens 508.8 tok/s (64.742 s), 131243 tokens 501.4 tok/s (261.759 s) |
| prefill-thinking | measured: 2216 tokens 432.6 tok/s (5.122 s), 8360 tokens 486.4 tok/s (17.187 s), 32940 tokens 505.4 tok/s (65.177 s), 131242 tokens 483.4 tok/s (271.492 s) |
| memory-busy | measured: mac: System-wide memory free percentage: 25%; total = 4096.00M  us |

## 2026-10-29 07:51: run `20261029-075115-speed`

Plan speed, done; served as `MiniMax-M3.1-Flash`.

Serving: engine_commit `dbcb9d791`; binary_sha256 `42ea5cbbab682611357ddc6b7a865150a1a88f410ea9e7777c834587236bcd5e`; served_model `{"object": "list", "data": [{"id": "MiniMax-M3.1-Flash", "object": "model", "created": 179`; chip `Apple M5 Ultra; 274877906944`; suite_commit `21db9b23f7be`

### ruler-fresh

| streams | prose total (a stream) | code total (a stream) | structured total (a stream) | list total (a stream) | first token |
|---:|---:|---:|---:|---:|---:|
| 1 | 19.5 (19.5) | 19.5 (19.5) | 19.5 (19.5) | 19.5 (19.5) | 1.48-1.56 s |
| 2 | 24.2 (12.1) | 23.8 (11.9) | 24.2 (12.1) | 23.6 (11.8) | 2.22-2.33 s |

Engine rounds (ruler-fresh):

| streams | tokens a round | drafts a round | accepted | ms a round | requests |
|---:|---:|---:|---:|---:|---:|
| 1 | 1.005 | 0.0 |  | 51.42 | 12 |
| 2 | 1.005 | 0.0 |  | 83.92 | 25 |

### ruler-after

| streams | prose total (a stream) | code total (a stream) | structured total (a stream) | list total (a stream) | first token |
|---:|---:|---:|---:|---:|---:|
| 1 | 19.5 (19.5) | 19.5 (19.5) | 19.5 (19.5) | 19.5 (19.5) | 1.48-1.57 s |

Engine rounds (ruler-after):

| streams | tokens a round | drafts a round | accepted | ms a round | requests |
|---:|---:|---:|---:|---:|---:|
| 1 | 1.005 | 0.0 |  | 51.45 | 13 |

### checks

| check | result |
|---|---|
| memory-idle | measured: mac: System-wide memory free percentage: 33%; total = 4096.00M  us |
| turns | pass: resumed == again: True; cold (after a restart): True; cached 4645 of 4725; ttft resumed 1.273s, cold 11.241s |
| memory-busy | measured: mac: System-wide memory free percentage: 32%; total = 4096.00M  us |

## 2026-10-29 07:50: run `20261029-075003-glm-vision`

Plan glm-vision, done; served as `MiniMax-M3.1-Flash`.

Serving: engine_commit `dbcb9d791`; binary_sha256 `42ea5cbbab682611357ddc6b7a865150a1a88f410ea9e7777c834587236bcd5e`; served_model `{"object": "list", "data": [{"id": "MiniMax-M3.1-Flash", "object": "model", "created": 179`; chip `Apple M5 Ultra; 274877906944`; suite_commit `21db9b23f7be`

### suite-vision

| check | passed |
|---|---:|
| vision | 3/6 |
| vision-concurrent | 12/16 |

## 2026-10-29 07:24: run `20261029-072424-quick`

Plan quick, done; served as `MiniMax-M3.1-Flash`.

Serving: engine_commit `dbcb9d791`; binary_sha256 `42ea5cbbab682611357ddc6b7a865150a1a88f410ea9e7777c834587236bcd5e`; served_model `{"object": "list", "data": [{"id": "MiniMax-M3.1-Flash", "object": "model", "created": 179`; chip `Apple M5 Ultra; 274877906944`; suite_commit `21db9b23f7be`

### ruler-fresh

| streams | prose total (a stream) | code total (a stream) | structured total (a stream) | list total (a stream) | first token |
|---:|---:|---:|---:|---:|---:|
| 1 | 19.5 (19.5) | 19.5 (19.5) | 19.5 (19.5) | 19.6 (19.6) | 1.48-1.57 s |

Engine rounds (ruler-fresh):

| streams | tokens a round | drafts a round | accepted | ms a round | requests |
|---:|---:|---:|---:|---:|---:|
| 1 | 1.005 | 0.0 |  | 51.41 | 12 |

### ruler-after

| streams | prose total (a stream) | code total (a stream) | structured total (a stream) | list total (a stream) | first token |
|---:|---:|---:|---:|---:|---:|
| 1 | 19.5 (19.5) | 19.5 (19.5) | 19.5 (19.5) | 19.5 (19.5) | 1.48-1.56 s |

Engine rounds (ruler-after):

| streams | tokens a round | drafts a round | accepted | ms a round | requests |
|---:|---:|---:|---:|---:|---:|
| 1 | 1.005 | 0.0 |  | 51.56 | 13 |

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
| memory-idle | measured: mac: System-wide memory free percentage: 32%; total = 5120.00M  us |
| structured | pass: 18/18 obey, drafted == plain 12/12; a bad regex -> 400 |
| tools | pass: 5/5 tool cases right |
| sampling | pass: 9/9 seeded replies equal on repeat and undrafted; 0 errors |
| turns | pass: resumed == again: True; cold (after a restart): True; cached 4645 of 4725; ttft resumed 1.271s, cold 11.241s |
| urls | FAIL: public 400; loopback 400; http 400; unexpected: ['public'] |

## 2026-10-29 07:06: run `20261029-070637-prefill`

Plan prefill, done; served as `MiniMax-M3.1-Flash`.

Serving: engine_commit `fda39c320`; binary_sha256 `bd364361c51159f64136a48a5a7faec8086585a45caaa7740fe972694ce51ce9`; served_model `{"object": "list", "data": [{"id": "MiniMax-M3.1-Flash", "object": "model", "created": 179`; chip `Apple M5 Ultra; 274877906944`; suite_commit `21db9b23f7be`

### checks

| check | result |
|---|---|
| memory-idle | measured: mac: System-wide memory free percentage: 33%; total = 5120.00M  us |
| prefill-off | measured: 2217 tokens 435.1 tok/s (5.095 s), 8363 tokens 486.6 tok/s (17.186 s), 32942 tokens 509.4 tok/s (64.672 s), 131244 tokens 502.4 tok/s (261.25 s) |
| prefill-thinking | measured: 2218 tokens 432.5 tok/s (5.128 s), 8366 tokens 486.1 tok/s (17.212 s), 32939 tokens 509.9 tok/s (64.598 s), 131243 tokens 503.2 tok/s (260.826 s) |
| memory-busy | measured: mac: System-wide memory free percentage: 26%; total = 5120.00M  us |

## 2026-10-29 06:55: run `20261029-065551-speed`

Plan speed, done; served as `MiniMax-M3.1-Flash`.

Serving: engine_commit `fda39c320`; binary_sha256 `bd364361c51159f64136a48a5a7faec8086585a45caaa7740fe972694ce51ce9`; served_model `{"object": "list", "data": [{"id": "MiniMax-M3.1-Flash", "object": "model", "created": 179`; chip `Apple M5 Ultra; 274877906944`; suite_commit `21db9b23f7be`

### ruler-fresh

| streams | prose total (a stream) | code total (a stream) | structured total (a stream) | list total (a stream) | first token |
|---:|---:|---:|---:|---:|---:|
| 1 | 19.5 (19.5) | 19.5 (19.5) | 19.5 (19.5) | 19.6 (19.6) | 1.48-1.57 s |
| 2 | 24.2 (12.1) | 23.8 (11.9) | 24.2 (12.1) | 23.6 (11.8) | 2.22-2.35 s |

Engine rounds (ruler-fresh):

| streams | tokens a round | drafts a round | accepted | ms a round | requests |
|---:|---:|---:|---:|---:|---:|
| 1 | 1.005 | 0.0 |  | 51.42 | 12 |
| 2 | 1.005 | 0.0 |  | 83.93 | 25 |

### ruler-after

| streams | prose total (a stream) | code total (a stream) | structured total (a stream) | list total (a stream) | first token |
|---:|---:|---:|---:|---:|---:|
| 1 | 19.5 (19.5) | 19.5 (19.5) | 19.5 (19.5) | 19.5 (19.5) | 1.48-1.56 s |

Engine rounds (ruler-after):

| streams | tokens a round | drafts a round | accepted | ms a round | requests |
|---:|---:|---:|---:|---:|---:|
| 1 | 1.005 | 0.0 |  | 51.48 | 13 |

### checks

| check | result |
|---|---|
| memory-idle | measured: mac: System-wide memory free percentage: 33%; total = 5120.00M  us |
| turns | pass: resumed == again: True; cold (after a restart): True; cached 4645 of 4725; ttft resumed 1.279s, cold 11.254s |
| memory-busy | measured: mac: System-wide memory free percentage: 32%; total = 5120.00M  us |

## 2026-10-29 06:54: run `20261029-065438-glm-vision`

Plan glm-vision, done; served as `MiniMax-M3.1-Flash`.

Serving: engine_commit `fda39c320`; binary_sha256 `bd364361c51159f64136a48a5a7faec8086585a45caaa7740fe972694ce51ce9`; served_model `{"object": "list", "data": [{"id": "MiniMax-M3.1-Flash", "object": "model", "created": 179`; chip `Apple M5 Ultra; 274877906944`; suite_commit `21db9b23f7be`

### suite-vision

| check | passed |
|---|---:|
| vision | 3/6 |
| vision-concurrent | 12/16 |

## 2026-10-29 06:29: run `20261029-062901-quick`

Plan quick, done; served as `MiniMax-M3.1-Flash`.

Serving: engine_commit `0f20fb9af`; binary_sha256 `bd364361c51159f64136a48a5a7faec8086585a45caaa7740fe972694ce51ce9`; served_model `{"object": "list", "data": [{"id": "MiniMax-M3.1-Flash", "object": "model", "created": 179`; chip `Apple M5 Ultra; 274877906944`; suite_commit `21db9b23f7be`

### ruler-fresh

| streams | prose total (a stream) | code total (a stream) | structured total (a stream) | list total (a stream) | first token |
|---:|---:|---:|---:|---:|---:|
| 1 | 19.5 (19.5) | 19.5 (19.5) | 19.5 (19.5) | 19.5 (19.5) | 1.48-1.56 s |

Engine rounds (ruler-fresh):

| streams | tokens a round | drafts a round | accepted | ms a round | requests |
|---:|---:|---:|---:|---:|---:|
| 1 | 1.005 | 0.0 |  | 51.55 | 12 |

### ruler-after

| streams | prose total (a stream) | code total (a stream) | structured total (a stream) | list total (a stream) | first token |
|---:|---:|---:|---:|---:|---:|
| 1 | 19.5 (19.5) | 19.5 (19.5) | 19.5 (19.5) | 19.5 (19.5) | 1.48-1.56 s |

Engine rounds (ruler-after):

| streams | tokens a round | drafts a round | accepted | ms a round | requests |
|---:|---:|---:|---:|---:|---:|
| 1 | 1.005 | 0.0 |  | 51.44 | 13 |

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
| memory-idle | measured: mac: System-wide memory free percentage: 33%; total = 5120.00M  us |
| structured | pass: 18/18 obey, drafted == plain 12/12; a bad regex -> 400 |
| tools | pass: 5/5 tool cases right |
| sampling | pass: 9/9 seeded replies equal on repeat and undrafted; 0 errors |
| turns | pass: resumed == again: True; cold (after a restart): True; cached 4645 of 4725; ttft resumed 1.277s, cold 11.241s |
| urls | FAIL: public 400; loopback 400; http 400; unexpected: ['public'] |

