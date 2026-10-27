# Qwen3.8-Flash-Next INT4-Mixed (AutoRound) on 2x NVIDIA DGX Spark (GB10, 128 GB unified each), TP=2 over RoCE

Target `qwen38-int4mixed`: Qwen3.8-Flash-Next INT4-Mixed, TensorFold native, TP=2 on two DGX Sparks. Engine: TensorFold native, CUDA. Rendered from `stats/qwen38-int4mixed.json` (21 runs); aggregate tok/s, total (a stream).

## 2026-10-27 00:00: run `evidence/2026-10-27-native-v1.1.6`

Plan published evidence, published; served as `Qwen3.8-Flash-Next-INT4-Mixed`.

### ruler

| streams | prose total (a stream) | code total (a stream) | structured total (a stream) | list total (a stream) | first token |
|---:|---:|---:|---:|---:|---:|
| 1 | 78.2 (78.2) | 127.1 (127.1) | 102.5 (102.5) | 130.6 (130.6) | 0.04-0.04 s |
| 4 | 161.1 (40.4) | 257.2 (66.7) | 205.2 (50.9) | 293.5 (69.7) | 0.08-0.10 s |
| 16 | 305.1 (19.0) | 516.3 (31.0) | 393.1 (23.9) | 526.9 (32.0) | 0.46-0.51 s |

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
| tools | 60/60 |
| json | 30/30 |
| ifeval | 130/150 |
| gsm8k | 241/250 |
| mgsm | 219/240 |
| mmlu | 283/342 |
| humaneval | 157/164 |
| repetition | 8/8 |
| long-context | 55/55 |
| vision | 12/12 |
| soak | 60/60 |
| snapshot | 12/12 |

## 2026-10-17 07:25: run `20261017-072502-rebase`

Plan rebase, done; served as `Qwen3.8-Flash-Next-INT4-Mixed`.

Serving: patch_sha `47c78d3f99593702c9e8a0baa64ec32c937520930186c78549004f411cd5f731`; image `tf-qwen38-int4mixed:native-v1.0.12 sha256:276fe2ba4ed3e778ec6f55ffad1430897b9ff439aff8352b`; server_args `--context 1048576 --no-thinking --parallel 16 --vision-urls --vision`

### ruler-fresh

| streams | prose total (a stream) | code total (a stream) | structured total (a stream) | list total (a stream) | first token |
|---:|---:|---:|---:|---:|---:|
| 1 | 78.0 (78.0) | 127.0 (127.0) | 102.1 (102.1) | 130.5 (130.5) | 0.03-0.04 s |
| 16 | 304.2 (18.9) | 516.3 (31.0) | 391.6 (24.0) | 524.9 (31.7) | 0.45-0.54 s |

Engine rounds (ruler-fresh):

| streams | tokens a round | drafts a round | accepted | ms a round | requests |
|---:|---:|---:|---:|---:|---:|
| 1 | 3.621 | 4.042 | 66% | 33.09 | 12 |
| 16 | 3.212 | 2.921 | 76% | 121.71 | 193 |

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

### suite-guided

| check | passed |
|---|---:|
| json-guided | 30/30 |
| tools | 60/60 |

### suite-thinking

| check | passed |
|---|---:|
| gsm8k | 234/250 |

### checks

| check | result |
|---|---|
| memory-idle | measured: head 22.6 GiB available; worker 25.3 GiB available |
| structured | pass: 18/18 obey; a bad regex -> 400 |
| sampling | pass: 9/9 seeded replies equal on repeat and undrafted; 0 errors |
| turns | pass: resumed == again == cold: True; cached 5575 of 5642; ttft resumed 0.105s, cold 0.035s |
| thinking | pass: thinking on: 10/10 right, 10/10 with reasoning_content, 0 leaks, 0 errors |

## 2026-10-15 17:13: run `20261015-171328-full`

Plan full, done; served as `Qwen3.8-Flash-Next-INT4-Mixed`.

Serving: patch_sha `186193c6a530d89ee6383c11a9e41f98bac95bb119959aa5901c65b0f93b21ea`; image `tf-qwen38-int4mixed:native-v1.0.11-3 sha256:7c5838987336819a3dcc51d8f9abcf169f80fbfe73222e`; server_args `--context 1048576 --no-thinking --parallel 16 --vision-urls --vision`

### ruler-fresh

