# MiniMax-M3.1-Flash, MLX mixed 3-bit (mix256k), 144k context on 1x Apple M5 Ultra (256 GB unified), macOS

Target `minimax-m31-mix256k-m5`: MiniMax-M3.1-Flash, MLX mixed 3-bit (mix256k), 144k context, TensorFold native Metal on one M5 Ultra. Engine: TensorFold native, Metal. Rendered from `stats/minimax-m31-mix256k-m5.json` (21 runs); aggregate tok/s, total (a stream).

## 2026-10-25 08:05: run `20261025-080537-quick`

Plan quick, done; served as `MiniMax-M3.1-Flash`.

Serving: engine_commit `c1ace3229`; binary_sha256 `8776ddb5e9e62c446949a202efc983d51874eb1759d020d1acc302cf30dfa088`; served_model `{"object": "list", "data": [{"id": "MiniMax-M3.1-Flash", "object": "model", "created": 179`; chip `Apple M5 Ultra; 274877906944`; suite_commit `277c842a1481`

### ruler-fresh

| streams | prose total (a stream) | code total (a stream) | structured total (a stream) | list total (a stream) | first token |
|---:|---:|---:|---:|---:|---:|
| 1 | 43.1 (43.1) | 59.2 (59.2) | 48.9 (48.9) | 53.0 (53.0) | 0.31-0.33 s |

Engine rounds (ruler-fresh):

| streams | tokens a round | drafts a round | accepted | ms a round | requests |
|---:|---:|---:|---:|---:|---:|
| 1 | 2.207 | 1.858 | 65% | 43.22 | 12 |

### ruler-after

| streams | prose total (a stream) | code total (a stream) | structured total (a stream) | list total (a stream) | first token |
|---:|---:|---:|---:|---:|---:|
| 1 | 43.2 (43.2) | 58.8 (58.8) | 49.6 (49.6) | 52.9 (52.9) | 0.31-0.33 s |

Engine rounds (ruler-after):

| streams | tokens a round | drafts a round | accepted | ms a round | requests |
|---:|---:|---:|---:|---:|---:|
| 1 | 2.261 | 1.959 | 64% | 44.22 | 13 |

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
| memory-idle | measured: mac: System-wide memory free percentage: 95%; total = 4096.00M  us |
| structured | pass: 18/18 obey, drafted == plain 12/12; a bad regex -> 400 |
| tools | pass: 5/5 tool cases right |
| sampling | pass: 9/9 seeded replies equal on repeat and undrafted; 0 errors |
| turns | pass: resumed == again: True; cold (after a restart): True; cached 4685 of 4793; ttft resumed 0.267s, cold 5.854s |
| urls | FAIL: public 400; loopback 400; http 400; unexpected: ['public'] |

## 2026-10-24 20:24: run `20261024-202437-dsv41-quality-off`

Plan dsv41-quality-off, done; served as `MiniMax-M3.1-Flash`.

Serving: engine_commit `e6b3b3bd0`; binary_sha256 `5b078b780af71ddf5fc7d92ff40119f5c835f8aecccef199d36c0b22775a86aa`; served_model `{"object": "list", "data": [{"id": "MiniMax-M3.1-Flash", "object": "model", "created": 179`; chip `Apple M5 Ultra; 274877906944`; suite_commit `277c842a1481`

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
| ifeval | 89/150 |
| gsm8k | 244/250 |
| mgsm | 197/240 |
| mmlu | 280/342 |
| math500 | 450/500 |

### checks

| check | result |
|---|---|
| memory-idle | measured: mac: System-wide memory free percentage: 23%; total = 4096.00M  us |

## 2026-10-24 19:30: run `20261024-193050-quick`

Plan quick, done; served as `MiniMax-M3.1-Flash`.

Serving: engine_commit `e6b3b3bd0`; binary_sha256 `5b078b780af71ddf5fc7d92ff40119f5c835f8aecccef199d36c0b22775a86aa`; served_model `{"object": "list", "data": [{"id": "MiniMax-M3.1-Flash", "object": "model", "created": 179`; chip `Apple M5 Ultra; 274877906944`; suite_commit `277c842a1481`

### ruler-fresh

| streams | prose total (a stream) | code total (a stream) | structured total (a stream) | list total (a stream) | first token |
|---:|---:|---:|---:|---:|---:|
| 1 | 44.4 (44.4) | 58.9 (58.9) | 49.5 (49.5) | 50.9 (50.9) | 0.31-0.33 s |

Engine rounds (ruler-fresh):

