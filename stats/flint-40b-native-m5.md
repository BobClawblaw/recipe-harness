# Recursive Flint 40B-A2.5B, MLX INT4 (g64) on 1x Apple M5 Ultra (256 GB unified), macOS

Target `flint-40b-native-m5`: Recursive Flint 40B-A2.5B, MLX INT4 (g64), TensorFold native Metal on one M5 Ultra. Engine: TensorFold native, Metal. Rendered from `stats/flint-40b-native-m5.json` (23 runs); aggregate tok/s, total (a stream).

## 2026-10-28 03:39: run `20261028-033917-quick`

Plan quick, running; served as `flint`.

Serving: engine_commit `664b488f3`; binary_sha256 `28c72363d214426aca770700842704ab2c8072d5469adc13a2cbdd8e1688453e`; served_model `{"object": "list", "data": [{"id": "flint", "object": "model", "created": 1793176765, "own`; chip `Apple M5 Ultra; 274877906944`; suite_commit `21db9b23f7be`

### ruler-fresh

| streams | prose total (a stream) | code total (a stream) | structured total (a stream) | list total (a stream) | first token |
|---:|---:|---:|---:|---:|---:|
| 1 | 183.7 (183.7) | 179.0 (179.0) | 193.5 (193.5) | 180.1 (180.1) | 0.03-0.04 s |

Engine rounds (ruler-fresh):

| streams | tokens a round | drafts a round | accepted | ms a round | requests |
|---:|---:|---:|---:|---:|---:|
| 1 | 1.044 | 0.076 | 52% | 5.67 | 12 |

### checks

| check | result |
|---|---|
| memory-idle | measured: mac: System-wide memory free percentage: 86%; total = 4096.00M  us |
| structured | pass: 18/18 obey, drafted == plain 12/12; a bad regex -> 400 |
| tools | pass: 5/5 tool cases right |

## 2026-10-28 01:33: run `20261028-013334-quick`

Plan quick, done; served as `flint`.

Serving: engine_commit `764489e83`; binary_sha256 `b1f534e906d2234474f32a3c995f005980fa46d22e0ac508578d0ef1ac0e9865`; served_model `{"object": "list", "data": [{"id": "flint", "object": "model", "created": 1793169222, "own`; chip `Apple M5 Ultra; 274877906944`; suite_commit `21db9b23f7be`

### ruler-fresh

| streams | prose total (a stream) | code total (a stream) | structured total (a stream) | list total (a stream) | first token |
|---:|---:|---:|---:|---:|---:|
| 1 | 17.8 (17.8) | 171.7 (171.7) | 188.4 (188.4) | 173.9 (173.9) | 0.03-0.28 s |

Engine rounds (ruler-fresh):

| streams | tokens a round | drafts a round | accepted | ms a round | requests |
|---:|---:|---:|---:|---:|---:|
| 1 | 1.044 | 0.076 | 52% | 7.57 | 12 |

### ruler-after

| streams | prose total (a stream) | code total (a stream) | structured total (a stream) | list total (a stream) | first token |
|---:|---:|---:|---:|---:|---:|
| 1 | 17.8 (17.8) | 17.5 (17.5) | 18.5 (18.5) | 14.7 (14.7) | 0.24-0.28 s |

Engine rounds (ruler-after):

| streams | tokens a round | drafts a round | accepted | ms a round | requests |
|---:|---:|---:|---:|---:|---:|
| 1 | 1.047 | 0.081 | 52% | 61.14 | 13 |

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
| copy | 1/2 |
| max-tokens | 3/3 |

### checks

| check | result |
|---|---|
| memory-idle | measured: mac: System-wide memory free percentage: 83%; total = 4096.00M  us |
| structured | pass: 18/18 obey, drafted == plain 12/12; a bad regex -> 400 |
| tools | pass: 5/5 tool cases right |
| sampling | pass: 9/9 seeded replies equal on repeat and undrafted; 0 errors |
| turns | pass: resumed == again: True; cold (after a restart): True; cached 4507 of 4627; ttft resumed 0.07s, cold 4.122s |
| urls | FAIL: public 400; loopback 400; http 400; unexpected: ['public'] |

## 2026-10-28 00:53: run `20261028-005329-quick`

Plan quick, done; served as `flint`.

Serving: engine_commit `40e1403b8`; binary_sha256 `071967bcb5df502d03058c5d1fdaaef3d80cd2a06383885ac4fcf06a92890445`; served_model `{"object": "list", "data": [{"id": "flint", "object": "model", "created": 1793166818, "own`; chip `Apple M5 Ultra; 274877906944`; suite_commit `a7ba7e392d57-dirty`

### ruler-fresh

