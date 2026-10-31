# Nanbeige4.3-33B-INT4 (QAT int4 g32), drafted by Nanbeige4.1-3B bf16 on 1x Apple M5 Ultra (256 GB unified), macOS

Target `nanbeige43-33b-int4draft-m5`: Nanbeige4.3-33B-INT4 (QAT int4 g32) with Nanbeige4.1-3B bf16 drafting, TensorFold native Metal (llama) on one M5 Ultra (131072-token window, 2 streams, every stream drafted). Engine: TensorFold native, Metal. Rendered from `stats/nanbeige43-33b-int4draft-m5.json` (11 runs); aggregate tok/s, total (a stream).

## 2026-10-31 15:57: run `20261031-155737-ab-tools-turns`

Plan ab-tools-turns, done; served as `nanbeige`.

Serving: engine_commit `19c80efab`; binary_sha256 `f895a054484899c8504a17c67139611b362bdac0c59cb2bfde2102c1d6e192ca`; served_model `{"object": "list", "data": [{"id": "nanbeige", "object": "model", "created": 1793480265, "`; chip `Apple M5 Ultra; 274877906944`; suite_commit `21db9b23f7be`

### checks

| check | result |
|---|---|
| tools | pass: 5/5 tool cases right |
| turns | pass: resumed == again: True; cold (after a restart): True; cached 5493 of 5649; ttft resumed 0.404s, cold 4.656s |

## 2026-10-31 15:36: run `20261031-153643-quick`

Plan quick, done; served as `nanbeige`.

Serving: engine_commit `2c8196497`; binary_sha256 `9e06644be12d49178b6cb79502ad14a36b3449ff2bdc77e2c19571c9164ee347`; served_model `{"object": "list", "data": [{"id": "nanbeige", "object": "model", "created": 1793479016, "`; chip `Apple M5 Ultra; 274877906944`; suite_commit `21db9b23f7be`

### ruler-fresh

| streams | prose total (a stream) | code total (a stream) | structured total (a stream) | list total (a stream) | first token |
|---:|---:|---:|---:|---:|---:|
| 1 | 85.9 (85.9) | 79.1 (79.1) | 76.1 (76.1) | 70.7 (70.7) | 0.28-0.33 s |

Engine rounds (ruler-fresh):

| streams | tokens a round | drafts a round | accepted | ms a round | requests |
|---:|---:|---:|---:|---:|---:|
| 1 | 2.181 | 1.276 | 92% | 27.98 | 12 |

### ruler-after

| streams | prose total (a stream) | code total (a stream) | structured total (a stream) | list total (a stream) | first token |
|---:|---:|---:|---:|---:|---:|
| 1 | 79.5 (79.5) | 80.7 (80.7) | 79.5 (79.5) | 73.8 (73.8) | 0.27-0.32 s |

Engine rounds (ruler-after):

| streams | tokens a round | drafts a round | accepted | ms a round | requests |
|---:|---:|---:|---:|---:|---:|
| 1 | 2.007 | 1.09 | 91% | 25.61 | 13 |

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
| memory-idle | measured: mac: System-wide memory free percentage: 82%; total = 1024.00M  us |
| structured | pass: 18/18 obey, drafted == plain 12/12; a bad regex -> 400 |
| tools | pass: 5/5 tool cases right |
| sampling | pass: 9/9 seeded replies equal on repeat and undrafted; 0 errors |
| turns | pass: resumed == again: True; cold (after a restart): True; cached 5493 of 5649; ttft resumed 0.425s, cold 4.946s |

## 2026-10-31 15:01: run `20261031-150116-quick`

Plan quick, done; served as `nanbeige`.

Serving: engine_commit `77dcfc650`; binary_sha256 `acd6f649485296e41297676b5c049b1be051e868d851d04f5efb3da3fe87a7a8`; served_model `{"object": "list", "data": [{"id": "nanbeige", "object": "model", "created": 1793476889, "`; chip `Apple M5 Ultra; 274877906944`; suite_commit `21db9b23f7be`

### ruler-fresh