| streams | tokens a round | drafts a round | accepted | ms a round | requests |
|---:|---:|---:|---:|---:|---:|
| 1 | 2.257 | 1.893 | 66% | 44.32 | 12 |

### ruler-after

| streams | prose total (a stream) | code total (a stream) | structured total (a stream) | list total (a stream) | first token |
|---:|---:|---:|---:|---:|---:|
| 1 | 42.4 (42.4) | 58.1 (58.1) | 48.9 (48.9) | 50.9 (50.9) | 0.31-0.33 s |

Engine rounds (ruler-after):

| streams | tokens a round | drafts a round | accepted | ms a round | requests |
|---:|---:|---:|---:|---:|---:|
| 1 | 2.1 | 1.691 | 65% | 41.93 | 13 |

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
| memory-idle | measured: mac: System-wide memory free percentage: 22%; total = 4096.00M  us |
| structured | pass: 18/18 obey, drafted == plain 12/12; a bad regex -> 400 |
| tools | pass: 5/5 tool cases right |
| sampling | pass: 9/9 seeded replies equal on repeat and undrafted; 0 errors |
| turns | pass: resumed == again: True; cold (after a restart): True; cached 4685 of 4793; ttft resumed 0.267s, cold 5.527s |
| urls | FAIL: public 400; loopback 400; http 400; unexpected: ['public'] |

## 2026-10-24 18:47: run `20261024-184727-prefill`

Plan prefill, done; served as `MiniMax-M3.1-Flash`.

Serving: engine_commit `057d59d53`; binary_sha256 `cbb06a790f3a8981b71a622655c5bf186fde6394fee0c81b1fd969baa9a31ced`; served_model `{"object": "list", "data": [{"id": "MiniMax-M3.1-Flash", "object": "model", "created": 179`; chip `Apple M5 Ultra; 274877906944`; suite_commit `277c842a1481`

### checks

| check | result |
|---|---|
| memory-idle | measured: mac: System-wide memory free percentage: 21%; total = 4096.00M  us |
| prefill-off | measured: 2259 tokens 578.3 tok/s (3.906 s), 8402 tokens 1483.4 tok/s (5.664 s), 32981 tokens 1490.5 tok/s (22.128 s), 131283 tokens 1378.7 tok/s (95.224 s) |
| prefill-thinking | measured: 2255 tokens 1302.7 tok/s (1.731 s), 8401 tokens 1466.1 tok/s (5.73 s), 32978 tokens 1483.2 tok/s (22.235 s), 131283 tokens 1365.9 tok/s (96.116 s) |
| memory-busy | measured: mac: System-wide memory free percentage: 14%; total = 4096.00M  us |

## 2026-10-24 18:31: run `20261024-183145-quick`

Plan quick, done; served as `MiniMax-M3.1-Flash`.

Serving: engine_commit `057d59d53`; binary_sha256 `cbb06a790f3a8981b71a622655c5bf186fde6394fee0c81b1fd969baa9a31ced`; served_model `{"object": "list", "data": [{"id": "MiniMax-M3.1-Flash", "object": "model", "created": 179`; chip `Apple M5 Ultra; 274877906944`; suite_commit `277c842a1481`

### ruler-fresh

| streams | prose total (a stream) | code total (a stream) | structured total (a stream) | list total (a stream) | first token |
|---:|---:|---:|---:|---:|---:|
| 1 | 42.5 (42.5) | 58.1 (58.1) | 47.7 (47.7) | 50.9 (50.9) | 0.31-0.33 s |

Engine rounds (ruler-fresh):

| streams | tokens a round | drafts a round | accepted | ms a round | requests |
|---:|---:|---:|---:|---:|---:|
| 1 | 2.093 | 1.677 | 65% | 42.03 | 12 |

### ruler-after

| streams | prose total (a stream) | code total (a stream) | structured total (a stream) | list total (a stream) | first token |
|---:|---:|---:|---:|---:|---:|
| 1 | 42.5 (42.5) | 58.8 (58.8) | 49.4 (49.4) | 50.9 (50.9) | 0.31-0.33 s |

Engine rounds (ruler-after):

| streams | tokens a round | drafts a round | accepted | ms a round | requests |
|---:|---:|---:|---:|---:|---:|
| 1 | 2.165 | 1.772 | 66% | 42.97 | 13 |

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
| memory-idle | measured: mac: System-wide memory free percentage: 22%; total = 3072.00M  us |
| structured | pass: 18/18 obey, drafted == plain 12/12; a bad regex -> 400 |
| tools | pass: 5/5 tool cases right |
| sampling | pass: 9/9 seeded replies equal on repeat and undrafted; 0 errors |
| turns | pass: resumed == again: True; cold (after a restart): True; cached 4685 of 4793; ttft resumed 0.259s, cold 5.388s |
| urls | FAIL: public 400; loopback 400; http 400; unexpected: ['public'] |

