# MiniMax-M3.1-Flash, EXL3 3.06 bpw (Mia-AiLab EAQ v1), 256k context on 1x Apple M5 Ultra (256 GB unified), macOS

Target `minimax-m31-exl3-m5`: MiniMax-M3.1-Flash, EXL3 3.06 bpw (Mia-AiLab EAQ v1), 256k context, TensorFold native Metal on one M5 Ultra. Engine: TensorFold native, Metal. Rendered from `stats/minimax-m31-exl3-m5.json` (10 runs); aggregate tok/s, total (a stream).

## 2026-10-29 08:50: run `20261029-085020-speed`

Plan speed, done; served as `MiniMax-M3.1-Flash`.

Serving: engine_commit `ac35cd022`; binary_sha256 `4b73bfa0dda82843ef2c27099e9ed883d9ab4dd8de31f6d7c42026f2bdc1bc1b`; served_model `{"object": "list", "data": [{"id": "MiniMax-M3.1-Flash", "object": "model", "created": 179`; chip `Apple M5 Ultra; 274877906944`; suite_commit `21db9b23f7be`

### ruler-fresh

| streams | prose total (a stream) | code total (a stream) | structured total (a stream) | list total (a stream) | first token |
|---:|---:|---:|---:|---:|---:|
| 1 | 17.9 (17.9) | 20.0 (20.0) | 17.7 (17.7) | 18.5 (18.5) | 1.52-1.62 s |
| 2 | 22.9 (11.4) | 21.3 (10.7) | 21.8 (10.9) | 23.6 (11.8) | 2.28-2.41 s |

Engine rounds (ruler-fresh):

| streams | tokens a round | drafts a round | accepted | ms a round | requests |
|---:|---:|---:|---:|---:|---:|
| 1 | 1.461 | 0.609 | 75% | 78.76 | 12 |
| 2 | 1.388 | 0.447 | 86% | 123.91 | 25 |

### ruler-after

| streams | prose total (a stream) | code total (a stream) | structured total (a stream) | list total (a stream) | first token |
|---:|---:|---:|---:|---:|---:|
| 1 | 17.6 (17.6) | 19.8 (19.8) | 17.7 (17.7) | 18.8 (18.8) | 1.51-1.60 s |

Engine rounds (ruler-after):

| streams | tokens a round | drafts a round | accepted | ms a round | requests |
|---:|---:|---:|---:|---:|---:|
| 1 | 1.415 | 0.555 | 74% | 76.5 | 13 |

### checks

| check | result |
|---|---|
| memory-idle | measured: mac: System-wide memory free percentage: 31%; total = 5120.00M  us |
| turns | pass: resumed == again: True; cold (after a restart): True; cached 4645 of 4725; ttft resumed 1.299s, cold 12.206s |
| memory-busy | measured: mac: System-wide memory free percentage: 30%; total = 5120.00M  us |

## 2026-10-29 08:23: run `20261029-082303-quick`

Plan quick, done; served as `MiniMax-M3.1-Flash`.

Serving: engine_commit `ac35cd022`; binary_sha256 `4b73bfa0dda82843ef2c27099e9ed883d9ab4dd8de31f6d7c42026f2bdc1bc1b`; served_model `{"object": "list", "data": [{"id": "MiniMax-M3.1-Flash", "object": "model", "created": 179`; chip `Apple M5 Ultra; 274877906944`; suite_commit `21db9b23f7be`

### ruler-fresh

| streams | prose total (a stream) | code total (a stream) | structured total (a stream) | list total (a stream) | first token |
|---:|---:|---:|---:|---:|---:|
| 1 | 18.6 (18.6) | 20.1 (20.1) | 17.7 (17.7) | 18.8 (18.8) | 1.52-1.61 s |

Engine rounds (ruler-fresh):

| streams | tokens a round | drafts a round | accepted | ms a round | requests |
|---:|---:|---:|---:|---:|---:|
| 1 | 1.376 | 0.477 | 78% | 73.27 | 12 |

### ruler-after

| streams | prose total (a stream) | code total (a stream) | structured total (a stream) | list total (a stream) | first token |
|---:|---:|---:|---:|---:|---:|
| 1 | 18.6 (18.6) | 20.3 (20.3) | 17.8 (17.8) | 18.6 (18.6) | 1.52-1.61 s |

Engine rounds (ruler-after):

