# Spark-X2.6-4B, MLX 8-bit on 1x Apple M5 Ultra (256 GB unified), macOS

Target `spark-x26-4b-8bit-m5`: Spark-X2.6-4B MLX affine 8-bit (a lossy conversion of the release), TensorFold native Metal (spark2_5) on one M5 Ultra (262144-token window, 4 streams). Engine: TensorFold native, Metal. Rendered from `stats/spark-x26-4b-8bit-m5.json` (8 runs); aggregate tok/s, total (a stream).

## 2026-10-30 10:23: run `20261030-102337-mlx-speed`

Plan mlx-speed, done; served as `spark`.

Serving: engine_commit `abf822585`; binary_sha256 `e247c861a8095bc38f326a3741ee88854b32e3ec23235a1e6bb4fb08bb75276e`; served_model `{"object": "list", "data": [{"id": "spark", "object": "model", "created": 1793373817, "own`; chip `Apple M5 Ultra; 274877906944`; suite_commit `21db9b23f7be`

### ruler-streams

| streams | prose total (a stream) | code total (a stream) | structured total (a stream) | list total (a stream) | first token |
|---:|---:|---:|---:|---:|---:|
| 1 | 165.8 (165.8) | 165.9 (165.9) | 165.9 (165.9) | 165.7 (165.7) | 0.04-0.06 s |
| 2 | 261.7 (130.9) | 259.2 (129.6) | 267.9 (133.9) | 263.3 (131.6) | 0.05-0.08 s |
| 4 | 366.5 (91.2) | 353.4 (88.4) | 368.0 (92.1) | 362.5 (90.2) | 0.09-0.13 s |

Engine rounds (ruler-streams):

| streams | tokens a round | drafts a round | accepted | ms a round | requests |
|---:|---:|---:|---:|---:|---:|
| 1 | 1.005 | 0.0 |  | 6.06 | 13 |
| 2 | 1.01 | 0.034 | 15% | 7.68 | 25 |
| 4 | 1.008 | 0.021 | 15% | 11.13 | 50 |

### checks

| check | result |
|---|---|
| memory-idle | measured: mac: System-wide memory free percentage: 89%; total = 3072.00M  us |

## 2026-10-30 10:22: run `20261030-102210-prefill`

Plan prefill, done; served as `spark`.

Serving: engine_commit `abf822585`; binary_sha256 `e247c861a8095bc38f326a3741ee88854b32e3ec23235a1e6bb4fb08bb75276e`; served_model `{"object": "list", "data": [{"id": "spark", "object": "model", "created": 1793373738, "own`; chip `Apple M5 Ultra; 274877906944`; suite_commit `21db9b23f7be`

### checks

| check | result |
|---|---|
| memory-idle | measured: mac: System-wide memory free percentage: 92%; total = 3072.00M  us |
| prefill-off | measured: 2337 tokens 8258.0 tok/s (0.283 s), 9396 tokens 9266.3 tok/s (1.014 s), 37247 tokens 7766.3 tok/s (4.796 s), 148571 tokens 4576.5 tok/s (32.464 s) |
| prefill-thinking | measured: 2416 tokens 8628.6 tok/s (0.28 s), 9363 tokens 9161.4 tok/s (1.022 s), 37194 tokens 7705.4 tok/s (4.827 s), 148570 tokens 4520.1 tok/s (32.869 s) |
| memory-busy | measured: mac: System-wide memory free percentage: 88%; total = 3072.00M  us |

## 2026-10-30 10:20: run `20261030-102058-speed`

Plan speed, done; served as `spark`.

Serving: engine_commit `abf822585`; binary_sha256 `e247c861a8095bc38f326a3741ee88854b32e3ec23235a1e6bb4fb08bb75276e`; served_model `{"object": "list", "data": [{"id": "spark", "object": "model", "created": 1793373666, "own`; chip `Apple M5 Ultra; 274877906944`; suite_commit `21db9b23f7be`

### ruler-fresh

| streams | prose total (a stream) | code total (a stream) | structured total (a stream) | list total (a stream) | first token |
|---:|---:|---:|---:|---:|---:|
| 1 | 166.4 (166.4) | 166.3 (166.3) | 166.2 (166.2) | 166.2 (166.2) | 0.04-0.05 s |
| 2 | 265.2 (132.6) | 258.6 (129.3) | 268.6 (134.3) | 263.6 (131.8) | 0.05-0.08 s |

Engine rounds (ruler-fresh):

| streams | tokens a round | drafts a round | accepted | ms a round | requests |
|---:|---:|---:|---:|---:|---:|
| 1 | 1.005 | 0.0 |  | 6.04 | 12 |
| 2 | 1.01 | 0.033 | 15% | 7.65 | 26 |

### ruler-after

| streams | prose total (a stream) | code total (a stream) | structured total (a stream) | list total (a stream) | first token |
|---:|---:|---:|---:|---:|---:|
| 1 | 165.9 (165.9) | 165.7 (165.7) | 165.6 (165.6) | 166.1 (166.1) | 0.04-0.06 s |

