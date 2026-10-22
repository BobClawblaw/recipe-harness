# NVIDIA Nemotron 3.5 Bolt 74B-A9B (24 GB: IQ2_XXS experts, Q8_0, NVFP4 Mamba) + vision on 1x NVIDIA RTX 5090 (32 GB)

Target `nemotron-bolt-5090`: Nemotron 3.5 Bolt 74B-A9B ModelOpt IQ2_XXS/Q8_0/NVFP4, TensorFold native CUDA on one RTX 5090 (262144, two streams, vision, host prompt cache). Engine: TensorFold native, CUDA. Rendered from `stats/nemotron-bolt-5090.json` (4 runs); aggregate tok/s, total (a stream).

## 2026-10-15 17:56: run `20261015-175621-full`

Plan full, done; served as `nemotron-bolt`.

Serving: recipe_commit `f546a71`; engine_commit `b2ec378d`; served_model `{"object": "list", "data": [{"id": "nemotron-bolt", "object": "model", "created": 17920869`

### ruler-fresh

| streams | prose total (a stream) | code total (a stream) | structured total (a stream) | list total (a stream) | first token |
|---:|---:|---:|---:|---:|---:|
| 1 | 149.7 (149.7) | 149.6 (149.6) | 150.1 (150.1) | 149.7 (149.7) | 0.03-0.03 s |

Engine rounds (ruler-fresh):

| streams | tokens a round | drafts a round | accepted | ms a round | requests |
|---:|---:|---:|---:|---:|---:|
| 1 | 1.011 | 0.0 |  | 6.75 | 217 |

### ruler-after

| streams | prose total (a stream) | code total (a stream) | structured total (a stream) | list total (a stream) | first token |
|---:|---:|---:|---:|---:|---:|
| 1 | 149.3 (149.3) | 149.2 (149.2) | 149.7 (149.7) | 149.3 (149.3) | 0.03-0.03 s |

Engine rounds (ruler-after):

| streams | tokens a round | drafts a round | accepted | ms a round | requests |
|---:|---:|---:|---:|---:|---:|
| 1 | 1.007 | 0.0 |  | 6.74 | 1781 |

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
| tools | 58/60 |
| json | 30/30 |
| ifeval | 120/150 |
| gsm8k | 241/250 |
| mgsm | 190/240 |
| mmlu | 279/342 |
| humaneval | 153/164 |
| repetition | 8/8 |
| long-context | 55/55 |
| vision | 12/12 |
| soak | 60/60 |
| snapshot | 12/12 |

### checks

| check | result |
|---|---|
| memory-idle | measured: gpu: 28716 MiB, 32607 MiB |
| structured | pass: 18/18 obey; a bad regex -> 400 |
| sampling | pass: 9/9 seeded replies equal on repeat; 0 errors |
| turns | pass: resumed == again == cold: True; cached 5832 of 5865; ttft resumed 0.053s, cold 0.134s |
| capacity | pass: 6/6 answered, 0 refused, 0 lost (no reply); a short request after: 200 |

## 2026-10-15 17:33: run `20261015-173359-full`

Plan full, running; served as `nemotron-bolt`.

Serving: recipe_commit `d3274f7`; engine_commit `58a647f6`; served_model `{"object": "list", "data": [{"id": "nemotron-bolt", "object": "model", "created": 17920856`

### ruler-fresh

| streams | prose total (a stream) | code total (a stream) | structured total (a stream) | list total (a stream) | first token |
|---:|---:|---:|---:|---:|---:|
| 1 | 150.0 (150.0) | 149.8 (149.8) | 150.2 (150.2) | 149.8 (149.8) | 0.02-0.02 s |

Engine rounds (ruler-fresh):

| streams | tokens a round | drafts a round | accepted | ms a round | requests |
|---:|---:|---:|---:|---:|---:|
| 1 | 1.011 | 0.0 |  | 6.74 | 878 |

### checks

| check | result |
|---|---|
| memory-idle | measured: gpu: 27954 MiB, 32607 MiB |

## 2026-10-15 17:22: run `20261015-172206-quick`

Plan quick, done; served as `nemotron-bolt`.

Serving: recipe_commit `3f90fea`; engine_commit `159ea92d`; served_model `{"object": "list", "data": [{"id": "nemotron-bolt", "object": "model", "created": 17920849`

### ruler-fresh

