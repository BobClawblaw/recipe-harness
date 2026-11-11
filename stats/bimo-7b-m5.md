# Bimo-7B-CyberAgent, bf16 on 1x Apple M5 Ultra (256 GB unified), macOS

Target `bimo-7b-m5`: Bimo-7B-CyberAgent bf16 as released, TensorFold native Metal (llama family, Qwen2) on one M5 Ultra (32768-token window, 2 streams). Engine: TensorFold native, Metal. Rendered from `stats/bimo-7b-m5.json` (6 runs); aggregate tok/s, total (a stream).

## 2026-11-10 22:29: run `20261110-222925-humaneval-long-32k-off`

Plan humaneval-long-32k-off, done; served as `bimo`.

Serving: engine_commit `4cc353f0b`; binary_sha256 `cd01a302a7cdf9cd0969961abd4b57d766b6c75da3185472c8fd3cfe9632b5be`; served_model `{"object": "list", "data": [{"id": "bimo", "object": "model", "created": 1794371373, "owne`; chip `Apple M5 Ultra; 274877906944`; suite_commit `b3b0ef38b8bc`

### suite-humaneval-long-32k

| check | passed |
|---|---:|
| humaneval | 79/164 |
| long-context | 3/3 |
| long-tasks | 0/0 |

## 2026-11-10 18:34: run `20261110-183417-quality-off`

Plan quality-off, done; served as `bimo`.

Serving: engine_commit `4cc353f0b`; binary_sha256 `cd01a302a7cdf9cd0969961abd4b57d766b6c75da3185472c8fd3cfe9632b5be`; served_model `{"object": "list", "data": [{"id": "bimo", "object": "model", "created": 1794357265, "owne`; chip `Apple M5 Ultra; 274877906944`; suite_commit `b3b0ef38b8bc`

### ruler-fresh

| streams | prose total (a stream) | code total (a stream) | structured total (a stream) | list total (a stream) | first token |
|---:|---:|---:|---:|---:|---:|
| 1 | 49.7 (49.7) | 45.6 (45.6) | 54.0 (54.0) | 40.5 (40.5) | 0.07-0.10 s |

Engine rounds (ruler-fresh):

| streams | tokens a round | drafts a round | accepted | ms a round | requests |
|---:|---:|---:|---:|---:|---:|
| 1 | 1.004 | 0.0 |  | 21.17 | 12 |

### ruler-after

| streams | prose total (a stream) | code total (a stream) | structured total (a stream) | list total (a stream) | first token |
|---:|---:|---:|---:|---:|---:|
| 1 | 41.4 (41.4) | 40.8 (40.8) | 41.6 (41.6) | 43.5 (43.5) | 0.10-0.11 s |

Engine rounds (ruler-after):

| streams | tokens a round | drafts a round | accepted | ms a round | requests |
|---:|---:|---:|---:|---:|---:|
| 1 | 1.005 | 0.0 |  | 24.01 | 14 |

### suite

| check | passed |
|---|---:|
| drafts | 12/12 |
| streaming | 4/4 |
| multiturn | 8/8 |
| stop | 3/3 |
| thinking | 0/10 |
| copy | 2/2 |
| max-tokens | 2/3 |
| tools | 9/60 |
| json | 25/30 |
| ifeval | 61/150 |
| gsm8k | 180/250 |
| mgsm | 96/240 |
| mmlu | 182/342 |
| math500 | 207/500 |
| gpqa | 47/198 |
| humaneval | 0/0 |
| repetition | 0/8 |
| long-context | 0/0 |
| long-tasks | 0/52 |
| soak | 60/60 |
| snapshot | 12/12 |
| vision | 0/6 |
| docvision | 0/0 |
| concurrent | 12/12 |
| vision-concurrent | 0/0 |

## 2026-11-10 18:16: run `20261110-181601-speed`

Plan speed, done; served as `bimo`.

