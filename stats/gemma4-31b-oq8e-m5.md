# Gemma 4 31B, oQ8e (8-bit) + DFlash on 1x Apple M5 Ultra (256 GB unified), macOS

Target `gemma4-31b-oq8e-m5`: Gemma 4 31B oQ8e (8-bit, groups of 64), DFlash drafts, images, TensorFold native Metal on one M5 Ultra. Engine: TensorFold native, Metal. Rendered from `stats/gemma4-31b-oq8e-m5.json` (1 runs); aggregate tok/s, total (a stream).

## 2026-10-16 18:02: run `20261016-180201-speed`

Plan speed, done; served as `gemma4-31b-oq8e`.

Serving: engine_commit `d9e36b7f`; binary_sha256 `2e29fee5da96ec1ffb1ba41302ac949dc12205572154f21b800823450eb4b2b0`; served_model `{"object": "list", "data": [{"id": "gemma4-31b-oq8e", "object": "model", "created": 179219`; chip `Apple M5 Ultra; 274877906944`

### ruler-fresh

| streams | prose total (a stream) | code total (a stream) | structured total (a stream) | list total (a stream) | first token |
|---:|---:|---:|---:|---:|---:|
| 1 | 40.3 (40.3) | 63.1 (63.1) | 52.4 (52.4) | 54.8 (54.8) | 0.10-0.11 s |
| 4 | 109.7 (27.7) | 172.9 (44.8) | 141.5 (34.2) | 180.3 (44.3) | 0.24-0.27 s |

Engine rounds (ruler-fresh):

| streams | tokens a round | drafts a round | accepted | ms a round | requests |
|---:|---:|---:|---:|---:|---:|
| 1 | 2.759 | 10.847 | 16% | 52.41 | 12 |
| 4 | 2.384 | 3.645 | 38% | 63.19 | 49 |

### suite

| check | passed |
|---|---:|
| drafts | 12/12 |
| concurrent | 12/12 |

### checks

| check | result |
|---|---|
| structured | pass: 18/18 obey; a bad regex -> 400 |

