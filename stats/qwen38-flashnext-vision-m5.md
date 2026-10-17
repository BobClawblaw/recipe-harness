# Qwen3.8-Flash-Next, 6-bit with vision on 1x Apple M5 Ultra (256 GB unified), macOS

Target `qwen38-flashnext-vision-m5`: Qwen3.8-Flash-Next 6-bit MTP with images and video, TensorFold native Metal on one M5 Ultra. Engine: TensorFold native, Metal. Rendered from `stats/qwen38-flashnext-vision-m5.json` (10 runs); aggregate tok/s, total (a stream).

## 2026-10-17 05:58: run `20261017-055855-fn-speed`

Plan fn-speed, done; served as `Qwen3.8-Flash-Next-MLX-6bit`.

Serving: engine_commit `8a509ab5`; binary_sha256 `61af7bb33cb65982710b0b19b7ddc434b94fd6bffcb556a858a17b53e74d64ff`; served_model `{"object": "list", "data": [{"id": "Qwen3.8-Flash-Next-MLX-6bit", "object": "model", "crea`; chip `Apple M5 Ultra; 274877906944`

### ruler-fresh

| streams | prose total (a stream) | code total (a stream) | structured total (a stream) | list total (a stream) | first token |
|---:|---:|---:|---:|---:|---:|
| 1 | 141.8 (141.8) | 208.0 (208.0) | 171.5 (171.5) | 205.2 (205.2) | 0.11-0.12 s |
| 2 | 196.0 (98.0) | 262.7 (131.4) | 231.6 (115.8) | 268.5 (134.2) | 0.17-0.19 s |

### suite

| check | passed |
|---|---:|
| drafts | 12/12 |
| concurrent | 12/12 |

### checks

| check | result |
|---|---|
| structured | FAIL: 0/18 obey; a bad regex -> 400; failed json_object/greedy, json_object/sampled, json_object/thinking, json_schema/greedy, json_schema/sampled, json_schema/thinking, guided_json/greedy, guided_json/sampled, guided_json/thinking, regex/greedy, regex/sampled, regex/thinking, choice/greedy, choice/sampled, choice/thinking, grammar/greedy, grammar/sampled, grammar/thinking |

## 2026-10-17 01:00: run `20261017-010018-fn-speed`

Plan fn-speed, done; served as `Qwen3.8-Flash-Next-MLX-6bit`.

Serving: engine_commit `7808bee8`; binary_sha256 `b34cfd768740820c73d7b223b8d98198dda3fd26a826806dd15ef039df948856`; served_model `{"object": "list", "data": [{"id": "Qwen3.8-Flash-Next-MLX-6bit", "object": "model", "crea`; chip `Apple M5 Ultra; 274877906944`

### ruler-fresh

| streams | prose total (a stream) | code total (a stream) | structured total (a stream) | list total (a stream) | first token |
|---:|---:|---:|---:|---:|---:|
| 1 | 138.4 (138.4) | 202.8 (202.8) | 169.6 (169.6) | 207.4 (207.4) | 0.11-0.12 s |
| 2 | 196.2 (98.1) | 253.3 (126.7) | 220.6 (110.3) | 268.8 (134.4) | 0.18-0.20 s |

### suite

| check | passed |
|---|---:|
| drafts | 12/12 |
| concurrent | 12/12 |

### checks

| check | result |
|---|---|
| structured | FAIL: 0/18 obey; a bad regex -> 400; failed json_object/greedy, json_object/sampled, json_object/thinking, json_schema/greedy, json_schema/sampled, json_schema/thinking, guided_json/greedy, guided_json/sampled, guided_json/thinking, regex/greedy, regex/sampled, regex/thinking, choice/greedy, choice/sampled, choice/thinking, grammar/greedy, grammar/sampled, grammar/thinking |

## 2026-10-17 00:57: run `20261017-005749-fn-speed`

Plan fn-speed, done; served as `Qwen3.8-Flash-Next-MLX-6bit`.

Serving: engine_commit `5164380e`; binary_sha256 `9e0dab55a0902d4072676f85c0e02eebe969a48e3626730c475e9c6631679428`; served_model `{"object": "list", "data": [{"id": "Qwen3.8-Flash-Next-MLX-6bit", "object": "model", "crea`; chip `Apple M5 Ultra; 274877906944`

