# Nanbeige4.3-33B bf16, drafted by Nanbeige4.1-3B MLX 4-bit on 1x Apple M5 Ultra (256 GB unified), macOS

Target `nanbeige43-33b-mlxdraft-m5`: Nanbeige4.3-33B bf16 with Nanbeige4.1-3B MLX 4-bit (mlx-community) drafting, TensorFold native Metal (llama) on one M5 Ultra (131072-token window, 1 stream: the drafter is recommended at --parallel 1 only). Engine: TensorFold native, Metal. Rendered from `stats/nanbeige43-33b-mlxdraft-m5.json` (8 runs); aggregate tok/s, total (a stream).

## 2026-10-28 02:31: run `20261028-023110-quick`

Plan quick, done; served as `nanbeige`.

Serving: engine_commit `4b257a042`; binary_sha256 `60378e65d3acdc2224200abe97402deb9163aef4ba9a87cec894c01b73951ad1`; served_model `{"object": "list", "data": [{"id": "nanbeige", "object": "model", "created": 1793172683, "`; chip `Apple M5 Ultra; 274877906944`; suite_commit `21db9b23f7be`

### ruler-fresh

| streams | prose total (a stream) | code total (a stream) | structured total (a stream) | list total (a stream) | first token |
|---:|---:|---:|---:|---:|---:|
| 1 | 80.2 (80.2) | 94.0 (94.0) | 91.8 (91.8) | 76.4 (76.4) | 0.26-0.30 s |

Engine rounds (ruler-fresh):

| streams | tokens a round | drafts a round | accepted | ms a round | requests |
|---:|---:|---:|---:|---:|---:|
| 1 | 4.465 | 4.034 | 86% | 52.18 | 12 |

### ruler-after

| streams | prose total (a stream) | code total (a stream) | structured total (a stream) | list total (a stream) | first token |
|---:|---:|---:|---:|---:|---:|
| 1 | 113.5 (113.5) | 110.7 (110.7) | 109.2 (109.2) | 101.8 (101.8) | 0.23-0.26 s |

Engine rounds (ruler-after):

| streams | tokens a round | drafts a round | accepted | ms a round | requests |
|---:|---:|---:|---:|---:|---:|
| 1 | 4.663 | 4.478 | 81% | 42.86 | 13 |

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
| turns | pass: resumed == again: True; cold (after a restart): True; cached 5493 of 5649; ttft resumed 0.359s, cold 4.362s |

## 2026-10-27 17:34: run `20261027-173414-quick`

Plan quick, done; served as `nanbeige`.

Serving: engine_commit `7d9ca99f0`; binary_sha256 `5b1664187235dfc985009170c110ea92e9946f6b600be189e34671034e3c2024`; served_model `{"object": "list", "data": [{"id": "nanbeige", "object": "model", "created": 1793140462, "`; chip `Apple M5 Ultra; 274877906944`; suite_commit `a7ba7e392d57`

### ruler-fresh

| streams | prose total (a stream) | code total (a stream) | structured total (a stream) | list total (a stream) | first token |
|---:|---:|---:|---:|---:|---:|
| 1 | 116.3 (116.3) | 106.9 (106.9) | 108.8 (108.8) | 99.9 (99.9) | 0.23-0.26 s |

Engine rounds (ruler-fresh):

| streams | tokens a round | drafts a round | accepted | ms a round | requests |
|---:|---:|---:|---:|---:|---:|
| 1 | 5.023 | 4.837 | 83% | 46.52 | 12 |

### ruler-after

| streams | prose total (a stream) | code total (a stream) | structured total (a stream) | list total (a stream) | first token |
|---:|---:|---:|---:|---:|---:|
| 1 | 112.5 (112.5) | 106.2 (106.2) | 108.2 (108.2) | 100.3 (100.3) | 0.23-0.26 s |

Engine rounds (ruler-after):

| streams | tokens a round | drafts a round | accepted | ms a round | requests |
|---:|---:|---:|---:|---:|---:|
| 1 | 4.631 | 4.444 | 81% | 43.35 | 13 |

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
| memory-idle | measured: mac: System-wide memory free percentage: 70%; total = 4096.00M  us |
| structured | pass: 18/18 obey, drafted == plain 12/12; a bad regex -> 400 |
| tools | pass: 5/5 tool cases right |
| sampling | pass: 9/9 seeded replies equal on repeat and undrafted; 0 errors |
| turns | pass: resumed == again: True; cold (after a restart): True; cached 5493 of 5649; ttft resumed 0.35s, cold 4.551s |

## 2026-10-27 16:06: run `20261027-160657-quick`

Plan quick, done; served as `nanbeige`.