## 2026-10-24 18:26: run `20261024-182630-speed`

Plan speed, done; served as `MiniMax-M3.1-Flash`.

Serving: engine_commit `057d59d53`; binary_sha256 `cbb06a790f3a8981b71a622655c5bf186fde6394fee0c81b1fd969baa9a31ced`; served_model `{"object": "list", "data": [{"id": "MiniMax-M3.1-Flash", "object": "model", "created": 179`; chip `Apple M5 Ultra; 274877906944`; suite_commit `277c842a1481`

### ruler-fresh

| streams | prose total (a stream) | code total (a stream) | structured total (a stream) | list total (a stream) | first token |
|---:|---:|---:|---:|---:|---:|
| 1 | 43.1 (43.1) | 58.9 (58.9) | 49.6 (49.6) | 50.3 (50.3) | 0.31-0.33 s |
| 2 | 57.6 (28.8) | 63.3 (31.7) | 61.3 (30.7) | 75.5 (37.7) | 0.46-0.49 s |

Engine rounds (ruler-fresh):

| streams | tokens a round | drafts a round | accepted | ms a round | requests |
|---:|---:|---:|---:|---:|---:|
| 1 | 2.112 | 1.667 | 66% | 41.83 | 12 |
| 2 | 1.828 | 1.083 | 76% | 56.74 | 25 |

### ruler-after

| streams | prose total (a stream) | code total (a stream) | structured total (a stream) | list total (a stream) | first token |
|---:|---:|---:|---:|---:|---:|
| 1 | 43.0 (43.0) | 58.7 (58.7) | 51.0 (51.0) | 50.3 (50.3) | 0.31-0.33 s |

Engine rounds (ruler-after):

| streams | tokens a round | drafts a round | accepted | ms a round | requests |
|---:|---:|---:|---:|---:|---:|
| 1 | 2.155 | 1.75 | 66% | 42.46 | 13 |

### checks

| check | result |
|---|---|
| memory-idle | measured: mac: System-wide memory free percentage: 21%; total = 3072.00M  us |
| turns | pass: resumed == again: True; cold (after a restart): True; cached 4685 of 4793; ttft resumed 0.269s, cold 3.588s |
| memory-busy | measured: mac: System-wide memory free percentage: 21%; total = 3072.00M  us |

## 2026-10-24 16:05: run `20261024-160557-quick`

Plan quick, done; served as `MiniMax-M3.1-Flash`.

Serving: engine_commit `959d24809`; binary_sha256 `ea1f7d307902de10e228c145d20838aae8dca28b975007ec93e0bb26b1dd324a`; served_model `{"object": "list", "data": [{"id": "MiniMax-M3.1-Flash", "object": "model", "created": 179`; chip `Apple M5 Ultra; 274877906944`; suite_commit `277c842a1481`

### ruler-fresh

| streams | prose total (a stream) | code total (a stream) | structured total (a stream) | list total (a stream) | first token |
|---:|---:|---:|---:|---:|---:|
| 1 | 42.3 (42.3) | 57.4 (57.4) | 48.1 (48.1) | 47.7 (47.7) | 0.31-0.33 s |

Engine rounds (ruler-fresh):

| streams | tokens a round | drafts a round | accepted | ms a round | requests |
|---:|---:|---:|---:|---:|---:|
| 1 | 2.159 | 1.799 | 64% | 44.2 | 12 |

### ruler-after

| streams | prose total (a stream) | code total (a stream) | structured total (a stream) | list total (a stream) | first token |
|---:|---:|---:|---:|---:|---:|
| 1 | 43.1 (43.1) | 57.1 (57.1) | 48.7 (48.7) | 47.7 (47.7) | 0.31-0.33 s |

Engine rounds (ruler-after):

| streams | tokens a round | drafts a round | accepted | ms a round | requests |
|---:|---:|---:|---:|---:|---:|
| 1 | 2.222 | 1.925 | 63% | 45.21 | 13 |

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
| memory-idle | measured: mac: System-wide memory free percentage: 34%; total = 3072.00M  us |
| structured | pass: 18/18 obey, drafted == plain 12/12; a bad regex -> 400 |
| tools | pass: 5/5 tool cases right |
| sampling | pass: 9/9 seeded replies equal on repeat and undrafted; 0 errors |
| turns | pass: resumed == again: True; cold (after a restart): True; cached 4685 of 4826; ttft resumed 0.29s, cold 5.113s |
| urls | FAIL: public 400; loopback 400; http 400; unexpected: ['public'] |