| streams | prose total (a stream) | code total (a stream) | structured total (a stream) | list total (a stream) | first token |
|---:|---:|---:|---:|---:|---:|
| 1 | 77.3 (77.3) | 127.0 (127.0) | 100.6 (100.6) | 129.6 (129.6) | 0.03-0.04 s |
| 4 | 159.1 (39.8) | 253.9 (65.0) | 201.7 (49.8) | 268.4 (61.8) | 0.07-0.10 s |
| 8 | 228.9 (28.8) | 385.2 (46.2) | 282.4 (35.8) | 423.1 (51.3) | 0.11-0.14 s |
| 16 | 301.9 (18.8) | 509.8 (30.6) | 391.3 (24.0) | 519.2 (31.6) | 0.44-0.55 s |

Engine rounds (ruler-fresh):

| streams | tokens a round | drafts a round | accepted | ms a round | requests |
|---:|---:|---:|---:|---:|---:|
| 1 | 3.621 | 4.042 | 66% | 33.33 | 12 |
| 4 | 3.173 | 2.949 | 74% | 58.64 | 49 |
| 8 | 3.09 | 2.653 | 80% | 76.26 | 100 |
| 16 | 3.222 | 2.925 | 77% | 122.65 | 196 |

### ruler-after

| streams | prose total (a stream) | code total (a stream) | structured total (a stream) | list total (a stream) | first token |
|---:|---:|---:|---:|---:|---:|
| 1 | 77.5 (77.5) | 125.9 (125.9) | 99.2 (99.2) | 129.7 (129.7) | 0.04-0.04 s |
| 16 | 302.3 (18.8) | 509.5 (30.4) | 389.8 (23.8) | 520.4 (31.6) | 0.44-0.50 s |

Engine rounds (ruler-after):

| streams | tokens a round | drafts a round | accepted | ms a round | requests |
|---:|---:|---:|---:|---:|---:|
| 1 | 3.567 | 4.016 | 65% | 33.01 | 13 |
| 16 | 3.21 | 2.914 | 76% | 122.7 | 193 |

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
| tools | 60/60 |
| json | 30/30 |
| ifeval | 130/150 |
| gsm8k | 241/250 |
| mgsm | 219/240 |
| mmlu | 283/342 |
| humaneval | 157/164 |
| repetition | 8/8 |
| long-context | 55/55 |
| vision | 12/12 |
| soak | 60/60 |
| snapshot | 12/12 |

### checks

| check | result |
|---|---|
| memory-idle | measured: head 21.8 GiB available; worker 25.2 GiB available |
| structured | pass: 18/18 obey; a bad regex -> 400 |
| sampling | pass: 9/9 seeded replies equal on repeat and undrafted; 0 errors |
| turns | pass: resumed == again == cold: True; cached 5575 of 5642; ttft resumed 0.118s, cold 0.035s |
| urls | pass: public 200; loopback 400; http 400 |
| capacity | pass: 4/6 answered, 2 refused, 0 lost (no reply); a short request after: 200 |

## 2026-10-15 00:00: run `evidence/2026-10-15-native-v1.0.11-2`

Plan published evidence, published; served as `Qwen3.8-Flash-Next-INT4-Mixed`.

### ruler-c16-repeat

| streams | prose total (a stream) | code total (a stream) | structured total (a stream) | list total (a stream) | first token |
|---:|---:|---:|---:|---:|---:|
| 16 | 293.2 (18.4) | 469.4 (27.7) | 355.3 (21.9) | 492.8 (30.5) | 0.52-0.66 s |

### ruler-c16-v1.0.11

| streams | prose total (a stream) | code total (a stream) | structured total (a stream) | list total (a stream) | first token |
|---:|---:|---:|---:|---:|---:|
| 16 | 286.8 (18.1) | 467.6 (27.6) | 349.3 (21.7) | 489.3 (30.2) | 0.58-0.68 s |

### ruler

| streams | prose total (a stream) | code total (a stream) | structured total (a stream) | list total (a stream) | first token |
|---:|---:|---:|---:|---:|---:|
| 1 | 75.5 (75.5) | 123.4 (123.4) | 99.1 (99.1) | 125.7 (125.7) | 0.04-0.04 s |
| 4 | 155.0 (38.9) | 250.4 (65.3) | 197.1 (48.7) | 270.6 (62.2) | 0.09-0.11 s |
| 16 | 291.5 (18.4) | 472.9 (28.0) | 360.1 (21.7) | 490.3 (29.9) | 0.52-0.74 s |

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
| tools | 60/60 |
| json | 30/30 |
| ifeval | 130/150 |
| gsm8k | 241/250 |
| mgsm | 219/240 |
| mmlu | 283/342 |
| humaneval | 157/164 |
| repetition | 8/8 |
| long-context | 55/55 |
| vision | 12/12 |
| soak | 60/60 |
| snapshot | 12/12 |

