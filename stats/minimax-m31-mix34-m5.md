# MiniMax-M3.1-Flash, MLX mixed 4/3-bit (mix34) on 1x Apple M5 Ultra (256 GB unified), macOS

Target `minimax-m31-mix34-m5`: MiniMax-M3.1-Flash, MLX mixed 4/3-bit (mix34), TensorFold native Metal on one M5 Ultra. Engine: TensorFold native, Metal. Rendered from `stats/minimax-m31-mix34-m5.json` (20 runs); aggregate tok/s, total (a stream).

## 2026-10-27 06:26: run `20261027-062647-glm-vision`

Plan glm-vision, done; served as `MiniMax-M3.1-Flash`.

Serving: engine_commit `cb35b7c28`; binary_sha256 `1cd3d3c900e7441653b99c2a764fa6c6f66de3a710c08d4ceeefa41ce948026a`; served_model `{"object": "list", "data": [{"id": "MiniMax-M3.1-Flash", "object": "model", "created": 179`; chip `Apple M5 Ultra; 274877906944`; suite_commit `a7ba7e392d57`

### suite-vision

| check | passed |
|---|---:|
| vision | 3/6 |
| vision-concurrent | 0/0 |

## 2026-10-27 06:09: run `20261027-060937-quick`

Plan quick, done; served as `MiniMax-M3.1-Flash`.

Serving: engine_commit `cb35b7c28`; binary_sha256 `1cd3d3c900e7441653b99c2a764fa6c6f66de3a710c08d4ceeefa41ce948026a`; served_model `{"object": "list", "data": [{"id": "MiniMax-M3.1-Flash", "object": "model", "created": 179`; chip `Apple M5 Ultra; 274877906944`; suite_commit `a7ba7e392d57`

### ruler-fresh

| streams | prose total (a stream) | code total (a stream) | structured total (a stream) | list total (a stream) | first token |
|---:|---:|---:|---:|---:|---:|
| 1 | 41.2 (41.2) | 61.3 (61.3) | 49.3 (49.3) | 55.3 (55.3) | 0.32-0.34 s |

Engine rounds (ruler-fresh):

| streams | tokens a round | drafts a round | accepted | ms a round | requests |
|---:|---:|---:|---:|---:|---:|
| 1 | 2.275 | 1.933 | 66% | 43.92 | 12 |

### ruler-after

| streams | prose total (a stream) | code total (a stream) | structured total (a stream) | list total (a stream) | first token |
|---:|---:|---:|---:|---:|---:|
| 1 | 40.8 (40.8) | 61.5 (61.5) | 49.9 (49.9) | 55.2 (55.2) | 0.31-0.33 s |

Engine rounds (ruler-after):

| streams | tokens a round | drafts a round | accepted | ms a round | requests |
|---:|---:|---:|---:|---:|---:|
| 1 | 2.305 | 2.04 | 64% | 44.45 | 13 |

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
| memory-idle | measured: mac: System-wide memory free percentage: 95%; total = 6144.00M  us |
| structured | pass: 18/18 obey, drafted == plain 12/12; a bad regex -> 400 |
| tools | pass: 5/5 tool cases right |
| sampling | pass: 9/9 seeded replies equal on repeat and undrafted; 0 errors |
| turns | pass: resumed == again: True; cold (after a restart): True; cached 4685 of 4826; ttft resumed 0.304s, cold 6.004s |
| urls | FAIL: public 400; loopback 400; http 400; unexpected: ['public'] |

## 2026-10-25 01:49: run `20261025-014954-dsv41-quality-off`

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
| tools | 57/60 |
| json | 30/30 |
| ifeval | 87/150 |
| gsm8k | 242/250 |
| mgsm | 203/240 |
| mmlu | 283/342 |
| math500 | 445/500 |

### checks

| check | result |
|---|---|
| memory-idle | measured: mac: System-wide memory free percentage: 95%; total = 3072.00M  us |

## 2026-10-24 19:18: run `20261024-191845-prefill-32k`

