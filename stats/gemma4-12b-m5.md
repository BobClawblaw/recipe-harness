# Gemma 4 12B, MLX 4-bit + MTP assistant on 1x Apple M5 Ultra (256 GB unified), macOS

Target `gemma4-12b-m5`: Gemma 4 12B 4-bit (groups of 64), MTP assistant drafts, images, TensorFold native Metal on one M5 Ultra. Engine: TensorFold native, Metal. Rendered from `stats/gemma4-12b-m5.json` (6 runs); aggregate tok/s, total (a stream).

## 2026-10-16 15:38: run `20261016-153843-thinking`

Plan thinking, running; served as `gemma4-12b`.

Serving: engine_commit `74005ebe`; binary_sha256 `215b4b7e3cd14a9d8178b4dc885d9f1dffbebd0f4ec2e9b274653820b71da8d2`; served_model `{"object": "list", "data": [{"id": "gemma4-12b", "object": "model", "created": 1792183124,`; chip `Apple M5 Ultra; 274877906944`

### checks

| check | result |
|---|---|
| thinking | FAIL: thinking on: 6/10 right, 10/10 with reasoning_content, 0 leaks, 0 errors |

## 2026-10-16 15:20: run `20261016-152057-structured`

Plan structured, done; served as `gemma4-12b`.

Serving: engine_commit `74005ebe`; binary_sha256 `215b4b7e3cd14a9d8178b4dc885d9f1dffbebd0f4ec2e9b274653820b71da8d2`; served_model `{"object": "list", "data": [{"id": "gemma4-12b", "object": "model", "created": 1792182065,`; chip `Apple M5 Ultra; 274877906944`

### checks

| check | result |
|---|---|
| structured | pass: 18/18 obey; a bad regex -> 400 |

## 2026-10-16 11:54: run `20261016-115409-structured`

Plan structured, done; served as `gemma4-12b`.

Serving: engine_commit `74005ebe`; binary_sha256 `215b4b7e3cd14a9d8178b4dc885d9f1dffbebd0f4ec2e9b274653820b71da8d2`; served_model `{"object": "list", "data": [{"id": "gemma4-12b", "object": "model", "created": 1792169657,`; chip `Apple M5 Ultra; 274877906944`

### checks

| check | result |
|---|---|
| structured | pass: 18/18 obey; a bad regex -> 400 |

## 2026-10-16 11:53: run `20261016-115336-structured`

Plan structured, done; served as `gemma4-12b`.

Serving: engine_commit `74005ebe`; binary_sha256 `215b4b7e3cd14a9d8178b4dc885d9f1dffbebd0f4ec2e9b274653820b71da8d2`; served_model `{"object": "list", "data": [{"id": "gemma4-12b", "object": "model", "created": 1792169624,`; chip `Apple M5 Ultra; 274877906944`

### checks

| check | result |
|---|---|
| structured | pass: 18/18 obey; a bad regex -> 400 |

## 2026-10-16 11:36: run `20261016-113616-g12-quality`

Plan g12-quality, done; served as `gemma4-12b`.

Serving: engine_commit `74005ebe`; binary_sha256 `215b4b7e3cd14a9d8178b4dc885d9f1dffbebd0f4ec2e9b274653820b71da8d2`; served_model `{"object": "list", "data": [{"id": "gemma4-12b", "object": "model", "created": 1792168585,`; chip `Apple M5 Ultra; 274877906944`

### suite

| check | passed |
|---|---:|
| tools | 58/60 |
| json | 30/30 |
| gsm8k | 239/250 |
| mmlu | 264/342 |

## 2026-10-16 11:31: run `20261016-113151-quick`

Plan quick, done; served as `gemma4-12b`.

Serving: engine_commit `74005ebe`; binary_sha256 `215b4b7e3cd14a9d8178b4dc885d9f1dffbebd0f4ec2e9b274653820b71da8d2`; served_model `{"object": "list", "data": [{"id": "gemma4-12b", "object": "model", "created": 1792168324,`; chip `Apple M5 Ultra; 274877906944`

### ruler-fresh

| streams | prose total (a stream) | code total (a stream) | structured total (a stream) | list total (a stream) | first token |
|---:|---:|---:|---:|---:|---:|
| 1 | 140.2 (140.2) | 223.3 (223.3) | 205.4 (205.4) | 247.7 (247.7) | 0.04-0.05 s |

Engine rounds (ruler-fresh):

| streams | tokens a round | drafts a round | accepted | ms a round | requests |
|---:|---:|---:|---:|---:|---:|
| 1 | 3.229 | 4.899 | 45% | 15.82 | 12 |

### ruler-after

| streams | prose total (a stream) | code total (a stream) | structured total (a stream) | list total (a stream) | first token |
|---:|---:|---:|---:|---:|---:|
| 1 | 140.6 (140.6) | 217.3 (217.3) | 205.3 (205.3) | 243.9 (243.9) | 0.05-0.05 s |

Engine rounds (ruler-after):

| streams | tokens a round | drafts a round | accepted | ms a round | requests |
|---:|---:|---:|---:|---:|---:|
| 1 | 3.207 | 4.837 | 45% | 15.89 | 17 |

### suite

| check | passed |
|---|---:|
| soak | 60/60 |
| drafts | 12/12 |
| concurrent | 12/12 |
| streaming | 4/4 |
| multiturn | 8/8 |
| stop | 3/3 |
| thinking | 8/10 |
| copy | 2/2 |
| max-tokens | 3/3 |

### checks

| check | result |
|---|---|
| memory-idle | measured: mac: System-wide memory free percentage: 88%; total = 4096.00M  us |
| structured | FAIL: 0/18 obey; a bad regex -> 400; failed json_object/greedy, json_object/sampled, json_object/thinking, json_schema/greedy, json_schema/sampled, json_schema/thinking, guided_json/greedy, guided_json/sampled, guided_json/thinking, regex/greedy, regex/sampled, regex/thinking, choice/greedy, choice/sampled, choice/thinking, grammar/greedy, grammar/sampled, grammar/thinking |
| sampling | pass: 9/9 seeded replies equal on repeat and undrafted; 0 errors |
| turns | pass: resumed == again == cold: True; cached 5494 of 5565; ttft resumed 0.063s, cold 0.062s |