Serving: engine_commit `8b78b1941`; binary_sha256 `b6fc3626c79a1e3d1d3dd3f2146b228196c4b7849d44800a5602c5db1524eb28`; served_model `{"object": "list", "data": [{"id": "nanbeige", "object": "model", "created": 1793135225, "`; chip `Apple M5 Ultra; 274877906944`; suite_commit `a7ba7e392d57`

### ruler-fresh

| streams | prose total (a stream) | code total (a stream) | structured total (a stream) | list total (a stream) | first token |
|---:|---:|---:|---:|---:|---:|
| 1 | 113.6 (113.6) | 113.7 (113.7) | 108.7 (108.7) | 99.1 (99.1) | 0.23-0.26 s |

Engine rounds (ruler-fresh):

| streams | tokens a round | drafts a round | accepted | ms a round | requests |
|---:|---:|---:|---:|---:|---:|
| 1 | 4.893 | 4.723 | 82% | 44.99 | 12 |

### ruler-after

| streams | prose total (a stream) | code total (a stream) | structured total (a stream) | list total (a stream) | first token |
|---:|---:|---:|---:|---:|---:|
| 1 | 99.7 (99.7) | 113.2 (113.2) | 108.6 (108.6) | 95.6 (95.6) | 0.23-0.26 s |

Engine rounds (ruler-after):

| streams | tokens a round | drafts a round | accepted | ms a round | requests |
|---:|---:|---:|---:|---:|---:|
| 1 | 4.679 | 4.499 | 81% | 44.88 | 13 |

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
| memory-idle | measured: mac: System-wide memory free percentage: 70%; total = 4096.00M  us |
| structured | pass: 18/18 obey, drafted == plain 12/12; a bad regex -> 400 |
| tools | pass: 5/5 tool cases right |
| sampling | pass: 9/9 seeded replies equal on repeat and undrafted; 0 errors |
| turns | pass: resumed == again: True; cold (after a restart): True; cached 5493 of 5649; ttft resumed 0.341s, cold 4.39s |

## 2026-10-27 15:46: run `20261027-154629-quick`

Plan quick, running; served as `nanbeige`.

Serving: engine_commit `8b78b1941`; binary_sha256 `b6fc3626c79a1e3d1d3dd3f2146b228196c4b7849d44800a5602c5db1524eb28`; served_model `{"object": "list", "data": [{"id": "nanbeige", "object": "model", "created": 1793134184, "`; chip `Apple M5 Ultra; 274877906944`; suite_commit `a7ba7e392d57`

### ruler-fresh

| streams | prose total (a stream) | code total (a stream) | structured total (a stream) | list total (a stream) | first token |
|---:|---:|---:|---:|---:|---:|
| 1 | 113.1 (113.1) | 109.7 (109.7) | - | - | 0.30-0.33 s |

Engine rounds (ruler-fresh):

| streams | tokens a round | drafts a round | accepted | ms a round | requests |
|---:|---:|---:|---:|---:|---:|
| 1 | 4.861 | 4.835 | 79% | 43.63 | 6 |

### ruler-after

| streams | prose total (a stream) | code total (a stream) | structured total (a stream) | list total (a stream) | first token |
|---:|---:|---:|---:|---:|---:|
| 1 | 113.0 (113.0) | 110.5 (110.5) | 108.6 (108.6) | 96.8 (96.8) | 0.23-0.26 s |

Engine rounds (ruler-after):

| streams | tokens a round | drafts a round | accepted | ms a round | requests |
|---:|---:|---:|---:|---:|---:|
| 1 | 4.647 | 4.487 | 81% | 43.34 | 13 |

### checks

| check | result |
|---|---|
| memory-idle | measured: mac: System-wide memory free percentage: 69%; total = 4096.00M  us |
| structured | FAIL: 0/18 obey, drafted == plain 12/12; a bad regex -> 400; failed json_object/greedy, json_object/sampled, json_object/thinking, json_schema/greedy, json_schema/sampled, json_schema/thinking, guided_json/greedy, guided_json/sampled, guided_json/thinking, regex/greedy, regex/sampled, regex/thinking, choice/greedy, choice/sampled, choice/thinking, grammar/greedy, grammar/sampled, grammar/thinking |
| tools | FAIL: 0/5 tool cases right; failed auto (503 {"error": {"message": "this Mac is under critical memory pressure: the server takes no new requests until it eases; retry shortly", "type": "invalid_request_error"}}); required (503 {"error": {"message": "this Mac is under critical memory pressure: the server takes no new requests until it eases; retry shortly", "type": "invalid_request_error"}}); named (503 {"error": {"message": "this Mac is under critical memory pressure: the server takes no new requests until it eases; retry shortly", "type": "invalid_request_error"}}); named/thinking (503 {"error": {"message": "this Mac is under critical memory pressure: the server takes no new requests until it eases; retry shortly", "type": "invalid_request_error"}}); named/stream (503 {"error": {"message": "this Mac is under critical memory pressure: the server takes no new requests until it eases; retry shortly", "type": "invalid_request_error"}}) |
| sampling | FAIL: 0/9 seeded replies equal on repeat and undrafted; 27 errors |
| turns | FAIL: resumed == again: True; cold (after a restart) not compared: 5553 prompt tokens (cached 0) against None; cached None of None; ttft resumed Nones, cold 4.432s; errors in ['turn1', 'turn2', 'turn3', 'turn3_again'] |

