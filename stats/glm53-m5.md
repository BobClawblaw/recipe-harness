# GLM-5.3-Flash, MLX 4-bit on 1x Apple M5 Ultra (256 GB unified), macOS

Target `glm53-m5`: GLM-5.3-Flash MLX 4-bit, TensorFold native on one M5 Ultra Mac (one stream, greedy). Engine: TensorFold native, Metal. Rendered from `stats/glm53-m5.json` (16 runs); aggregate tok/s, total (a stream).

## 2026-11-09 12:15: run `20261109-121537-glm-vision`

Plan glm-vision, done; served as `GLM-5.3-Flash-MLX-4bit`.

Serving: engine_commit `7070b25ca`; binary_sha256 `351fb8c93fee1f096435e85890f21c6a0a9328d7b6623c6d8f52542a6fac12ad`; suite_commit `206803ca7135`

## 2026-11-09 12:15: run `20261109-121502-sampling`

Plan sampling, done; served as `GLM-5.3-Flash-MLX-4bit`.

Serving: engine_commit `7070b25ca`; binary_sha256 `351fb8c93fee1f096435e85890f21c6a0a9328d7b6623c6d8f52542a6fac12ad`; suite_commit `206803ca7135`

### checks

| check | result |
|---|---|
| sampling | pass: 9/9 seeded replies equal on repeat and undrafted; 0 errors |

## 2026-11-09 12:14: run `20261109-121446-structured`

Plan structured, done; served as `GLM-5.3-Flash-MLX-4bit`.

Serving: engine_commit `7070b25ca`; binary_sha256 `351fb8c93fee1f096435e85890f21c6a0a9328d7b6623c6d8f52542a6fac12ad`; suite_commit `206803ca7135`

### checks

| check | result |
|---|---|
| structured | FAIL: 0/18 obey, drafted == plain 12/12; a bad regex -> 400; failed json_object/greedy, json_object/sampled, json_object/thinking, json_schema/greedy, json_schema/sampled, json_schema/thinking, guided_json/greedy, guided_json/sampled, guided_json/thinking, regex/greedy, regex/sampled, regex/thinking, choice/greedy, choice/sampled, choice/thinking, grammar/greedy, grammar/sampled, grammar/thinking |
| tools | FAIL: 1/5 tool cases right; failed required (400 {"error": {"message": "backend 'glm-zig' cannot enforce tool_choice \"required\" or a named function: it has no token grammar support; send \"auto\" or \"none\"", "type": "invalid_request_error"}}); named (400 {"error": {"message": "backend 'glm-zig' cannot enforce tool_choice \"required\" or a named function: it has no token grammar support; send \"auto\" or \"none\"", "type": "invalid_request_error"}}); named/thinking (400 {"error": {"message": "backend 'glm-zig' cannot enforce tool_choice \"required\" or a named function: it has no token grammar support; send \"auto\" or \"none\"", "type": "invalid_request_error"}}); named/stream (400 {"error": {"message": "backend 'glm-zig' cannot enforce tool_choice \"required\" or a named function: it has no token grammar support; send \"auto\" or \"none\"", "type": "invalid_request_error"}}) |

## 2026-11-09 12:07: run `20261109-120751-quick`

Plan quick, done; served as `GLM-5.3-Flash-MLX-4bit`.

Serving: engine_commit `7070b25ca`; binary_sha256 `351fb8c93fee1f096435e85890f21c6a0a9328d7b6623c6d8f52542a6fac12ad`; suite_commit `206803ca7135`

### ruler-fresh

| streams | prose total (a stream) | code total (a stream) | structured total (a stream) | list total (a stream) | first token |
|---:|---:|---:|---:|---:|---:|
| 1 | 91.9 (91.9) | 103.0 (103.0) | 97.2 (97.2) | 94.0 (94.0) | 0.10-0.14 s |

### ruler-after

| streams | prose total (a stream) | code total (a stream) | structured total (a stream) | list total (a stream) | first token |
|---:|---:|---:|---:|---:|---:|
| 1 | 90.9 (90.9) | 103.0 (103.0) | 98.1 (98.1) | 94.8 (94.8) | 0.10-0.14 s |

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
| memory-idle | measured: mac: ssh: Could not resolve hostname unused: nodename nor servnam |
| tools | pass: 1/1 tool cases right; not tested (features.structured = false): required, named, named/thinking, named/stream |
| turns | measured: resumed == again: True; cold (padded) not compared: 4777 prompt tokens (cached 0) against 4776; cached 4652 of 4776; ttft resumed 0.19s, cold 4.294s |

## 2026-11-09 11:35: run `20261109-113557-quick`

Plan quick, done; served as `GLM-5.3-Flash-MLX-4bit`.

Serving: engine_commit `7070b25ca`; binary_sha256 `351fb8c93fee1f096435e85890f21c6a0a9328d7b6623c6d8f52542a6fac12ad`; suite_commit `206803ca7135`

### ruler-fresh