### ruler-fresh

| streams | prose total (a stream) | code total (a stream) | structured total (a stream) | list total (a stream) | first token |
|---:|---:|---:|---:|---:|---:|
| 1 | 139.9 (139.9) | 207.3 (207.3) | 167.7 (167.7) | 210.1 (210.1) | 0.28-0.31 s |
| 2 | 188.6 (94.3) | 247.6 (123.8) | 210.0 (105.0) | 260.8 (130.4) | 0.34-0.38 s |

### suite

| check | passed |
|---|---:|
| drafts | 12/12 |
| concurrent | 12/12 |

### checks

| check | result |
|---|---|
| structured | FAIL: 0/18 obey; a bad regex -> 400; failed json_object/greedy, json_object/sampled, json_object/thinking, json_schema/greedy, json_schema/sampled, json_schema/thinking, guided_json/greedy, guided_json/sampled, guided_json/thinking, regex/greedy, regex/sampled, regex/thinking, choice/greedy, choice/sampled, choice/thinking, grammar/greedy, grammar/sampled, grammar/thinking |

## 2026-10-16 19:29: run `20261016-192936-fn-speed`

Plan fn-speed, done; served as `Qwen3.8-Flash-Next-MLX-6bit`.

Serving: engine_commit `5164380e`; binary_sha256 `9e0dab55a0902d4072676f85c0e02eebe969a48e3626730c475e9c6631679428`; served_model `{"object": "list", "data": [{"id": "Qwen3.8-Flash-Next-MLX-6bit", "object": "model", "crea`; chip `Apple M5 Ultra; 274877906944`

### ruler-fresh

| streams | prose total (a stream) | code total (a stream) | structured total (a stream) | list total (a stream) | first token |
|---:|---:|---:|---:|---:|---:|
| 1 | 141.0 (141.0) | 201.8 (201.8) | 172.5 (172.5) | 207.3 (207.3) | 0.28-0.31 s |
| 2 | 193.8 (96.9) | 249.1 (124.6) | 210.6 (105.3) | 264.1 (132.1) | 0.34-0.37 s |

### suite

| check | passed |
|---|---:|
| drafts | 12/12 |
| concurrent | 12/12 |

### checks

| check | result |
|---|---|
| structured | FAIL: 0/18 obey; a bad regex -> 400; failed json_object/greedy, json_object/sampled, json_object/thinking, json_schema/greedy, json_schema/sampled, json_schema/thinking, guided_json/greedy, guided_json/sampled, guided_json/thinking, regex/greedy, regex/sampled, regex/thinking, choice/greedy, choice/sampled, choice/thinking, grammar/greedy, grammar/sampled, grammar/thinking |

## 2026-10-16 19:26: run `20261016-192624-fn-speed`

Plan fn-speed, done; served as `Qwen3.8-Flash-Next-MLX-6bit`.

Serving: engine_commit `7808bee8`; binary_sha256 `b34cfd768740820c73d7b223b8d98198dda3fd26a826806dd15ef039df948856`; served_model `{"object": "list", "data": [{"id": "Qwen3.8-Flash-Next-MLX-6bit", "object": "model", "crea`; chip `Apple M5 Ultra; 274877906944`

### ruler-fresh

| streams | prose total (a stream) | code total (a stream) | structured total (a stream) | list total (a stream) | first token |
|---:|---:|---:|---:|---:|---:|
| 1 | 139.3 (139.3) | 207.3 (207.3) | 167.4 (167.4) | 206.8 (206.8) | 0.11-0.12 s |
| 2 | 194.5 (97.2) | 263.3 (131.7) | 216.4 (108.2) | 268.2 (134.1) | 0.18-0.20 s |

### suite

| check | passed |
|---|---:|
| drafts | 12/12 |
| concurrent | 12/12 |

### checks

| check | result |
|---|---|
| structured | FAIL: 0/18 obey; a bad regex -> 400; failed json_object/greedy, json_object/sampled, json_object/thinking, json_schema/greedy, json_schema/sampled, json_schema/thinking, guided_json/greedy, guided_json/sampled, guided_json/thinking, regex/greedy, regex/sampled, regex/thinking, choice/greedy, choice/sampled, choice/thinking, grammar/greedy, grammar/sampled, grammar/thinking |