Engine rounds (ruler-after):

| streams | tokens a round | drafts a round | accepted | ms a round | requests |
|---:|---:|---:|---:|---:|---:|
| 1 | 1.005 | 0.006 | 7% | 6.06 | 13 |

### checks

| check | result |
|---|---|
| memory-idle | measured: mac: System-wide memory free percentage: 92%; total = 3072.00M  us |
| turns | pass: resumed == again: True; cold (after a restart): True; cached 5499 of 5630; ttft resumed 0.052s, cold 0.642s |
| memory-busy | measured: mac: System-wide memory free percentage: 92%; total = 3072.00M  us |

## 2026-10-30 10:17: run `20261030-101706-quick`

Plan quick, done; served as `spark`.

Serving: engine_commit `abf822585`; binary_sha256 `e247c861a8095bc38f326a3741ee88854b32e3ec23235a1e6bb4fb08bb75276e`; served_model `{"object": "list", "data": [{"id": "spark", "object": "model", "created": 1793373434, "own`; chip `Apple M5 Ultra; 274877906944`; suite_commit `21db9b23f7be`

### ruler-fresh

| streams | prose total (a stream) | code total (a stream) | structured total (a stream) | list total (a stream) | first token |
|---:|---:|---:|---:|---:|---:|
| 1 | 165.3 (165.3) | 165.6 (165.6) | 165.7 (165.7) | 165.8 (165.8) | 0.04-0.06 s |

Engine rounds (ruler-fresh):

| streams | tokens a round | drafts a round | accepted | ms a round | requests |
|---:|---:|---:|---:|---:|---:|
| 1 | 1.005 | 0.0 |  | 6.07 | 12 |

### ruler-after

| streams | prose total (a stream) | code total (a stream) | structured total (a stream) | list total (a stream) | first token |
|---:|---:|---:|---:|---:|---:|
| 1 | 165.6 (165.6) | 165.9 (165.9) | 165.9 (165.9) | 165.6 (165.6) | 0.04-0.05 s |

Engine rounds (ruler-after):

| streams | tokens a round | drafts a round | accepted | ms a round | requests |
|---:|---:|---:|---:|---:|---:|
| 1 | 1.005 | 0.006 | 7% | 6.07 | 13 |

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
| memory-idle | measured: mac: System-wide memory free percentage: 93%; total = 3072.00M  us |
| structured | pass: 18/18 obey, drafted == plain 12/12; a bad regex -> 400 |
| tools | pass: 5/5 tool cases right |
| sampling | pass: 9/9 seeded replies equal on repeat and undrafted; 0 errors |
| turns | pass: resumed == again: True; cold (after a restart): True; cached 5499 of 5630; ttft resumed 0.049s, cold 0.648s |

## 2026-10-25 18:00: run `20261025-180037-mlx-speed`

Plan mlx-speed, done; served as `spark`.

Serving: engine_commit `cc840195e`; binary_sha256 `5a20c6f0cb2289384f0deda99840d9acc01d10766beea0cfb1d1de78e938be46`; served_model `{"object": "list", "data": [{"id": "spark", "object": "model", "created": 1792969237, "own`; chip `Apple M5 Ultra; 274877906944`; suite_commit `277c842a1481`

### ruler-streams

| streams | prose total (a stream) | code total (a stream) | structured total (a stream) | list total (a stream) | first token |
|---:|---:|---:|---:|---:|---:|
| 1 | 167.1 (167.1) | 167.0 (167.0) | 166.9 (166.9) | 167.1 (167.1) | 0.03-0.05 s |
| 2 | 267.6 (133.8) | 260.8 (130.4) | 272.0 (136.0) | 265.4 (132.7) | 0.05-0.08 s |
| 4 | 368.3 (92.1) | 354.6 (88.6) | 369.6 (93.3) | 364.3 (90.5) | 0.09-0.13 s |

Engine rounds (ruler-streams):

| streams | tokens a round | drafts a round | accepted | ms a round | requests |
|---:|---:|---:|---:|---:|---:|
| 1 | 1.005 | 0.0 |  | 6.02 | 12 |
| 2 | 1.01 | 0.034 | 15% | 7.58 | 25 |
| 4 | 1.008 | 0.021 | 15% | 11.06 | 50 |

### checks

| check | result |
|---|---|
| memory-idle | measured: mac: System-wide memory free percentage: 93%; total = 3072.00M  us |

## 2026-10-25 17:59: run `20261025-175905-prefill`

Plan prefill, done; served as `spark`.

Serving: engine_commit `cc840195e`; binary_sha256 `5a20c6f0cb2289384f0deda99840d9acc01d10766beea0cfb1d1de78e938be46`; served_model `{"object": "list", "data": [{"id": "spark", "object": "model", "created": 1792969153, "own`; chip `Apple M5 Ultra; 274877906944`; suite_commit `277c842a1481`

### checks

