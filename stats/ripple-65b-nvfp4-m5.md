# ricursiveAI Ripple-65B-Preview-NVFP4 (NVFP4 MLPs, bf16 attention) on 1x Apple M5 Ultra (256 GB unified), macOS

Target `ripple-65b-nvfp4-m5`: ricursiveAI Ripple-65B-Preview-NVFP4 (MLPs NVFP4, attention bf16; activations bf16), TensorFold native Metal on one M5 Ultra. Engine: TensorFold native, Metal. Rendered from `stats/ripple-65b-nvfp4-m5.json` (9 runs); aggregate tok/s, total (a stream).

## 2026-11-05 08:06: run `20261105-080630-speed`

Plan speed, done; served as `ripple`.

Serving: engine_commit `45685de42`; binary_sha256 `5323602e8f282c9f7e5e6f242e5ca2cc4c1f0b9699fec05da11c7b366bdfac1b`; served_model `{"object": "list", "data": [{"id": "ripple", "object": "model", "created": 1793887605, "ow`; chip `Apple M5 Ultra; 274877906944`; suite_commit `21db9b23f7be`

### ruler-fresh

| streams | prose total (a stream) | code total (a stream) | structured total (a stream) | list total (a stream) | first token |
|---:|---:|---:|---:|---:|---:|
| 1 | 10.2 (10.2) | 10.2 (10.2) | 10.3 (10.3) | 10.2 (10.2) | 0.60-0.72 s |
| 2 | 18.9 (9.5) | 18.8 (9.4) | 19.2 (9.6) | 18.9 (9.5) | 0.92-1.08 s |

Engine rounds (ruler-fresh):

| streams | tokens a round | drafts a round | accepted | ms a round | requests |
|---:|---:|---:|---:|---:|---:|
| 1 | 1.006 | 0.0 |  | 98.21 | 12 |
| 2 | 1.007 | 0.009 | 8% | 106.07 | 25 |

### ruler-after

| streams | prose total (a stream) | code total (a stream) | structured total (a stream) | list total (a stream) | first token |
|---:|---:|---:|---:|---:|---:|
| 1 | 10.3 (10.3) | 10.3 (10.3) | 10.3 (10.3) | 10.3 (10.3) | 0.60-0.72 s |

Engine rounds (ruler-after):

| streams | tokens a round | drafts a round | accepted | ms a round | requests |
|---:|---:|---:|---:|---:|---:|
| 1 | 1.007 | 0.0 |  | 98.11 | 13 |

### checks

| check | result |
|---|---|
| memory-idle | measured: mac: System-wide memory free percentage: 69%; total = 6144.00M  us |
| turns | pass: resumed == again: True; cold (after a restart): True; cached 4513 of 4597; ttft resumed 0.653s, cold 7.724s |
| memory-busy | measured: mac: System-wide memory free percentage: 69%; total = 6144.00M  us |

## 2026-11-05 07:55: run `20261105-075517-speed`

Plan speed, done; served as `ripple`.

Serving: engine_commit `3a5954f38`; binary_sha256 `95711121b17e5b171ab2c2c3f7232df13ab281e690453c677bb6554869fa7730`; served_model `{"object": "list", "data": [{"id": "ripple", "object": "model", "created": 1793886932, "ow`; chip `Apple M5 Ultra; 274877906944`; suite_commit `21db9b23f7be`

### ruler-fresh

| streams | prose total (a stream) | code total (a stream) | structured total (a stream) | list total (a stream) | first token |
|---:|---:|---:|---:|---:|---:|
| 1 | 10.2 (10.2) | 10.2 (10.2) | 10.3 (10.3) | 10.2 (10.2) | 0.60-0.72 s |
| 2 | 19.0 (9.5) | 18.9 (9.4) | 19.2 (9.6) | 18.9 (9.5) | 0.92-1.08 s |

Engine rounds (ruler-fresh):

| streams | tokens a round | drafts a round | accepted | ms a round | requests |
|---:|---:|---:|---:|---:|---:|
| 1 | 1.006 | 0.0 |  | 98.19 | 12 |
| 2 | 1.007 | 0.009 | 8% | 106.0 | 25 |

### ruler-after

| streams | prose total (a stream) | code total (a stream) | structured total (a stream) | list total (a stream) | first token |
|---:|---:|---:|---:|---:|---:|
| 1 | 10.2 (10.2) | 10.2 (10.2) | 10.3 (10.3) | 10.2 (10.2) | 0.60-0.72 s |