| streams | tokens a round | drafts a round | accepted | ms a round | requests |
|---:|---:|---:|---:|---:|---:|
| 1 | 1.409 | 0.528 | 77% | 74.82 | 13 |

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
| memory-idle | measured: mac: System-wide memory free percentage: 29%; total = 7168.00M  us |
| structured | pass: 18/18 obey, drafted == plain 12/12; a bad regex -> 400 |
| tools | pass: 5/5 tool cases right |
| sampling | pass: 9/9 seeded replies equal on repeat and undrafted; 0 errors |
| turns | pass: resumed == again: True; cold (after a restart): True; cached 4645 of 4725; ttft resumed 1.289s, cold 11.913s |
| urls | FAIL: public 400; loopback 400; http 400; unexpected: ['public'] |

## 2026-10-29 08:02: run `20261029-080202-prefill`

Plan prefill, done; served as `MiniMax-M3.1-Flash`.

Serving: engine_commit `dbcb9d791`; binary_sha256 `42ea5cbbab682611357ddc6b7a865150a1a88f410ea9e7777c834587236bcd5e`; served_model `{"object": "list", "data": [{"id": "MiniMax-M3.1-Flash", "object": "model", "created": 179`; chip `Apple M5 Ultra; 274877906944`; suite_commit `21db9b23f7be`

### checks

| check | result |
|---|---|
| memory-idle | measured: mac: System-wide memory free percentage: 32%; total = 4096.00M  us |
| prefill-off | measured: 2217 tokens 434.0 tok/s (5.108 s), 8362 tokens 485.5 tok/s (17.222 s), 32943 tokens 508.8 tok/s (64.742 s), 131243 tokens 501.4 tok/s (261.759 s) |
| prefill-thinking | measured: 2216 tokens 432.6 tok/s (5.122 s), 8360 tokens 486.4 tok/s (17.187 s), 32940 tokens 505.4 tok/s (65.177 s), 131242 tokens 483.4 tok/s (271.492 s) |
| memory-busy | measured: mac: System-wide memory free percentage: 25%; total = 4096.00M  us |

## 2026-10-29 07:51: run `20261029-075115-speed`

Plan speed, done; served as `MiniMax-M3.1-Flash`.

Serving: engine_commit `dbcb9d791`; binary_sha256 `42ea5cbbab682611357ddc6b7a865150a1a88f410ea9e7777c834587236bcd5e`; served_model `{"object": "list", "data": [{"id": "MiniMax-M3.1-Flash", "object": "model", "created": 179`; chip `Apple M5 Ultra; 274877906944`; suite_commit `21db9b23f7be`

### ruler-fresh

| streams | prose total (a stream) | code total (a stream) | structured total (a stream) | list total (a stream) | first token |
|---:|---:|---:|---:|---:|---:|
| 1 | 19.5 (19.5) | 19.5 (19.5) | 19.5 (19.5) | 19.5 (19.5) | 1.48-1.56 s |
| 2 | 24.2 (12.1) | 23.8 (11.9) | 24.2 (12.1) | 23.6 (11.8) | 2.22-2.33 s |

Engine rounds (ruler-fresh):

| streams | tokens a round | drafts a round | accepted | ms a round | requests |
|---:|---:|---:|---:|---:|---:|
| 1 | 1.005 | 0.0 |  | 51.42 | 12 |
| 2 | 1.005 | 0.0 |  | 83.92 | 25 |

### ruler-after

| streams | prose total (a stream) | code total (a stream) | structured total (a stream) | list total (a stream) | first token |
|---:|---:|---:|---:|---:|---:|
| 1 | 19.5 (19.5) | 19.5 (19.5) | 19.5 (19.5) | 19.5 (19.5) | 1.48-1.57 s |

Engine rounds (ruler-after):

| streams | tokens a round | drafts a round | accepted | ms a round | requests |
|---:|---:|---:|---:|---:|---:|
| 1 | 1.005 | 0.0 |  | 51.45 | 13 |

### checks

| check | result |
|---|---|
| memory-idle | measured: mac: System-wide memory free percentage: 33%; total = 4096.00M  us |
| turns | pass: resumed == again: True; cold (after a restart): True; cached 4645 of 4725; ttft resumed 1.273s, cold 11.241s |
| memory-busy | measured: mac: System-wide memory free percentage: 32%; total = 4096.00M  us |

## 2026-10-29 07:50: run `20261029-075003-glm-vision`

Plan glm-vision, done; served as `MiniMax-M3.1-Flash`.