| streams | prose total (a stream) | code total (a stream) | structured total (a stream) | list total (a stream) | first token |
|---:|---:|---:|---:|---:|---:|
| 1 | 6297.6 (6297.6) | 1284.1 (1284.1) | 1363.5 (1363.5) | 3194.0 (3194.0) | 1.80-8.69 s |

Engine rounds (ruler-fresh):

| streams | tokens a round | drafts a round | accepted | ms a round | requests |
|---:|---:|---:|---:|---:|---:|
| 1 | 1.591 | 0.698 | 84% | 0.52 | 12 |

### ruler-after

| streams | prose total (a stream) | code total (a stream) | structured total (a stream) | list total (a stream) | first token |
|---:|---:|---:|---:|---:|---:|
| 1 | 6300.4 (6300.4) | 1280.6 (1280.6) | 1362.2 (1362.2) | 3212.2 (3212.2) | 1.82-8.72 s |

Engine rounds (ruler-after):

| streams | tokens a round | drafts a round | accepted | ms a round | requests |
|---:|---:|---:|---:|---:|---:|
| 1 | 1.585 | 0.692 | 84% | 0.52 | 13 |

### suite

| check | passed |
|---|---:|
| soak | 60/60 |
| drafts | 12/12 |
| concurrent | 12/12 |
| streaming | 4/4 |
| multiturn | 8/8 |
| stop | 0/3 |
| thinking | 10/10 |
| copy | 1/2 |
| max-tokens | 0/3 |

### checks

| check | result |
|---|---|
| memory-idle | measured: mac: System-wide memory free percentage: 87%; total = 4096.00M  us |
| structured | pass: 18/18 obey, drafted == plain 12/12; a bad regex -> 400 |
| tools | pass: 5/5 tool cases right |
| sampling | pass: 9/9 seeded replies equal on repeat and undrafted; 0 errors |
| turns | pass: resumed == again: True; cold (after a restart): True; cached 4507 of 4592; ttft resumed 0.577s, cold 1.217s |
| urls | FAIL: public 400; loopback 400; http 400; unexpected: ['public'] |

## 2026-10-28 00:47: run `20261028-004730-together`

Plan together, done; served as `flint`.

Serving: engine_commit `2052603f5`; binary_sha256 `071967bcb5df502d03058c5d1fdaaef3d80cd2a06383885ac4fcf06a92890445`; served_model `{"object": "list", "data": [{"id": "flint", "object": "model", "created": 1793166458, "own`; chip `Apple M5 Ultra; 274877906944`; suite_commit `a7ba7e392d57-dirty`

### suite-together

| check | passed |
|---|---:|
| concurrent | 12/12 |
| drafts | 12/12 |

## 2026-10-28 00:41: run `20261028-004159-quick`

Plan quick, done; served as `flint`.

Serving: engine_commit `2052603f5`; binary_sha256 `071967bcb5df502d03058c5d1fdaaef3d80cd2a06383885ac4fcf06a92890445`; served_model `{"object": "list", "data": [{"id": "flint", "object": "model", "created": 1793166127, "own`; chip `Apple M5 Ultra; 274877906944`; suite_commit `a7ba7e392d57-dirty`

### ruler-fresh

| streams | prose total (a stream) | code total (a stream) | structured total (a stream) | list total (a stream) | first token |
|---:|---:|---:|---:|---:|---:|
| 1 | - | - | - | - | 1.39-1.55 s |

Engine rounds (ruler-fresh):

| streams | tokens a round | drafts a round | accepted | ms a round | requests |
|---:|---:|---:|---:|---:|---:|
| 1 | 1.044 | 0.076 | 52% |  | 12 |

### ruler-after

| streams | prose total (a stream) | code total (a stream) | structured total (a stream) | list total (a stream) | first token |
|---:|---:|---:|---:|---:|---:|
| 1 | - | - | - | - | 1.37-1.48 s |

Engine rounds (ruler-after):

| streams | tokens a round | drafts a round | accepted | ms a round | requests |
|---:|---:|---:|---:|---:|---:|
| 1 | 1.043 | 0.075 | 52% |  | 13 |

### suite

| check | passed |
|---|---:|
| soak | 60/60 |
| drafts | 12/12 |
| concurrent | 12/12 |
| streaming | 4/4 |
| multiturn | 0/8 |
| stop | 0/3 |
| thinking | 10/10 |
| copy | 1/2 |
| max-tokens | 3/3 |

### checks

| check | result |
|---|---|
| memory-idle | measured: mac: System-wide memory free percentage: 87%; total = 4096.00M  us |
| structured | pass: 18/18 obey, drafted == plain 12/12; a bad regex -> 400 |
| tools | pass: 5/5 tool cases right |
| sampling | pass: 9/9 seeded replies equal on repeat and undrafted; 0 errors |
| turns | pass: resumed == again: True; cold (after a restart): True; cached 4507 of 4529; ttft resumed Nones, cold Nones |
| urls | FAIL: public 400; loopback 400; http 400; unexpected: ['public'] |