## 2026-10-12 00:00: run `evidence/2026-10-12-parallel8`

Plan published evidence, published; served as `Qwen3.8-Flash-Next-6bit`.

### ruler

| streams | prose total (a stream) | code total (a stream) | structured total (a stream) | list total (a stream) | first token |
|---:|---:|---:|---:|---:|---:|
| 1 | 127.7 (127.7) | 174.1 (174.1) | 147.8 (147.8) | 175.4 (175.4) | 0.16-0.17 s |
| 4 | 210.2 (52.9) | 303.3 (76.3) | 249.2 (61.1) | 316.9 (77.8) | 0.37-0.40 s |
| 8 | 271.5 (34.1) | 330.0 (40.8) | 292.5 (36.5) | 339.3 (41.7) | 0.76-0.84 s |

## 2026-10-12 00:00: run `evidence/2026-10-12-lane-parity`

Plan published evidence, published; served as `Qwen3.8-Flash-Next-6bit`.

### ruler_trial

| streams | prose total (a stream) | code total (a stream) | structured total (a stream) | list total (a stream) | first token |
|---:|---:|---:|---:|---:|---:|
| 1 | 141.6 (141.6) | 202.7 (202.7) | 169.1 (169.1) | 191.5 (191.5) | 0.12-0.20 s |
| 4 | 244.7 (60.9) | 325.4 (80.9) | 277.4 (68.6) | 327.2 (83.3) | 0.41-0.44 s |

## 2026-10-12 00:00: run `evidence/2026-10-12-262k-cache`

Plan published evidence, published; served as `Qwen3.8-Flash-Next-6bit`.

### ruler

| streams | prose total (a stream) | code total (a stream) | structured total (a stream) | list total (a stream) | first token |
|---:|---:|---:|---:|---:|---:|
| 1 | 129.3 (129.3) | 176.6 (176.6) | 149.8 (149.8) | 177.4 (177.4) | 0.19-0.20 s |
| 4 | 209.5 (52.6) | 309.6 (78.3) | 245.9 (60.7) | 321.5 (78.4) | 0.39-0.41 s |

## 2026-10-11 00:00: run `evidence/2026-10-11-launchd`

Plan published evidence, published; served as `Qwen3.8-Flash-Next-6bit`.

### ruler-1user

| streams | prose total (a stream) | code total (a stream) | structured total (a stream) | list total (a stream) | first token |
|---:|---:|---:|---:|---:|---:|
| 1 | 144.6 (144.6) | 205.6 (205.6) | 172.6 (172.6) | 194.7 (194.7) | 0.10-0.20 s |

### suite

| check | passed |
|---|---:|
| drafts | 12/12 |
| streaming | 4/4 |
| multiturn | 8/8 |
| stop | 3/3 |
| thinking | 10/10 |
| copy | 2/2 |
| max-tokens | 3/3 |
| tools | 59/60 |
| json | 30/30 |

## 2026-10-11 00:00: run `evidence/2026-10-11-1m-parallel4`

Plan published evidence, published; served as `Qwen3.8-Flash-Next-6bit`.

### ruler

| streams | prose total (a stream) | code total (a stream) | structured total (a stream) | list total (a stream) | first token |
|---:|---:|---:|---:|---:|---:|
| 1 | 131.3 (131.3) | 178.9 (178.9) | 160.2 (160.2) | 183.9 (183.9) | 0.12-0.16 s |
| 4 | 211.0 (52.0) | 311.5 (77.0) | 259.8 (64.7) | 317.6 (78.8) | 0.36-0.42 s |

### suite

| check | passed |
|---|---:|
| drafts | 12/12 |
| streaming | 4/4 |
| multiturn | 8/8 |
| stop | 3/3 |
| thinking | 10/10 |
| copy | 2/2 |
| max-tokens | 3/3 |
| tools | 56/60 |
| json | 30/30 |
| ifeval | 132/150 |
| gsm8k | 241/250 |
| concurrent | 12/12 |

