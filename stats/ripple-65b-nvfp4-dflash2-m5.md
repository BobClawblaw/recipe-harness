# ricursiveAI Ripple-65B-Preview-NVFP4 (NVFP4 MLPs, bf16 attention) + DFlash2 drafter on 1x Apple M5 Ultra (256 GB unified), macOS

Target `ripple-65b-nvfp4-dflash2-m5`: ricursiveAI Ripple-65B-Preview-NVFP4 + its DFlash2 drafter (bf16), TensorFold native Metal on one M5 Ultra. Engine: TensorFold native, Metal. Rendered from `stats/ripple-65b-nvfp4-dflash2-m5.json` (8 runs); aggregate tok/s, total (a stream).

## 2026-11-05 19:09: run `20261105-190943-speed`

Plan speed, done; served as `ripple`.

Serving: engine_commit `a869c4f32`; binary_sha256 `99b793dbbfe6dad5e06245e61c6cd0d57fd6e99ef4ea3221f5d69188d163c770`; served_model `{"object": "list", "data": [{"id": "ripple", "object": "model", "created": 1793927408, "ow`; chip `Apple M5 Ultra; 274877906944`; suite_commit `21db9b23f7be`

### ruler-fresh

| streams | prose total (a stream) | code total (a stream) | structured total (a stream) | list total (a stream) | first token |
|---:|---:|---:|---:|---:|---:|
| 1 | 15.5 (15.5) | 27.5 (27.5) | 17.8 (17.8) | 19.8 (19.8) | 0.53-0.65 s |
| 2 | 22.5 (11.2) | 37.7 (18.9) | 26.6 (13.3) | 40.6 (20.3) | 0.82-0.98 s |

Engine rounds (ruler-fresh):

| streams | tokens a round | drafts a round | accepted | ms a round | requests |
|---:|---:|---:|---:|---:|---:|
| 1 | 2.646 | 3.36 | 48% | 131.15 | 12 |
| 2 | 2.646 | 2.912 | 56% | 166.24 | 25 |

### ruler-after

| streams | prose total (a stream) | code total (a stream) | structured total (a stream) | list total (a stream) | first token |
|---:|---:|---:|---:|---:|---:|
| 1 | 15.5 (15.5) | 27.6 (27.6) | 17.8 (17.8) | 19.6 (19.6) | 0.53-0.65 s |

Engine rounds (ruler-after):

| streams | tokens a round | drafts a round | accepted | ms a round | requests |
|---:|---:|---:|---:|---:|---:|
| 1 | 2.648 | 3.471 | 47% | 131.5 | 13 |

### checks

| check | result |
|---|---|
| memory-idle | measured: mac: System-wide memory free percentage: 63%; total = 6144.00M  us |
| turns | pass: resumed == again: True; cold (after a restart): True; cached 4513 of 4597; ttft resumed 0.593s, cold 8.097s |
| memory-busy | measured: mac: System-wide memory free percentage: 63%; total = 6144.00M  us |

## 2026-11-05 17:58: run `20261105-175828-speed`

Plan speed, contended (another job held ~12 cores; rerun 20261105-190943-speed); served as `ripple`.

Serving: engine_commit `925ae9563`; binary_sha256 `99b793dbbfe6dad5e06245e61c6cd0d57fd6e99ef4ea3221f5d69188d163c770`; served_model `{"object": "list", "data": [{"id": "ripple", "object": "model", "created": 1793923133, "ow`; chip `Apple M5 Ultra; 274877906944`; suite_commit `21db9b23f7be`

### ruler-fresh

| streams | prose total (a stream) | code total (a stream) | structured total (a stream) | list total (a stream) | first token |
|---:|---:|---:|---:|---:|---:|
| 1 | 13.8 (13.8) | 22.8 (22.8) | 15.9 (15.9) | 17.5 (17.5) | 0.56-0.78 s |
| 2 | 19.0 (9.5) | 32.1 (16.1) | 22.8 (11.4) | 34.7 (17.4) | 0.84-1.17 s |

Engine rounds (ruler-fresh):

| streams | tokens a round | drafts a round | accepted | ms a round | requests |
|---:|---:|---:|---:|---:|---:|
| 1 | 2.57 | 3.138 | 50% | 146.81 | 12 |
| 2 | 2.597 | 2.677 | 59% | 191.29 | 25 |

### ruler-after

| streams | prose total (a stream) | code total (a stream) | structured total (a stream) | list total (a stream) | first token |
|---:|---:|---:|---:|---:|---:|
| 1 | 13.5 (13.5) | 23.1 (23.1) | 15.8 (15.8) | 15.3 (15.3) | 0.58-0.77 s |

Engine rounds (ruler-after):

| streams | tokens a round | drafts a round | accepted | ms a round | requests |
|---:|---:|---:|---:|---:|---:|
| 1 | 2.601 | 3.397 | 47% | 153.61 | 13 |

### checks

| check | result |
|---|---|
| memory-idle | measured: mac: System-wide memory free percentage: 63%; total = 6144.00M  us |
| turns | pass: resumed == again: True; cold (after a restart): True; cached 4513 of 4597; ttft resumed 0.614s, cold 10.042s |
| memory-busy | measured: mac: System-wide memory free percentage: 63%; total = 6144.00M  us |

## 2026-11-05 17:31: run `20261105-173134-quick`

Plan quick, done; served as `ripple`.

Serving: engine_commit `925ae9563`; binary_sha256 `99b793dbbfe6dad5e06245e61c6cd0d57fd6e99ef4ea3221f5d69188d163c770`; served_model `{"object": "list", "data": [{"id": "ripple", "object": "model", "created": 1793921519, "ow`; chip `Apple M5 Ultra; 274877906944`; suite_commit `21db9b23f7be`

### ruler-fresh

| streams | prose total (a stream) | code total (a stream) | structured total (a stream) | list total (a stream) | first token |
|---:|---:|---:|---:|---:|---:|
| 1 | 15.5 (15.5) | 27.3 (27.3) | 17.7 (17.7) | 19.6 (19.6) | 0.53-0.65 s |

Engine rounds (ruler-fresh):

| streams | tokens a round | drafts a round | accepted | ms a round | requests |
|---:|---:|---:|---:|---:|---:|
| 1 | 2.649 | 3.427 | 48% | 132.37 | 12 |

### ruler-after

| streams | prose total (a stream) | code total (a stream) | structured total (a stream) | list total (a stream) | first token |
|---:|---:|---:|---:|---:|---:|
| 1 | 15.5 (15.5) | 27.5 (27.5) | 17.8 (17.8) | 19.6 (19.6) | 0.53-0.65 s |

Engine rounds (ruler-after):

| streams | tokens a round | drafts a round | accepted | ms a round | requests |
|---:|---:|---:|---:|---:|---:|
| 1 | 2.651 | 3.48 | 47% | 132.03 | 13 |

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
| structured | pass: 18/18 obey, drafted == plain 12/12; a bad regex -> 400 |
| tools | pass: 5/5 tool cases right |
| sampling | pass: 9/9 seeded replies equal on repeat and undrafted; 0 errors |
| turns | pass: resumed == again: True; cold (after a restart): True; cached 4513 of 4597; ttft resumed 0.592s, cold 7.792s |
| urls | FAIL: public 400; loopback 400; http 400; unexpected: ['public'] |

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