Plan prefill-32k, done; served as `MiniMax-M3.1-Flash`.

Serving: engine_commit `057d59d53`; binary_sha256 `cbb06a790f3a8981b71a622655c5bf186fde6394fee0c81b1fd969baa9a31ced`; served_model `{"object": "list", "data": [{"id": "MiniMax-M3.1-Flash", "object": "model", "created": 179`; chip `Apple M5 Ultra; 274877906944`; suite_commit `277c842a1481`

### checks

| check | result |
|---|---|
| memory-idle | measured: mac: System-wide memory free percentage: 20%; total = 4096.00M  us |
| prefill-off | measured: 2258 tokens 551.8 tok/s (4.092 s), 8404 tokens 1441.0 tok/s (5.832 s), 16595 tokens 1451.9 tok/s (11.43 s), 30932 tokens 1450.8 tok/s (21.321 s) |
| prefill-thinking | measured: 2260 tokens 1299.6 tok/s (1.739 s), 8401 tokens 1426.6 tok/s (5.889 s), 16597 tokens 1443.2 tok/s (11.5 s), 30931 tokens 1445.8 tok/s (21.393 s) |
| memory-busy | measured: mac: System-wide memory free percentage: 14%; total = 4096.00M  us |

## 2026-10-24 19:01: run `20261024-190149-quick`

Plan quick, done; served as `MiniMax-M3.1-Flash`.

Serving: engine_commit `057d59d53`; binary_sha256 `cbb06a790f3a8981b71a622655c5bf186fde6394fee0c81b1fd969baa9a31ced`; served_model `{"object": "list", "data": [{"id": "MiniMax-M3.1-Flash", "object": "model", "created": 179`; chip `Apple M5 Ultra; 274877906944`; suite_commit `277c842a1481`

### ruler-fresh

| streams | prose total (a stream) | code total (a stream) | structured total (a stream) | list total (a stream) | first token |
|---:|---:|---:|---:|---:|---:|
| 1 | 42.8 (42.8) | 59.2 (59.2) | 50.3 (50.3) | 55.8 (55.8) | 0.31-0.33 s |

Engine rounds (ruler-fresh):

| streams | tokens a round | drafts a round | accepted | ms a round | requests |
|---:|---:|---:|---:|---:|---:|
| 1 | 2.35 | 1.93 | 70% | 45.18 | 12 |

### ruler-after

| streams | prose total (a stream) | code total (a stream) | structured total (a stream) | list total (a stream) | first token |
|---:|---:|---:|---:|---:|---:|
| 1 | 42.6 (42.6) | 58.8 (58.8) | 48.5 (48.5) | 56.0 (56.0) | 0.32-0.33 s |

Engine rounds (ruler-after):

| streams | tokens a round | drafts a round | accepted | ms a round | requests |
|---:|---:|---:|---:|---:|---:|
| 1 | 2.347 | 2.007 | 67% | 45.61 | 13 |

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
| memory-idle | measured: mac: System-wide memory free percentage: 16%; total = 5120.00M  us |
| structured | pass: 18/18 obey, drafted == plain 12/12; a bad regex -> 400 |
| tools | pass: 5/5 tool cases right |
| sampling | pass: 9/9 seeded replies equal on repeat and undrafted; 0 errors |
| turns | pass: resumed == again: True; cold (after a restart): True; cached 4685 of 4826; ttft resumed 0.298s, cold 5.567s |
| urls | FAIL: public 400; loopback 400; http 400; unexpected: ['public'] |

## 2026-10-24 18:55: run `20261024-185520-speed`

Plan speed, done; served as `MiniMax-M3.1-Flash`.

Serving: engine_commit `057d59d53`; binary_sha256 `cbb06a790f3a8981b71a622655c5bf186fde6394fee0c81b1fd969baa9a31ced`; served_model `{"object": "list", "data": [{"id": "MiniMax-M3.1-Flash", "object": "model", "created": 179`; chip `Apple M5 Ultra; 274877906944`; suite_commit `277c842a1481`

