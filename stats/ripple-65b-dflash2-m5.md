# ricursiveAI Ripple-65B-Preview (bf16) + DFlash2 drafter on 1x Apple M5 Ultra (256 GB unified), macOS

Target `ripple-65b-dflash2-m5`: ricursiveAI Ripple-65B-Preview (bf16 release) + its DFlash2 drafter (bf16), TensorFold native Metal on one M5 Ultra. Engine: TensorFold native, Metal. Rendered from `stats/ripple-65b-dflash2-m5.json` (2 runs); aggregate tok/s, total (a stream).

## 2026-11-06 05:15: run `20261106-051500-speed`

Plan speed, running; served as `ripple`.

Serving: engine_commit `b7ff7854f`; binary_sha256 `40cade17c2254999237c082761470cdf70982a6a02e5ec3658fdb6fe9bc17016`; served_model `{"object": "list", "data": [{"id": "ripple", "object": "model", "created": 1793963755, "ow`; chip `Apple M5 Ultra; 274877906944`; suite_commit `21db9b23f7be`

### ruler-fresh

| streams | prose total (a stream) | code total (a stream) | structured total (a stream) | list total (a stream) | first token |
|---:|---:|---:|---:|---:|---:|
| 1 | 13.4 (13.4) | 30.7 (30.7) | 13.3 (13.3) | 18.7 (18.7) | 0.39-1.06 s |
| 2 | 25.7 (12.9) | 63.3 (31.6) | 26.0 (13.0) | 54.8 (27.4) | 3.24-7.98 s |

Engine rounds (ruler-fresh):

| streams | tokens a round | drafts a round | accepted | ms a round | requests |
|---:|---:|---:|---:|---:|---:|
| 1 | 2.931 | 6.547 | 29% | 154.04 | 12 |
| 2 | 3.151 | 6.027 | 35% | 148.44 | 25 |

### checks

| check | result |
|---|---|
| memory-idle | measured: mac: System-wide memory free percentage: 22%; total = 8192.00M  us |

## 2026-11-06 05:08: run `20261106-050830-together`

Plan together, done; served as `ripple`.

Serving: engine_commit `b7ff7854f`; binary_sha256 `40cade17c2254999237c082761470cdf70982a6a02e5ec3658fdb6fe9bc17016`; served_model `{"object": "list", "data": [{"id": "ripple", "object": "model", "created": 1793963366, "ow`; chip `Apple M5 Ultra; 274877906944`; suite_commit `21db9b23f7be`

### suite-together

| check | passed |
|---|---:|
| concurrent | 12/12 |
| drafts | 12/12 |

