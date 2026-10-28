# Nanbeige4.3-33B, MLX 8-bit on 1x Apple M5 Ultra (256 GB unified), macOS

Target `nanbeige43-33b-mlx8-m5`: Nanbeige4.3-33B MLX 8-bit as published (fcmeyer/Nanbeige4.3-33B-MLX-8bit), TensorFold native Metal (llama) on one M5 Ultra (131072-token window, 2 streams). Engine: TensorFold native, Metal. Rendered from `stats/nanbeige43-33b-mlx8-m5.json` (3 runs); aggregate tok/s, total (a stream).

## 2026-10-27 10:32: run `20261027-103259-quick`

Plan quick, done; served as `nanbeige`.

Serving: engine_commit `657ac711c`; binary_sha256 `56fb3ebeaa8facd66a071318c4602df8920f6675171b8a3b093c639695609e9c`; served_model `{"object": "list", "data": [{"id": "nanbeige", "object": "model", "created": 1793115187, "`; chip `Apple M5 Ultra; 274877906944`; suite_commit `a7ba7e392d57`

### ruler-fresh

| streams | prose total (a stream) | code total (a stream) | structured total (a stream) | list total (a stream) | first token |
|---:|---:|---:|---:|---:|---:|
| 1 | 28.4 (28.4) | 27.9 (27.9) | 28.3 (28.3) | 28.3 (28.3) | 0.15-0.16 s |

Engine rounds (ruler-fresh):

| streams | tokens a round | drafts a round | accepted | ms a round | requests |
|---:|---:|---:|---:|---:|---:|
| 1 | 1.005 | 0.017 | 0% | 35.58 | 12 |

### ruler-after

| streams | prose total (a stream) | code total (a stream) | structured total (a stream) | list total (a stream) | first token |
|---:|---:|---:|---:|---:|---:|
| 1 | 28.3 (28.3) | 27.8 (27.8) | 28.3 (28.3) | 28.3 (28.3) | 0.15-0.16 s |

Engine rounds (ruler-after):

| streams | tokens a round | drafts a round | accepted | ms a round | requests |
|---:|---:|---:|---:|---:|---:|
| 1 | 1.007 | 0.022 | 10% | 35.76 | 13 |

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
| memory-idle | measured: mac: System-wide memory free percentage: 46%; total = 4096.00M  us |
| structured | pass: 18/18 obey, drafted == plain 12/12; a bad regex -> 400 |
| tools | pass: 5/5 tool cases right |
| sampling | pass: 9/9 seeded replies equal on repeat and undrafted; 0 errors |
| turns | pass: resumed == again: True; cold (after a restart): True; cached 5493 of 5649; ttft resumed 0.275s, cold 4.494s |

## 2026-10-27 10:18: run `20261027-101853-prefill-64k`

Plan prefill-64k, done; served as `nanbeige`.

Serving: engine_commit `657ac711c`; binary_sha256 `56fb3ebeaa8facd66a071318c4602df8920f6675171b8a3b093c639695609e9c`; served_model `{"object": "list", "data": [{"id": "nanbeige", "object": "model", "created": 1793114341, "`; chip `Apple M5 Ultra; 274877906944`; suite_commit `a7ba7e392d57`

### checks

| check | result |
|---|---|
| memory-idle | measured: mac: System-wide memory free percentage: 46%; total = 4096.00M  us |
| prefill-off | measured: 2107 tokens 1268.5 tok/s (1.661 s), 8253 tokens 1253.3 tok/s (6.585 s), 32828 tokens 1022.2 tok/s (32.115 s), 61499 tokens 832.2 tok/s (73.896 s) |
| prefill-thinking | measured: 2106 tokens 1248.4 tok/s (1.687 s), 8249 tokens 1220.6 tok/s (6.758 s), 32827 tokens 996.9 tok/s (32.93 s), 61495 tokens 793.0 tok/s (77.543 s) |
| memory-busy | measured: mac: System-wide memory free percentage: 42%; total = 4096.00M  us |

## 2026-10-27 10:13: run `20261027-101318-speed`

Plan speed, done; served as `nanbeige`.

Serving: engine_commit `657ac711c`; binary_sha256 `56fb3ebeaa8facd66a071318c4602df8920f6675171b8a3b093c639695609e9c`; served_model `{"object": "list", "data": [{"id": "nanbeige", "object": "model", "created": 1793114006, "`; chip `Apple M5 Ultra; 274877906944`; suite_commit `a7ba7e392d57`

### ruler-fresh

| streams | prose total (a stream) | code total (a stream) | structured total (a stream) | list total (a stream) | first token |
|---:|---:|---:|---:|---:|---:|
| 1 | 28.4 (28.4) | 27.9 (27.9) | 28.3 (28.3) | 28.3 (28.3) | 0.15-0.16 s |
| 2 | 51.5 (25.8) | 49.2 (24.6) | 51.3 (25.7) | 51.5 (25.8) | 0.22-0.24 s |

Engine rounds (ruler-fresh):

| streams | tokens a round | drafts a round | accepted | ms a round | requests |
|---:|---:|---:|---:|---:|---:|
| 1 | 1.005 | 0.017 | 0% | 35.61 | 12 |
| 2 | 1.023 | 0.059 | 30% | 40.18 | 25 |

### ruler-after

| streams | prose total (a stream) | code total (a stream) | structured total (a stream) | list total (a stream) | first token |
|---:|---:|---:|---:|---:|---:|
| 1 | 28.3 (28.3) | 27.9 (27.9) | 28.3 (28.3) | 28.3 (28.3) | 0.15-0.16 s |

Engine rounds (ruler-after):

| streams | tokens a round | drafts a round | accepted | ms a round | requests |
|---:|---:|---:|---:|---:|---:|
| 1 | 1.007 | 0.022 | 10% | 35.69 | 13 |

### checks

| check | result |
|---|---|
| memory-idle | measured: mac: System-wide memory free percentage: 46%; total = 4096.00M  us |
| turns | pass: resumed == again: True; cold (after a restart): True; cached 5493 of 5649; ttft resumed 0.284s, cold 4.483s |
| memory-busy | measured: mac: System-wide memory free percentage: 46%; total = 4096.00M  us |