| streams | prose total (a stream) | code total (a stream) | structured total (a stream) | list total (a stream) | first token |
|---:|---:|---:|---:|---:|---:|
| 1 | 76.0 (76.0) | 76.8 (76.8) | 76.1 (76.1) | 79.1 (79.1) | 0.28-0.32 s |

Engine rounds (ruler-fresh):

| streams | tokens a round | drafts a round | accepted | ms a round | requests |
|---:|---:|---:|---:|---:|---:|
| 1 | 1.992 | 1.086 | 90% | 25.87 | 12 |

### ruler-after

| streams | prose total (a stream) | code total (a stream) | structured total (a stream) | list total (a stream) | first token |
|---:|---:|---:|---:|---:|---:|
| 1 | 80.0 (80.0) | 81.2 (81.2) | 81.5 (81.5) | 81.5 (81.5) | 0.27-0.30 s |

Engine rounds (ruler-after):

| streams | tokens a round | drafts a round | accepted | ms a round | requests |
|---:|---:|---:|---:|---:|---:|
| 1 | 1.998 | 1.08 | 92% | 24.65 | 13 |

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
| memory-idle | measured: mac: System-wide memory free percentage: 81%; total = 1024.00M  us |
| structured | pass: 18/18 obey, drafted == plain 12/12; a bad regex -> 400 |
| tools | pass: 5/5 tool cases right |
| sampling | pass: 9/9 seeded replies equal on repeat and undrafted; 0 errors |
| turns | pass: resumed == again: True; cold (after a restart): True; cached 5493 of 5649; ttft resumed 0.415s, cold 4.727s |

## 2026-10-31 14:30: run `20261031-143040-prefill-64k`

Plan prefill-64k, done; served as `nanbeige`.

Serving: engine_commit `a110eeee6`; binary_sha256 `e06dd8097c8bf9a9e6b8ec006c1d516182bf034c8c60ccd4fcb1048833a93741`; served_model `{"object": "list", "data": [{"id": "nanbeige", "object": "model", "created": 1793475048, "`; chip `Apple M5 Ultra; 274877906944`; suite_commit `21db9b23f7be`

### checks

| check | result |
|---|---|
| memory-idle | measured: mac: System-wide memory free percentage: 82%; total = 1024.00M  us |
| prefill-off | measured: 2111 tokens 1114.0 tok/s (1.895 s), 8253 tokens 1175.1 tok/s (7.023 s), 32829 tokens 977.0 tok/s (33.603 s), 61501 tokens 778.7 tok/s (78.983 s) |
| prefill-thinking | measured: 2103 tokens 1125.8 tok/s (1.868 s), 8251 tokens 1152.2 tok/s (7.161 s), 32825 tokens 921.6 tok/s (35.617 s), 61496 tokens 723.3 tok/s (85.017 s) |
| memory-busy | measured: mac: System-wide memory free percentage: 73%; total = 1024.00M  us |

## 2026-10-31 14:27: run `20261031-142713-speed`

Plan speed, done; served as `nanbeige`.

Serving: engine_commit `a110eeee6`; binary_sha256 `e06dd8097c8bf9a9e6b8ec006c1d516182bf034c8c60ccd4fcb1048833a93741`; served_model `{"object": "list", "data": [{"id": "nanbeige", "object": "model", "created": 1793474841, "`; chip `Apple M5 Ultra; 274877906944`; suite_commit `21db9b23f7be`

### ruler-fresh

| streams | prose total (a stream) | code total (a stream) | structured total (a stream) | list total (a stream) | first token |
|---:|---:|---:|---:|---:|---:|
| 1 | 79.4 (79.4) | 79.6 (79.6) | 81.0 (81.0) | 80.5 (80.5) | 0.27-0.31 s |
| 2 | 74.4 (37.2) | 74.6 (37.3) | 73.7 (36.8) | 74.8 (37.4) | 0.41-0.46 s |

Engine rounds (ruler-fresh):