## 2026-10-24 16:00: run `20261024-160047-prefill`

Plan prefill, done; served as `MiniMax-M3.1-Flash`.

Serving: engine_commit `959d24809`; binary_sha256 `ea1f7d307902de10e228c145d20838aae8dca28b975007ec93e0bb26b1dd324a`; served_model `{"object": "list", "data": [{"id": "MiniMax-M3.1-Flash", "object": "model", "created": 179`; chip `Apple M5 Ultra; 274877906944`; suite_commit `277c842a1481`

### checks

| check | result |
|---|---|
| memory-idle | measured: mac: System-wide memory free percentage: 40%; total = 3072.00M  us |
| prefill-off | measured: 2257 tokens 645.4 tok/s (3.497 s), 8402 tokens 1432.6 tok/s (5.865 s), 32978 tokens 1424.0 tok/s (23.158 s), 131284 tokens 1319.1 tok/s (99.528 s) |
| prefill-thinking | measured: 2256 tokens 1285.5 tok/s (1.755 s), 8402 tokens 1384.4 tok/s (6.069 s), 32977 tokens 1395.3 tok/s (23.634 s), 131283 tokens 1316.7 tok/s (99.704 s) |
| memory-busy | measured: mac: System-wide memory free percentage: 18%; total = 3072.00M  us |

## 2026-10-24 13:49: run `20261024-134959-quick`

Plan quick, done; served as `MiniMax-M3.1-Flash`.

Serving: engine_commit `ec0c099de`; binary_sha256 `e3074abc85c644cd302a184a831347fe84922daf5959a36aed4f5bf6904f8706`; served_model `{"object": "list", "data": [{"id": "MiniMax-M3.1-Flash", "object": "model", "created": 179`; chip `Apple M5 Ultra; 274877906944`; suite_commit `277c842a1481`

### ruler-fresh

| streams | prose total (a stream) | code total (a stream) | structured total (a stream) | list total (a stream) | first token |
|---:|---:|---:|---:|---:|---:|
| 1 | 42.5 (42.5) | 57.6 (57.6) | 48.0 (48.0) | 47.7 (47.7) | 0.31-0.33 s |

Engine rounds (ruler-fresh):

| streams | tokens a round | drafts a round | accepted | ms a round | requests |
|---:|---:|---:|---:|---:|---:|
| 1 | 2.164 | 1.811 | 64% | 44.24 | 12 |

### ruler-after

| streams | prose total (a stream) | code total (a stream) | structured total (a stream) | list total (a stream) | first token |
|---:|---:|---:|---:|---:|---:|
| 1 | 42.3 (42.3) | 57.0 (57.0) | 48.7 (48.7) | 48.9 (48.9) | 0.30-0.33 s |

Engine rounds (ruler-after):

| streams | tokens a round | drafts a round | accepted | ms a round | requests |
|---:|---:|---:|---:|---:|---:|
| 1 | 2.222 | 1.919 | 63% | 45.12 | 13 |

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
| memory-idle | measured: mac: System-wide memory free percentage: 34%; total = 3072.00M  us |
| structured | pass: 18/18 obey, drafted == plain 12/12; a bad regex -> 400 |
| tools | pass: 5/5 tool cases right |
| sampling | pass: 9/9 seeded replies equal on repeat and undrafted; 0 errors |
| turns | pass: resumed == again: True; cold (after a restart): True; cached 4685 of 4826; ttft resumed 0.296s, cold 5.602s |
| urls | FAIL: public 400; loopback 400; http 400; unexpected: ['public'] |

## 2026-10-24 13:44: run `20261024-134445-prefill`

Plan prefill, done; served as `MiniMax-M3.1-Flash`.

Serving: engine_commit `ec0c099de`; binary_sha256 `e3074abc85c644cd302a184a831347fe84922daf5959a36aed4f5bf6904f8706`; served_model `{"object": "list", "data": [{"id": "MiniMax-M3.1-Flash", "object": "model", "created": 179`; chip `Apple M5 Ultra; 274877906944`; suite_commit `277c842a1481`

### checks

