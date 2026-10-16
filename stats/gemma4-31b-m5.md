# Gemma 4 31B, MLX 4-bit + DFlash on 1x Apple M5 Ultra (256 GB unified), macOS

Target `gemma4-31b-m5`: Gemma 4 31B 4-bit (groups of 64), DFlash drafts, images, TensorFold native Metal on one M5 Ultra. Engine: TensorFold native, Metal. Rendered from `stats/gemma4-31b-m5.json` (2 runs); aggregate tok/s, total (a stream).

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