## 2026-10-27 21:31: run `20261027-213155-quality-off`

Plan quality-off, done; served as `flint`.

Serving: engine_commit `a011f1c4a`; binary_sha256 `7da93990044c5eb2f6a33d770136e8b4a4070899fad7c63027974a492cf0130b`; served_model `{"object": "list", "data": [{"id": "flint", "object": "model", "created": 1793154723, "own`; chip `Apple M5 Ultra; 274877906944`; suite_commit `a7ba7e392d57-dirty`

### ruler-fresh

| streams | prose total (a stream) | code total (a stream) | structured total (a stream) | list total (a stream) | first token |
|---:|---:|---:|---:|---:|---:|
| 1 | 181.6 (181.6) | 176.3 (176.3) | 190.9 (190.9) | 202.7 (202.7) | 0.03-0.04 s |

Engine rounds (ruler-fresh):

| streams | tokens a round | drafts a round | accepted | ms a round | requests |
|---:|---:|---:|---:|---:|---:|
| 1 | 1.085 | 0.133 | 60% | 5.77 | 12 |

### ruler-after

| streams | prose total (a stream) | code total (a stream) | structured total (a stream) | list total (a stream) | first token |
|---:|---:|---:|---:|---:|---:|
| 1 | 182.2 (182.2) | 175.6 (175.6) | 191.7 (191.7) | 203.5 (203.5) | 0.03-0.04 s |

Engine rounds (ruler-after):

| streams | tokens a round | drafts a round | accepted | ms a round | requests |
|---:|---:|---:|---:|---:|---:|
| 1 | 1.083 | 0.142 | 56% | 5.75 | 16 |

### suite

| check | passed |
|---|---:|
| drafts | 12/12 |
| streaming | 4/4 |
| multiturn | 8/8 |
| stop | 3/3 |
| thinking | 10/10 |
| copy | 1/2 |
| max-tokens | 3/3 |
| tools | 52/60 |
| json | 29/30 |
| ifeval | 91/150 |
| gsm8k | 226/250 |
| mgsm | 182/240 |
| mmlu | 237/342 |
| math500 | 425/500 |
| gpqa | 85/198 |
| humaneval | 0/0 |
| repetition | 2/8 |
| long-context | 0/55 |
| long-tasks | 3/52 |
| soak | 60/60 |
| snapshot | 12/12 |
| vision | 0/6 |
| docvision | 0/0 |
| concurrent | 12/12 |
| vision-concurrent | 0/0 |

## 2026-10-27 21:03: run `20261027-210306-together`

Plan together, done; served as `flint`.

Serving: engine_commit `c0d0c5424`; binary_sha256 `868fb3db38a83b4a7a56f6fbc9c6ff9d36dfd23b00ca9983e2f0f7bc16e44acf`; served_model `{"object": "list", "data": [{"id": "flint", "object": "model", "created": 1793152994, "own`; chip `Apple M5 Ultra; 274877906944`; suite_commit `a7ba7e392d57-dirty`

### suite-together

| check | passed |
|---|---:|
| concurrent | 12/12 |
| drafts | 12/12 |

## 2026-10-27 20:58: run `20261027-205816-quick`

Plan quick, done; served as `flint`.

Serving: engine_commit `c0d0c5424`; binary_sha256 `868fb3db38a83b4a7a56f6fbc9c6ff9d36dfd23b00ca9983e2f0f7bc16e44acf`; served_model `{"object": "list", "data": [{"id": "flint", "object": "model", "created": 1793152704, "own`; chip `Apple M5 Ultra; 274877906944`; suite_commit `a7ba7e392d57-dirty`

### ruler-fresh

| streams | prose total (a stream) | code total (a stream) | structured total (a stream) | list total (a stream) | first token |
|---:|---:|---:|---:|---:|---:|
| 1 | 183.4 (183.4) | 178.5 (178.5) | 193.1 (193.1) | 179.6 (179.6) | 0.03-0.04 s |

Engine rounds (ruler-fresh):

| streams | tokens a round | drafts a round | accepted | ms a round | requests |
|---:|---:|---:|---:|---:|---:|
| 1 | 1.044 | 0.076 | 52% | 5.68 | 12 |

### ruler-after

| streams | prose total (a stream) | code total (a stream) | structured total (a stream) | list total (a stream) | first token |
|---:|---:|---:|---:|---:|---:|
| 1 | 183.2 (183.2) | 177.9 (177.9) | 192.5 (192.5) | 179.6 (179.6) | 0.03-0.04 s |

Engine rounds (ruler-after):

