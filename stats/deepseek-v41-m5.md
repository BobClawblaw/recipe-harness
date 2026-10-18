# DeepSeek-V4.1-Flash-1017, 2/3-bit experts on 1x Apple M5 Ultra (256 GB unified), macOS

Target `deepseek-v41-m5`: DeepSeek-V4.1-Flash-1017, 2/3-bit experts with images and DSpark drafts, TensorFold native Metal on one M5 Ultra. Engine: TensorFold native, Metal. Rendered from `stats/deepseek-v41-m5.json` (3 runs); aggregate tok/s, total (a stream).

## 2026-10-17 19:33: run `20261017-193300-speed`

Plan speed, done; served as `DeepSeek-V4.1-Flash`.

Serving: engine_commit `fcf9e0b4`; binary_sha256 `8f57204baa1917419a5c85097de13f44ac705891557b2dc95aed1e9d59b6cfa3`; served_model `{"object": "list", "data": [{"id": "DeepSeek-V4.1-Flash", "object": "model", "created": 17`; checkpoint `{'repo': 'deepseek-ai/DeepSeek-V4.1-Flash-1017', 'expert_bits': 2, 'layer_bits': '10-29:3'`; chip `Apple M5 Ultra; 274877906944`

### ruler-fresh

| streams | prose total (a stream) | code total (a stream) | structured total (a stream) | list total (a stream) | first token |
|---:|---:|---:|---:|---:|---:|
| 1 | 70.6 (70.6) | 96.3 (96.3) | 76.1 (76.1) | 91.6 (91.6) | 0.13-0.19 s |
| 2 | 76.6 (38.3) | 94.7 (47.3) | 77.0 (38.5) | 117.6 (58.8) | 0.20-0.30 s |

### ruler-after

| streams | prose total (a stream) | code total (a stream) | structured total (a stream) | list total (a stream) | first token |
|---:|---:|---:|---:|---:|---:|
| 1 | 73.1 (73.1) | 96.5 (96.5) | 77.5 (77.5) | 98.6 (98.6) | 0.13-0.19 s |

### checks

| check | result |
|---|---|
| memory-idle | measured: mac: System-wide memory free percentage: 16%; total = 5120.00M  us |
| turns | pass: resumed == again == cold: True; cached 4541 of 4561; ttft resumed 0.17s, cold 1.714s |
| memory-busy | measured: mac: System-wide memory free percentage: 17%; total = 5120.00M  us |

## 2026-10-17 17:54: run `20261017-175442-speed`

Plan speed, done; served as `DeepSeek-V4.1-Flash`.

Serving: engine_commit `2f1c1009`; binary_sha256 `7e0216350cf9d28aa27dcb1ad7d786f6e14e525d1ac9c9a89b2782f16b00abbe`; served_model `{"object": "list", "data": [{"id": "DeepSeek-V4.1-Flash", "object": "model", "created": 17`; checkpoint `{'repo': 'deepseek-ai/DeepSeek-V4.1-Flash-1017', 'expert_bits': 2, 'layer_bits': '10-29:3'`; chip `Apple M5 Ultra; 274877906944`

### ruler-fresh

| streams | prose total (a stream) | code total (a stream) | structured total (a stream) | list total (a stream) | first token |
|---:|---:|---:|---:|---:|---:|
| 1 | 57.7 (57.7) | 90.5 (90.5) | 69.5 (69.5) | 93.1 (93.1) | 0.14-0.19 s |
| 2 | 62.6 (31.3) | 90.1 (45.0) | 74.3 (37.1) | 112.6 (56.3) | 0.20-0.30 s |

### ruler-after

| streams | prose total (a stream) | code total (a stream) | structured total (a stream) | list total (a stream) | first token |
|---:|---:|---:|---:|---:|---:|
| 1 | 58.9 (58.9) | 91.1 (91.1) | 73.3 (73.3) | 92.9 (92.9) | 0.14-0.19 s |

### checks

| check | result |
|---|---|
| memory-idle | measured: mac: System-wide memory free percentage: 15%; total = 3072.00M  us |
| turns | pass: resumed == again == cold: True; cached 4541 of 4569; ttft resumed 0.201s, cold 1.766s |
| memory-busy | measured: mac: System-wide memory free percentage: 15%; total = 3072.00M  us |

## 2026-10-17 14:57: run `20261017-145733-speed`

Plan speed, done; served as `DeepSeek-V4.1-Flash`.

Serving: engine_commit `e35a22a4`; binary_sha256 `c0f8ffddd712df7e2cc2132fb4ee46d9a16054f9677e1c1503de7509661f9340`; served_model `{"object": "list", "data": [{"id": "DeepSeek-V4.1-Flash", "object": "model", "created": 17`; checkpoint `{'repo': 'deepseek-ai/DeepSeek-V4.1-Flash-1017', 'expert_bits': 2, 'layer_bits': '10-29:3'`; chip `Apple M5 Ultra; 274877906944`

### ruler-fresh

| streams | prose total (a stream) | code total (a stream) | structured total (a stream) | list total (a stream) | first token |
|---:|---:|---:|---:|---:|---:|
| 1 | 41.1 (41.1) | 56.7 (56.7) | 48.4 (48.4) | 62.2 (62.2) | 0.15-0.22 s |
| 2 | 42.7 (21.3) | 58.3 (29.2) | 49.4 (24.7) | 78.5 (39.3) | 0.23-0.33 s |

### ruler-after

| streams | prose total (a stream) | code total (a stream) | structured total (a stream) | list total (a stream) | first token |
|---:|---:|---:|---:|---:|---:|
| 1 | 43.1 (43.1) | 59.2 (59.2) | 50.2 (50.2) | 64.6 (64.6) | 0.15-0.22 s |

### checks

| check | result |
|---|---|
| memory-idle | measured: mac: System-wide memory free percentage: 14%; total = 7168.00M  us |
| turns | pass: resumed == again == cold: True; cached 4541 of 4561; ttft resumed 0.222s, cold 2.037s |
| memory-busy | measured: mac: System-wide memory free percentage: 13%; total = 7168.00M  us |