## 2026-10-27 11:30: run `20261027-113000-speed`

Plan speed, done; served as `nanbeige`.

Serving: engine_commit `80daf482a`; binary_sha256 `1492e990e5f64251043cb422645bd6e0a3fed4e8279e12dd9f8286cf4377fd58`; served_model `{"object": "list", "data": [{"id": "nanbeige", "object": "model", "created": 1793118614, "`; chip `Apple M5 Ultra; 274877906944`; suite_commit `a7ba7e392d57`

### ruler-fresh

| streams | prose total (a stream) | code total (a stream) | structured total (a stream) | list total (a stream) | first token |
|---:|---:|---:|---:|---:|---:|
| 1 | 116.8 (116.8) | 110.8 (110.8) | 109.3 (109.3) | 99.5 (99.5) | 0.23-0.26 s |
| 2 | 46.6 (23.3) | 148.3 (74.2) | 53.1 (26.6) | 106.9 (53.4) | 1.55-6.15 s |

Engine rounds (ruler-fresh):

| streams | tokens a round | drafts a round | accepted | ms a round | requests |
|---:|---:|---:|---:|---:|---:|
| 1 | 4.884 | 4.75 | 81% | 44.77 | 12 |
| 2 | 2.626 | 2.722 | 59% | 59.17 | 25 |

### ruler-after

| streams | prose total (a stream) | code total (a stream) | structured total (a stream) | list total (a stream) | first token |
|---:|---:|---:|---:|---:|---:|
| 1 | 107.3 (107.3) | 114.0 (114.0) | 108.9 (108.9) | 99.5 (99.5) | 0.23-0.26 s |

Engine rounds (ruler-after):

| streams | tokens a round | drafts a round | accepted | ms a round | requests |
|---:|---:|---:|---:|---:|---:|
| 1 | 4.696 | 4.445 | 83% | 43.71 | 13 |

### checks

| check | result |
|---|---|
| memory-idle | measured: mac: System-wide memory free percentage: 34%; total = 4096.00M  us |
| turns | pass: resumed == again: True; cold (after a restart): True; cached 5493 of 5649; ttft resumed 0.355s, cold 4.385s |
| memory-busy | measured: mac: System-wide memory free percentage: 34%; total = 4096.00M  us |

## 2026-10-27 11:05: run `20261027-110535-quick`

Plan quick, done; served as `nanbeige`.

Serving: engine_commit `80daf482a`; binary_sha256 `1492e990e5f64251043cb422645bd6e0a3fed4e8279e12dd9f8286cf4377fd58`; served_model `{"object": "list", "data": [{"id": "nanbeige", "object": "model", "created": 1793117143, "`; chip `Apple M5 Ultra; 274877906944`; suite_commit `a7ba7e392d57`

### ruler-fresh

| streams | prose total (a stream) | code total (a stream) | structured total (a stream) | list total (a stream) | first token |
|---:|---:|---:|---:|---:|---:|
| 1 | 116.8 (116.8) | 110.9 (110.9) | 109.6 (109.6) | 104.9 (104.9) | 0.23-0.26 s |

Engine rounds (ruler-fresh):

| streams | tokens a round | drafts a round | accepted | ms a round | requests |
|---:|---:|---:|---:|---:|---:|
| 1 | 4.911 | 4.791 | 81% | 44.42 | 12 |

### ruler-after

| streams | prose total (a stream) | code total (a stream) | structured total (a stream) | list total (a stream) | first token |
|---:|---:|---:|---:|---:|---:|
| 1 | 110.5 (110.5) | 108.4 (108.4) | 109.0 (109.0) | 105.1 (105.1) | 0.23-0.26 s |

Engine rounds (ruler-after):

| streams | tokens a round | drafts a round | accepted | ms a round | requests |
|---:|---:|---:|---:|---:|---:|
| 1 | 4.737 | 4.549 | 82% | 43.76 | 13 |

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
| memory-idle | measured: mac: System-wide memory free percentage: 34%; total = 4096.00M  us |
| structured | pass: 18/18 obey, drafted == plain 12/12; a bad regex -> 400 |
| tools | pass: 5/5 tool cases right |
| sampling | pass: 9/9 seeded replies equal on repeat and undrafted; 0 errors |
| turns | pass: resumed == again: True; cold (after a restart): True; cached 5493 of 5649; ttft resumed 0.349s, cold 4.39s |