| streams | tokens a round | drafts a round | accepted | ms a round | requests |
|---:|---:|---:|---:|---:|---:|
| 1 | 1.047 | 0.081 | 52% | 5.71 | 13 |

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
| copy | 1/2 |
| max-tokens | 3/3 |

### checks

| check | result |
|---|---|
| memory-idle | measured: mac: System-wide memory free percentage: 87%; total = 4096.00M  us |
| structured | pass: 18/18 obey, drafted == plain 12/12; a bad regex -> 400 |
| tools | pass: 5/5 tool cases right |
| sampling | pass: 9/9 seeded replies equal on repeat and undrafted; 0 errors |
| turns | pass: resumed == again: True; cold (after a restart): True; cached 4507 of 4627; ttft resumed 0.066s, cold 0.712s |
| urls | FAIL: public 400; loopback 400; http 400; unexpected: ['public'] |

## 2026-10-25 08:00: run `20261025-080039-quick`

Plan quick, done; served as `flint`.

Serving: engine_commit `a011f1c4a`; binary_sha256 `f7f6a57a319a9aef9b424395d9ad5bdf7ecc658934a3981c51afd76ca1dcbeb6`; served_model `{"object": "list", "data": [{"id": "flint", "object": "model", "created": 1792933247, "own`; chip `Apple M5 Ultra; 274877906944`; suite_commit `277c842a1481`

### ruler-fresh

| streams | prose total (a stream) | code total (a stream) | structured total (a stream) | list total (a stream) | first token |
|---:|---:|---:|---:|---:|---:|
| 1 | 184.1 (184.1) | 177.8 (177.8) | 193.8 (193.8) | 205.3 (205.3) | 0.03-0.04 s |

Engine rounds (ruler-fresh):

| streams | tokens a round | drafts a round | accepted | ms a round | requests |
|---:|---:|---:|---:|---:|---:|
| 1 | 1.085 | 0.133 | 60% | 5.7 | 12 |

### ruler-after

| streams | prose total (a stream) | code total (a stream) | structured total (a stream) | list total (a stream) | first token |
|---:|---:|---:|---:|---:|---:|
| 1 | 182.5 (182.5) | 176.3 (176.3) | 192.3 (192.3) | 203.8 (203.8) | 0.03-0.04 s |

Engine rounds (ruler-after):

| streams | tokens a round | drafts a round | accepted | ms a round | requests |
|---:|---:|---:|---:|---:|---:|
| 1 | 1.084 | 0.137 | 58% | 5.74 | 13 |

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
| copy | 1/2 |
| max-tokens | 3/3 |

### checks

| check | result |
|---|---|
| memory-idle | measured: mac: System-wide memory free percentage: 86%; total = 4096.00M  us |
| structured | pass: 18/18 obey, drafted == plain 12/12; a bad regex -> 400 |
| tools | pass: 5/5 tool cases right |
| sampling | pass: 9/9 seeded replies equal on repeat and undrafted; 0 errors |
| turns | pass: resumed == again: True; cold (after a restart): True; cached 4507 of 4627; ttft resumed 0.066s, cold 0.716s |
| urls | FAIL: public 400; loopback 400; http 400; unexpected: ['public'] |

## 2026-10-21 19:18: run `20261021-191844-structured`

Plan structured, done; served as `flint`.

Serving: engine_commit `22a56a19`; binary_sha256 `95d4941a3b0e99db43ed8c305e745b0363a0d040c543e9561b84aa01f9daddc7`; served_model `{"object": "list", "data": [{"id": "flint", "object": "model", "created": 1792628324, "own`; chip `Apple M5 Ultra; 274877906944`; suite_commit `277c842a1481`

### checks

| check | result |
|---|---|
| structured | pass: 18/18 obey, drafted == plain 12/12; a bad regex -> 400 |
| tools | pass: 5/5 tool cases right |

## 2026-10-21 19:17: run `20261021-191727-mlx-speed`

Plan mlx-speed, done; served as `flint`.

Serving: engine_commit `22a56a19`; binary_sha256 `95d4941a3b0e99db43ed8c305e745b0363a0d040c543e9561b84aa01f9daddc7`; served_model `{"object": "list", "data": [{"id": "flint", "object": "model", "created": 1792628247, "own`; chip `Apple M5 Ultra; 274877906944`; suite_commit `277c842a1481`

### ruler-streams

| streams | prose total (a stream) | code total (a stream) | structured total (a stream) | list total (a stream) | first token |
|---:|---:|---:|---:|---:|---:|
| 1 | 183.1 (183.1) | 177.0 (177.0) | 192.9 (192.9) | 204.4 (204.4) | 0.03-0.04 s |
| 2 | 259.2 (129.6) | 256.1 (128.1) | 277.3 (138.6) | 277.8 (138.9) | 0.04-0.07 s |
| 4 | 354.5 (88.6) | 347.5 (86.7) | 364.0 (91.0) | 360.8 (88.6) | 0.07-0.11 s |

