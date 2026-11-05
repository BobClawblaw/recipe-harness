# ricursiveAI Ripple-65B-Preview-NVFP4 (NVFP4 MLPs, bf16 attention) + DFlash2 drafter on 1x Apple M5 Ultra (256 GB unified), macOS

Target `ripple-65b-nvfp4-dflash2-m5`: ricursiveAI Ripple-65B-Preview-NVFP4 + its DFlash2 drafter (bf16), TensorFold native Metal on one M5 Ultra. Engine: TensorFold native, Metal. Rendered from `stats/ripple-65b-nvfp4-dflash2-m5.json` (5 runs); aggregate tok/s, total (a stream).

## 2026-11-05 07:41: run `20261105-074141-speed`

Plan speed, done; served as `ripple`.

Serving: engine_commit `eee30fc8a`; binary_sha256 `ec09dcb61208331782f8ef5ee2831e7affda284a1e583d00b05ad1041ae4b544`; served_model `{"object": "list", "data": [{"id": "ripple", "object": "model", "created": 1793886127, "ow`; chip `Apple M5 Ultra; 274877906944`; suite_commit `21db9b23f7be`

### ruler-fresh

| streams | prose total (a stream) | code total (a stream) | structured total (a stream) | list total (a stream) | first token |
|---:|---:|---:|---:|---:|---:|
| 1 | 15.7 (15.7) | 27.5 (27.5) | 17.9 (17.9) | 19.7 (19.7) | 0.53-0.65 s |
| 2 | 23.2 (11.6) | 37.3 (18.7) | 27.0 (13.5) | 41.1 (20.5) | 0.80-0.97 s |

Engine rounds (ruler-fresh):

| streams | tokens a round | drafts a round | accepted | ms a round | requests |
|---:|---:|---:|---:|---:|---:|
| 1 | 2.657 | 3.442 | 48% | 131.45 | 12 |
| 2 | 2.679 | 3.011 | 55% | 166.62 | 25 |

### ruler-after

| streams | prose total (a stream) | code total (a stream) | structured total (a stream) | list total (a stream) | first token |
|---:|---:|---:|---:|---:|---:|
| 1 | 15.7 (15.7) | 27.5 (27.5) | 17.9 (17.9) | 19.7 (19.7) | 0.53-0.65 s |

Engine rounds (ruler-after):

| streams | tokens a round | drafts a round | accepted | ms a round | requests |
|---:|---:|---:|---:|---:|---:|
| 1 | 2.659 | 3.434 | 48% | 131.51 | 13 |

### checks

| check | result |
|---|---|
| memory-idle | measured: mac: System-wide memory free percentage: 66%; total = 6144.00M  us |
| turns | pass: resumed == again: True; cold (after a restart): True; cached 4513 of 4597; ttft resumed 0.577s, cold 7.693s |
| memory-busy | measured: mac: System-wide memory free percentage: 65%; total = 6144.00M  us |

## 2026-11-05 07:01: run `20261105-070147-quick`

Plan quick, done; served as `ripple`.

Serving: engine_commit `eee30fc8a`; binary_sha256 `ec09dcb61208331782f8ef5ee2831e7affda284a1e583d00b05ad1041ae4b544`; served_model `{"object": "list", "data": [{"id": "ripple", "object": "model", "created": 1793883732, "ow`; chip `Apple M5 Ultra; 274877906944`; suite_commit `21db9b23f7be`

### ruler-fresh

| streams | prose total (a stream) | code total (a stream) | structured total (a stream) | list total (a stream) | first token |
|---:|---:|---:|---:|---:|---:|
| 1 | 9.6 (9.6) | 16.7 (16.7) | 10.4 (10.4) | 11.8 (11.8) | 0.81-0.90 s |

Engine rounds (ruler-fresh):

| streams | tokens a round | drafts a round | accepted | ms a round | requests |
|---:|---:|---:|---:|---:|---:|
| 1 | 2.612 | 3.443 | 46% | 215.73 | 12 |

### ruler-after

