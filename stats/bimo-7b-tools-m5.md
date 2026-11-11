# Bimo-7B-CyberAgent, bf16 on 1x Apple M5 Ultra (256 GB unified), macOS

Target `bimo-7b-tools-m5`: Bimo-7B-CyberAgent bf16 as released with the base model's tool-rendering template, TensorFold native Metal (llama family, Qwen2) on one M5 Ultra (32768-token window, 2 streams). Engine: TensorFold native, Metal. Rendered from `stats/bimo-7b-tools-m5.json` (1 runs); aggregate tok/s, total (a stream).

## 2026-11-10 18:07: run `20261110-180712-quick`

Plan quick, done; served as `bimo`.

Serving: engine_commit `7662e079c`; binary_sha256 `cd01a302a7cdf9cd0969961abd4b57d766b6c75da3185472c8fd3cfe9632b5be`; served_model `{"object": "list", "data": [{"id": "bimo", "object": "model", "created": 1794355640, "owne`; chip `Apple M5 Ultra; 274877906944`; suite_commit `b3b0ef38b8bc`

### ruler-fresh

| streams | prose total (a stream) | code total (a stream) | structured total (a stream) | list total (a stream) | first token |
|---:|---:|---:|---:|---:|---:|
| 1 | 64.8 (64.8) | 51.4 (51.4) | 48.6 (48.6) | 44.1 (44.1) | 0.07-0.09 s |

Engine rounds (ruler-fresh):

| streams | tokens a round | drafts a round | accepted | ms a round | requests |
|---:|---:|---:|---:|---:|---:|
| 1 | 1.049 | 0.095 | 47% | 20.09 | 12 |

### ruler-after

| streams | prose total (a stream) | code total (a stream) | structured total (a stream) | list total (a stream) | first token |
|---:|---:|---:|---:|---:|---:|
| 1 | 53.4 (53.4) | 52.9 (52.9) | 55.2 (55.2) | 47.9 (47.9) | 0.07-0.10 s |

Engine rounds (ruler-after):

| streams | tokens a round | drafts a round | accepted | ms a round | requests |
|---:|---:|---:|---:|---:|---:|
| 1 | 1.049 | 0.094 | 47% | 20.03 | 13 |

### suite

| check | passed |
|---|---:|
| soak | 60/60 |
| drafts | 12/12 |
| concurrent | 12/12 |
| streaming | 4/4 |
| multiturn | 8/8 |
| stop | 3/3 |
| thinking | 0/10 |
| copy | 2/2 |
| max-tokens | 2/3 |

### checks

| check | result |
|---|---|
| memory-idle | measured: mac: System-wide memory free percentage: 89%; total = 13312.00M  u |
| structured | pass: 18/18 obey, drafted == plain 12/12; a bad regex -> 400 |
| tools | FAIL: 4/5 tool cases right; failed auto (finish stop) |
| sampling | pass: 9/9 seeded replies equal on repeat and undrafted; 0 errors |
| turns | pass: resumed == again: True; cold (after a restart): True; cached 5493 of 5583; ttft resumed 0.106s, cold 1.082s |