Engine rounds (ruler-after):

| streams | tokens a round | drafts a round | accepted | ms a round | requests |
|---:|---:|---:|---:|---:|---:|
| 1 | 1.007 | 0.0 |  | 98.22 | 13 |

### checks

| check | result |
|---|---|
| memory-idle | measured: mac: System-wide memory free percentage: 69%; total = 6144.00M  us |
| turns | pass: resumed == again: True; cold (after a restart): True; cached 4513 of 4597; ttft resumed 0.653s, cold 7.721s |
| memory-busy | measured: mac: System-wide memory free percentage: 68%; total = 6144.00M  us |

## 2026-11-05 05:02: run `20261105-050202-structured`

Plan structured, done; served as `ripple`.

Serving: engine_commit `68e1993d9`; binary_sha256 `844d17a7447fb02f89be67eaefac41ac8769de0cc6cfd4bd8e6d46e5c3dcc52e`; served_model `{"object": "list", "data": [{"id": "ripple", "object": "model", "created": 1793876522, "ow`; chip `Apple M5 Ultra; 274877906944`; suite_commit `21db9b23f7be`

### checks

| check | result |
|---|---|
| structured | pass: 18/18 obey, drafted == plain 12/12; a bad regex -> 400 |
| tools | pass: 5/5 tool cases right |

## 2026-11-05 00:17: run `20261105-001750-structured`

Plan structured, done; served as `ripple`.

Serving: engine_commit `1f5209927`; binary_sha256 `f6540390d02baf06fa92ae5a6bc5141112e06b1c221b55358067321b3c3600db`; served_model `{"object": "list", "data": [{"id": "ripple", "object": "model", "created": 1793859471, "ow`; chip `Apple M5 Ultra; 274877906944`; suite_commit `21db9b23f7be`

### checks

| check | result |
|---|---|
| structured | pass: 18/18 obey, drafted == plain 12/12; a bad regex -> 400 |
| tools | pass: 5/5 tool cases right |

## 2026-11-04 23:29: run `20261104-232908-quick`

Plan quick, done; served as `ripple`.

Serving: engine_commit `e2ca8c387`; binary_sha256 `795faeb7019fcf030068f844b7cfcb261744b05be7ddfc2986cb4d0539727bf0`; served_model `{"object": "list", "data": [{"id": "ripple", "object": "model", "created": 1793856569, "ow`; chip `Apple M5 Ultra; 274877906944`; suite_commit `21db9b23f7be`

### ruler-fresh

| streams | prose total (a stream) | code total (a stream) | structured total (a stream) | list total (a stream) | first token |
|---:|---:|---:|---:|---:|---:|
| 1 | 10.2 (10.2) | 10.1 (10.1) | 10.2 (10.2) | 10.1 (10.1) | 0.61-0.73 s |

Engine rounds (ruler-fresh):

| streams | tokens a round | drafts a round | accepted | ms a round | requests |
|---:|---:|---:|---:|---:|---:|
| 1 | 1.006 | 0.0 |  | 99.19 | 12 |

### ruler-after

| streams | prose total (a stream) | code total (a stream) | structured total (a stream) | list total (a stream) | first token |
|---:|---:|---:|---:|---:|---:|
| 1 | 10.2 (10.2) | 10.2 (10.2) | 10.2 (10.2) | 10.2 (10.2) | 0.61-0.73 s |

Engine rounds (ruler-after):

| streams | tokens a round | drafts a round | accepted | ms a round | requests |
|---:|---:|---:|---:|---:|---:|
| 1 | 1.007 | 0.0 |  | 98.98 | 13 |

### suite

| check | passed |
|---|---:|
| soak | 60/60 |
| drafts | 12/12 |
| concurrent | 12/12 |
| streaming | 4/4 |
| multiturn | 8/8 |
| stop | 3/3 |
| thinking | 5/10 |
| copy | 2/2 |
| max-tokens | 3/3 |

### checks

| check | result |
|---|---|
| memory-idle | measured: mac: System-wide memory free percentage: 68%; total = 6144.00M  us |
| structured | pass: 18/18 obey, drafted == plain 12/12; a bad regex -> 400 |
| tools | pass: 5/5 tool cases right |
| sampling | pass: 9/9 seeded replies equal on repeat and undrafted; 0 errors |
| turns | pass: resumed == again: True; cold (after a restart): True; cached 4513 of 4597; ttft resumed 0.667s, cold 8.093s |
| urls | FAIL: public 400; loopback 400; http 400; unexpected: ['public'] |

