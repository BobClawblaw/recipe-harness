# DeepSeek-V4.1-Flash-1017, 2/3-bit experts on 1x Apple M5 Ultra (256 GB unified), macOS

Target `deepseek-v41-m5`: DeepSeek-V4.1-Flash-1017, 2/3-bit experts with images and DSpark drafts, TensorFold native Metal on one M5 Ultra. Engine: TensorFold native, Metal. Rendered from `stats/deepseek-v41-m5.json` (1 runs); aggregate tok/s, total (a stream).

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