Serving: engine_commit `7662e079c`; binary_sha256 `cd01a302a7cdf9cd0969961abd4b57d766b6c75da3185472c8fd3cfe9632b5be`; served_model `{"object": "list", "data": [{"id": "bimo", "object": "model", "created": 1794356169, "owne`; chip `Apple M5 Ultra; 274877906944`; suite_commit `b3b0ef38b8bc`

### ruler-fresh

| streams | prose total (a stream) | code total (a stream) | structured total (a stream) | list total (a stream) | first token |
|---:|---:|---:|---:|---:|---:|
| 1 | 55.7 (55.7) | 44.4 (44.4) | 55.6 (55.6) | 55.9 (55.9) | 0.07-0.10 s |
| 2 | 88.6 (44.3) | 103.8 (51.9) | 113.3 (56.7) | 113.4 (56.7) | 0.11-0.14 s |

Engine rounds (ruler-fresh):

| streams | tokens a round | drafts a round | accepted | ms a round | requests |
|---:|---:|---:|---:|---:|---:|
| 1 | 1.004 | 0.0 |  | 18.99 | 12 |
| 2 | 1.005 | 0.0 |  | 19.17 | 25 |

### ruler-after

| streams | prose total (a stream) | code total (a stream) | structured total (a stream) | list total (a stream) | first token |
|---:|---:|---:|---:|---:|---:|
| 1 | 44.3 (44.3) | 45.6 (45.6) | 48.9 (48.9) | 42.4 (42.4) | 0.09-0.10 s |

Engine rounds (ruler-after):

| streams | tokens a round | drafts a round | accepted | ms a round | requests |
|---:|---:|---:|---:|---:|---:|
| 1 | 1.004 | 0.0 |  | 22.17 | 13 |

### checks

| check | result |
|---|---|
| memory-idle | measured: mac: System-wide memory free percentage: 89%; total = 13312.00M  u |
| turns | pass: resumed == again: True; cold (after a restart): True; cached 5493 of 5583; ttft resumed 0.133s, cold 1.061s |
| memory-busy | measured: mac: System-wide memory free percentage: 55%; total = 13312.00M  u |

## 2026-11-10 18:06: run `20261110-180619-prefill-32k`

Plan prefill-32k, done; served as `bimo`.

Serving: engine_commit `7662e079c`; binary_sha256 `cd01a302a7cdf9cd0969961abd4b57d766b6c75da3185472c8fd3cfe9632b5be`; served_model `{"object": "list", "data": [{"id": "bimo", "object": "model", "created": 1794355587, "owne`; chip `Apple M5 Ultra; 274877906944`; suite_commit `b3b0ef38b8bc`

### checks

| check | result |
|---|---|
| memory-idle | measured: mac: System-wide memory free percentage: 89%; total = 13312.00M  u |
| prefill-off | FAIL: 2288 tokens 5973.9 tok/s (0.383 s), 8838 tokens 6163.2 tok/s (1.434 s), 17567 tokens 5654.0 tok/s (3.107 s); not cold or failed: ['30720'] |
| prefill-thinking | FAIL: 2256 tokens 6130.4 tok/s (0.368 s), 8808 tokens 6150.8 tok/s (1.432 s), 17551 tokens 5700.2 tok/s (3.079 s); not cold or failed: ['30720'] |
| memory-busy | measured: mac: System-wide memory free percentage: 88%; total = 13312.00M  u |

## 2026-11-10 18:03: run `20261110-180301-speed`

Plan speed, done; served as `bimo`.

Serving: engine_commit `7662e079c`; binary_sha256 `cd01a302a7cdf9cd0969961abd4b57d766b6c75da3185472c8fd3cfe9632b5be`; served_model `{"object": "list", "data": [{"id": "bimo", "object": "model", "created": 1794355389, "owne`; chip `Apple M5 Ultra; 274877906944`; suite_commit `b3b0ef38b8bc`

### ruler-fresh

| streams | prose total (a stream) | code total (a stream) | structured total (a stream) | list total (a stream) | first token |
|---:|---:|---:|---:|---:|---:|
| 1 | 50.6 (50.6) | 44.4 (44.4) | 57.4 (57.4) | 55.3 (55.3) | 0.07-0.10 s |
| 2 | 119.3 (59.7) | 112.4 (56.2) | 109.3 (54.7) | 113.7 (56.9) | 0.11-0.11 s |