## 2026-11-04 21:23: run `20261104-212334-quick`

Plan quick, done; served as `ripple`.

Serving: engine_commit `d26cd59ad`; binary_sha256 `89a225a8a60c3383a194f2e44cdbad4ce82e5f9008be00678408b30f3465ebee`; served_model `{"object": "list", "data": [{"id": "ripple", "object": "model", "created": 1793849029, "ow`; chip `Apple M5 Ultra; 274877906944`; suite_commit `21db9b23f7be`

### ruler-fresh

| streams | prose total (a stream) | code total (a stream) | structured total (a stream) | list total (a stream) | first token |
|---:|---:|---:|---:|---:|---:|
| 1 | 10.2 (10.2) | 10.2 (10.2) | 10.2 (10.2) | 10.2 (10.2) | 0.60-0.72 s |

Engine rounds (ruler-fresh):

| streams | tokens a round | drafts a round | accepted | ms a round | requests |
|---:|---:|---:|---:|---:|---:|
| 1 | 1.006 | 0.0 |  | 98.31 | 12 |

### ruler-after

| streams | prose total (a stream) | code total (a stream) | structured total (a stream) | list total (a stream) | first token |
|---:|---:|---:|---:|---:|---:|
| 1 | 10.2 (10.2) | 10.2 (10.2) | 10.3 (10.3) | 10.2 (10.2) | 0.60-0.72 s |

Engine rounds (ruler-after):

| streams | tokens a round | drafts a round | accepted | ms a round | requests |
|---:|---:|---:|---:|---:|---:|
| 1 | 1.007 | 0.0 |  | 98.25 | 13 |

### suite

| check | passed |
|---|---:|
| soak | 60/60 |
| drafts | 12/12 |
| concurrent | 12/12 |
| streaming | 4/4 |
| multiturn | 8/8 |
| stop | 3/3 |
| thinking | 5/10 |
| copy | 2/2 |
| max-tokens | 3/3 |

### checks

| check | result |
|---|---|
| memory-idle | measured: mac: System-wide memory free percentage: 68%; total = 6144.00M  us |
| structured | pass: 18/18 obey, drafted == plain 12/12; a bad regex -> 400 |
| tools | pass: 5/5 tool cases right |
| sampling | pass: 9/9 seeded replies equal on repeat and undrafted; 0 errors |
| turns | pass: resumed == again: True; cold (after a restart): True; cached 4513 of 4597; ttft resumed 0.65s, cold 7.734s |
| urls | FAIL: public 400; loopback 400; http 400; unexpected: ['public'] |

## 2026-11-04 20:36: run `20261104-203630-prefill`

Plan prefill, done; served as `ripple`.

Serving: engine_commit `588e7d2a2`; binary_sha256 `b322b32e218068be2060eb4a76c7b03e50ca7607a3a465aeee1f2b0e5dc4d33b`; served_model `{"object": "list", "data": [{"id": "ripple", "object": "model", "created": 1793846211, "ow`; chip `Apple M5 Ultra; 274877906944`; suite_commit `21db9b23f7be`

### checks

| check | result |
|---|---|
| memory-idle | measured: mac: System-wide memory free percentage: 68%; total = 6144.00M  us |
| prefill-off | measured: 2220 tokens 569.1 tok/s (3.901 s), 8776 tokens 604.6 tok/s (14.515 s), 35015 tokens 587.3 tok/s (59.625 s), 139723 tokens 433.8 tok/s (322.123 s) |
| prefill-thinking | measured: 2209 tokens 487.7 tok/s (4.529 s), 8798 tokens 458.0 tok/s (19.211 s), 34985 tokens 503.0 tok/s (69.553 s), 139811 tokens 409.9 tok/s (341.105 s) |
| memory-busy | measured: mac: System-wide memory free percentage: 64%; total = 6144.00M  us |

## 2026-11-04 20:25: run `20261104-202505-speed`

Plan speed, done; served as `ripple`.

Serving: engine_commit `588e7d2a2`; binary_sha256 `b322b32e218068be2060eb4a76c7b03e50ca7607a3a465aeee1f2b0e5dc4d33b`; served_model `{"object": "list", "data": [{"id": "ripple", "object": "model", "created": 1793845520, "ow`; chip `Apple M5 Ultra; 274877906944`; suite_commit `21db9b23f7be`

