# Gemma 4 12B, oQ8e (8-bit) + MTP assistant on 1x Apple M5 Ultra (256 GB unified), macOS

Target `gemma4-12b-oq8e-m5`: Gemma 4 12B oQ8e (8-bit, groups of 64), MTP assistant drafts, images, TensorFold native Metal on one M5 Ultra. Engine: TensorFold native, Metal. Rendered from `stats/gemma4-12b-oq8e-m5.json` (2 runs); aggregate tok/s, total (a stream).

## 2026-10-16 17:54: run `20261016-175459-speed`

Plan speed, done; served as `gemma4-12b-oq8e`.

Serving: engine_commit `d9e36b7f`; binary_sha256 `2e29fee5da96ec1ffb1ba41302ac949dc12205572154f21b800823450eb4b2b0`; served_model `{"object": "list", "data": [{"id": "gemma4-12b-oq8e", "object": "model", "created": 179219`; chip `Apple M5 Ultra; 274877906944`

### ruler-fresh

| streams | prose total (a stream) | code total (a stream) | structured total (a stream) | list total (a stream) | first token |
|---:|---:|---:|---:|---:|---:|
| 1 | 92.8 (92.8) | 142.3 (142.3) | 145.7 (145.7) | 158.1 (158.1) | 0.05-0.05 s |
| 4 | 261.5 (64.8) | 324.2 (81.3) | 328.5 (80.7) | 340.0 (83.6) | 0.12-0.12 s |

Engine rounds (ruler-fresh):

| streams | tokens a round | drafts a round | accepted | ms a round | requests |
|---:|---:|---:|---:|---:|---:|
| 1 | 3.55 | 5.525 | 47% | 26.35 | 12 |
| 4 | 2.944 | 3.177 | 62% | 37.94 | 49 |

### suite

| check | passed |
|---|---:|
| drafts | 12/12 |
| concurrent | 12/12 |

### checks

| check | result |
|---|---|
| structured | pass: 18/18 obey; a bad regex -> 400 |

## 2026-10-16 17:37: run `20261016-173745-speed`

Plan speed, done; served as `gemma4-12b-oq8e`.

Serving: engine_commit `80ef355c`; binary_sha256 `d51532609b3a9faccaf6ef181118dd9096b5819befc6e753f321233856cce571`; served_model `{"object": "list", "data": [{"id": "gemma4-12b-oq8e", "object": "model", "created": 179219`; chip `Apple M5 Ultra; 274877906944`

### ruler-fresh

| streams | prose total (a stream) | code total (a stream) | structured total (a stream) | list total (a stream) | first token |
|---:|---:|---:|---:|---:|---:|
| 1 | 94.4 (94.4) | 141.2 (141.2) | 150.0 (150.0) | 158.2 (158.2) | 0.05-0.05 s |
| 4 | 264.6 (64.7) | 325.4 (81.6) | 330.2 (82.3) | 325.5 (80.6) | 0.12-0.12 s |

Engine rounds (ruler-fresh):

| streams | tokens a round | drafts a round | accepted | ms a round | requests |
|---:|---:|---:|---:|---:|---:|
| 1 | 3.586 | 5.49 | 48% | 26.38 | 12 |
| 4 | 2.958 | 3.194 | 62% | 38.28 | 50 |

### suite

| check | passed |
|---|---:|
| drafts | 12/12 |
| concurrent | 12/12 |

### checks

| check | result |
|---|---|
| structured | pass: 18/18 obey; a bad regex -> 400 |