Engine rounds (ruler-streams):

| streams | tokens a round | drafts a round | accepted | ms a round | requests |
|---:|---:|---:|---:|---:|---:|
| 1 | 1.085 | 0.133 | 60% | 5.73 | 13 |
| 2 | 1.083 | 0.157 | 50% | 8.09 | 25 |
| 4 | 1.068 | 0.145 | 44% | 12.04 | 50 |

### checks

| check | result |
|---|---|
| memory-idle | measured: mac: System-wide memory free percentage: 70%; total = 3072.00M  us |

## 2026-10-21 19:15: run `20261021-191546-prefill`

Plan prefill, done; served as `flint`.

Serving: engine_commit `22a56a19`; binary_sha256 `95d4941a3b0e99db43ed8c305e745b0363a0d040c543e9561b84aa01f9daddc7`; served_model `{"object": "list", "data": [{"id": "flint", "object": "model", "created": 1792628154, "own`; chip `Apple M5 Ultra; 274877906944`; suite_commit `277c842a1481`

### checks

| check | result |
|---|---|
| memory-idle | measured: mac: System-wide memory free percentage: 73%; total = 3072.00M  us |
| prefill-off | measured: 2068 tokens 6503.1 tok/s (0.318 s), 8215 tokens 7039.4 tok/s (1.167 s), 32791 tokens 5887.1 tok/s (5.57 s), 131094 tokens 3360.0 tok/s (39.016 s) |
| prefill-thinking | measured: 2068 tokens 6714.3 tok/s (0.308 s), 8214 tokens 7032.5 tok/s (1.168 s), 32787 tokens 5894.8 tok/s (5.562 s), 131092 tokens 3353.5 tok/s (39.091 s) |
| memory-busy | measured: mac: System-wide memory free percentage: 69%; total = 3072.00M  us |

## 2026-10-21 19:14: run `20261021-191428-speed`

Plan speed, done; served as `flint`.

Serving: engine_commit `22a56a19`; binary_sha256 `95d4941a3b0e99db43ed8c305e745b0363a0d040c543e9561b84aa01f9daddc7`; served_model `{"object": "list", "data": [{"id": "flint", "object": "model", "created": 1792628077, "own`; chip `Apple M5 Ultra; 274877906944`; suite_commit `277c842a1481`

### ruler-fresh

| streams | prose total (a stream) | code total (a stream) | structured total (a stream) | list total (a stream) | first token |
|---:|---:|---:|---:|---:|---:|
| 1 | 183.9 (183.9) | 177.6 (177.6) | 193.6 (193.6) | 205.2 (205.2) | 0.03-0.04 s |
| 2 | 259.0 (129.5) | 255.8 (127.9) | 277.4 (138.7) | 275.1 (137.6) | 0.04-0.07 s |

Engine rounds (ruler-fresh):

| streams | tokens a round | drafts a round | accepted | ms a round | requests |
|---:|---:|---:|---:|---:|---:|
| 1 | 1.085 | 0.133 | 60% | 5.71 | 12 |
| 2 | 1.086 | 0.16 | 51% | 8.14 | 26 |

### ruler-after

| streams | prose total (a stream) | code total (a stream) | structured total (a stream) | list total (a stream) | first token |
|---:|---:|---:|---:|---:|---:|
| 1 | 184.1 (184.1) | 177.9 (177.9) | 193.9 (193.9) | 205.5 (205.5) | 0.03-0.04 s |

Engine rounds (ruler-after):

| streams | tokens a round | drafts a round | accepted | ms a round | requests |
|---:|---:|---:|---:|---:|---:|
| 1 | 1.084 | 0.137 | 58% | 5.7 | 13 |

### checks

| check | result |
|---|---|
| memory-idle | measured: mac: System-wide memory free percentage: 73%; total = 3072.00M  us |
| turns | pass: resumed == again: True; cold (after a restart): True; cached 4507 of 4627; ttft resumed 0.068s, cold 0.726s |
| memory-busy | measured: mac: System-wide memory free percentage: 72%; total = 3072.00M  us |

## 2026-10-21 18:23: run `20261021-182348-structured`

Plan structured, done; served as `flint`.

Serving: engine_commit `8b23061a`; binary_sha256 `bbc90c8eaeb9f9c6f75ff0edff13bdb659b193fdc51380a2c0ae27f0fdd49926`; served_model `{"object": "list", "data": [{"id": "flint", "object": "model", "created": 1792625028, "own`; chip `Apple M5 Ultra; 274877906944`; suite_commit `277c842a1481`

### checks

| check | result |
|---|---|
| structured | pass: 18/18 obey, drafted == plain 12/12; a bad regex -> 400 |
| tools | pass: 5/5 tool cases right |