## 2026-10-27 10:00: run `20261027-100045-speed`

Plan speed, done; served as `nanbeige`.

Serving: engine_commit `80daf482a`; binary_sha256 `1492e990e5f64251043cb422645bd6e0a3fed4e8279e12dd9f8286cf4377fd58`; served_model `{"object": "list", "data": [{"id": "nanbeige", "object": "model", "created": 1793113258, "`; chip `Apple M5 Ultra; 274877906944`; suite_commit `a7ba7e392d57`

### ruler-fresh

| streams | prose total (a stream) | code total (a stream) | structured total (a stream) | list total (a stream) | first token |
|---:|---:|---:|---:|---:|---:|
| 1 | 116.8 (116.8) | 110.9 (110.9) | 109.1 (109.1) | 95.1 (95.1) | 0.23-0.26 s |
| 2 | 31.9 (15.9) | 31.9 (16.0) | 32.5 (16.3) | 32.0 (16.0) | 0.34-0.39 s |

Engine rounds (ruler-fresh):

| streams | tokens a round | drafts a round | accepted | ms a round | requests |
|---:|---:|---:|---:|---:|---:|
| 1 | 4.875 | 4.75 | 81% | 45.15 | 12 |
| 2 | 1.046 | 0.044 | 94% | 65.28 | 25 |

### ruler-after

| streams | prose total (a stream) | code total (a stream) | structured total (a stream) | list total (a stream) | first token |
|---:|---:|---:|---:|---:|---:|
| 1 | 110.4 (110.4) | 113.6 (113.6) | 108.9 (108.9) | 95.6 (95.6) | 0.23-0.26 s |

Engine rounds (ruler-after):

| streams | tokens a round | drafts a round | accepted | ms a round | requests |
|---:|---:|---:|---:|---:|---:|
| 1 | 4.704 | 4.479 | 82% | 43.9 | 13 |

### checks

| check | result |
|---|---|
| memory-idle | measured: mac: System-wide memory free percentage: 34%; total = 4096.00M  us |
| turns | pass: resumed == again: True; cold (after a restart): True; cached 5493 of 5649; ttft resumed 0.356s, cold 4.4s |
| memory-busy | measured: mac: System-wide memory free percentage: 34%; total = 4096.00M  us |

## 2026-10-27 09:36: run `20261027-093646-quick`

Plan quick, done; served as `nanbeige`.

Serving: engine_commit `80daf482a`; binary_sha256 `1492e990e5f64251043cb422645bd6e0a3fed4e8279e12dd9f8286cf4377fd58`; served_model `{"object": "list", "data": [{"id": "nanbeige", "object": "model", "created": 1793111819, "`; chip `Apple M5 Ultra; 274877906944`; suite_commit `a7ba7e392d57`

### ruler-fresh

| streams | prose total (a stream) | code total (a stream) | structured total (a stream) | list total (a stream) | first token |
|---:|---:|---:|---:|---:|---:|
| 1 | 113.7 (113.7) | 113.7 (113.7) | 109.3 (109.3) | 100.2 (100.2) | 0.23-0.26 s |

Engine rounds (ruler-fresh):

| streams | tokens a round | drafts a round | accepted | ms a round | requests |
|---:|---:|---:|---:|---:|---:|
| 1 | 4.902 | 4.752 | 82% | 44.88 | 12 |

### ruler-after

| streams | prose total (a stream) | code total (a stream) | structured total (a stream) | list total (a stream) | first token |
|---:|---:|---:|---:|---:|---:|
| 1 | 110.9 (110.9) | 113.9 (113.9) | 108.9 (108.9) | 94.8 (94.8) | 0.23-0.26 s |

Engine rounds (ruler-after):

| streams | tokens a round | drafts a round | accepted | ms a round | requests |
|---:|---:|---:|---:|---:|---:|
| 1 | 4.712 | 4.487 | 82% | 43.98 | 13 |

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
| memory-idle | measured: mac: System-wide memory free percentage: 34%; total = 4096.00M  us |
| structured | pass: 18/18 obey, drafted == plain 12/12; a bad regex -> 400 |
| tools | pass: 5/5 tool cases right |
| sampling | pass: 9/9 seeded replies equal on repeat and undrafted; 0 errors |
| turns | pass: resumed == again: True; cold (after a restart): True; cached 5493 of 5649; ttft resumed 0.34s, cold 4.393s |