### suite-guided

| check | passed |
|---|---:|
| json-guided | 30/30 |
| tools | 60/60 |

## 2026-10-15 00:00: run `evidence/2026-10-15-native-v1.0.11`

Plan published evidence, published; served as `Qwen3.8-Flash-Next-INT4-Mixed`.

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
| tools | 60/60 |
| json | 30/30 |
| ifeval | 130/150 |
| gsm8k | 241/250 |
| mgsm | 219/240 |
| mmlu | 283/342 |
| humaneval | 157/164 |
| repetition | 8/8 |
| long-context | 55/55 |
| vision | 12/12 |
| soak | 60/60 |
| snapshot | 12/12 |

### suite-guided

| check | passed |
|---|---:|
| json-guided | 30/30 |
| tools | 60/60 |

## 2026-10-11 00:00: run `evidence/2026-10-11-native-v1.0.7`

Plan published evidence, published; served as `Qwen3.8-Flash-Next-INT4-Mixed`.

### ruler-before-batched-admission

| streams | prose total (a stream) | code total (a stream) | structured total (a stream) | list total (a stream) | first token |
|---:|---:|---:|---:|---:|---:|
| 1 | 73.2 (73.2) | 120.5 (120.5) | 96.6 (96.6) | 122.3 (122.3) | 0.06-0.08 s |
| 16 | 285.6 (18.0) | 464.0 (27.2) | 350.6 (21.3) | 478.8 (29.7) | 0.65-0.83 s |

### ruler

| streams | prose total (a stream) | code total (a stream) | structured total (a stream) | list total (a stream) | first token |
|---:|---:|---:|---:|---:|---:|
| 1 | 71.7 (71.7) | 120.1 (120.1) | 97.0 (97.0) | 119.7 (119.7) | 0.06-0.08 s |
| 16 | 295.9 (18.4) | 507.2 (30.2) | 382.3 (23.3) | 516.5 (31.0) | 0.54-0.62 s |

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
| tools | 60/60 |
| json | 30/30 |
| ifeval | 130/150 |
| gsm8k | 241/250 |
| mgsm | 219/240 |
| mmlu | 283/342 |
| humaneval | 157/164 |
| repetition | 8/8 |
| long-context | 55/55 |
| vision | 12/12 |
| soak | 60/60 |
| snapshot | 12/12 |

### suite-batched

| check | passed |
|---|---:|
| drafts | 12/12 |
| streaming | 4/4 |
| multiturn | 8/8 |
| stop | 3/3 |
| thinking | 10/10 |
| copy | 2/2 |
| max-tokens | 3/3 |
| tools | 60/60 |
| json | 30/30 |
| soak | 60/60 |
| snapshot | 12/12 |

### suite-batched-2

| check | passed |
|---|---:|
| concurrent | 12/12 |
| vision | 12/12 |

## 2026-10-11 00:00: run `evidence/2026-10-11-c16`

Plan published evidence, published; served as `Qwen3.8-Flash-Next-INT4-Mixed`.

### ruler

| streams | prose total (a stream) | code total (a stream) | structured total (a stream) | list total (a stream) | first token |
|---:|---:|---:|---:|---:|---:|
| 1 | 72.4 (72.4) | 120.4 (120.4) | 95.3 (95.3) | 121.7 (121.7) | 0.07-0.08 s |
| 16 | 295.6 (18.4) | 507.1 (30.2) | 384.6 (23.5) | 516.4 (31.3) | 0.50-0.59 s |

## 2026-10-10 09:45: run `20261010-094527-quick`

Plan quick, done; served as `Qwen3.8-Flash-Next-INT4-Mixed`.

Serving: patch_sha `bc0402c1b6f31946984c0c469bb85d77eb926f4dc31ff9b8fcdb876ee4dbe8b5`; image `tf-qwen38-int4mixed:native-v1.0.4 sha256:159e8b61d9ec0827e4a2c76b9933b3ec3e358dc05ab0b7067`; server_args `--context 1048576 --no-thinking --parallel 16 --vision-urls --vision`