## 2026-10-21 18:22: run `20261021-182231-mlx-speed`

Plan mlx-speed, done; served as `flint`.

Serving: engine_commit `8b23061a`; binary_sha256 `bbc90c8eaeb9f9c6f75ff0edff13bdb659b193fdc51380a2c0ae27f0fdd49926`; served_model `{"object": "list", "data": [{"id": "flint", "object": "model", "created": 1792624951, "own`; chip `Apple M5 Ultra; 274877906944`; suite_commit `277c842a1481`

### ruler-streams

| streams | prose total (a stream) | code total (a stream) | structured total (a stream) | list total (a stream) | first token |
|---:|---:|---:|---:|---:|---:|
| 1 | 180.8 (180.8) | 177.0 (177.0) | 192.8 (192.8) | 204.7 (204.7) | 0.03-0.04 s |
| 2 | 260.5 (130.3) | 257.2 (128.6) | 278.5 (139.3) | 277.0 (138.5) | 0.04-0.07 s |
| 4 | 356.4 (89.1) | 348.8 (87.4) | 365.4 (91.2) | 363.6 (88.1) | 0.07-0.11 s |

Engine rounds (ruler-streams):

| streams | tokens a round | drafts a round | accepted | ms a round | requests |
|---:|---:|---:|---:|---:|---:|
| 1 | 1.092 | 0.141 | 62% | 5.79 | 13 |
| 2 | 1.086 | 0.16 | 51% | 8.1 | 26 |
| 4 | 1.068 | 0.145 | 44% | 12.01 | 50 |

### checks

| check | result |
|---|---|
| memory-idle | measured: mac: System-wide memory free percentage: 78%; total = 3072.00M  us |

## 2026-10-21 18:21: run `20261021-182114-speed`

Plan speed, done; served as `flint`.

Serving: engine_commit `8b23061a`; binary_sha256 `bbc90c8eaeb9f9c6f75ff0edff13bdb659b193fdc51380a2c0ae27f0fdd49926`; served_model `{"object": "list", "data": [{"id": "flint", "object": "model", "created": 1792624882, "own`; chip `Apple M5 Ultra; 274877906944`; suite_commit `277c842a1481`

### ruler-fresh

| streams | prose total (a stream) | code total (a stream) | structured total (a stream) | list total (a stream) | first token |
|---:|---:|---:|---:|---:|---:|
| 1 | 182.3 (182.3) | 176.2 (176.2) | 192.0 (192.0) | 203.8 (203.8) | 0.03-0.04 s |
| 2 | 257.9 (129.0) | 254.4 (127.2) | 276.2 (138.1) | 274.3 (137.1) | 0.04-0.07 s |

Engine rounds (ruler-fresh):

| streams | tokens a round | drafts a round | accepted | ms a round | requests |
|---:|---:|---:|---:|---:|---:|
| 1 | 1.085 | 0.133 | 60% | 5.75 | 12 |
| 2 | 1.083 | 0.157 | 50% | 8.15 | 25 |

### ruler-after

| streams | prose total (a stream) | code total (a stream) | structured total (a stream) | list total (a stream) | first token |
|---:|---:|---:|---:|---:|---:|
| 1 | 183.1 (183.1) | 176.8 (176.8) | 192.8 (192.8) | 204.4 (204.4) | 0.03-0.04 s |

Engine rounds (ruler-after):

| streams | tokens a round | drafts a round | accepted | ms a round | requests |
|---:|---:|---:|---:|---:|---:|
| 1 | 1.084 | 0.137 | 58% | 5.73 | 13 |

### checks

| check | result |
|---|---|
| memory-idle | measured: mac: System-wide memory free percentage: 78%; total = 3072.00M  us |
| turns | pass: resumed == again: True; cold (after a restart): True; cached 4507 of 4627; ttft resumed 0.066s, cold 0.726s |
| memory-busy | measured: mac: System-wide memory free percentage: 78%; total = 3072.00M  us |

## 2026-10-21 17:56: run `20261021-175627-structured`

Plan structured, done; served as `flint`.

Serving: engine_commit `8a815d78`; binary_sha256 `78f6466bdb6196e496cd9108f5addde5d1f93dc31a53c2c5d2b629594f064c7b`; served_model `{"object": "list", "data": [{"id": "flint", "object": "model", "created": 1792623387, "own`; chip `Apple M5 Ultra; 274877906944`; suite_commit `277c842a1481`

### checks

| check | result |
|---|---|
| structured | pass: 18/18 obey, drafted == plain 12/12; a bad regex -> 400 |
| tools | pass: 5/5 tool cases right |

## 2026-10-21 17:55: run `20261021-175508-mlx-speed`

Plan mlx-speed, done; served as `flint`.