| streams | tokens a round | drafts a round | accepted | ms a round | requests |
|---:|---:|---:|---:|---:|---:|
| 1 | 1.984 | 1.07 | 91% | 24.76 | 12 |
| 2 | 1.032 | 0.027 | 100% | 27.75 | 25 |

### ruler-after

| streams | prose total (a stream) | code total (a stream) | structured total (a stream) | list total (a stream) | first token |
|---:|---:|---:|---:|---:|---:|
| 1 | 81.2 (81.2) | 80.3 (80.3) | 80.0 (80.0) | 79.7 (79.7) | 0.27-0.30 s |

Engine rounds (ruler-after):

| streams | tokens a round | drafts a round | accepted | ms a round | requests |
|---:|---:|---:|---:|---:|---:|
| 1 | 1.995 | 1.076 | 92% | 24.85 | 13 |

### checks

| check | result |
|---|---|
| memory-idle | measured: mac: System-wide memory free percentage: 81%; total = 1024.00M  us |
| turns | pass: resumed == again: True; cold (after a restart): True; cached 5493 of 5649; ttft resumed 0.413s, cold 4.922s |
| memory-busy | measured: mac: System-wide memory free percentage: 82%; total = 1024.00M  us |

## 2026-10-31 14:11: run `20261031-141154-quick`

Plan quick, done; served as `nanbeige`.

Serving: engine_commit `a110eeee6`; binary_sha256 `e06dd8097c8bf9a9e6b8ec006c1d516182bf034c8c60ccd4fcb1048833a93741`; served_model `{"object": "list", "data": [{"id": "nanbeige", "object": "model", "created": 1793473922, "`; chip `Apple M5 Ultra; 274877906944`; suite_commit `21db9b23f7be`

### ruler-fresh

| streams | prose total (a stream) | code total (a stream) | structured total (a stream) | list total (a stream) | first token |
|---:|---:|---:|---:|---:|---:|
| 1 | 81.1 (81.1) | 80.9 (80.9) | 81.1 (81.1) | 81.4 (81.4) | 0.27-0.30 s |

Engine rounds (ruler-fresh):

| streams | tokens a round | drafts a round | accepted | ms a round | requests |
|---:|---:|---:|---:|---:|---:|
| 1 | 1.958 | 1.035 | 92% | 24.13 | 12 |

### ruler-after

| streams | prose total (a stream) | code total (a stream) | structured total (a stream) | list total (a stream) | first token |
|---:|---:|---:|---:|---:|---:|
| 1 | 82.0 (82.0) | 81.0 (81.0) | 79.1 (79.1) | 81.2 (81.2) | 0.27-0.30 s |

Engine rounds (ruler-after):

| streams | tokens a round | drafts a round | accepted | ms a round | requests |
|---:|---:|---:|---:|---:|---:|
| 1 | 1.979 | 1.055 | 92% | 24.49 | 13 |

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
| memory-idle | measured: mac: System-wide memory free percentage: 82%; total = 1024.00M  us |
| structured | pass: 18/18 obey, drafted == plain 12/12; a bad regex -> 400 |
| tools | pass: 5/5 tool cases right |
| sampling | pass: 9/9 seeded replies equal on repeat and undrafted; 0 errors |
| turns | pass: resumed == again: True; cold (after a restart): True; cached 5493 of 5649; ttft resumed 0.401s, cold 4.65s |

## 2026-10-31 12:23: run `20261031-122312-prefill-64k`

Plan prefill-64k, done; served as `nanbeige`.

Serving: engine_commit `2e580cd76`; binary_sha256 `9e5abee41c72ae11079c59fa2f12df9e68eb2c697d26b90db7f36c36e8b84c6c`; served_model `{"object": "list", "data": [{"id": "nanbeige", "object": "model", "created": 1793467400, "`; chip `Apple M5 Ultra; 274877906944`; suite_commit `21db9b23f7be`

### checks