Serving: engine_commit `dbcb9d791`; binary_sha256 `42ea5cbbab682611357ddc6b7a865150a1a88f410ea9e7777c834587236bcd5e`; served_model `{"object": "list", "data": [{"id": "MiniMax-M3.1-Flash", "object": "model", "created": 179`; chip `Apple M5 Ultra; 274877906944`; suite_commit `21db9b23f7be`

### suite-vision

| check | passed |
|---|---:|
| vision | 3/6 |
| vision-concurrent | 12/16 |

## 2026-10-29 07:24: run `20261029-072424-quick`

Plan quick, done; served as `MiniMax-M3.1-Flash`.

Serving: engine_commit `dbcb9d791`; binary_sha256 `42ea5cbbab682611357ddc6b7a865150a1a88f410ea9e7777c834587236bcd5e`; served_model `{"object": "list", "data": [{"id": "MiniMax-M3.1-Flash", "object": "model", "created": 179`; chip `Apple M5 Ultra; 274877906944`; suite_commit `21db9b23f7be`

### ruler-fresh

| streams | prose total (a stream) | code total (a stream) | structured total (a stream) | list total (a stream) | first token |
|---:|---:|---:|---:|---:|---:|
| 1 | 19.5 (19.5) | 19.5 (19.5) | 19.5 (19.5) | 19.6 (19.6) | 1.48-1.57 s |

Engine rounds (ruler-fresh):

| streams | tokens a round | drafts a round | accepted | ms a round | requests |
|---:|---:|---:|---:|---:|---:|
| 1 | 1.005 | 0.0 |  | 51.41 | 12 |

### ruler-after

| streams | prose total (a stream) | code total (a stream) | structured total (a stream) | list total (a stream) | first token |
|---:|---:|---:|---:|---:|---:|
| 1 | 19.5 (19.5) | 19.5 (19.5) | 19.5 (19.5) | 19.5 (19.5) | 1.48-1.56 s |

Engine rounds (ruler-after):

| streams | tokens a round | drafts a round | accepted | ms a round | requests |
|---:|---:|---:|---:|---:|---:|
| 1 | 1.005 | 0.0 |  | 51.56 | 13 |

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
| memory-idle | measured: mac: System-wide memory free percentage: 32%; total = 5120.00M  us |
| structured | pass: 18/18 obey, drafted == plain 12/12; a bad regex -> 400 |
| tools | pass: 5/5 tool cases right |
| sampling | pass: 9/9 seeded replies equal on repeat and undrafted; 0 errors |
| turns | pass: resumed == again: True; cold (after a restart): True; cached 4645 of 4725; ttft resumed 1.271s, cold 11.241s |
| urls | FAIL: public 400; loopback 400; http 400; unexpected: ['public'] |

## 2026-10-29 07:06: run `20261029-070637-prefill`

Plan prefill, done; served as `MiniMax-M3.1-Flash`.

Serving: engine_commit `fda39c320`; binary_sha256 `bd364361c51159f64136a48a5a7faec8086585a45caaa7740fe972694ce51ce9`; served_model `{"object": "list", "data": [{"id": "MiniMax-M3.1-Flash", "object": "model", "created": 179`; chip `Apple M5 Ultra; 274877906944`; suite_commit `21db9b23f7be`

### checks

| check | result |
|---|---|
| memory-idle | measured: mac: System-wide memory free percentage: 33%; total = 5120.00M  us |
| prefill-off | measured: 2217 tokens 435.1 tok/s (5.095 s), 8363 tokens 486.6 tok/s (17.186 s), 32942 tokens 509.4 tok/s (64.672 s), 131244 tokens 502.4 tok/s (261.25 s) |
| prefill-thinking | measured: 2218 tokens 432.5 tok/s (5.128 s), 8366 tokens 486.1 tok/s (17.212 s), 32939 tokens 509.9 tok/s (64.598 s), 131243 tokens 503.2 tok/s (260.826 s) |
| memory-busy | measured: mac: System-wide memory free percentage: 26%; total = 5120.00M  us |

## 2026-10-29 06:55: run `20261029-065551-speed`

Plan speed, done; served as `MiniMax-M3.1-Flash`.

Serving: engine_commit `fda39c320`; binary_sha256 `bd364361c51159f64136a48a5a7faec8086585a45caaa7740fe972694ce51ce9`; served_model `{"object": "list", "data": [{"id": "MiniMax-M3.1-Flash", "object": "model", "created": 179`; chip `Apple M5 Ultra; 274877906944`; suite_commit `21db9b23f7be`

### ruler-fresh