### ruler-fresh

| streams | prose total (a stream) | code total (a stream) | structured total (a stream) | list total (a stream) | first token |
|---:|---:|---:|---:|---:|---:|
| 1 | 42.7 (42.7) | 58.5 (58.5) | 50.3 (50.3) | 55.8 (55.8) | 0.31-0.33 s |
| 2 | 51.0 (25.5) | 65.1 (32.5) | 57.9 (28.9) | 83.3 (41.7) | 0.47-0.49 s |

Engine rounds (ruler-fresh):

| streams | tokens a round | drafts a round | accepted | ms a round | requests |
|---:|---:|---:|---:|---:|---:|
| 1 | 2.345 | 1.934 | 69% | 45.24 | 12 |
| 2 | 2.118 | 1.475 | 76% | 65.85 | 25 |

### ruler-after

| streams | prose total (a stream) | code total (a stream) | structured total (a stream) | list total (a stream) | first token |
|---:|---:|---:|---:|---:|---:|
| 1 | 42.5 (42.5) | 58.7 (58.7) | 50.3 (50.3) | 55.9 (55.9) | 0.31-0.33 s |

Engine rounds (ruler-after):

| streams | tokens a round | drafts a round | accepted | ms a round | requests |
|---:|---:|---:|---:|---:|---:|
| 1 | 2.342 | 1.915 | 70% | 45.14 | 13 |

### checks

| check | result |
|---|---|
| memory-idle | measured: mac: System-wide memory free percentage: 95%; total = 5120.00M  us |
| turns | pass: resumed == again: True; cold (after a restart): True; cached 4685 of 4826; ttft resumed 0.297s, cold 3.661s |
| memory-busy | measured: mac: System-wide memory free percentage: 16%; total = 5120.00M  us |

## 2026-10-24 16:21: run `20261024-162156-quick`

Plan quick, done; served as `MiniMax-M3.1-Flash`.

Serving: engine_commit `959d24809`; binary_sha256 `ea1f7d307902de10e228c145d20838aae8dca28b975007ec93e0bb26b1dd324a`; served_model `{"object": "list", "data": [{"id": "MiniMax-M3.1-Flash", "object": "model", "created": 179`; chip `Apple M5 Ultra; 274877906944`; suite_commit `277c842a1481`

### ruler-fresh

| streams | prose total (a stream) | code total (a stream) | structured total (a stream) | list total (a stream) | first token |
|---:|---:|---:|---:|---:|---:|
| 1 | 41.6 (41.6) | 65.1 (65.1) | 46.0 (46.0) | 56.2 (56.2) | 0.31-0.33 s |

Engine rounds (ruler-fresh):

| streams | tokens a round | drafts a round | accepted | ms a round | requests |
|---:|---:|---:|---:|---:|---:|
| 1 | 2.442 | 2.093 | 69% | 46.77 | 12 |

### ruler-after

| streams | prose total (a stream) | code total (a stream) | structured total (a stream) | list total (a stream) | first token |
|---:|---:|---:|---:|---:|---:|
| 1 | 41.6 (41.6) | 66.2 (66.2) | 47.0 (47.0) | 56.3 (56.3) | 0.32-0.34 s |

Engine rounds (ruler-after):

| streams | tokens a round | drafts a round | accepted | ms a round | requests |
|---:|---:|---:|---:|---:|---:|
| 1 | 2.481 | 2.154 | 69% | 47.02 | 13 |

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
| memory-idle | measured: mac: System-wide memory free percentage: 95%; total = 3072.00M  us |
| structured | pass: 18/18 obey, drafted == plain 12/12; a bad regex -> 400 |
| tools | pass: 5/5 tool cases right |
| sampling | pass: 9/9 seeded replies equal on repeat and undrafted; 0 errors |
| turns | pass: resumed == again: True; cold (after a restart): True; cached 4685 of 4826; ttft resumed 0.309s, cold 6.076s |
| urls | FAIL: public 400; loopback 400; http 400; unexpected: ['public'] |

