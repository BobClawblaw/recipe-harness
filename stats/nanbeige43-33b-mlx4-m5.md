# Nanbeige4.3-33B, MLX 4-bit on 1x Apple M5 Ultra (256 GB unified), macOS

Target `nanbeige43-33b-mlx4-m5`: Nanbeige4.3-33B MLX 4-bit as published (pratikgx/Nanbeige4.3-33B-MLX-4bit), TensorFold native Metal (llama) on one M5 Ultra (131072-token window, 2 streams). Engine: TensorFold native, Metal. Rendered from `stats/nanbeige43-33b-mlx4-m5.json` (6 runs); aggregate tok/s, total (a stream).

## 2026-10-27 10:59: run `20261027-105907-structured`

Plan structured, done; served as `nanbeige`.

Serving: engine_commit `657ac711c`; binary_sha256 `56fb3ebeaa8facd66a071318c4602df8920f6675171b8a3b093c639695609e9c`; served_model `{"object": "list", "data": [{"id": "nanbeige", "object": "model", "created": 1793116747, "`; chip `Apple M5 Ultra; 274877906944`; suite_commit `a7ba7e392d57`

### checks

| check | result |
|---|---|
| structured | pass: 18/18 obey, drafted == plain 12/12; a bad regex -> 400 |
| tools | pass: 5/5 tool cases right |

## 2026-10-27 10:58: run `20261027-105818-ab-tools-turns`

Plan ab-tools-turns, done; served as `nanbeige`.

Serving: engine_commit `657ac711c`; binary_sha256 `56fb3ebeaa8facd66a071318c4602df8920f6675171b8a3b093c639695609e9c`; served_model `{"object": "list", "data": [{"id": "nanbeige", "object": "model", "created": 1793116707, "`; chip `Apple M5 Ultra; 274877906944`; suite_commit `a7ba7e392d57`

### checks

| check | result |
|---|---|
| tools | pass: 5/5 tool cases right |
| turns | pass: resumed == again: True; cold (after a restart): True; cached 5493 of 5649; ttft resumed 0.239s, cold 4.153s |

## 2026-10-27 10:32: run `20261027-103208-ab-tools-turns`

Plan ab-tools-turns, done; served as `nanbeige`.

Serving: engine_commit `657ac711c`; binary_sha256 `56fb3ebeaa8facd66a071318c4602df8920f6675171b8a3b093c639695609e9c`; served_model `{"object": "list", "data": [{"id": "nanbeige", "object": "model", "created": 1793115136, "`; chip `Apple M5 Ultra; 274877906944`; suite_commit `a7ba7e392d57`

### checks

| check | result |
|---|---|
| tools | pass: 5/5 tool cases right |
| turns | pass: resumed == again: True; cold (after a restart): True; cached 5493 of 5649; ttft resumed 0.242s, cold 4.156s |

## 2026-10-27 10:09: run `20261027-100929-prefill-64k`

Plan prefill-64k, done; served as `nanbeige`.

Serving: engine_commit `657ac711c`; binary_sha256 `56fb3ebeaa8facd66a071318c4602df8920f6675171b8a3b093c639695609e9c`; served_model `{"object": "list", "data": [{"id": "nanbeige", "object": "model", "created": 1793113777, "`; chip `Apple M5 Ultra; 274877906944`; suite_commit `a7ba7e392d57`

### checks

| check | result |
|---|---|
| memory-idle | measured: mac: System-wide memory free percentage: 52%; total = 4096.00M  us |
| prefill-off | measured: 2108 tokens 1369.7 tok/s (1.539 s), 8252 tokens 1348.1 tok/s (6.121 s), 32829 tokens 1080.9 tok/s (30.372 s), 61501 tokens 872.0 tok/s (70.53 s) |
| prefill-thinking | measured: 2102 tokens 1359.6 tok/s (1.546 s), 8248 tokens 1337.9 tok/s (6.165 s), 32826 tokens 1079.8 tok/s (30.401 s), 61498 tokens 852.6 tok/s (72.126 s) |
| memory-busy | measured: mac: System-wide memory free percentage: 48%; total = 4096.00M  us |

## 2026-10-27 10:05: run `20261027-100550-speed`

Plan speed, done; served as `nanbeige`.

Serving: engine_commit `657ac711c`; binary_sha256 `56fb3ebeaa8facd66a071318c4602df8920f6675171b8a3b093c639695609e9c`; served_model `{"object": "list", "data": [{"id": "nanbeige", "object": "model", "created": 1793113558, "`; chip `Apple M5 Ultra; 274877906944`; suite_commit `a7ba7e392d57`

### ruler-fresh