Serving: engine_commit `8a815d78`; binary_sha256 `78f6466bdb6196e496cd9108f5addde5d1f93dc31a53c2c5d2b629594f064c7b`; served_model `{"object": "list", "data": [{"id": "flint", "object": "model", "created": 1792623309, "own`; chip `Apple M5 Ultra; 274877906944`; suite_commit `277c842a1481`

### ruler-streams

| streams | prose total (a stream) | code total (a stream) | structured total (a stream) | list total (a stream) | first token |
|---:|---:|---:|---:|---:|---:|
| 1 | 171.5 (171.5) | 166.2 (166.2) | 178.6 (178.6) | 189.0 (189.0) | 0.02-0.04 s |
| 2 | 258.8 (129.4) | 256.0 (128.0) | 276.3 (138.2) | 274.4 (137.2) | 0.04-0.06 s |
| 4 | 351.6 (87.9) | 344.3 (86.1) | 360.3 (90.0) | 358.5 (87.4) | 0.06-0.10 s |

Engine rounds (ruler-streams):

| streams | tokens a round | drafts a round | accepted | ms a round | requests |
|---:|---:|---:|---:|---:|---:|
| 1 | 1.092 | 0.167 | 52% | 6.19 | 12 |
| 2 | 1.083 | 0.16 | 49% | 8.13 | 25 |
| 4 | 1.068 | 0.145 | 44% | 12.16 | 50 |

### checks

| check | result |
|---|---|
| memory-idle | measured: mac: System-wide memory free percentage: 87%; total = 3072.00M  us |

## 2026-10-21 17:53: run `20261021-175339-speed`

Plan speed, done; served as `flint`.

Serving: engine_commit `8a815d78`; binary_sha256 `78f6466bdb6196e496cd9108f5addde5d1f93dc31a53c2c5d2b629594f064c7b`; served_model `{"object": "list", "data": [{"id": "flint", "object": "model", "created": 1792623227, "own`; chip `Apple M5 Ultra; 274877906944`; suite_commit `277c842a1481`

### ruler-fresh

| streams | prose total (a stream) | code total (a stream) | structured total (a stream) | list total (a stream) | first token |
|---:|---:|---:|---:|---:|---:|
| 1 | 169.6 (169.6) | 164.9 (164.9) | 177.4 (177.4) | 187.8 (187.8) | 0.02-0.04 s |
| 2 | 257.1 (128.5) | 253.5 (126.8) | 273.8 (136.9) | 272.1 (136.1) | 0.04-0.06 s |

Engine rounds (ruler-fresh):

| streams | tokens a round | drafts a round | accepted | ms a round | requests |
|---:|---:|---:|---:|---:|---:|
| 1 | 1.092 | 0.167 | 52% | 6.24 | 12 |
| 2 | 1.087 | 0.165 | 50% | 8.23 | 26 |

### ruler-after

| streams | prose total (a stream) | code total (a stream) | structured total (a stream) | list total (a stream) | first token |
|---:|---:|---:|---:|---:|---:|
| 1 | 171.3 (171.3) | 166.3 (166.3) | 178.7 (178.7) | 189.4 (189.4) | 0.02-0.04 s |

Engine rounds (ruler-after):

| streams | tokens a round | drafts a round | accepted | ms a round | requests |
|---:|---:|---:|---:|---:|---:|
| 1 | 1.091 | 0.17 | 51% | 6.19 | 13 |

### checks

| check | result |
|---|---|
| memory-idle | measured: mac: System-wide memory free percentage: 87%; total = 3072.00M  us |
| turns | pass: resumed == again: True; cold (after a restart): True; cached 4507 of 4627; ttft resumed 0.059s, cold 0.727s |
| memory-busy | measured: mac: System-wide memory free percentage: 86%; total = 3072.00M  us |

## 2026-10-21 17:23: run `20261021-172342-speed`

Plan speed, done; served as `flint`.

Serving: engine_commit `8491096c`; binary_sha256 `7bbe2fa3fe4bb1708e023c2a0ee586a933558ca3f32273fcdfa811bb7d53a4b7`; served_model `{"object": "list", "data": [{"id": "flint", "object": "model", "created": 1792621430, "own`; chip `Apple M5 Ultra; 274877906944`; suite_commit `277c842a1481`

### ruler-fresh

| streams | prose total (a stream) | code total (a stream) | structured total (a stream) | list total (a stream) | first token |
|---:|---:|---:|---:|---:|---:|
| 1 | 136.4 (136.4) | 132.7 (132.7) | 142.6 (142.6) | 132.9 (132.9) | 0.03-0.05 s |
| 2 | 182.8 (91.4) | 179.1 (89.5) | 193.3 (96.7) | 178.1 (89.1) | 0.04-0.07 s |

Engine rounds (ruler-fresh):