### ruler-fresh

| streams | prose total (a stream) | code total (a stream) | structured total (a stream) | list total (a stream) | first token |
|---:|---:|---:|---:|---:|---:|
| 1 | 68.8 (68.8) | 105.3 (105.3) | 86.0 (86.0) | 109.5 (109.5) | 0.08-0.11 s |

### ruler-after

| streams | prose total (a stream) | code total (a stream) | structured total (a stream) | list total (a stream) | first token |
|---:|---:|---:|---:|---:|---:|
| 1 | 67.2 (67.2) | 103.5 (103.5) | 83.8 (83.8) | 108.4 (108.4) | 0.08-0.12 s |

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

### checks

| check | result |
|---|---|
| memory-idle | measured: head 20.5 GiB available; worker 24.9 GiB available |
| structured | pass: 18/18 obey; a bad regex -> 400 |
| sampling | pass: 9/9 seeded replies equal on repeat and undrafted; 0 errors |
| turns | pass: resumed == again == cold: True; cached 5575 of 5642; ttft resumed 0.121s, cold 2.088s |
| urls | pass: public 200; loopback 400; http 400 |

## 2026-10-10 00:00: run `evidence/2026-10-10-native-v1.0.5-kept`

Plan published evidence, published; served as `Qwen3.8-Flash-Next-INT4-Mixed`.

### ruler-c1-repeat1

| streams | prose total (a stream) | code total (a stream) | structured total (a stream) | list total (a stream) | first token |
|---:|---:|---:|---:|---:|---:|
| 1 | 72.2 (72.2) | 121.9 (121.9) | 95.0 (95.0) | 121.7 (121.7) | 0.03-0.04 s |

### ruler-c1-repeat2

| streams | prose total (a stream) | code total (a stream) | structured total (a stream) | list total (a stream) | first token |
|---:|---:|---:|---:|---:|---:|
| 1 | 72.3 (72.3) | 121.5 (121.5) | 94.6 (94.6) | 121.9 (121.9) | 0.03-0.04 s |

### ruler-fresh

| streams | prose total (a stream) | code total (a stream) | structured total (a stream) | list total (a stream) | first token |
|---:|---:|---:|---:|---:|---:|
| 1 | 74.8 (74.8) | 122.0 (122.0) | 95.9 (95.9) | 121.6 (121.6) | 0.03-0.04 s |
| 16 | 296.4 (18.5) | 510.3 (30.4) | 385.9 (23.5) | 518.3 (31.4) | 0.40-0.49 s |

### gate

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

## 2026-10-10 00:00: run `evidence/2026-10-10-native-v1.0.5`

Plan published evidence, published; served as `Qwen3.8-Flash-Next-INT4-Mixed`.

### ruler-after

| streams | prose total (a stream) | code total (a stream) | structured total (a stream) | list total (a stream) | first token |
|---:|---:|---:|---:|---:|---:|
| 1 | 76.5 (76.5) | 124.6 (124.6) | 97.8 (97.8) | 125.1 (125.1) | 0.07-0.10 s |

### ruler-c1-repeat

| streams | prose total (a stream) | code total (a stream) | structured total (a stream) | list total (a stream) | first token |
|---:|---:|---:|---:|---:|---:|
| 1 | 76.5 (76.5) | 126.4 (126.4) | 97.9 (97.9) | 126.9 (126.9) | 0.04-0.06 s |

### ruler-fresh

| streams | prose total (a stream) | code total (a stream) | structured total (a stream) | list total (a stream) | first token |
|---:|---:|---:|---:|---:|---:|
| 1 | 76.9 (76.9) | 125.9 (125.9) | 99.3 (99.3) | 128.0 (128.0) | 0.07-0.09 s |
| 4 | 158.5 (39.7) | 250.3 (64.4) | 199.6 (49.6) | 273.7 (63.3) | 0.14-0.21 s |
| 8 | 221.5 (28.1) | 384.6 (45.1) | 273.2 (34.6) | 411.0 (50.2) | 0.24-0.30 s |
| 16 | 297.2 (18.5) | 510.9 (30.3) | 387.7 (23.6) | 518.4 (31.3) | 0.44-0.49 s |

