# qwen38-27b-5090-q35speed on ?

Target `qwen38-27b-5090-q35speed`: . Engine: ?. Rendered from `stats/qwen38-27b-5090-q35speed.json` (3 runs); aggregate tok/s, total (a stream).

## 2026-10-19 22:26: run `20261019-222616-thinking`

Plan thinking, done; served as `qwen38-27b`.

Serving: recipe_commit `6f7277d`; engine_commit `29eb2574`; served_model `{"object": "list", "data": [{"id": "qwen38-27b", "object": "model", "created": 1792448776,`

### suite-thinking

| check | passed |
|---|---:|
| gsm8k | 222/250 |

### checks

| check | result |
|---|---|
| thinking | pass: thinking on: 10/10 right, 10/10 with reasoning_content, 0 leaks, 0 errors |

## 2026-10-19 21:44: run `20261019-214404-full`

Plan full, done; served as `qwen38-27b`.

Serving: recipe_commit `6f7277d`; engine_commit `29eb2574`; served_model `{"object": "list", "data": [{"id": "qwen38-27b", "object": "model", "created": 1792446292,`

### ruler-fresh

| streams | prose total (a stream) | code total (a stream) | structured total (a stream) | list total (a stream) | first token |
|---:|---:|---:|---:|---:|---:|
| 1 | 235.8 (235.8) | 436.8 (436.8) | 292.7 (292.7) | 288.5 (288.5) | 0.10-0.10 s |

### ruler-after

| streams | prose total (a stream) | code total (a stream) | structured total (a stream) | list total (a stream) | first token |
|---:|---:|---:|---:|---:|---:|
| 1 | 238.0 (238.0) | 423.6 (423.6) | 291.4 (291.4) | 287.1 (287.1) | 0.10-0.10 s |

### suite

| check | passed |
|---|---:|
| drafts | 12/12 |
| concurrent | 12/12 |
| streaming | 4/4 |
| multiturn | 7/8 |
| stop | 3/3 |
| thinking | 10/10 |
| copy | 2/2 |
| max-tokens | 3/3 |
| tools | 59/60 |
| json | 30/30 |
| ifeval | 126/150 |
| gsm8k | 238/250 |
| mgsm | 214/240 |
| mmlu | 270/342 |
| humaneval | 0/0 |
| repetition | 8/8 |
| long-context | 55/55 |
| vision | 12/12 |
| soak | 60/60 |
| snapshot | 12/12 |

### checks

| check | result |
|---|---|
| memory-idle | measured: gpu: 28058 MiB, 32607 MiB |
| sampling | pass: 9/9 seeded replies equal on repeat and undrafted; 0 errors |

## 2026-10-19 18:52: run `20261019-185213-speed`

Plan speed, done; served as `qwen38-27b`.

Serving: recipe_commit `6f7277d`; engine_commit `12fa9d63`; served_model `{"object": "list", "data": [{"id": "qwen38-27b", "object": "model", "created": 1792435986,`

### ruler-fresh

| streams | prose total (a stream) | code total (a stream) | structured total (a stream) | list total (a stream) | first token |
|---:|---:|---:|---:|---:|---:|
| 1 | 243.3 (243.3) | 450.8 (450.8) | 293.6 (293.6) | 283.5 (283.5) | 0.10-0.10 s |

### checks

| check | result |
|---|---|
| memory-idle | measured: gpu: 26892 MiB, 32607 MiB |
| memory-busy | measured: gpu: 26896 MiB, 32607 MiB |