## 2026-10-24 14:32: run `20261024-143234-prefill-64k`

Plan prefill-64k, done; served as `MiniMax-M3.1-Flash`.

Serving: engine_commit `60305dd4f`; binary_sha256 `14da99e1e085aa1791982158160ffb9882085a8b66528cea5623183fcd022021`; served_model `{"object": "list", "data": [{"id": "MiniMax-M3.1-Flash", "object": "model", "created": 179`; chip `Apple M5 Ultra; 274877906944`; suite_commit `277c842a1481`

### checks

| check | result |
|---|---|
| memory-idle | measured: mac: System-wide memory free percentage: 95%; total = 3072.00M  us |
| prefill-off | measured: 2261 tokens 571.2 tok/s (3.958 s), 8403 tokens 1392.6 tok/s (6.034 s), 32980 tokens 1391.7 tok/s (23.697 s), 61651 tokens 1363.8 tok/s (45.204 s) |
| prefill-thinking | measured: 2258 tokens 1272.8 tok/s (1.774 s), 8404 tokens 1381.1 tok/s (6.085 s), 32978 tokens 1389.8 tok/s (23.729 s), 61650 tokens 1345.7 tok/s (45.812 s) |
| memory-busy | measured: mac: System-wide memory free percentage: 14%; total = 3072.00M  us |

## 2026-10-24 14:06: run `20261024-140604-quick`

Plan quick, done; served as `MiniMax-M3.1-Flash`.

Serving: engine_commit `ec0c099de`; binary_sha256 `e3074abc85c644cd302a184a831347fe84922daf5959a36aed4f5bf6904f8706`; served_model `{"object": "list", "data": [{"id": "MiniMax-M3.1-Flash", "object": "model", "created": 179`; chip `Apple M5 Ultra; 274877906944`; suite_commit `277c842a1481`

### ruler-fresh

| streams | prose total (a stream) | code total (a stream) | structured total (a stream) | list total (a stream) | first token |
|---:|---:|---:|---:|---:|---:|
| 1 | 41.6 (41.6) | 65.1 (65.1) | 46.0 (46.0) | 56.3 (56.3) | 0.31-0.34 s |

Engine rounds (ruler-fresh):

| streams | tokens a round | drafts a round | accepted | ms a round | requests |
|---:|---:|---:|---:|---:|---:|
| 1 | 2.412 | 2.047 | 69% | 46.16 | 12 |

### ruler-after

| streams | prose total (a stream) | code total (a stream) | structured total (a stream) | list total (a stream) | first token |
|---:|---:|---:|---:|---:|---:|
| 1 | 41.7 (41.7) | 65.1 (65.1) | 47.2 (47.2) | 56.3 (56.3) | 0.31-0.33 s |

Engine rounds (ruler-after):

| streams | tokens a round | drafts a round | accepted | ms a round | requests |
|---:|---:|---:|---:|---:|---:|
| 1 | 2.414 | 2.083 | 68% | 45.93 | 13 |

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
| memory-idle | measured: mac: System-wide memory free percentage: 95%; total = 3072.00M  us |
| structured | pass: 18/18 obey, drafted == plain 12/12; a bad regex -> 400 |
| tools | pass: 5/5 tool cases right |
| sampling | pass: 9/9 seeded replies equal on repeat and undrafted; 0 errors |
| turns | pass: resumed == again: True; cold (after a restart): True; cached 4685 of 4826; ttft resumed 0.307s, cold 6.041s |
| urls | FAIL: public 400; loopback 400; http 400; unexpected: ['public'] |

## 2026-10-24 13:20: run `20261024-132010-quick`

Plan quick, done; served as `MiniMax-M3.1-Flash`.