### port-checks/suite

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
| tools | 60/60 |
| json | 30/30 |
| ifeval | 130/150 |
| gsm8k | 241/250 |
| mgsm | 219/240 |
| mmlu | 283/342 |
| humaneval | 157/164 |
| repetition | 8/8 |
| long-context | 55/55 |
| vision | 12/12 |
| snapshot | 12/12 |

### soak

| check | passed |
|---|---:|
| soak | 60/60 |

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

## 2026-10-10 00:00: run `evidence/2026-10-10-native-v1.0.4-split-shared`

Plan published evidence, published; served as `Qwen3.8-Flash-Next-INT4-Mixed`.

### ruler-after

| streams | prose total (a stream) | code total (a stream) | structured total (a stream) | list total (a stream) | first token |
|---:|---:|---:|---:|---:|---:|
| 1 | 77.1 (77.1) | 124.7 (124.7) | 97.0 (97.0) | 125.3 (125.3) | 0.07-0.09 s |

### ruler-fresh

| streams | prose total (a stream) | code total (a stream) | structured total (a stream) | list total (a stream) | first token |
|---:|---:|---:|---:|---:|---:|
| 1 | 77.1 (77.1) | 125.7 (125.7) | 99.1 (99.1) | 125.7 (125.7) | 0.08-0.09 s |
| 4 | 157.5 (39.5) | 247.6 (64.9) | 194.4 (48.3) | 281.3 (65.6) | 0.13-0.19 s |
| 8 | 223.2 (28.1) | 380.3 (45.2) | 279.8 (35.0) | 410.4 (49.8) | 0.23-0.32 s |
| 16 | 297.8 (18.6) | 506.7 (30.5) | 383.7 (23.7) | 517.3 (31.4) | 0.42-0.49 s |

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

## 2026-10-10 00:00: run `evidence/2026-10-10-native-v1.0.4-graphs`

Plan published evidence, published; served as `Qwen3.8-Flash-Next-INT4-Mixed`.

### ruler-after

| streams | prose total (a stream) | code total (a stream) | structured total (a stream) | list total (a stream) | first token |
|---:|---:|---:|---:|---:|---:|
| 1 | 67.1 (67.1) | 103.4 (103.4) | 84.1 (84.1) | 107.5 (107.5) | 0.08-0.12 s |

### ruler-fresh

| streams | prose total (a stream) | code total (a stream) | structured total (a stream) | list total (a stream) | first token |
|---:|---:|---:|---:|---:|---:|
| 1 | 66.8 (66.8) | 106.1 (106.1) | 85.1 (85.1) | 106.9 (106.9) | 0.08-0.11 s |
| 16 | 295.8 (18.5) | 506.1 (30.1) | 380.8 (23.3) | 501.9 (30.2) | 0.42-0.51 s |

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

## 2026-10-10 00:00: run `evidence/2026-10-10-native-v1.0.4`

Plan published evidence, published; served as `Qwen3.8-Flash-Next-INT4-Mixed`.

### ruler

| streams | prose total (a stream) | code total (a stream) | structured total (a stream) | list total (a stream) | first token |
|---:|---:|---:|---:|---:|---:|
| 1 | 69.1 (69.1) | 110.0 (110.0) | 88.7 (88.7) | 112.5 (112.5) | 0.07-0.09 s |
| 4 | 157.1 (39.2) | 252.3 (66.2) | 197.4 (49.2) | 288.6 (68.3) | 0.15-0.21 s |
| 8 | 221.9 (28.0) | 382.2 (45.8) | 279.7 (35.5) | 412.3 (50.5) | 0.23-0.32 s |
| 16 | 297.3 (18.5) | 511.8 (30.3) | 383.5 (23.6) | 519.8 (31.2) | 0.41-0.55 s |

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
| tools | 60/60 |
| json | 30/30 |
| ifeval | 130/150 |
| gsm8k | 241/250 |
| mgsm | 219/240 |
| mmlu | 283/342 |
| humaneval | 157/164 |
| repetition | 8/8 |
| long-context | 55/55 |
| vision | 12/12 |
| snapshot | 12/12 |

## 2026-10-10 00:00: run `evidence/2026-10-10-native-integrate`

Plan published evidence, published; served as `Qwen3.8-Flash-Next-INT4-Mixed`.

### ruler

