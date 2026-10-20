# DeepSeek-V4.1-Flash-1017 EXL3 2.9bpw abliterated on 2x NVIDIA DGX Spark (GB10, 128 GB unified each), TP=2 over RoCE

Target `dsv41-1017-ablit`: DeepSeek-V4.1-Flash-1017 EXL3 2.9 bpw abliterated, TensorFold native (Zig) TP=2 on two DGX Sparks, 4 slots, 1M window. Engine: TensorFold native (Zig, CUDA) + EXL3 TP=2 kit, recipe defaults (replay prefill, DSpark drafts, thinking on). Rendered from `stats/dsv41-1017-ablit.json` (3 runs); aggregate tok/s, total (a stream).

## 2026-10-20 13:14: run `20261020-131445-dsv41-speed8`

Plan dsv41-speed8, done; served as `DeepSeek-V4.1-Flash-1017`.

Serving: image `d9acaf504779`; patches `8eb5919ff0a4`; ablit `0bdc2036`; served `{"object": "list", "data": [{"id": "DeepSeek-V4.1-Flash-1017", "object": "model", "created`; pack `6c4679e6407806ab`; suite_commit `35b24fedcc37`

### ruler-streams

| streams | prose total (a stream) | code total (a stream) | structured total (a stream) | list total (a stream) | first token |
|---:|---:|---:|---:|---:|---:|
| 1 | 65.3 (65.3) | 94.6 (94.6) | 87.3 (87.3) | 94.9 (94.9) | 0.10-0.16 s |
| 2 | 91.9 (45.9) | 132.3 (66.2) | 109.1 (54.6) | 163.3 (81.6) | 0.15-0.24 s |
| 4 | 119.5 (29.9) | 164.3 (40.0) | 136.1 (34.3) | 211.2 (51.4) | 0.25-0.41 s |
| 8 | 226.2 (27.9) | 318.9 (41.1) | 249.9 (30.6) | 358.8 (43.0) | 1.76-3.96 s |

### checks

| check | result |
|---|---|
| memory-idle | measured: head 6.5 GiB available; worker 8.4 GiB available |

## 2026-10-20 13:05: run `20261020-130511-quick`

Plan quick, done; served as `DeepSeek-V4.1-Flash-1017`.

Serving: image `d9acaf504779`; patches `8eb5919ff0a4`; ablit `0bdc2036`; served `{"object": "list", "data": [{"id": "DeepSeek-V4.1-Flash-1017", "object": "model", "created`; pack `6c4679e6407806ab`; suite_commit `35b24fedcc37`

### ruler-fresh

| streams | prose total (a stream) | code total (a stream) | structured total (a stream) | list total (a stream) | first token |
|---:|---:|---:|---:|---:|---:|
| 1 | 65.4 (65.4) | 94.3 (94.3) | 87.5 (87.5) | 95.6 (95.6) | 0.10-0.16 s |

### ruler-after

| streams | prose total (a stream) | code total (a stream) | structured total (a stream) | list total (a stream) | first token |
|---:|---:|---:|---:|---:|---:|
| 1 | 65.6 (65.6) | 94.8 (94.8) | 87.3 (87.3) | 95.4 (95.4) | 0.10-0.16 s |

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
| memory-idle | measured: head 7.2 GiB available; worker 9.1 GiB available |
| sampling | pass: 9/9 seeded replies equal on repeat and undrafted; 0 errors |
| turns | pass: resumed == again == cold: True; cached 4096 of 4556; ttft resumed 0.501s, cold 0.515s |

## 2026-10-20 12:55: run `20261020-125507-quick`

Plan quick, done; served as `DeepSeek-V4.1-Flash-1017`.

Serving: image `d9acaf504779`; patches `8eb5919ff0a4`; ablit `0bdc2036`; served `{"object": "list", "data": [{"id": "DeepSeek-V4.1-Flash-1017", "object": "model", "created`; pack `6c4679e6407806ab`; suite_commit `35b24fedcc37`

### ruler-fresh

| streams | prose total (a stream) | code total (a stream) | structured total (a stream) | list total (a stream) | first token |
|---:|---:|---:|---:|---:|---:|
| 1 | 65.6 (65.6) | 94.1 (94.1) | 88.1 (88.1) | 95.2 (95.2) | 0.10-0.16 s |

### ruler-after

| streams | prose total (a stream) | code total (a stream) | structured total (a stream) | list total (a stream) | first token |
|---:|---:|---:|---:|---:|---:|
| 1 | 65.7 (65.7) | 94.5 (94.5) | 87.4 (87.4) | 95.4 (95.4) | 0.10-0.16 s |

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
| memory-idle | measured: head 7.2 GiB available; worker 9.0 GiB available |
| structured | FAIL: 0/18 obey, drafted == plain 12/12; a bad regex -> 400; failed json_object/greedy, json_object/sampled, json_object/thinking, json_schema/greedy, json_schema/sampled, json_schema/thinking, guided_json/greedy, guided_json/sampled, guided_json/thinking, regex/greedy, regex/sampled, regex/thinking, choice/greedy, choice/sampled, choice/thinking, grammar/greedy, grammar/sampled, grammar/thinking |
| sampling | pass: 9/9 seeded replies equal on repeat and undrafted; 0 errors |
| turns | pass: resumed == again == cold: True; cached 4096 of 4556; ttft resumed 0.505s, cold 0.514s |