| streams | tokens a round | drafts a round | accepted | ms a round | requests |
|---:|---:|---:|---:|---:|---:|
| 1 | 1.048 | 0.092 | 48% | 7.7 | 12 |
| 2 | 1.051 | 0.116 | 41% | 11.47 | 25 |

### ruler-after

| streams | prose total (a stream) | code total (a stream) | structured total (a stream) | list total (a stream) | first token |
|---:|---:|---:|---:|---:|---:|
| 1 | 135.7 (135.7) | 131.8 (131.8) | 142.5 (142.5) | 132.2 (132.2) | 0.03-0.05 s |

Engine rounds (ruler-after):

| streams | tokens a round | drafts a round | accepted | ms a round | requests |
|---:|---:|---:|---:|---:|---:|
| 1 | 1.048 | 0.096 | 46% | 7.73 | 13 |

### checks

| check | result |
|---|---|
| memory-idle | measured: mac: System-wide memory free percentage: 87%; total = 3072.00M  us |
| turns | pass: resumed == again: True; cold (after a restart): True; cached 4507 of 4627; ttft resumed 0.073s, cold 0.912s |
| memory-busy | measured: mac: System-wide memory free percentage: 87%; total = 3072.00M  us |

## 2026-10-21 17:10: run `20261021-171056-prefill`

Plan prefill, done; served as `flint`.

Serving: engine_commit `97ce2ef3`; binary_sha256 `c19c2847652def0f298490541cd6bf2dbb0f0379aaf19ec9b20adcc6441d9152`; served_model `{"object": "list", "data": [{"id": "flint", "object": "model", "created": 1792620664, "own`; chip `Apple M5 Ultra; 274877906944`; suite_commit `277c842a1481`

### checks

| check | result |
|---|---|
| memory-idle | measured: mac: System-wide memory free percentage: 87%; total = 3072.00M  us |
| prefill-off | measured: 2067 tokens 5327.3 tok/s (0.388 s), 8213 tokens 5508.4 tok/s (1.491 s), 32791 tokens 4766.1 tok/s (6.88 s), 131092 tokens 2930.2 tok/s (44.739 s) |
| prefill-thinking | measured: 2068 tokens 5209.1 tok/s (0.397 s), 8211 tokens 5474.0 tok/s (1.5 s), 32791 tokens 4730.4 tok/s (6.932 s), 131095 tokens 2930.3 tok/s (44.737 s) |
| memory-busy | measured: mac: System-wide memory free percentage: 84%; total = 3072.00M  us |

## 2026-10-21 17:08: run `20261021-170851-structured`

Plan structured, done; served as `flint`.

Serving: engine_commit `97ce2ef3`; binary_sha256 `c19c2847652def0f298490541cd6bf2dbb0f0379aaf19ec9b20adcc6441d9152`; served_model `{"object": "list", "data": [{"id": "flint", "object": "model", "created": 1792620531, "own`; chip `Apple M5 Ultra; 274877906944`; suite_commit `277c842a1481`

### checks

| check | result |
|---|---|
| structured | pass: 18/18 obey, drafted == plain 12/12; a bad regex -> 400 |
| tools | pass: 5/5 tool cases right |

## 2026-10-21 17:06: run `20261021-170658-mlx-speed`

Plan mlx-speed, done; served as `flint`.

Serving: engine_commit `97ce2ef3`; binary_sha256 `c19c2847652def0f298490541cd6bf2dbb0f0379aaf19ec9b20adcc6441d9152`; served_model `{"object": "list", "data": [{"id": "flint", "object": "model", "created": 1792620418, "own`; chip `Apple M5 Ultra; 274877906944`; suite_commit `277c842a1481`

### ruler-streams

| streams | prose total (a stream) | code total (a stream) | structured total (a stream) | list total (a stream) | first token |
|---:|---:|---:|---:|---:|---:|
| 1 | 135.4 (135.4) | 131.3 (131.3) | 143.4 (143.4) | 131.9 (131.9) | 0.03-0.05 s |
| 2 | 182.4 (91.2) | 181.0 (90.5) | 193.2 (96.6) | 178.8 (89.4) | 0.04-0.07 s |
| 4 | 230.3 (57.6) | 227.6 (56.9) | 237.0 (59.2) | 229.2 (57.1) | 0.07-0.12 s |

Engine rounds (ruler-streams):

| streams | tokens a round | drafts a round | accepted | ms a round | requests |
|---:|---:|---:|---:|---:|---:|
| 1 | 1.048 | 0.092 | 48% | 7.73 | 12 |
| 2 | 1.051 | 0.116 | 41% | 11.44 | 25 |
| 4 | 1.055 | 0.128 | 40% | 18.28 | 50 |

### checks

| check | result |
|---|---|
| memory-idle | measured: mac: System-wide memory free percentage: 87%; total = 3072.00M  us |