| check | result |
|---|---|
| memory-idle | measured: mac: System-wide memory free percentage: 22%; total = 3072.00M  us |
| prefill-off | measured: 2261 tokens 665.8 tok/s (3.396 s), 8403 tokens 1428.8 tok/s (5.881 s), 32978 tokens 1420.4 tok/s (23.218 s), 131285 tokens 1318.7 tok/s (99.555 s) |
| prefill-thinking | measured: 2258 tokens 1289.5 tok/s (1.751 s), 8402 tokens 1382.4 tok/s (6.078 s), 32976 tokens 1369.5 tok/s (24.078 s), 131280 tokens 1269.7 tok/s (103.392 s) |
| memory-busy | measured: mac: System-wide memory free percentage: 18%; total = 3072.00M  us |

## 2026-10-24 11:56: run `20261024-115618-quick`

Plan quick, done; served as `MiniMax-M3.1-Flash`.

Serving: engine_commit `3cdf8794d`; binary_sha256 `79d22c1783a96bb722855d436f9c712224390890efce564122ee0ac666caea65`; served_model `{"object": "list", "data": [{"id": "MiniMax-M3.1-Flash", "object": "model", "created": 179`; chip `Apple M5 Ultra; 274877906944`; suite_commit `277c842a1481`

### ruler-fresh

| streams | prose total (a stream) | code total (a stream) | structured total (a stream) | list total (a stream) | first token |
|---:|---:|---:|---:|---:|---:|
| 1 | 41.0 (41.0) | 56.4 (56.4) | 48.6 (48.6) | 47.3 (47.3) | 0.31-0.33 s |

Engine rounds (ruler-fresh):

| streams | tokens a round | drafts a round | accepted | ms a round | requests |
|---:|---:|---:|---:|---:|---:|
| 1 | 2.094 | 1.677 | 65% | 43.3 | 12 |

### ruler-after

| streams | prose total (a stream) | code total (a stream) | structured total (a stream) | list total (a stream) | first token |
|---:|---:|---:|---:|---:|---:|
| 1 | 42.3 (42.3) | 56.6 (56.6) | 48.7 (48.7) | 48.5 (48.5) | 0.31-0.33 s |

Engine rounds (ruler-after):

| streams | tokens a round | drafts a round | accepted | ms a round | requests |
|---:|---:|---:|---:|---:|---:|
| 1 | 2.244 | 1.944 | 64% | 45.77 | 13 |

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
| memory-idle | measured: mac: System-wide memory free percentage: 95%; total = 5120.00M  us |
| structured | pass: 18/18 obey, drafted == plain 12/12; a bad regex -> 400 |
| tools | pass: 5/5 tool cases right |
| sampling | pass: 9/9 seeded replies equal on repeat and undrafted; 0 errors |
| turns | pass: resumed == again: True; cold (after a restart): True; cached 4685 of 4826; ttft resumed 0.294s, cold 5.956s |
| urls | FAIL: public 400; loopback 400; http 400; unexpected: ['public'] |

## 2026-10-24 11:50: run `20261024-115050-prefill`

Plan prefill, done; served as `MiniMax-M3.1-Flash`.

Serving: engine_commit `3cdf8794d`; binary_sha256 `79d22c1783a96bb722855d436f9c712224390890efce564122ee0ac666caea65`; served_model `{"object": "list", "data": [{"id": "MiniMax-M3.1-Flash", "object": "model", "created": 179`; chip `Apple M5 Ultra; 274877906944`; suite_commit `277c842a1481`

### checks

| check | result |
|---|---|
| memory-idle | measured: mac: System-wide memory free percentage: 57%; total = 5120.00M  us |
| prefill-off | measured: 2259 tokens 610.9 tok/s (3.698 s), 8402 tokens 1394.1 tok/s (6.027 s), 32980 tokens 1383.1 tok/s (23.845 s), 131282 tokens 1279.8 tok/s (102.579 s) |
| prefill-thinking | measured: 2257 tokens 1256.7 tok/s (1.796 s), 8402 tokens 1327.7 tok/s (6.328 s), 32980 tokens 1314.0 tok/s (25.099 s), 131281 tokens 1223.1 tok/s (107.336 s) |
| memory-busy | measured: mac: System-wide memory free percentage: 18%; total = 5120.00M  us |

## 2026-10-24 11:07: run `20261024-110714-quick`

Plan quick, done; served as `MiniMax-M3.1-Flash`.

Serving: engine_commit `4c2abaa87`; binary_sha256 `cd20cbee23dacbb74acdd628c50393eb370a1d991ad3b04e6f42d9edfb8d39b6`; served_model `{"object": "list", "data": [{"id": "MiniMax-M3.1-Flash", "object": "model", "created": 179`; chip `Apple M5 Ultra; 274877906944`; suite_commit `277c842a1481`