| streams | prose total (a stream) | code total (a stream) | structured total (a stream) | list total (a stream) | first token |
|---:|---:|---:|---:|---:|---:|
| 1 | 91.2 (91.2) | 103.1 (103.1) | 97.5 (97.5) | 93.9 (93.9) | 0.10-0.14 s |

### ruler-after

| streams | prose total (a stream) | code total (a stream) | structured total (a stream) | list total (a stream) | first token |
|---:|---:|---:|---:|---:|---:|
| 1 | 91.4 (91.4) | 103.1 (103.1) | 97.5 (97.5) | 93.4 (93.4) | 0.11-0.14 s |

### suite

| check | passed |
|---|---:|
| soak | 0/60 |
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
| memory-idle | measured: mac: ssh: Could not resolve hostname unused: nodename nor servnam |
| tools | pass: 1/1 tool cases right; not tested (features.structured = false): required, named, named/thinking, named/stream |
| turns | pass: resumed == again: True; cold (after a restart): True; cached 4652 of 4776; ttft resumed 0.187s, cold 2.445s |

## 2026-11-09 11:09: run `20261109-110901-speed`

Plan speed, done; served as `GLM-5.3-Flash-MLX-4bit`.

Serving: engine_commit `7070b25ca`; binary_sha256 `351fb8c93fee1f096435e85890f21c6a0a9328d7b6623c6d8f52542a6fac12ad`; suite_commit `206803ca7135`

### ruler-fresh

| streams | prose total (a stream) | code total (a stream) | structured total (a stream) | list total (a stream) | first token |
|---:|---:|---:|---:|---:|---:|
| 1 | 43.1 (43.1) | 101.7 (101.7) | 22.4 (22.4) | 19.5 (19.5) | 0.12-0.15 s |

### ruler-after

| streams | prose total (a stream) | code total (a stream) | structured total (a stream) | list total (a stream) | first token |
|---:|---:|---:|---:|---:|---:|
| 1 | 30.7 (30.7) | 65.7 (65.7) | 55.0 (55.0) | 15.1 (15.1) | 0.12-0.14 s |

### checks

| check | result |
|---|---|
| memory-idle | measured: mac: ssh: Could not resolve hostname unused: nodename nor servnam |
| turns | pass: resumed == again: True; cold (after a restart): True; cached 4652 of 4776; ttft resumed 1.314s, cold 3.922s |
| memory-busy | measured: mac: ssh: Could not resolve hostname unused: nodename nor servnam |

## 2026-10-16 08:23: run `20261016-082326-glm-gate-novision`

Plan glm-gate-novision, done; served as `GLM-5.3-Flash-MLX-4bit`.

Serving: engine_commit `e8b60549`; binary_sha256 `d90e44c9818187ae4bc61d06312989cd796033b5dea6e0fc02164fe2730660fe`

### ruler-fresh

| streams | prose total (a stream) | code total (a stream) | structured total (a stream) | list total (a stream) | first token |
|---:|---:|---:|---:|---:|---:|
| 1 | 74.4 (74.4) | 78.3 (78.3) | 77.5 (77.5) | 86.5 (86.5) | 0.11-0.15 s |

### suite

| check | passed |
|---|---:|
| drafts | 12/12 |
| concurrent | 12/12 |
| streaming | 4/4 |
| multiturn | 8/8 |
| stop | 3/3 |
| thinking | 10/10 |
| copy | 2/2 |
| max-tokens | 3/3 |
| tools | 57/60 |
| json | 30/30 |
| gsm8k | 246/250 |
| mmlu | 290/342 |

## 2026-10-16 08:04: run `20261016-080418-glm-gate-novision`

Plan glm-gate-novision, done; served as `GLM-5.3-Flash-MLX-4bit`.

Serving: engine_commit `46a08c18`; binary_sha256 `c040cfbfafa63174bdd6b668e3c23ebaf3afb26c2dcab9516a430790009c5390`

### ruler-fresh

| streams | prose total (a stream) | code total (a stream) | structured total (a stream) | list total (a stream) | first token |
|---:|---:|---:|---:|---:|---:|
| 1 | 77.7 (77.7) | 77.6 (77.6) | 77.8 (77.8) | 77.9 (77.9) | 0.10-0.15 s |

### suite

| check | passed |
|---|---:|
| drafts | 12/12 |
| concurrent | 12/12 |
| streaming | 4/4 |
| multiturn | 8/8 |
| stop | 3/3 |
| thinking | 10/10 |
| copy | 2/2 |
| max-tokens | 3/3 |
| tools | 57/60 |
| json | 30/30 |
| gsm8k | 246/250 |
| mmlu | 292/342 |

## 2026-10-16 00:35: run `20261016-003511-glm-gate`

Plan glm-gate, done; served as `GLM-5.3-Flash-MLX-4bit`.

Serving: engine_commit `c5304036`; binary_sha256 `507c6fc3b1f9f5a521185d3da00ec3f555c39e20188ba8eefec2547581bb618d`

### ruler-fresh