| streams | prose total (a stream) | code total (a stream) | structured total (a stream) | list total (a stream) | first token |
|---:|---:|---:|---:|---:|---:|
| 1 | 46.7 (46.7) | 46.0 (46.0) | 46.7 (46.7) | 46.7 (46.7) | 0.12-0.13 s |
| 2 | 79.1 (39.6) | 76.5 (38.2) | 78.7 (39.3) | 79.3 (39.7) | 0.18-0.20 s |

Engine rounds (ruler-fresh):

| streams | tokens a round | drafts a round | accepted | ms a round | requests |
|---:|---:|---:|---:|---:|---:|
| 1 | 1.011 | 0.034 | 20% | 21.73 | 12 |
| 2 | 1.02 | 0.042 | 36% | 26.01 | 25 |

### ruler-after

| streams | prose total (a stream) | code total (a stream) | structured total (a stream) | list total (a stream) | first token |
|---:|---:|---:|---:|---:|---:|
| 1 | 46.2 (46.2) | 45.6 (45.6) | 46.3 (46.3) | 46.3 (46.3) | 0.12-0.13 s |

Engine rounds (ruler-after):

| streams | tokens a round | drafts a round | accepted | ms a round | requests |
|---:|---:|---:|---:|---:|---:|
| 1 | 1.012 | 0.034 | 20% | 21.95 | 13 |

### checks

| check | result |
|---|---|
| memory-idle | measured: mac: System-wide memory free percentage: 52%; total = 4096.00M  us |
| turns | pass: resumed == again: True; cold (after a restart): True; cached 5493 of 5649; ttft resumed 0.24s, cold 4.16s |
| memory-busy | measured: mac: System-wide memory free percentage: 52%; total = 4096.00M  us |

## 2026-10-27 08:05: run `20261027-080526-quick`

Plan quick, done; served as `nanbeige`.

Serving: engine_commit `28a428047`; binary_sha256 `56fb3ebeaa8facd66a071318c4602df8920f6675171b8a3b093c639695609e9c`; served_model `{"object": "list", "data": [{"id": "nanbeige", "object": "model", "created": 1793106334, "`; chip `Apple M5 Ultra; 274877906944`; suite_commit `a7ba7e392d57`

### ruler-fresh

| streams | prose total (a stream) | code total (a stream) | structured total (a stream) | list total (a stream) | first token |
|---:|---:|---:|---:|---:|---:|
| 1 | 8.0 (8.0) | 45.2 (45.2) | 45.9 (45.9) | 46.1 (46.1) | 0.12-0.61 s |

Engine rounds (ruler-fresh):

| streams | tokens a round | drafts a round | accepted | ms a round | requests |
|---:|---:|---:|---:|---:|---:|
| 1 | 1.011 | 0.034 | 20% | 27.85 | 12 |

### ruler-after

| streams | prose total (a stream) | code total (a stream) | structured total (a stream) | list total (a stream) | first token |
|---:|---:|---:|---:|---:|---:|
| 1 | 44.8 (44.8) | 42.4 (42.4) | 42.8 (42.8) | 43.1 (43.1) | 0.12-0.15 s |

Engine rounds (ruler-after):

| streams | tokens a round | drafts a round | accepted | ms a round | requests |
|---:|---:|---:|---:|---:|---:|
| 1 | 1.012 | 0.034 | 20% | 23.38 | 13 |

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
| memory-idle | measured: mac: System-wide memory free percentage: 41%; total = 4096.00M  us |
| structured | FAIL: 0/18 obey, drafted == plain 12/12; a bad regex -> 400; failed json_object/greedy, json_object/sampled, json_object/thinking, json_schema/greedy, json_schema/sampled, json_schema/thinking, guided_json/greedy, guided_json/sampled, guided_json/thinking, regex/greedy, regex/sampled, regex/thinking, choice/greedy, choice/sampled, choice/thinking, grammar/greedy, grammar/sampled, grammar/thinking |
| tools | FAIL: 1/5 tool cases right; failed required (400 {"error": {"message": "tool_choice \"required\" or a named function on backend 'metal': libtfgrammar.dylib is required for structured output and required tool calls (HTTP 400 when missing); restore th); named (400 {"error": {"message": "tool_choice \"required\" or a named function on backend 'metal': libtfgrammar.dylib is required for structured output and required tool calls (HTTP 400 when missing); restore th); named/thinking (400 {"error": {"message": "tool_choice \"required\" or a named function on backend 'metal': libtfgrammar.dylib is required for structured output and required tool calls (HTTP 400 when missing); restore th); named/stream (400 {"error": {"message": "tool_choice \"required\" or a named function on backend 'metal': libtfgrammar.dylib is required for structured output and required tool calls (HTTP 400 when missing); restore th) |
| sampling | pass: 9/9 seeded replies equal on repeat and undrafted; 0 errors |
| turns | pass: resumed == again: True; cold (after a restart): True; cached 5493 of 5649; ttft resumed 0.726s, cold 7.018s |