### ruler-fresh

| streams | prose total (a stream) | code total (a stream) | structured total (a stream) | list total (a stream) | first token |
|---:|---:|---:|---:|---:|---:|
| 1 | 42.7 (42.7) | 54.7 (54.7) | 47.3 (47.3) | 47.5 (47.5) | 0.31-0.33 s |

Engine rounds (ruler-fresh):

| streams | tokens a round | drafts a round | accepted | ms a round | requests |
|---:|---:|---:|---:|---:|---:|
| 1 | 2.159 | 1.746 | 66% | 44.93 | 12 |

### ruler-after

| streams | prose total (a stream) | code total (a stream) | structured total (a stream) | list total (a stream) | first token |
|---:|---:|---:|---:|---:|---:|
| 1 | 43.0 (43.0) | 57.0 (57.0) | 47.9 (47.9) | 47.6 (47.6) | 0.31-0.33 s |

Engine rounds (ruler-after):

| streams | tokens a round | drafts a round | accepted | ms a round | requests |
|---:|---:|---:|---:|---:|---:|
| 1 | 2.194 | 1.855 | 64% | 44.91 | 13 |

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
| memory-idle | measured: mac: System-wide memory free percentage: 57%; total = 5120.00M  us |
| structured | pass: 18/18 obey, drafted == plain 12/12; a bad regex -> 400 |
| tools | pass: 5/5 tool cases right |
| sampling | pass: 9/9 seeded replies equal on repeat and undrafted; 0 errors |
| turns | pass: resumed == again: True; cold (after a restart): True; cached 4685 of 4826; ttft resumed 0.288s, cold 3.675s |
| urls | FAIL: public 400; loopback 400; http 400; unexpected: ['public'] |

## 2026-10-24 11:01: run `20261024-110141-prefill`

Plan prefill, done; served as `MiniMax-M3.1-Flash`.

Serving: engine_commit `4c2abaa87`; binary_sha256 `cd20cbee23dacbb74acdd628c50393eb370a1d991ad3b04e6f42d9edfb8d39b6`; served_model `{"object": "list", "data": [{"id": "MiniMax-M3.1-Flash", "object": "model", "created": 179`; chip `Apple M5 Ultra; 274877906944`; suite_commit `277c842a1481`

### checks

| check | result |
|---|---|
| memory-idle | measured: mac: System-wide memory free percentage: 23%; total = 4096.00M  us |
| prefill-off | measured: 2259 tokens 672.7 tok/s (3.358 s), 8406 tokens 1408.0 tok/s (5.97 s), 32980 tokens 1401.6 tok/s (23.531 s), 131285 tokens 1291.0 tok/s (101.695 s) |
| prefill-thinking | measured: 2259 tokens 1258.5 tok/s (1.795 s), 8401 tokens 1346.5 tok/s (6.239 s), 32979 tokens 1336.8 tok/s (24.67 s), 131279 tokens 1256.1 tok/s (104.514 s) |
| memory-busy | measured: mac: System-wide memory free percentage: 19%; total = 4096.00M  us |

## 2026-10-24 09:03: run `20261024-090309-quick`

Plan quick, done; served as `MiniMax-M3.1-Flash`.

Serving: engine_commit `353954b31`; binary_sha256 `a8e1aea82aad3c074acd7e674ec889dc5db590b113ffb47f521274a036af3968`; served_model `{"object": "list", "data": [{"id": "MiniMax-M3.1-Flash", "object": "model", "created": 179`; chip `Apple M5 Ultra; 274877906944`; suite_commit `277c842a1481`

### ruler-fresh

| streams | prose total (a stream) | code total (a stream) | structured total (a stream) | list total (a stream) | first token |
|---:|---:|---:|---:|---:|---:|
| 1 | 42.8 (42.8) | 54.9 (54.9) | 48.4 (48.4) | 48.1 (48.1) | 0.31-0.34 s |

Engine rounds (ruler-fresh):

| streams | tokens a round | drafts a round | accepted | ms a round | requests |
|---:|---:|---:|---:|---:|---:|
| 1 | 2.091 | 1.696 | 64% | 43.06 | 12 |

### ruler-after

| streams | prose total (a stream) | code total (a stream) | structured total (a stream) | list total (a stream) | first token |
|---:|---:|---:|---:|---:|---:|
| 1 | 42.3 (42.3) | 57.4 (57.4) | 48.3 (48.3) | 48.0 (48.0) | 0.31-0.34 s |

