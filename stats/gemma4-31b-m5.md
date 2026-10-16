# Gemma 4 31B, MLX 4-bit + DFlash on 1x Apple M5 Ultra (256 GB unified), macOS

Target `gemma4-31b-m5`: Gemma 4 31B 4-bit (groups of 64), DFlash drafts, images, TensorFold native Metal on one M5 Ultra. Engine: TensorFold native, Metal. Rendered from `stats/gemma4-31b-m5.json` (6 runs); aggregate tok/s, total (a stream).

## 2026-10-16 08:54: run `20261016-085420-quick`

Plan quick, done; served as `gemma4-31b`.

Serving: engine_commit `e8b60549`; binary_sha256 `d90e44c9818187ae4bc61d06312989cd796033b5dea6e0fc02164fe2730660fe`; served_model `{"object": "list", "data": [{"id": "gemma4-31b", "object": "model", "created": 1792158874,`; chip `Apple M5 Ultra; 274877906944`

### ruler-fresh

| streams | prose total (a stream) | code total (a stream) | structured total (a stream) | list total (a stream) | first token |
|---:|---:|---:|---:|---:|---:|
| 1 | 87.1 (87.1) | 157.9 (157.9) | 156.7 (156.7) | 130.4 (130.4) | 0.08-0.10 s |

Engine rounds (ruler-fresh):

| streams | tokens a round | drafts a round | accepted | ms a round | requests |
|---:|---:|---:|---:|---:|---:|
| 1 | 3.288 | 13.003 | 18% | 24.71 | 12 |

### ruler-after

| streams | prose total (a stream) | code total (a stream) | structured total (a stream) | list total (a stream) | first token |
|---:|---:|---:|---:|---:|---:|
| 1 | 92.1 (92.1) | 161.4 (161.4) | 146.6 (146.6) | 126.1 (126.1) | 0.09-0.10 s |

Engine rounds (ruler-after):

| streams | tokens a round | drafts a round | accepted | ms a round | requests |
|---:|---:|---:|---:|---:|---:|
| 1 | 3.333 | 13.215 | 18% | 25.34 | 17 |

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
| memory-idle | measured: mac: System-wide memory free percentage: 75%; total = 3072.00M  us |
| structured | pass: 18/18 obey; a bad regex -> 400 |
| sampling | pass: 9/9 seeded replies equal on repeat and undrafted; 0 errors |
| turns | pass: resumed == again == cold: True; cached 5494 of 5564; ttft resumed 0.137s, cold 0.137s |

## 2026-10-16 06:28: run `20261016-062851-quick`

Plan quick, done; served as `gemma4-31b`.

Serving: engine_commit `7032c3ee`; binary_sha256 `1ffe379affacadd4905c604462a41f9a19babcd64f8db958b40b67fcedd78ac4`; served_model `{"object": "list", "data": [{"id": "gemma4-31b", "object": "model", "created": 1792150144,`; chip `Apple M5 Ultra; 274877906944`

### ruler-fresh

| streams | prose total (a stream) | code total (a stream) | structured total (a stream) | list total (a stream) | first token |
|---:|---:|---:|---:|---:|---:|
| 1 | 89.9 (89.9) | 156.5 (156.5) | 141.6 (141.6) | 129.7 (129.7) | 0.09-0.10 s |

Engine rounds (ruler-fresh):

| streams | tokens a round | drafts a round | accepted | ms a round | requests |
|---:|---:|---:|---:|---:|---:|
| 1 | 3.235 | 12.922 | 17% | 24.99 | 12 |

### ruler-after

| streams | prose total (a stream) | code total (a stream) | structured total (a stream) | list total (a stream) | first token |
|---:|---:|---:|---:|---:|---:|
| 1 | 90.9 (90.9) | 154.5 (154.5) | 141.2 (141.2) | 128.3 (128.3) | 0.09-0.10 s |

Engine rounds (ruler-after):

| streams | tokens a round | drafts a round | accepted | ms a round | requests |
|---:|---:|---:|---:|---:|---:|
| 1 | 3.262 | 12.799 | 18% | 25.34 | 17 |

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
| memory-idle | measured: mac: System-wide memory free percentage: 76%; total = 3072.00M  us |
| structured | pass: 18/18 obey; a bad regex -> 400 |
| sampling | pass: 9/9 seeded replies equal on repeat and undrafted; 0 errors |
| turns | pass: resumed == again == cold: True; cached 5494 of 5564; ttft resumed 0.141s, cold 0.141s |