| streams | prose total (a stream) | code total (a stream) | structured total (a stream) | list total (a stream) | first token |
|---:|---:|---:|---:|---:|---:|
| 1 | 68.6 (68.6) | 105.8 (105.8) | 85.0 (85.0) | 108.3 (108.3) | 0.07-0.10 s |
| 4 | 152.8 (38.1) | 245.2 (64.4) | 189.7 (46.9) | 269.2 (62.2) | 0.15-0.21 s |
| 8 | 219.4 (27.8) | 378.1 (45.2) | 276.3 (34.7) | 402.3 (48.9) | 0.24-0.32 s |
| 16 | 294.7 (18.4) | 505.5 (29.9) | 379.5 (23.4) | 513.3 (31.3) | 0.41-0.46 s |

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
| tools | 60/60 |
| json | 30/30 |
| ifeval | 130/150 |
| gsm8k | 241/250 |
| mgsm | 219/240 |
| mmlu | 283/342 |
| humaneval | 157/164 |
| repetition | 8/8 |
| long-context | 55/55 |
| vision | 12/12 |
| snapshot | 12/12 |

## 2026-10-09 00:00: run `evidence/2026-10-09-native-v1.0.2`

Plan published evidence, published; served as `Qwen3.8-Flash-Next-INT4-Mixed`.

### ruler-c1

| streams | prose total (a stream) | code total (a stream) | structured total (a stream) | list total (a stream) | first token |
|---:|---:|---:|---:|---:|---:|
| 1 | 68.6 (68.6) | 106.4 (106.4) | 86.6 (86.6) | 109.2 (109.2) | 0.13-0.34 s |

### ruler

| streams | prose total (a stream) | code total (a stream) | structured total (a stream) | list total (a stream) | first token |
|---:|---:|---:|---:|---:|---:|
| 1 | 68.7 (68.7) | 105.2 (105.2) | 86.2 (86.2) | 107.5 (107.5) | 0.10-0.11 s |
| 4 | 144.0 (36.1) | 221.2 (56.6) | 180.6 (45.1) | 249.7 (57.9) | 0.22-0.28 s |
| 8 | 194.2 (24.3) | 331.0 (38.6) | 238.9 (29.2) | 354.4 (43.9) | 0.40-0.50 s |
| 16 | 259.7 (16.4) | 412.2 (24.3) | 311.2 (19.0) | 428.8 (26.5) | 0.78-0.98 s |

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
| tools | 60/60 |
| json | 30/30 |
| ifeval | 130/150 |
| gsm8k | 241/250 |
| mgsm | 219/240 |
| mmlu | 283/342 |
| humaneval | 157/164 |
| repetition | 8/8 |
| long-context | 55/55 |
| vision | 11/12 |
| snapshot | 12/12 |

### vision/native

| check | passed |
|---|---:|
| vision | 12/12 |

### vision/python

| check | passed |
|---|---:|
| vision | 12/12 |

## 2026-10-09 00:00: run `evidence/2026-10-09-kv-int4-ab`

Plan published evidence, published; served as `Qwen3.8-Flash-Next-INT4-Mixed`.

### native-int4/suite

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
| tools | 58/60 |
| json | 30/30 |
| ifeval | 130/150 |
| gsm8k | 240/250 |
| mgsm | 219/240 |
| mmlu | 282/342 |
| humaneval | 156/164 |
| repetition | 8/8 |
| long-context | 55/55 |
| vision | 12/12 |
| snapshot | 12/12 |

### python-int4/suite

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
| tools | 58/60 |
| json | 30/30 |
| ifeval | 130/150 |
| gsm8k | 240/250 |
| mgsm | 219/240 |
| mmlu | 282/342 |
| humaneval | 156/164 |
| repetition | 8/8 |
| long-context | 0/0 |
| vision | 12/12 |
| snapshot | 0/0 |

### python-int8/suite

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
| tools | 60/60 |
| json | 30/30 |
| ifeval | 130/150 |
| gsm8k | 241/250 |
| mgsm | 219/240 |
| mmlu | 283/342 |
| humaneval | 157/164 |
| repetition | 8/8 |
| long-context | 55/55 |
| vision | 12/12 |
| snapshot | 12/12 |

## 2026-10-08 00:00: run `evidence/2026-10-08-two-rails`

Plan published evidence, published; served as `Qwen3.8-Flash-Next-INT4-Mixed`.

### ruler-c1-c16