Engine rounds (ruler-after):

| streams | tokens a round | drafts a round | accepted | ms a round | requests |
|---:|---:|---:|---:|---:|---:|
| 1 | 2.074 | 1.684 | 63% | 42.31 | 13 |

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
| memory-idle | measured: mac: System-wide memory free percentage: 23%; total = 4096.00M  us |
| structured | pass: 18/18 obey, drafted == plain 12/12; a bad regex -> 400 |
| tools | pass: 5/5 tool cases right |
| sampling | pass: 9/9 seeded replies equal on repeat and undrafted; 0 errors |
| turns | pass: resumed == again: True; cold (after a restart): True; cached 4685 of 4826; ttft resumed 0.293s, cold 3.865s |
| urls | FAIL: public 400; loopback 400; http 400; unexpected: ['public'] |

## 2026-10-24 08:57: run `20261024-085738-prefill`

Plan prefill, done; served as `MiniMax-M3.1-Flash`.

Serving: engine_commit `353954b31`; binary_sha256 `a8e1aea82aad3c074acd7e674ec889dc5db590b113ffb47f521274a036af3968`; served_model `{"object": "list", "data": [{"id": "MiniMax-M3.1-Flash", "object": "model", "created": 179`; chip `Apple M5 Ultra; 274877906944`; suite_commit `277c842a1481`

### checks

| check | result |
|---|---|
| memory-idle | measured: mac: System-wide memory free percentage: 97%; total = 4096.00M  us |
| prefill-off | measured: 2259 tokens 594.5 tok/s (3.8 s), 8405 tokens 1366.0 tok/s (6.153 s), 32979 tokens 1362.8 tok/s (24.2 s), 131283 tokens 1266.2 tok/s (103.685 s) |
| prefill-thinking | measured: 2256 tokens 1226.8 tok/s (1.839 s), 8400 tokens 1352.2 tok/s (6.212 s), 32978 tokens 1343.1 tok/s (24.554 s), 131279 tokens 1265.8 tok/s (103.715 s) |
| memory-busy | measured: mac: System-wide memory free percentage: 19%; total = 4096.00M  us |

## 2026-10-24 03:42: run `20261024-034251-mlx-speed`

Plan mlx-speed, done; served as `MiniMax-M3.1-Flash`.

Serving: engine_commit `39746b53e`; binary_sha256 `d56e474b3cef52e1cdaf7383f9fb415098b778f688850572dbae187b27a728df`; served_model `{"object": "list", "data": [{"id": "MiniMax-M3.1-Flash", "object": "model", "created": 179`; chip `Apple M5 Ultra; 274877906944`; suite_commit `277c842a1481`

### ruler-streams

| streams | prose total (a stream) | code total (a stream) | structured total (a stream) | list total (a stream) | first token |
|---:|---:|---:|---:|---:|---:|
| 1 | 44.1 (44.1) | 44.0 (44.0) | 44.0 (44.0) | 44.1 (44.1) | 0.32-0.34 s |
| 2 | 63.3 (31.7) | 62.8 (31.4) | 64.1 (32.0) | 63.6 (31.8) | 0.48-0.51 s |
| 4 | 126.3 (31.6) | 125.6 (31.4) | 126.3 (30.9) | 126.6 (31.7) | 3.40-4.81 s |

Engine rounds (ruler-streams):

| streams | tokens a round | drafts a round | accepted | ms a round | requests |
|---:|---:|---:|---:|---:|---:|
| 1 | 1.004 | 0.0 |  | 22.8 | 12 |
| 2 | 1.004 | 0.0 |  | 31.66 | 25 |
| 4 | 1.004 | 0.0 |  | 31.99 | 50 |

### checks

| check | result |
|---|---|
| memory-idle | measured: mac: System-wide memory free percentage: 96%; total = 4096.00M  us |

## 2026-10-24 03:33: run `20261024-033319-prefill`

Plan prefill, done; served as `MiniMax-M3.1-Flash`.

Serving: engine_commit `39746b53e`; binary_sha256 `d56e474b3cef52e1cdaf7383f9fb415098b778f688850572dbae187b27a728df`; served_model `{"object": "list", "data": [{"id": "MiniMax-M3.1-Flash", "object": "model", "created": 179`; chip `Apple M5 Ultra; 274877906944`; suite_commit `277c842a1481`

### checks