| streams | prose total (a stream) | code total (a stream) | structured total (a stream) | list total (a stream) | first token |
|---:|---:|---:|---:|---:|---:|
| 1 | 150.0 (150.0) | 149.8 (149.8) | 150.2 (150.2) | 149.8 (149.8) | 0.02-0.03 s |

Engine rounds (ruler-fresh):

| streams | tokens a round | drafts a round | accepted | ms a round | requests |
|---:|---:|---:|---:|---:|---:|
| 1 | 1.01 | 0.0 |  | 6.73 | 295 |

### ruler-after

| streams | prose total (a stream) | code total (a stream) | structured total (a stream) | list total (a stream) | first token |
|---:|---:|---:|---:|---:|---:|
| 1 | 149.7 (149.7) | 149.6 (149.6) | 150.2 (150.2) | 149.4 (149.4) | 0.02-0.02 s |

Engine rounds (ruler-after):

| streams | tokens a round | drafts a round | accepted | ms a round | requests |
|---:|---:|---:|---:|---:|---:|
| 1 | 1.01 | 0.0 |  | 6.74 | 330 |

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
| memory-idle | measured: gpu: 28552 MiB, 32607 MiB |
| structured | FAIL: 0/18 obey; a bad regex -> 400; failed json_object/greedy, json_object/sampled, json_object/thinking, json_schema/greedy, json_schema/sampled, json_schema/thinking, guided_json/greedy, guided_json/sampled, guided_json/thinking, regex/greedy, regex/sampled, regex/thinking, choice/greedy, choice/sampled, choice/thinking, grammar/greedy, grammar/sampled, grammar/thinking |
| sampling | pass: 9/9 seeded replies equal on repeat; 0 errors |
| turns | pass: resumed == again == cold: True; cached 5832 of 5865; ttft resumed 0.035s, cold 0.747s |

## 2026-10-15 17:13: run `20261015-171302-quick`

Plan quick, done; served as `nemotron-bolt`.

Serving: recipe_commit `3f90fea`; engine_commit `ca6fd71f`; served_model `{"object": "list", "data": [{"id": "nemotron-bolt", "object": "model", "created": 17920843`

### ruler-fresh

| streams | prose total (a stream) | code total (a stream) | structured total (a stream) | list total (a stream) | first token |
|---:|---:|---:|---:|---:|---:|
| 1 | 149.8 (149.8) | 149.6 (149.6) | 150.1 (150.1) | 149.7 (149.7) | 0.02-0.04 s |

Engine rounds (ruler-fresh):

| streams | tokens a round | drafts a round | accepted | ms a round | requests |
|---:|---:|---:|---:|---:|---:|
| 1 | 1.005 | 0.0 |  | 6.71 | 12 |

### ruler-after

| streams | prose total (a stream) | code total (a stream) | structured total (a stream) | list total (a stream) | first token |
|---:|---:|---:|---:|---:|---:|
| 1 | 149.6 (149.6) | 149.6 (149.6) | 150.1 (150.1) | 149.5 (149.5) | 0.02-0.02 s |

Engine rounds (ruler-after):

| streams | tokens a round | drafts a round | accepted | ms a round | requests |
|---:|---:|---:|---:|---:|---:|
| 1 | 1.008 | 0.0 |  | 6.73 | 47 |

### suite

| check | passed |
|---|---:|
| soak | 0/60 |
| drafts | 12/12 |
| concurrent | 12/12 |
| streaming | 1/4 |
| multiturn | 8/8 |
| stop | 3/3 |
| thinking | 10/10 |
| copy | 2/2 |
| max-tokens | 3/3 |

### checks

| check | result |
|---|---|
| memory-idle | measured: gpu: 28552 MiB, 32607 MiB |
| structured | FAIL: 0/18 obey; a bad regex -> 400; failed json_object/greedy, json_object/sampled, json_object/thinking, json_schema/greedy, json_schema/sampled, json_schema/thinking, guided_json/greedy, guided_json/sampled, guided_json/thinking, regex/greedy, regex/sampled, regex/thinking, choice/greedy, choice/sampled, choice/thinking, grammar/greedy, grammar/sampled, grammar/thinking |
| sampling | FAIL: 6/9 seeded replies equal on repeat; 0 errors |
| turns | pass: resumed == again == cold: True; cached 5832 of 5865; ttft resumed 0.035s, cold 0.747s |