| streams | prose total (a stream) | code total (a stream) | structured total (a stream) | list total (a stream) | first token |
|---:|---:|---:|---:|---:|---:|
| 1 | 4.6 (4.6) | 9.9 (9.9) | 16.0 (16.0) | 18.2 (18.2) | 0.54-1.28 s |

Engine rounds (ruler-after):

| streams | tokens a round | drafts a round | accepted | ms a round | requests |
|---:|---:|---:|---:|---:|---:|
| 1 | 2.929 | 6.017 | 32% | 240.62 | 13 |

### suite

| check | passed |
|---|---:|
| soak | 60/60 |
| drafts | 12/12 |
| concurrent | 12/12 |
| streaming | 4/4 |
| multiturn | 8/8 |
| stop | 3/3 |
| thinking | 5/10 |
| copy | 2/2 |
| max-tokens | 3/3 |

### checks

| check | result |
|---|---|
| memory-idle | measured: mac: System-wide memory free percentage: 59%; total = 6144.00M  us |
| structured | pass: 18/18 obey, drafted == plain 12/12; a bad regex -> 400 |
| tools | pass: 5/5 tool cases right |
| sampling | pass: 9/9 seeded replies equal on repeat and undrafted; 0 errors |
| turns | pass: resumed == again: True; cold (after a restart): True; cached 4513 of 4597; ttft resumed 1.66s, cold 15.387s |
| urls | FAIL: public 400; loopback 400; http 400; unexpected: ['public'] |

## 2026-11-05 05:37: run `20261105-053701-speed`

Plan speed, done; served as `ripple`.

Serving: engine_commit `4a5e12425`; binary_sha256 `bea92a80c57b3c17682ff8f38eecbf71aa425ce9b51a162438fdd7343db0769e`; served_model `{"object": "list", "data": [{"id": "ripple", "object": "model", "created": 1793878646, "ow`; chip `Apple M5 Ultra; 274877906944`; suite_commit `21db9b23f7be`

### ruler-fresh

| streams | prose total (a stream) | code total (a stream) | structured total (a stream) | list total (a stream) | first token |
|---:|---:|---:|---:|---:|---:|
| 1 | 15.8 (15.8) | 27.6 (27.6) | 17.9 (17.9) | 19.6 (19.6) | 0.53-0.65 s |
| 2 | 23.2 (11.6) | 37.4 (18.7) | 27.0 (13.5) | 42.8 (21.4) | 0.81-0.97 s |

Engine rounds (ruler-fresh):

| streams | tokens a round | drafts a round | accepted | ms a round | requests |
|---:|---:|---:|---:|---:|---:|
| 1 | 2.664 | 3.504 | 47% | 131.8 | 12 |
| 2 | 2.679 | 3.015 | 55% | 164.36 | 25 |

### ruler-after

| streams | prose total (a stream) | code total (a stream) | structured total (a stream) | list total (a stream) | first token |
|---:|---:|---:|---:|---:|---:|
| 1 | 15.8 (15.8) | 27.5 (27.5) | 17.9 (17.9) | 19.8 (19.8) | 0.53-0.65 s |

Engine rounds (ruler-after):

| streams | tokens a round | drafts a round | accepted | ms a round | requests |
|---:|---:|---:|---:|---:|---:|
| 1 | 2.659 | 3.432 | 48% | 131.43 | 13 |

### checks

| check | result |
|---|---|
| memory-idle | measured: mac: System-wide memory free percentage: 65%; total = 6144.00M  us |
| turns | pass: resumed == again: True; cold (after a restart): True; cached 4513 of 4597; ttft resumed 0.58s, cold 7.689s |
| memory-busy | measured: mac: System-wide memory free percentage: 65%; total = 6144.00M  us |

## 2026-11-05 05:34: run `20261105-053434-structured`

Plan structured, done; served as `ripple`.

Serving: engine_commit `4a5e12425`; binary_sha256 `bea92a80c57b3c17682ff8f38eecbf71aa425ce9b51a162438fdd7343db0769e`; served_model `{"object": "list", "data": [{"id": "ripple", "object": "model", "created": 1793878474, "ow`; chip `Apple M5 Ultra; 274877906944`; suite_commit `21db9b23f7be`

