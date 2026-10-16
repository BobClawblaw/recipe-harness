# Step-5-Preview, MLX 2-bit experts (8-bit rest) + MTP on 1x Apple M5 Ultra (256 GB unified), macOS

Target `step5-m5`: Step-5-Preview 2-bit (experts 2/128, rest 8/64, MTP, images), TensorFold native Metal on one M5 Ultra. Engine: TensorFold native, Metal. Rendered from `stats/step5-m5.json` (3 runs); aggregate tok/s, total (a stream).

## 2026-10-15 19:44: run `20261015-194421-one-stream`

Plan one-stream, done; served as `step5-preview`.

Serving: engine_commit `6e791da6`; binary_sha256 `be201a04b22bc474aa9f61091078dd7d07354b61683cd1ac0eed12374e3ddaab`; served_model `{"object": "list", "data": [{"id": "step5-preview", "object": "model", "created": 17921115`; chip `Apple M5 Ultra; 274877906944`

### ruler-fresh

| streams | prose total (a stream) | code total (a stream) | structured total (a stream) | list total (a stream) | first token |
|---:|---:|---:|---:|---:|---:|
| 1 | 39.3 (39.3) | 50.9 (50.9) | 40.7 (40.7) | 48.3 (48.3) | 0.24-0.28 s |

Engine rounds (ruler-fresh):

| streams | tokens a round | drafts a round | accepted | ms a round | requests |
|---:|---:|---:|---:|---:|---:|
| 1 | 2.381 | 2.072 | 67% | 53.15 | 12 |

### ruler-after

| streams | prose total (a stream) | code total (a stream) | structured total (a stream) | list total (a stream) | first token |
|---:|---:|---:|---:|---:|---:|
| 1 | 39.1 (39.1) | 50.6 (50.6) | 40.6 (40.6) | 48.2 (48.2) | 0.24-0.28 s |

Engine rounds (ruler-after):

| streams | tokens a round | drafts a round | accepted | ms a round | requests |
|---:|---:|---:|---:|---:|---:|
| 1 | 2.339 | 1.939 | 69% | 52.39 | 13 |

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
| tools | 58/60 |
| json | 30/30 |
| gsm8k | 49/50 |
| ifeval | 41/50 |

### checks

| check | result |
|---|---|
| memory-idle | measured: mac: System-wide memory free percentage: 27%; total = 4096.00M  us |
| sampling | pass: 9/9 seeded replies equal on repeat and undrafted; 0 errors |
| memory-busy | measured: mac: System-wide memory free percentage: 27%; total = 4096.00M  us |

## 2026-10-15 19:28: run `20261015-192840-quick`

Plan quick, done; served as `step5-preview`.

Serving: engine_commit `6e791da6`; binary_sha256 `be201a04b22bc474aa9f61091078dd7d07354b61683cd1ac0eed12374e3ddaab`; served_model `{"object": "list", "data": [{"id": "step5-preview", "object": "model", "created": 17921105`; chip `Apple M5 Ultra; 274877906944`

### ruler-fresh

| streams | prose total (a stream) | code total (a stream) | structured total (a stream) | list total (a stream) | first token |
|---:|---:|---:|---:|---:|---:|
| 1 | 39.1 (39.1) | 50.5 (50.5) | 40.6 (40.6) | 48.0 (48.0) | 0.24-0.28 s |

Engine rounds (ruler-fresh):

| streams | tokens a round | drafts a round | accepted | ms a round | requests |
|---:|---:|---:|---:|---:|---:|
| 1 | 2.381 | 2.072 | 67% | 53.42 | 12 |

### ruler-after

| streams | prose total (a stream) | code total (a stream) | structured total (a stream) | list total (a stream) | first token |
|---:|---:|---:|---:|---:|---:|
| 1 | 39.1 (39.1) | 50.5 (50.5) | 40.6 (40.6) | 48.1 (48.1) | 0.24-0.28 s |

Engine rounds (ruler-after):

| streams | tokens a round | drafts a round | accepted | ms a round | requests |
|---:|---:|---:|---:|---:|---:|
| 1 | 2.382 | 2.087 | 66% | 53.44 | 13 |

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
| memory-idle | measured: mac: System-wide memory free percentage: 27%; total = 4096.00M  us |
| structured | pass: 18/18 obey; a bad regex -> 400 |
| sampling | pass: 9/9 seeded replies equal on repeat and undrafted; 0 errors |
| turns | pass: resumed == again == cold: True; cached 4514 of 4618; ttft resumed 0.348s, cold 3.277s |

## 2026-10-15 13:43: run `20261015-134330-one-stream`

Plan one-stream, done; served as `step5-preview`.

Serving: engine_commit `aa221b11`; binary_sha256 `4f89cf81182d203e84aac48335e84a90a29ba6ae26de96b32ec387e50c7e878f`; served_model `{"object": "list", "data": [{"id": "step5-preview", "object": "model", "created": 17920898`; chip `Apple M5 Ultra; 274877906944`

### ruler-fresh

| streams | prose total (a stream) | code total (a stream) | structured total (a stream) | list total (a stream) | first token |
|---:|---:|---:|---:|---:|---:|
| 1 | 39.2 (39.2) | 50.6 (50.6) | 40.7 (40.7) | 48.2 (48.2) | 0.23-0.27 s |

Engine rounds (ruler-fresh):

| streams | tokens a round | drafts a round | accepted | ms a round | requests |
|---:|---:|---:|---:|---:|---:|
| 1 | 2.381 | 2.072 | 67% | 53.3 | 12 |

### ruler-after

| streams | prose total (a stream) | code total (a stream) | structured total (a stream) | list total (a stream) | first token |
|---:|---:|---:|---:|---:|---:|
| 1 | 39.2 (39.2) | 50.6 (50.6) | 40.6 (40.6) | 48.1 (48.1) | 0.23-0.27 s |

Engine rounds (ruler-after):

| streams | tokens a round | drafts a round | accepted | ms a round | requests |
|---:|---:|---:|---:|---:|---:|
| 1 | 2.339 | 1.939 | 69% | 52.42 | 13 |

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
| tools | 58/60 |
| json | 30/30 |
| gsm8k | 49/50 |
| ifeval | 41/50 |

### checks

| check | result |
|---|---|
| memory-idle | measured: mac: System-wide memory free percentage: 95%; total = 2048.00M  us |
| sampling | pass: 9/9 seeded replies equal on repeat and undrafted; 0 errors |
| memory-busy | measured: mac: System-wide memory free percentage: 28%; total = 2048.00M  us |