Serving: engine_commit `90deb57b7`; binary_sha256 `79d22c1783a96bb722855d436f9c712224390890efce564122ee0ac666caea65`; served_model `{"object": "list", "data": [{"id": "MiniMax-M3.1-Flash", "object": "model", "created": 179`; chip `Apple M5 Ultra; 274877906944`; suite_commit `277c842a1481`

### ruler-fresh

| streams | prose total (a stream) | code total (a stream) | structured total (a stream) | list total (a stream) | first token |
|---:|---:|---:|---:|---:|---:|
| 1 | 41.6 (41.6) | 66.1 (66.1) | 47.2 (47.2) | 56.4 (56.4) | 0.32-0.34 s |

Engine rounds (ruler-fresh):

| streams | tokens a round | drafts a round | accepted | ms a round | requests |
|---:|---:|---:|---:|---:|---:|
| 1 | 2.469 | 2.104 | 70% | 46.75 | 12 |

### ruler-after

| streams | prose total (a stream) | code total (a stream) | structured total (a stream) | list total (a stream) | first token |
|---:|---:|---:|---:|---:|---:|
| 1 | 41.6 (41.6) | 65.0 (65.0) | 48.0 (48.0) | 56.1 (56.1) | 0.32-0.34 s |

Engine rounds (ruler-after):

| streams | tokens a round | drafts a round | accepted | ms a round | requests |
|---:|---:|---:|---:|---:|---:|
| 1 | 2.426 | 2.102 | 68% | 46.07 | 13 |

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
| memory-idle | measured: mac: System-wide memory free percentage: 15%; total = 3072.00M  us |
| structured | pass: 18/18 obey, drafted == plain 12/12; a bad regex -> 400 |
| tools | pass: 5/5 tool cases right |
| sampling | pass: 9/9 seeded replies equal on repeat and undrafted; 0 errors |
| turns | pass: resumed == again: True; cold (after a restart): True; cached 4685 of 4826; ttft resumed 0.312s, cold 6.069s |
| urls | FAIL: public 400; loopback 400; http 400; unexpected: ['public'] |

## 2026-10-24 05:59: run `20261024-055952-quick`

Plan quick, done; served as `MiniMax-M3.1-Flash`.

Serving: engine_commit `ba77394b8`; binary_sha256 `7c6092fb5ad8fd67650d56fd0984393e786f996b34a0f6ae660559af530ec696`; served_model `{"object": "list", "data": [{"id": "MiniMax-M3.1-Flash", "object": "model", "created": 179`; chip `Apple M5 Ultra; 274877906944`; suite_commit `277c842a1481`

### ruler-fresh

| streams | prose total (a stream) | code total (a stream) | structured total (a stream) | list total (a stream) | first token |
|---:|---:|---:|---:|---:|---:|
| 1 | 41.9 (41.9) | 65.2 (65.2) | 46.8 (46.8) | 56.5 (56.5) | 0.32-0.34 s |

Engine rounds (ruler-fresh):

| streams | tokens a round | drafts a round | accepted | ms a round | requests |
|---:|---:|---:|---:|---:|---:|

### ruler-after

| streams | prose total (a stream) | code total (a stream) | structured total (a stream) | list total (a stream) | first token |
|---:|---:|---:|---:|---:|---:|
| 1 | 41.8 (41.8) | 65.3 (65.3) | 46.1 (46.1) | 56.4 (56.4) | 0.32-0.34 s |

Engine rounds (ruler-after):

| streams | tokens a round | drafts a round | accepted | ms a round | requests |
|---:|---:|---:|---:|---:|---:|
| 1 | 2.45 | 2.152 | 67% | 46.74 | 13 |

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
| structured | pass: 18/18 obey, drafted == plain 12/12; a bad regex -> 400 |
| tools | pass: 5/5 tool cases right |
| sampling | pass: 9/9 seeded replies equal on repeat and undrafted; 0 errors |
| turns | pass: resumed == again: True; cold (after a restart): True; cached 4685 of 4826; ttft resumed 0.33s, cold 6.843s |
| urls | FAIL: public 400; loopback 400; http 400; unexpected: ['public'] |