### checks

| check | result |
|---|---|
| structured | pass: 18/18 obey, drafted == plain 12/12; a bad regex -> 400 |
| tools | pass: 5/5 tool cases right |

## 2026-11-05 05:10: run `20261105-051016-quick`

Plan quick, done; served as `ripple`.

Serving: engine_commit `4a5e12425`; binary_sha256 `bea92a80c57b3c17682ff8f38eecbf71aa425ce9b51a162438fdd7343db0769e`; served_model `{"object": "list", "data": [{"id": "ripple", "object": "model", "created": 1793877046, "ow`; chip `Apple M5 Ultra; 274877906944`; suite_commit `21db9b23f7be`

### ruler-fresh

| streams | prose total (a stream) | code total (a stream) | structured total (a stream) | list total (a stream) | first token |
|---:|---:|---:|---:|---:|---:|
| 1 | 15.7 (15.7) | 25.3 (25.3) | 16.5 (16.5) | 18.2 (18.2) | 0.54-0.65 s |

Engine rounds (ruler-fresh):

| streams | tokens a round | drafts a round | accepted | ms a round | requests |
|---:|---:|---:|---:|---:|---:|
| 1 | 2.726 | 4.378 | 39% | 144.0 | 12 |

### ruler-after

| streams | prose total (a stream) | code total (a stream) | structured total (a stream) | list total (a stream) | first token |
|---:|---:|---:|---:|---:|---:|
| 1 | 15.7 (15.7) | 27.1 (27.1) | 17.8 (17.8) | 19.6 (19.6) | 0.53-0.65 s |

Engine rounds (ruler-after):

| streams | tokens a round | drafts a round | accepted | ms a round | requests |
|---:|---:|---:|---:|---:|---:|
| 1 | 2.659 | 3.459 | 47% | 132.64 | 13 |

### suite

| check | passed |
|---|---:|
| soak | 60/60 |
| drafts | 12/12 |
| concurrent | 12/12 |
| streaming | 4/4 |
| multiturn | 8/8 |
| stop | 3/3 |
| thinking | 5/10 |
| copy | 2/2 |
| max-tokens | 3/3 |

### checks

| check | result |
|---|---|
| memory-idle | measured: mac: System-wide memory free percentage: 65%; total = 6144.00M  us |
| structured | FAIL: 0/18 obey, drafted == plain 12/12; a bad regex -> 400; failed json_object/greedy, json_object/sampled, json_object/thinking, json_schema/greedy, json_schema/sampled, json_schema/thinking, guided_json/greedy, guided_json/sampled, guided_json/thinking, regex/greedy, regex/sampled, regex/thinking, choice/greedy, choice/sampled, choice/thinking, grammar/greedy, grammar/sampled, grammar/thinking |
| tools | FAIL: 1/5 tool cases right; failed required (400 {"error": {"message": "tool_choice \"required\" or a named function on backend 'metal': libtfgrammar.dylib is required for structured output and required tool calls (HTTP 400 when missing); restore th); named (400 {"error": {"message": "tool_choice \"required\" or a named function on backend 'metal': libtfgrammar.dylib is required for structured output and required tool calls (HTTP 400 when missing); restore th); named/thinking (400 {"error": {"message": "tool_choice \"required\" or a named function on backend 'metal': libtfgrammar.dylib is required for structured output and required tool calls (HTTP 400 when missing); restore th); named/stream (400 {"error": {"message": "tool_choice \"required\" or a named function on backend 'metal': libtfgrammar.dylib is required for structured output and required tool calls (HTTP 400 when missing); restore th) |
| sampling | pass: 9/9 seeded replies equal on repeat and undrafted; 0 errors |
| turns | pass: resumed == again: True; cold (after a restart): True; cached 4513 of 4597; ttft resumed 0.593s, cold 7.802s |
| urls | FAIL: public 400; loopback 400; http 400; unexpected: ['public'] |