| streams | prose total (a stream) | code total (a stream) | structured total (a stream) | list total (a stream) | first token |
|---:|---:|---:|---:|---:|---:|
| 1 | 19.5 (19.5) | 19.5 (19.5) | 19.5 (19.5) | 19.6 (19.6) | 1.48-1.57 s |
| 2 | 24.2 (12.1) | 23.8 (11.9) | 24.2 (12.1) | 23.6 (11.8) | 2.22-2.35 s |

Engine rounds (ruler-fresh):

| streams | tokens a round | drafts a round | accepted | ms a round | requests |
|---:|---:|---:|---:|---:|---:|
| 1 | 1.005 | 0.0 |  | 51.42 | 12 |
| 2 | 1.005 | 0.0 |  | 83.93 | 25 |

### ruler-after

| streams | prose total (a stream) | code total (a stream) | structured total (a stream) | list total (a stream) | first token |
|---:|---:|---:|---:|---:|---:|
| 1 | 19.5 (19.5) | 19.5 (19.5) | 19.5 (19.5) | 19.5 (19.5) | 1.48-1.56 s |

Engine rounds (ruler-after):

| streams | tokens a round | drafts a round | accepted | ms a round | requests |
|---:|---:|---:|---:|---:|---:|
| 1 | 1.005 | 0.0 |  | 51.48 | 13 |

### checks

| check | result |
|---|---|
| memory-idle | measured: mac: System-wide memory free percentage: 33%; total = 5120.00M  us |
| turns | pass: resumed == again: True; cold (after a restart): True; cached 4645 of 4725; ttft resumed 1.279s, cold 11.254s |
| memory-busy | measured: mac: System-wide memory free percentage: 32%; total = 5120.00M  us |

## 2026-10-29 06:54: run `20261029-065438-glm-vision`

Plan glm-vision, done; served as `MiniMax-M3.1-Flash`.

Serving: engine_commit `fda39c320`; binary_sha256 `bd364361c51159f64136a48a5a7faec8086585a45caaa7740fe972694ce51ce9`; served_model `{"object": "list", "data": [{"id": "MiniMax-M3.1-Flash", "object": "model", "created": 179`; chip `Apple M5 Ultra; 274877906944`; suite_commit `21db9b23f7be`

### suite-vision

| check | passed |
|---|---:|
| vision | 3/6 |
| vision-concurrent | 12/16 |

## 2026-10-29 06:29: run `20261029-062901-quick`

Plan quick, done; served as `MiniMax-M3.1-Flash`.

Serving: engine_commit `0f20fb9af`; binary_sha256 `bd364361c51159f64136a48a5a7faec8086585a45caaa7740fe972694ce51ce9`; served_model `{"object": "list", "data": [{"id": "MiniMax-M3.1-Flash", "object": "model", "created": 179`; chip `Apple M5 Ultra; 274877906944`; suite_commit `21db9b23f7be`

### ruler-fresh

| streams | prose total (a stream) | code total (a stream) | structured total (a stream) | list total (a stream) | first token |
|---:|---:|---:|---:|---:|---:|
| 1 | 19.5 (19.5) | 19.5 (19.5) | 19.5 (19.5) | 19.5 (19.5) | 1.48-1.56 s |

Engine rounds (ruler-fresh):

| streams | tokens a round | drafts a round | accepted | ms a round | requests |
|---:|---:|---:|---:|---:|---:|
| 1 | 1.005 | 0.0 |  | 51.55 | 12 |

### ruler-after

| streams | prose total (a stream) | code total (a stream) | structured total (a stream) | list total (a stream) | first token |
|---:|---:|---:|---:|---:|---:|
| 1 | 19.5 (19.5) | 19.5 (19.5) | 19.5 (19.5) | 19.5 (19.5) | 1.48-1.56 s |

Engine rounds (ruler-after):

| streams | tokens a round | drafts a round | accepted | ms a round | requests |
|---:|---:|---:|---:|---:|---:|
| 1 | 1.005 | 0.0 |  | 51.44 | 13 |

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
| memory-idle | measured: mac: System-wide memory free percentage: 33%; total = 5120.00M  us |
| structured | pass: 18/18 obey, drafted == plain 12/12; a bad regex -> 400 |
| tools | pass: 5/5 tool cases right |
| sampling | pass: 9/9 seeded replies equal on repeat and undrafted; 0 errors |
| turns | pass: resumed == again: True; cold (after a restart): True; cached 4645 of 4725; ttft resumed 1.277s, cold 11.241s |
| urls | FAIL: public 400; loopback 400; http 400; unexpected: ['public'] |