### ruler-fresh

| streams | prose total (a stream) | code total (a stream) | structured total (a stream) | list total (a stream) | first token |
|---:|---:|---:|---:|---:|---:|
| 1 | 10.1 (10.1) | 10.1 (10.1) | 10.2 (10.2) | 10.1 (10.1) | 0.61-0.74 s |
| 2 | 18.8 (9.4) | 18.6 (9.3) | 19.1 (9.5) | 18.8 (9.4) | 0.93-1.10 s |

Engine rounds (ruler-fresh):

| streams | tokens a round | drafts a round | accepted | ms a round | requests |
|---:|---:|---:|---:|---:|---:|
| 1 | 1.006 | 0.0 |  | 99.24 | 12 |
| 2 | 1.007 | 0.009 | 8% | 106.99 | 25 |

### ruler-after

| streams | prose total (a stream) | code total (a stream) | structured total (a stream) | list total (a stream) | first token |
|---:|---:|---:|---:|---:|---:|
| 1 | 10.1 (10.1) | 10.1 (10.1) | 10.2 (10.2) | 10.1 (10.1) | 0.61-0.73 s |

Engine rounds (ruler-after):

| streams | tokens a round | drafts a round | accepted | ms a round | requests |
|---:|---:|---:|---:|---:|---:|
| 1 | 1.007 | 0.0 |  | 99.35 | 13 |

### checks

| check | result |
|---|---|
| memory-idle | measured: mac: System-wide memory free percentage: 68%; total = 6144.00M  us |
| turns | pass: resumed == again: True; cold (after a restart): True; cached 4513 of 4597; ttft resumed 0.666s, cold 8.176s |
| memory-busy | measured: mac: System-wide memory free percentage: 68%; total = 6144.00M  us |

## 2026-11-04 19:42: run `20261104-194257-quick`

Plan quick, done; served as `ripple`.

Serving: engine_commit `588e7d2a2`; binary_sha256 `b322b32e218068be2060eb4a76c7b03e50ca7607a3a465aeee1f2b0e5dc4d33b`; served_model `{"object": "list", "data": [{"id": "ripple", "object": "model", "created": 1793842997, "ow`; chip `Apple M5 Ultra; 274877906944`; suite_commit `21db9b23f7be`

### ruler-fresh

| streams | prose total (a stream) | code total (a stream) | structured total (a stream) | list total (a stream) | first token |
|---:|---:|---:|---:|---:|---:|
| 1 | 10.2 (10.2) | 10.2 (10.2) | 10.3 (10.3) | 10.2 (10.2) | 0.60-0.73 s |

Engine rounds (ruler-fresh):

| streams | tokens a round | drafts a round | accepted | ms a round | requests |
|---:|---:|---:|---:|---:|---:|
| 1 | 1.006 | 0.0 |  | 98.32 | 12 |

### ruler-after

| streams | prose total (a stream) | code total (a stream) | structured total (a stream) | list total (a stream) | first token |
|---:|---:|---:|---:|---:|---:|
| 1 | 10.2 (10.2) | 10.2 (10.2) | 10.3 (10.3) | 10.2 (10.2) | 0.60-0.72 s |

Engine rounds (ruler-after):

| streams | tokens a round | drafts a round | accepted | ms a round | requests |
|---:|---:|---:|---:|---:|---:|
| 1 | 1.007 | 0.0 |  | 98.46 | 13 |

### suite

| check | passed |
|---|---:|
| soak | 60/60 |
| drafts | 12/12 |
| concurrent | 12/12 |
| streaming | 4/4 |
| multiturn | 8/8 |
| stop | 3/3 |
| thinking | 5/10 |
| copy | 2/2 |
| max-tokens | 3/3 |

### checks

| check | result |
|---|---|
| memory-idle | measured: mac: System-wide memory free percentage: 68%; total = 6144.00M  us |
| structured | pass: 18/18 obey, drafted == plain 12/12; a bad regex -> 400 |
| tools | pass: 5/5 tool cases right |
| sampling | pass: 9/9 seeded replies equal on repeat and undrafted; 0 errors |
| turns | pass: resumed == again: True; cold (after a restart): True; cached 4513 of 4597; ttft resumed 0.654s, cold 7.778s |
| urls | FAIL: public 400; loopback 400; http 400; unexpected: ['public'] |