| streams | prose total (a stream) | code total (a stream) | structured total (a stream) | list total (a stream) | first token |
|---:|---:|---:|---:|---:|---:|
| 1 | 78.0 (78.0) | 78.7 (78.7) | 77.9 (77.9) | 87.0 (87.0) | 0.11-0.15 s |

### suite

| check | passed |
|---|---:|
| drafts | 12/12 |
| concurrent | 12/12 |
| streaming | 4/4 |
| multiturn | 8/8 |
| stop | 3/3 |
| thinking | 10/10 |
| copy | 2/2 |
| max-tokens | 3/3 |
| tools | 57/60 |
| json | 30/30 |
| vision | 12/12 |
| gsm8k | 246/250 |
| mmlu | 290/342 |

## 2026-10-10 00:00: run `evidence/2026-10-10-wiredreads`

Plan published evidence, published; served as `GLM-5.3-Flash-MLX-4bit`.

### ruler-repeat

| streams | prose total (a stream) | code total (a stream) | structured total (a stream) | list total (a stream) | first token |
|---:|---:|---:|---:|---:|---:|
| 1 | 92.4 (92.4) | 103.6 (103.6) | 97.0 (97.0) | 94.9 (94.9) | 0.11-0.15 s |

### ruler

| streams | prose total (a stream) | code total (a stream) | structured total (a stream) | list total (a stream) | first token |
|---:|---:|---:|---:|---:|---:|
| 1 | 90.7 (90.7) | 103.7 (103.7) | 99.1 (99.1) | 41.8 (41.8) | 0.12-0.15 s |

### suite

| check | passed |
|---|---:|
| snapshot | 12/12 |
| drafts | 12/12 |
| concurrent | 12/12 |

## 2026-10-10 00:00: run `evidence/2026-10-10-thinking-on`

Plan published evidence, published; served as `GLM-5.3-Flash-MLX-4bit`.

### suite

| check | passed |
|---|---:|
| drafts | 12/12 |
| concurrent | 12/12 |
| streaming | 4/4 |
| multiturn | 8/8 |
| stop | 3/3 |
| thinking | 10/10 |
| copy | 2/2 |
| max-tokens | 0/3 |
| tools | 58/60 |
| json | 30/30 |
| ifeval | 127/150 |
| gsm8k | 248/250 |
| mgsm | 221/240 |
| mmlu | 307/342 |
| repetition | 8/8 |
| long-context | 54/55 |
| vision | 12/12 |
| snapshot | 12/12 |

## 2026-10-10 00:00: run `evidence/2026-10-10-1.0.5-thinking`

Plan published evidence, published; served as `GLM-5.3-Flash-MLX-4bit`.

### suite

| check | passed |
|---|---:|
| drafts | 12/12 |
| concurrent | 12/12 |
| streaming | 4/4 |
| multiturn | 8/8 |
| stop | 3/3 |
| thinking | 10/10 |
| copy | 2/2 |
| max-tokens | 0/3 |
| tools | 57/60 |
| json | 30/30 |
| ifeval | 131/150 |
| gsm8k | 248/250 |
| mgsm | 226/240 |
| mmlu | 308/342 |
| repetition | 8/8 |
| long-context | 54/55 |
| vision | 12/12 |
| snapshot | 12/12 |

## 2026-10-10 00:00: run `evidence/2026-10-10-1.0.5`

Plan published evidence, published; served as `GLM-5.3-Flash-MLX-4bit`.

### suite

| check | passed |
|---|---:|
| drafts | 12/12 |
| concurrent | 12/12 |
| streaming | 4/4 |
| multiturn | 8/8 |
| stop | 3/3 |
| thinking | 10/10 |
| copy | 2/2 |
| max-tokens | 3/3 |
| tools | 57/60 |
| json | 30/30 |
| ifeval | 96/150 |
| gsm8k | 246/250 |
| mgsm | 217/240 |
| mmlu | 292/342 |
| repetition | 8/8 |
| long-context | 55/55 |
| vision | 12/12 |
| snapshot | 12/12 |

## 2026-10-09 00:00: run `evidence/2026-10-09-ruler-1.0.4`

Plan published evidence, published; served as `GLM-5.3-Flash-MLX-4bit`.

### ruler

| streams | prose total (a stream) | code total (a stream) | structured total (a stream) | list total (a stream) | first token |
|---:|---:|---:|---:|---:|---:|
| 1 | 93.3 (93.3) | 104.6 (104.6) | 104.2 (104.2) | 89.7 (89.7) | 0.23-0.29 s |

## 2026-10-09 00:00: run `evidence/2026-10-09-quality-1.0.4-part3`

Plan published evidence, published; served as `GLM-5.3-Flash-MLX-4bit`.

### suite

| check | passed |
|---|---:|
| mmlu | 288/342 |
| repetition | 8/8 |
| long-context | 29/29 |
| vision | 12/12 |
| snapshot | 12/12 |

## 2026-10-09 00:00: run `evidence/2026-10-09-quality-1.0.4-long128`

Plan published evidence, published; served as `GLM-5.3-Flash-MLX-4bit`.

### suite

| check | passed |
|---|---:|
| long-context | 42/42 |