| check | result |
|---|---|
| memory-idle | measured: mac: System-wide memory free percentage: 83%; total = 1024.00M  us |
| prefill-off | measured: 2111 tokens 1171.5 tok/s (1.802 s), 8255 tokens 1216.3 tok/s (6.787 s), 32829 tokens 1026.3 tok/s (31.987 s), 61498 tokens 815.4 tok/s (75.422 s) |
| prefill-thinking | measured: 2107 tokens 1175.8 tok/s (1.792 s), 8248 tokens 1239.2 tok/s (6.656 s), 32825 tokens 1003.0 tok/s (32.728 s), 61497 tokens 810.3 tok/s (75.892 s) |
| memory-busy | measured: mac: System-wide memory free percentage: 74%; total = 1024.00M  us |

## 2026-10-31 12:19: run `20261031-121952-speed`

Plan speed, done; served as `nanbeige`.

Serving: engine_commit `2e580cd76`; binary_sha256 `9e5abee41c72ae11079c59fa2f12df9e68eb2c697d26b90db7f36c36e8b84c6c`; served_model `{"object": "list", "data": [{"id": "nanbeige", "object": "model", "created": 1793467200, "`; chip `Apple M5 Ultra; 274877906944`; suite_commit `21db9b23f7be`

### ruler-fresh

| streams | prose total (a stream) | code total (a stream) | structured total (a stream) | list total (a stream) | first token |
|---:|---:|---:|---:|---:|---:|
| 1 | 81.3 (81.3) | 80.7 (80.7) | 81.0 (81.0) | 82.0 (82.0) | 0.27-0.30 s |
| 2 | 75.1 (37.5) | 75.2 (37.6) | 74.3 (37.2) | 75.8 (37.9) | 0.40-0.45 s |

Engine rounds (ruler-fresh):

| streams | tokens a round | drafts a round | accepted | ms a round | requests |
|---:|---:|---:|---:|---:|---:|
| 1 | 1.961 | 1.039 | 92% | 24.13 | 12 |
| 2 | 1.031 | 0.027 | 99% | 27.45 | 25 |

### ruler-after

| streams | prose total (a stream) | code total (a stream) | structured total (a stream) | list total (a stream) | first token |
|---:|---:|---:|---:|---:|---:|
| 1 | 82.0 (82.0) | 80.9 (80.9) | 81.1 (81.1) | 81.3 (81.3) | 0.27-0.30 s |

Engine rounds (ruler-after):

| streams | tokens a round | drafts a round | accepted | ms a round | requests |
|---:|---:|---:|---:|---:|---:|
| 1 | 1.983 | 1.06 | 92% | 24.38 | 13 |

### checks

| check | result |
|---|---|
| memory-idle | measured: mac: System-wide memory free percentage: 82%; total = 1024.00M  us |
| turns | pass: resumed == again: True; cold (after a restart): True; cached 5493 of 5649; ttft resumed 0.395s, cold 4.834s |
| memory-busy | measured: mac: System-wide memory free percentage: 83%; total = 1024.00M  us |

## 2026-10-31 12:00: run `20261031-120051-prefill-64k`

Plan prefill-64k, running; served as `nanbeige`.

Serving: engine_commit `2e580cd76`; binary_sha256 `2ac57539605adeffed625d9156f29f353df3da4dcb26fcb58438cc8dc7db6380`; served_model `{"object": "list", "data": [{"id": "nanbeige", "object": "model", "created": 1793466059, "`; chip `Apple M5 Ultra; 274877906944`; suite_commit `21db9b23f7be`

### checks

| check | result |
|---|---|
| memory-idle | measured: mac: System-wide memory free percentage: 82%; total = 1024.00M  us |
| prefill-off | measured: 2110 tokens 1167.0 tok/s (1.808 s), 8252 tokens 1234.8 tok/s (6.683 s), 32830 tokens 1024.1 tok/s (32.057 s), 61502 tokens 822.3 tok/s (74.795 s) |

## 2026-10-31 11:57: run `20261031-115730-speed`

Plan speed, done; served as `nanbeige`.

Serving: engine_commit `2e580cd76`; binary_sha256 `2ac57539605adeffed625d9156f29f353df3da4dcb26fcb58438cc8dc7db6380`; served_model `{"object": "list", "data": [{"id": "nanbeige", "object": "model", "created": 1793465859, "`; chip `Apple M5 Ultra; 274877906944`; suite_commit `21db9b23f7be`