## 2026-10-24 04:09: run `20261024-040956-quick`

Plan quick, done; served as `MiniMax-M3.1-Flash`.

Serving: engine_commit `904432fce`; binary_sha256 `b561127947134514a502efca419c70d18a48b4e892e9bd1019190d6bf541dfed`; served_model `{"object": "list", "data": [{"id": "MiniMax-M3.1-Flash", "object": "model", "created": 179`; chip `Apple M5 Ultra; 274877906944`; suite_commit `277c842a1481`

### ruler-fresh

| streams | prose total (a stream) | code total (a stream) | structured total (a stream) | list total (a stream) | first token |
|---:|---:|---:|---:|---:|---:|
| 1 | 42.5 (42.5) | 66.6 (66.6) | 47.7 (47.7) | 56.8 (56.8) | 0.32-0.34 s |

Engine rounds (ruler-fresh):

| streams | tokens a round | drafts a round | accepted | ms a round | requests |
|---:|---:|---:|---:|---:|---:|
| 1 | 2.416 | 2.034 | 69% | 45.25 | 12 |

### ruler-after

| streams | prose total (a stream) | code total (a stream) | structured total (a stream) | list total (a stream) | first token |
|---:|---:|---:|---:|---:|---:|
| 1 | 43.1 (43.1) | 65.6 (65.6) | 47.0 (47.0) | 56.7 (56.7) | 0.32-0.34 s |

Engine rounds (ruler-after):

| streams | tokens a round | drafts a round | accepted | ms a round | requests |
|---:|---:|---:|---:|---:|---:|
| 1 | 2.414 | 2.065 | 68% | 45.46 | 13 |

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
| memory-idle | measured: mac: System-wide memory free percentage: 96%; total = 5120.00M  us |
| structured | pass: 18/18 obey, drafted == plain 12/12; a bad regex -> 400 |
| tools | pass: 5/5 tool cases right |
| sampling | pass: 9/9 seeded replies equal on repeat and undrafted; 0 errors |
| turns | pass: resumed == again: True; cold (after a restart): True; cached 4685 of 4826; ttft resumed 0.323s, cold 6.563s |
| urls | FAIL: public 400; loopback 400; http 400; unexpected: ['public'] |

## 2026-10-24 03:49: run `20261024-034906-prefill-64k`

Plan prefill-64k, done; served as `MiniMax-M3.1-Flash`.

Serving: engine_commit `39746b53e`; binary_sha256 `d56e474b3cef52e1cdaf7383f9fb415098b778f688850572dbae187b27a728df`; served_model `{"object": "list", "data": [{"id": "MiniMax-M3.1-Flash", "object": "model", "created": 179`; chip `Apple M5 Ultra; 274877906944`; suite_commit `277c842a1481`

### checks

| check | result |
|---|---|
| memory-idle | measured: mac: System-wide memory free percentage: 83%; total = 5120.00M  us |
| prefill-off | measured: 2257 tokens 486.3 tok/s (4.641 s), 8404 tokens 1176.7 tok/s (7.142 s), 32978 tokens 1010.9 tok/s (32.622 s), 61655 tokens 886.3 tok/s (69.567 s) |
| prefill-thinking | measured: 2259 tokens 1142.1 tok/s (1.978 s), 8404 tokens 1167.9 tok/s (7.196 s), 32978 tokens 989.6 tok/s (33.324 s), 61649 tokens 892.3 tok/s (69.093 s) |
| memory-busy | measured: mac: System-wide memory free percentage: 15%; total = 4096.00M  us |

## 2026-10-23 21:17: run `20261023-211739-dsv41-quality-off`

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
| tools | 57/60 |
| json | 30/30 |
| ifeval | 86/150 |
| gsm8k | 241/250 |
| mgsm | 199/240 |
| mmlu | 284/342 |
| math500 | 454/500 |

### checks

| check | result |
|---|---|
| memory-idle | measured: mac: System-wide memory free percentage: 95%; total = 5120.00M  us |