| check | result |
|---|---|
| memory-idle | measured: mac: System-wide memory free percentage: 93%; total = 3072.00M  us |
| prefill-off | measured: 2382 tokens 8270.8 tok/s (0.288 s), 9333 tokens 9258.9 tok/s (1.008 s), 37307 tokens 7759.4 tok/s (4.808 s), 148507 tokens 4584.0 tok/s (32.397 s) |
| prefill-thinking | measured: 2407 tokens 8535.5 tok/s (0.282 s), 9396 tokens 9202.7 tok/s (1.021 s), 37153 tokens 7679.4 tok/s (4.838 s), 148591 tokens 4564.9 tok/s (32.551 s) |
| memory-busy | measured: mac: System-wide memory free percentage: 88%; total = 3072.00M  us |

## 2026-10-25 17:57: run `20261025-175753-speed`

Plan speed, done; served as `spark`.

Serving: engine_commit `cc840195e`; binary_sha256 `5a20c6f0cb2289384f0deda99840d9acc01d10766beea0cfb1d1de78e938be46`; served_model `{"object": "list", "data": [{"id": "spark", "object": "model", "created": 1792969081, "own`; chip `Apple M5 Ultra; 274877906944`; suite_commit `277c842a1481`

### ruler-fresh

| streams | prose total (a stream) | code total (a stream) | structured total (a stream) | list total (a stream) | first token |
|---:|---:|---:|---:|---:|---:|
| 1 | 166.4 (166.4) | 166.6 (166.6) | 166.6 (166.6) | 166.4 (166.4) | 0.04-0.05 s |
| 2 | 265.6 (132.8) | 259.3 (129.6) | 269.0 (134.5) | 263.9 (131.9) | 0.05-0.08 s |

Engine rounds (ruler-fresh):

| streams | tokens a round | drafts a round | accepted | ms a round | requests |
|---:|---:|---:|---:|---:|---:|
| 1 | 1.005 | 0.0 |  | 6.03 | 12 |
| 2 | 1.01 | 0.033 | 15% | 7.64 | 26 |

### ruler-after

| streams | prose total (a stream) | code total (a stream) | structured total (a stream) | list total (a stream) | first token |
|---:|---:|---:|---:|---:|---:|
| 1 | 166.9 (166.9) | 167.2 (167.2) | 166.8 (166.8) | 166.9 (166.9) | 0.04-0.05 s |

Engine rounds (ruler-after):

| streams | tokens a round | drafts a round | accepted | ms a round | requests |
|---:|---:|---:|---:|---:|---:|
| 1 | 1.005 | 0.006 | 7% | 6.02 | 13 |

### checks

| check | result |
|---|---|
| memory-idle | measured: mac: System-wide memory free percentage: 92%; total = 3072.00M  us |
| turns | pass: resumed == again: True; cold (after a restart): True; cached 5499 of 5630; ttft resumed 0.05s, cold 0.644s |
| memory-busy | measured: mac: System-wide memory free percentage: 92%; total = 3072.00M  us |

## 2026-10-25 17:54: run `20261025-175402-quick`

Plan quick, done; served as `spark`.

Serving: engine_commit `cc840195e`; binary_sha256 `5a20c6f0cb2289384f0deda99840d9acc01d10766beea0cfb1d1de78e938be46`; served_model `{"object": "list", "data": [{"id": "spark", "object": "model", "created": 1792968850, "own`; chip `Apple M5 Ultra; 274877906944`; suite_commit `277c842a1481`

### ruler-fresh

| streams | prose total (a stream) | code total (a stream) | structured total (a stream) | list total (a stream) | first token |
|---:|---:|---:|---:|---:|---:|
| 1 | 167.7 (167.7) | 167.7 (167.7) | 167.6 (167.6) | 167.5 (167.5) | 0.04-0.06 s |

Engine rounds (ruler-fresh):

| streams | tokens a round | drafts a round | accepted | ms a round | requests |
|---:|---:|---:|---:|---:|---:|
| 1 | 1.005 | 0.0 |  | 5.99 | 12 |

### ruler-after

| streams | prose total (a stream) | code total (a stream) | structured total (a stream) | list total (a stream) | first token |
|---:|---:|---:|---:|---:|---:|
| 1 | 166.7 (166.7) | 166.9 (166.9) | 166.8 (166.8) | 166.8 (166.8) | 0.04-0.05 s |

Engine rounds (ruler-after):

| streams | tokens a round | drafts a round | accepted | ms a round | requests |
|---:|---:|---:|---:|---:|---:|
| 1 | 1.005 | 0.006 | 7% | 6.03 | 13 |

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
| memory-idle | measured: mac: System-wide memory free percentage: 93%; total = 3072.00M  us |
| structured | pass: 18/18 obey, drafted == plain 12/12; a bad regex -> 400 |
| tools | pass: 5/5 tool cases right |
| sampling | pass: 9/9 seeded replies equal on repeat and undrafted; 0 errors |
| turns | pass: resumed == again: True; cold (after a restart): True; cached 5499 of 5630; ttft resumed 0.05s, cold 0.653s |