### ruler-fresh

| streams | prose total (a stream) | code total (a stream) | structured total (a stream) | list total (a stream) | first token |
|---:|---:|---:|---:|---:|---:|
| 1 | 80.2 (80.2) | 80.7 (80.7) | 81.5 (81.5) | 79.5 (79.5) | 0.27-0.30 s |
| 2 | 74.8 (37.4) | 75.1 (37.6) | 74.2 (37.1) | 75.1 (37.6) | 0.41-0.45 s |

Engine rounds (ruler-fresh):

| streams | tokens a round | drafts a round | accepted | ms a round | requests |
|---:|---:|---:|---:|---:|---:|
| 1 | 1.975 | 1.067 | 90% | 24.54 | 12 |
| 2 | 1.031 | 0.027 | 99% | 27.56 | 25 |

### ruler-after

| streams | prose total (a stream) | code total (a stream) | structured total (a stream) | list total (a stream) | first token |
|---:|---:|---:|---:|---:|---:|
| 1 | 81.9 (81.9) | 79.2 (79.2) | 81.1 (81.1) | 81.2 (81.2) | 0.27-0.30 s |

Engine rounds (ruler-after):

| streams | tokens a round | drafts a round | accepted | ms a round | requests |
|---:|---:|---:|---:|---:|---:|
| 1 | 1.98 | 1.055 | 92% | 24.49 | 13 |

### checks

| check | result |
|---|---|
| memory-idle | measured: mac: System-wide memory free percentage: 82%; total = 1024.00M  us |
| turns | pass: resumed == again: True; cold (after a restart): True; cached 5493 of 5649; ttft resumed 0.405s, cold 4.798s |
| memory-busy | measured: mac: System-wide memory free percentage: 82%; total = 1024.00M  us |

## 2026-10-31 11:25: run `20261031-112510-quick`

Plan quick, done; served as `nanbeige`.

Serving: engine_commit `2e580cd76`; binary_sha256 `2ac57539605adeffed625d9156f29f353df3da4dcb26fcb58438cc8dc7db6380`; served_model `{"object": "list", "data": [{"id": "nanbeige", "object": "model", "created": 1793463923, "`; chip `Apple M5 Ultra; 274877906944`; suite_commit `21db9b23f7be`

### ruler-fresh

| streams | prose total (a stream) | code total (a stream) | structured total (a stream) | list total (a stream) | first token |
|---:|---:|---:|---:|---:|---:|
| 1 | 76.8 (76.8) | 77.4 (77.4) | 77.7 (77.7) | 80.2 (80.2) | 0.28-0.32 s |

Engine rounds (ruler-fresh):

| streams | tokens a round | drafts a round | accepted | ms a round | requests |
|---:|---:|---:|---:|---:|---:|
| 1 | 1.975 | 1.07 | 90% | 25.32 | 12 |

### ruler-after

| streams | prose total (a stream) | code total (a stream) | structured total (a stream) | list total (a stream) | first token |
|---:|---:|---:|---:|---:|---:|
| 1 | 35.8 (35.8) | 30.7 (30.7) | 26.6 (26.6) | 77.8 (77.8) | 0.30-0.88 s |

Engine rounds (ruler-after):

| streams | tokens a round | drafts a round | accepted | ms a round | requests |
|---:|---:|---:|---:|---:|---:|
| 1 | 2.826 | 1.995 | 91% | 66.16 | 13 |

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
| memory-idle | measured: mac: System-wide memory free percentage: 82%; total = 1024.00M  us |
| structured | pass: 18/18 obey, drafted == plain 12/12; a bad regex -> 400 |
| tools | pass: 5/5 tool cases right |
| sampling | pass: 9/9 seeded replies equal on repeat and undrafted; 0 errors |
| turns | pass: resumed == again: True; cold (after a restart): True; cached 5493 of 5649; ttft resumed 0.417s, cold 5.049s |