## 2026-10-23 21:16: run `20261023-211601-structured`

Plan structured, done; served as `MiniMax-M3.1-Flash`.

Serving: engine_commit `da75eb499`; binary_sha256 `d56e474b3cef52e1cdaf7383f9fb415098b778f688850572dbae187b27a728df`; served_model `{"object": "list", "data": [{"id": "MiniMax-M3.1-Flash", "object": "model", "created": 179`; chip `Apple M5 Ultra; 274877906944`; suite_commit `277c842a1481`

### checks

| check | result |
|---|---|
| structured | pass: 18/18 obey, drafted == plain 12/12; a bad regex -> 400 |
| tools | pass: 5/5 tool cases right |

## 2026-10-23 21:07: run `20261023-210731-structured`

Plan structured, done; served as `MiniMax-M3.1-Flash`.

Serving: engine_commit `da75eb499`; binary_sha256 `a006db43cc1d3157720d9111d4048faac3d99dd41660019183fe281041db13cd`; served_model `{"object": "list", "data": [{"id": "MiniMax-M3.1-Flash", "object": "model", "created": 179`; chip `Apple M5 Ultra; 274877906944`; suite_commit `277c842a1481`

### checks

| check | result |
|---|---|
| structured | pass: 18/18 obey, drafted == plain 12/12; a bad regex -> 400 |
| tools | FAIL: 3/5 tool cases right; failed named (calls ['book_flight', 'book_flight', 'book_flight', 'book_flight', 'book_flight', 'book_flight', 'book_flight', 'book_flight']); named/stream (calls ['book_flight', 'book_flight', 'book_flight', 'book_flight', 'book_flight', 'book_flight', 'book_flight', 'book_flight']) |

## 2026-10-23 21:01: run `20261023-210120-mlx-speed`

Plan mlx-speed, done; served as `MiniMax-M3.1-Flash`.

Serving: engine_commit `da75eb499`; binary_sha256 `a006db43cc1d3157720d9111d4048faac3d99dd41660019183fe281041db13cd`; served_model `{"object": "list", "data": [{"id": "MiniMax-M3.1-Flash", "object": "model", "created": 179`; chip `Apple M5 Ultra; 274877906944`; suite_commit `277c842a1481`

### ruler-streams

| streams | prose total (a stream) | code total (a stream) | structured total (a stream) | list total (a stream) | first token |
|---:|---:|---:|---:|---:|---:|
| 1 | 43.4 (43.4) | 43.3 (43.3) | 43.4 (43.4) | 43.5 (43.5) | 0.33-0.35 s |
| 2 | 62.2 (31.1) | 61.6 (30.8) | 61.8 (30.9) | 62.1 (31.1) | 0.50-0.53 s |
| 4 | 123.7 (30.9) | 122.0 (30.7) | 125.3 (31.9) | 123.6 (30.7) | 3.72-4.88 s |

Engine rounds (ruler-streams):

| streams | tokens a round | drafts a round | accepted | ms a round | requests |
|---:|---:|---:|---:|---:|---:|
| 1 | 1.004 | 0.0 |  | 23.14 | 12 |
| 2 | 1.004 | 0.0 |  | 32.43 | 25 |
| 4 | 1.005 | 0.0 |  | 32.33 | 50 |

### checks

| check | result |
|---|---|
| memory-idle | measured: mac: System-wide memory free percentage: 95%; total = 6144.00M  us |

## 2026-10-23 20:59: run `20261023-205954-mlx-speed`

Plan mlx-speed, aborted: the server died during ruler-streams; its result is discarded; served as `MiniMax-M3.1-Flash`.

Serving: engine_commit `da75eb499`; binary_sha256 `a006db43cc1d3157720d9111d4048faac3d99dd41660019183fe281041db13cd`; served_model `{"object": "list", "data": [{"id": "MiniMax-M3.1-Flash", "object": "model", "created": 179`; chip `Apple M5 Ultra; 274877906944`; suite_commit `277c842a1481`