## 2026-10-16 05:24: run `20261016-052455-structured`

Plan structured, done; served as `gemma4-31b`.

Serving: engine_commit `5154a1b5`; binary_sha256 `1bd7ed5fd7e9e8eb94354fc2b9f9fd2d1ac774cf00a4f835a56788353f0199c7`; served_model `{"object": "list", "data": [{"id": "gemma4-31b", "object": "model", "created": 1792146308,`; chip `Apple M5 Ultra; 274877906944`

### checks

| check | result |
|---|---|
| structured | pass: 18/18 obey; a bad regex -> 400 |

## 2026-10-16 05:11: run `20261016-051157-structured`

Plan structured, done; served as `gemma4-31b`.

Serving: engine_commit `0fbb3e2d`; binary_sha256 `3062bfb742a5f24d8346c6dc92c9849d2a4d3a598160b80644d81e72952eefdb`; served_model `{"object": "list", "data": [{"id": "gemma4-31b", "object": "model", "created": 1792145531,`; chip `Apple M5 Ultra; 274877906944`

### checks

| check | result |
|---|---|
| structured | pass: 18/18 obey; a bad regex -> 400 |

## 2026-10-15 23:59: run `20261015-235922-structured`

Plan structured, done; served as `gemma4-31b`.

Serving: engine_commit `8c37d22c`; binary_sha256 `507c6fc3b1f9f5a521185d3da00ec3f555c39e20188ba8eefec2547581bb618d`; served_model `{"object": "list", "data": [{"id": "gemma4-31b", "object": "model", "created": 1792126775,`; chip `Apple M5 Ultra; 274877906944`

### checks

| check | result |
|---|---|
| structured | pass: 18/18 obey; a bad regex -> 400 |

## 2026-10-15 20:09: run `20261015-200951-quick`

Plan quick, done; served as `gemma4-31b`.

Serving: engine_commit `8c37d22c`; binary_sha256 `bb91242a259030711be1d274c53dbbfbcca01d805d94c2cc6de4da1c07919e2b`; served_model `{"object": "list", "data": [{"id": "gemma4-31b", "object": "model", "created": 1792113009,`; chip `Apple M5 Ultra; 274877906944`

### ruler-fresh

| streams | prose total (a stream) | code total (a stream) | structured total (a stream) | list total (a stream) | first token |
|---:|---:|---:|---:|---:|---:|
| 1 | 90.4 (90.4) | 153.8 (153.8) | 148.4 (148.4) | 126.1 (126.1) | 0.11-0.15 s |

Engine rounds (ruler-fresh):

| streams | tokens a round | drafts a round | accepted | ms a round | requests |
|---:|---:|---:|---:|---:|---:|
| 1 | 3.315 | 13.036 | 18% | 25.57 | 12 |

### ruler-after

| streams | prose total (a stream) | code total (a stream) | structured total (a stream) | list total (a stream) | first token |
|---:|---:|---:|---:|---:|---:|
| 1 | 90.1 (90.1) | 164.2 (164.2) | 145.9 (145.9) | 124.2 (124.2) | 0.10-0.16 s |

Engine rounds (ruler-after):

| streams | tokens a round | drafts a round | accepted | ms a round | requests |
|---:|---:|---:|---:|---:|---:|
| 1 | 3.328 | 12.662 | 18% | 25.39 | 17 |

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
| memory-idle | measured: mac: System-wide memory free percentage: 96%; total = 4096.00M  us |
| structured | FAIL: 0/18 obey; a bad regex -> 400; failed json_object/greedy, json_object/sampled, json_object/thinking, json_schema/greedy, json_schema/sampled, json_schema/thinking, guided_json/greedy, guided_json/sampled, guided_json/thinking, regex/greedy, regex/sampled, regex/thinking, choice/greedy, choice/sampled, choice/thinking, grammar/greedy, grammar/sampled, grammar/thinking |
| sampling | pass: 9/9 seeded replies equal on repeat and undrafted; 0 errors |
| turns | pass: resumed == again == cold: True; cached 5494 of 5564; ttft resumed 0.135s, cold 0.134s |