Engine rounds (ruler-fresh):

| streams | tokens a round | drafts a round | accepted | ms a round | requests |
|---:|---:|---:|---:|---:|---:|
| 1 | 1.049 | 0.095 | 47% | 20.21 | 12 |
| 2 | 1.03 | 0.074 | 34% | 18.12 | 25 |

### ruler-after

| streams | prose total (a stream) | code total (a stream) | structured total (a stream) | list total (a stream) | first token |
|---:|---:|---:|---:|---:|---:|
| 1 | 53.0 (53.0) | 42.4 (42.4) | 43.9 (43.9) | 53.5 (53.5) | 0.10-0.11 s |

Engine rounds (ruler-after):

| streams | tokens a round | drafts a round | accepted | ms a round | requests |
|---:|---:|---:|---:|---:|---:|
| 1 | 1.049 | 0.094 | 47% | 21.76 | 13 |

### checks

| check | result |
|---|---|
| memory-idle | measured: mac: System-wide memory free percentage: 70%; total = 13312.00M  u |
| turns | pass: resumed == again: True; cold (after a restart): True; cached 5493 of 5583; ttft resumed 0.095s, cold 0.962s |
| memory-busy | measured: mac: System-wide memory free percentage: 89%; total = 13312.00M  u |

## 2026-11-10 17:54: run `20261110-175449-quick`

Plan quick, done; served as `bimo`.

Serving: engine_commit `7662e079c`; binary_sha256 `cd01a302a7cdf9cd0969961abd4b57d766b6c75da3185472c8fd3cfe9632b5be`; served_model `{"object": "list", "data": [{"id": "bimo", "object": "model", "created": 1794354897, "owne`; chip `Apple M5 Ultra; 274877906944`; suite_commit `b3b0ef38b8bc`

### ruler-fresh

| streams | prose total (a stream) | code total (a stream) | structured total (a stream) | list total (a stream) | first token |
|---:|---:|---:|---:|---:|---:|
| 1 | 63.7 (63.7) | 43.7 (43.7) | 56.4 (56.4) | 43.9 (43.9) | 0.07-0.10 s |

Engine rounds (ruler-fresh):

| streams | tokens a round | drafts a round | accepted | ms a round | requests |
|---:|---:|---:|---:|---:|---:|
| 1 | 1.049 | 0.095 | 47% | 20.19 | 12 |

### ruler-after

| streams | prose total (a stream) | code total (a stream) | structured total (a stream) | list total (a stream) | first token |
|---:|---:|---:|---:|---:|---:|
| 1 | 61.1 (61.1) | 51.7 (51.7) | 48.2 (48.2) | 52.7 (52.7) | 0.07-0.10 s |

Engine rounds (ruler-after):

| streams | tokens a round | drafts a round | accepted | ms a round | requests |
|---:|---:|---:|---:|---:|---:|
| 1 | 1.049 | 0.094 | 47% | 19.63 | 13 |

### suite

| check | passed |
|---|---:|
| soak | 60/60 |
| drafts | 12/12 |
| concurrent | 12/12 |
| streaming | 4/4 |
| multiturn | 8/8 |
| stop | 3/3 |
| thinking | 0/10 |
| copy | 2/2 |
| max-tokens | 2/3 |

### checks

| check | result |
|---|---|
| memory-idle | measured: mac: System-wide memory free percentage: 89%; total = 13312.00M  u |
| structured | pass: 18/18 obey, drafted == plain 12/12; a bad regex -> 400 |
| tools | FAIL: 4/5 tool cases right; failed auto (finish stop) |
| sampling | pass: 9/9 seeded replies equal on repeat and undrafted; 0 errors |
| turns | pass: resumed == again: True; cold (after a restart): True; cached 5493 of 5583; ttft resumed 0.133s, cold 0.959s |