| check | result |
|---|---|
| memory-idle | measured: mac: System-wide memory free percentage: 96%; total = 4096.00M  us |
| prefill-off | measured: 2261 tokens 579.7 tok/s (3.9 s), 8402 tokens 1205.6 tok/s (6.969 s), 32980 tokens 1020.4 tok/s (32.321 s), 131282 tokens 702.7 tok/s (186.829 s) |
| prefill-thinking | measured: 2259 tokens 1172.3 tok/s (1.927 s), 8407 tokens 1194.0 tok/s (7.041 s), 32979 tokens 1025.0 tok/s (32.176 s), 131283 tokens 699.8 tok/s (187.603 s) |
| memory-busy | measured: mac: System-wide memory free percentage: 19%; total = 4096.00M  us |

## 2026-10-24 00:46: run `20261024-004651-dsv41-quality-off`

Plan dsv41-quality-off, done; served as `MiniMax-M3.1-Flash`.

Serving: engine_commit `39746b53e`; binary_sha256 `d56e474b3cef52e1cdaf7383f9fb415098b778f688850572dbae187b27a728df`; served_model `{"object": "list", "data": [{"id": "MiniMax-M3.1-Flash", "object": "model", "created": 179`; chip `Apple M5 Ultra; 274877906944`; suite_commit `277c842a1481`

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
| tools | 55/60 |
| json | 30/30 |
| ifeval | 86/150 |
| gsm8k | 244/250 |
| mgsm | 210/240 |
| mmlu | 280/342 |
| math500 | 454/500 |

### checks

| check | result |
|---|---|
| memory-idle | measured: mac: System-wide memory free percentage: 22%; total = 4096.00M  us |

## 2026-10-24 00:45: run `20261024-004535-structured`

Plan structured, done; served as `MiniMax-M3.1-Flash`.

Serving: engine_commit `39746b53e`; binary_sha256 `d56e474b3cef52e1cdaf7383f9fb415098b778f688850572dbae187b27a728df`; served_model `{"object": "list", "data": [{"id": "MiniMax-M3.1-Flash", "object": "model", "created": 179`; chip `Apple M5 Ultra; 274877906944`; suite_commit `277c842a1481`

### checks

| check | result |
|---|---|
| structured | pass: 18/18 obey, drafted == plain 12/12; a bad regex -> 400 |
| tools | pass: 5/5 tool cases right |

## 2026-10-24 00:39: run `20261024-003948-speed`

Plan speed, done; served as `MiniMax-M3.1-Flash`.

Serving: engine_commit `39746b53e`; binary_sha256 `d56e474b3cef52e1cdaf7383f9fb415098b778f688850572dbae187b27a728df`; served_model `{"object": "list", "data": [{"id": "MiniMax-M3.1-Flash", "object": "model", "created": 179`; chip `Apple M5 Ultra; 274877906944`; suite_commit `277c842a1481`

### ruler-fresh

| streams | prose total (a stream) | code total (a stream) | structured total (a stream) | list total (a stream) | first token |
|---:|---:|---:|---:|---:|---:|
| 1 | 42.8 (42.8) | 57.9 (57.9) | 48.7 (48.7) | 47.9 (47.9) | 0.31-0.33 s |
| 2 | 52.2 (26.1) | 65.5 (32.8) | 58.1 (29.0) | 74.7 (37.3) | 0.47-0.50 s |

Engine rounds (ruler-fresh):

| streams | tokens a round | drafts a round | accepted | ms a round | requests |
|---:|---:|---:|---:|---:|---:|
| 1 | 2.085 | 1.666 | 65% | 42.25 | 12 |
| 2 | 2.161 | 1.528 | 76% | 69.01 | 25 |

### ruler-after

| streams | prose total (a stream) | code total (a stream) | structured total (a stream) | list total (a stream) | first token |
|---:|---:|---:|---:|---:|---:|
| 1 | 42.2 (42.2) | 58.1 (58.1) | 48.6 (48.6) | 47.8 (47.8) | 0.31-0.33 s |

Engine rounds (ruler-after):

| streams | tokens a round | drafts a round | accepted | ms a round | requests |
|---:|---:|---:|---:|---:|---:|
| 1 | 2.14 | 1.759 | 64% | 43.48 | 13 |

### checks

| check | result |
|---|---|
| memory-idle | measured: mac: System-wide memory free percentage: 22%; total = 4096.00M  us |
| turns | pass: resumed == again: True; cold (after a restart): True; cached 4685 of 4826; ttft resumed 0.309s, cold 6.217s |
| memory-busy | measured: mac: System-wide memory free percentage: 22%; total = 4096.00M  us |