### checks

| check | result |
|---|---|
| memory-idle | measured: mac: System-wide memory free percentage: 92%; total = 5120.00M  us |

## 2026-10-23 20:52: run `20261023-205238-speed`

Plan speed, done; served as `MiniMax-M3.1-Flash`.

Serving: engine_commit `da75eb499`; binary_sha256 `a006db43cc1d3157720d9111d4048faac3d99dd41660019183fe281041db13cd`; served_model `{"object": "list", "data": [{"id": "MiniMax-M3.1-Flash", "object": "model", "created": 179`; chip `Apple M5 Ultra; 274877906944`; suite_commit `277c842a1481`

### ruler-fresh

| streams | prose total (a stream) | code total (a stream) | structured total (a stream) | list total (a stream) | first token |
|---:|---:|---:|---:|---:|---:|
| 1 | 42.1 (42.1) | 65.9 (65.9) | 47.5 (47.5) | 56.8 (56.8) | 0.32-0.34 s |
| 2 | 49.7 (24.9) | 65.8 (32.9) | 53.9 (26.9) | 76.1 (38.0) | 0.48-0.51 s |

Engine rounds (ruler-fresh):

| streams | tokens a round | drafts a round | accepted | ms a round | requests |
|---:|---:|---:|---:|---:|---:|
| 1 | 2.427 | 2.076 | 69% | 45.7 | 12 |
| 2 | 2.21 | 1.626 | 74% | 72.03 | 25 |

### ruler-after

| streams | prose total (a stream) | code total (a stream) | structured total (a stream) | list total (a stream) | first token |
|---:|---:|---:|---:|---:|---:|
| 1 | 42.0 (42.0) | 66.6 (66.6) | 46.5 (46.5) | 56.7 (56.7) | 0.32-0.34 s |

Engine rounds (ruler-after):

| streams | tokens a round | drafts a round | accepted | ms a round | requests |
|---:|---:|---:|---:|---:|---:|
| 1 | 2.452 | 2.152 | 67% | 46.29 | 13 |

### checks

| check | result |
|---|---|
| memory-idle | measured: mac: System-wide memory free percentage: 16%; total = 5120.00M  us |
| turns | pass: resumed == again: True; cold (after a restart): True; cached 4685 of 4826; ttft resumed 0.325s, cold 4.248s |
| memory-busy | measured: mac: System-wide memory free percentage: 16%; total = 5120.00M  us |

## 2026-10-23 20:28: run `20261023-202804-speed`

Plan speed, aborted: minimax-m31-mix34-m5 never came up after 1 starts; served as `MiniMax-M3.1-Flash`.

Serving: engine_commit `c32d30c4f`; binary_sha256 `a006db43cc1d3157720d9111d4048faac3d99dd41660019183fe281041db13cd`; served_model `{"object": "list", "data": [{"id": "MiniMax-M3.1-Flash", "object": "model", "created": 179`; chip `Apple M5 Ultra; 274877906944`; suite_commit `277c842a1481`

### ruler-fresh

| streams | prose total (a stream) | code total (a stream) | structured total (a stream) | list total (a stream) | first token |
|---:|---:|---:|---:|---:|---:|
| 1 | 41.9 (41.9) | 64.3 (64.3) | 46.8 (46.8) | 56.4 (56.4) | 0.32-0.34 s |
| 2 | 49.8 (24.9) | 64.8 (32.4) | 54.2 (27.1) | 74.2 (37.1) | 0.48-0.51 s |

Engine rounds (ruler-fresh):

| streams | tokens a round | drafts a round | accepted | ms a round | requests |
|---:|---:|---:|---:|---:|---:|
| 1 | 2.442 | 2.113 | 68% | 46.64 | 12 |
| 2 | 2.217 | 1.629 | 74% | 72.98 | 25 |

### checks

| check | result |
|---|---|
| memory-idle | measured: mac: System-wide memory free percentage: 94%; total = 5120.00M  us |