| streams | prose total (a stream) | code total (a stream) | structured total (a stream) | list total (a stream) | first token |
|---:|---:|---:|---:|---:|---:|
| 1 | 68.1 (68.1) | 107.1 (107.1) | 88.6 (88.6) | 108.4 (108.4) | 0.06-0.09 s |
| 16 | 300.7 (18.9) | 519.4 (29.7) | 377.9 (23.3) | 540.2 (34.0) | 0.44-0.56 s |

## 2026-10-08 00:00: run `evidence/2026-10-08-shipped-image`

Plan published evidence, published; served as `Qwen3.8-Flash-Next-INT4-Mixed`.

### ruler-dev

| streams | prose total (a stream) | code total (a stream) | structured total (a stream) | list total (a stream) | first token |
|---:|---:|---:|---:|---:|---:|
| 1 | 69.0 (69.0) | 107.7 (107.7) | 89.4 (89.4) | 109.7 (109.7) | 0.06-0.10 s |
| 4 | 147.4 (37.1) | 230.0 (59.8) | 197.3 (48.8) | 279.9 (67.0) | 0.12-0.19 s |
| 8 | 214.1 (26.9) | 366.0 (42.3) | 273.2 (34.8) | 403.7 (50.0) | 0.24-0.30 s |
| 16 | 299.2 (18.8) | 474.0 (27.4) | 372.7 (23.0) | 540.8 (34.1) | 0.52-0.66 s |

### ruler-image

| streams | prose total (a stream) | code total (a stream) | structured total (a stream) | list total (a stream) | first token |
|---:|---:|---:|---:|---:|---:|
| 1 | 68.7 (68.7) | 109.0 (109.0) | 89.0 (89.0) | 109.9 (109.9) | 0.06-0.10 s |
| 16 | 299.5 (18.8) | 475.2 (27.5) | 372.0 (22.8) | 542.0 (34.1) | 0.51-0.72 s |

### quality

| check | passed |
|---|---:|
| tools | 60/60 |
| streaming | 4/4 |
| multiturn | 8/8 |
| stop | 3/3 |
| thinking | 10/10 |
| copy | 2/2 |
| max-tokens | 3/3 |
| long-context | 55/55 |

### quality-image-first

| check | passed |
|---|---:|
| drafts | 12/12 |
| concurrent | 12/12 |
| vision | 12/12 |

## 2026-10-08 00:00: run `evidence/2026-10-08-python-0.6`

Plan published evidence, published; served as `Qwen3.8-Flash-Next-INT4-Mixed`.

### ruler

| streams | prose total (a stream) | code total (a stream) | structured total (a stream) | list total (a stream) | first token |
|---:|---:|---:|---:|---:|---:|
| 1 | 69.3 (69.3) | 107.6 (107.6) | 88.3 (88.3) | 110.4 (110.4) | 0.06-0.17 s |
| 16 | 298.9 (18.8) | 442.6 (26.1) | 375.3 (23.2) | 541.8 (34.1) | 0.44-0.58 s |

### quality

| check | passed |
|---|---:|
| drafts | 12/12 |
| concurrent | 12/12 |
| vision | 12/12 |

### quality-json

| check | passed |
|---|---:|
| json-guided | 30/30 |

## 2026-10-08 00:00: run `evidence/2026-10-08-prefill-fusions`

Plan published evidence, published; served as `Qwen3.8-Flash-Next-INT4-Mixed`.

### ruler-c1-c16

| streams | prose total (a stream) | code total (a stream) | structured total (a stream) | list total (a stream) | first token |
|---:|---:|---:|---:|---:|---:|
| 1 | 67.6 (67.6) | 107.6 (107.6) | 88.0 (88.0) | 109.9 (109.9) | 0.06-0.10 s |
| 16 | 297.9 (18.7) | 441.7 (26.1) | 375.3 (23.0) | 535.3 (33.7) | 0.45-0.58 s |

## 2026-10-07 00:00: run `evidence/2026-10-07-first-boot`

Plan published evidence, published; served as `Qwen3.8-Flash-Next-INT4-Mixed`.

### v1-bf16-dense/quality

| check | passed |
|---|---:|
| drafts | 12/12 |

### v2-concurrent-1m/quality/q

| check | passed |
|---|---:|
| drafts | 12/12 |
| concurrent | 12/12 |

### v2-concurrent-1m/quality

| check | passed |
|---|---:|
| drafts | 12/12 |
| concurrent | 12/12 |

### v2-int8-dense/quality

| check | passed |
|---|---:|
| drafts | 12/12 |

