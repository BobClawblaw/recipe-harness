# DeepSeek-V4.1-Flash-1017, 2/3-bit experts on 1x Apple M5 Ultra (256 GB unified), macOS

Target `deepseek-v41-m5`: DeepSeek-V4.1-Flash-1017, 2/3-bit experts with images and DSpark drafts, TensorFold native Metal on one M5 Ultra. Engine: TensorFold native, Metal. Rendered from `stats/deepseek-v41-m5.json` (17 runs); aggregate tok/s, total (a stream).

## 2026-10-20 06:19: run `20261020-061904-dsv41-speed`

Plan dsv41-speed, done; served as `DeepSeek-V4.1-Flash`.

Serving: engine_commit `98e41cae`; binary_sha256 `46342bce7499c5db2eebc177b04bfcc32e5d0c2fb155882824ad13fb424489b5`; served_model `{"object": "list", "data": [{"id": "DeepSeek-V4.1-Flash-Abliterated", "object": "model", "`; checkpoint `{'repo': 'deepseek-ai/DeepSeek-V4.1-Flash-1017', 'expert_bits': 2, 'layer_bits': '10-29:3'`; chip `Apple M5 Ultra; 274877906944`; suite_commit `277c842a1481`

### ruler-streams

| streams | prose total (a stream) | code total (a stream) | structured total (a stream) | list total (a stream) | first token |
|---:|---:|---:|---:|---:|---:|
| 1 | 70.6 (70.6) | 86.4 (86.4) | 76.2 (76.2) | 92.9 (92.9) | 0.10-0.14 s |
| 2 | 86.9 (43.4) | 103.1 (51.5) | 97.5 (48.8) | 117.0 (58.5) | 0.21-0.28 s |
| 4 | 107.2 (26.0) | 118.5 (30.3) | 114.3 (28.6) | 123.5 (29.8) | 0.44-0.58 s |

### checks

| check | result |
|---|---|
| memory-idle | measured: mac: System-wide memory free percentage: 14%; total = 5120.00M  us |

## 2026-10-20 06:13: run `20261020-061318-prefill`

Plan prefill, done; served as `DeepSeek-V4.1-Flash`.

Serving: engine_commit `98e41cae`; binary_sha256 `46342bce7499c5db2eebc177b04bfcc32e5d0c2fb155882824ad13fb424489b5`; served_model `{"object": "list", "data": [{"id": "DeepSeek-V4.1-Flash-Abliterated", "object": "model", "`; checkpoint `{'repo': 'deepseek-ai/DeepSeek-V4.1-Flash-1017', 'expert_bits': 2, 'layer_bits': '10-29:3'`; chip `Apple M5 Ultra; 274877906944`; suite_commit `277c842a1481`

### checks

| check | result |
|---|---|
| memory-idle | measured: mac: System-wide memory free percentage: 15%; total = 5120.00M  us |
| prefill-off | measured: 2071 tokens 1172.0 tok/s (1.767 s), 8216 tokens 1453.1 tok/s (5.654 s), 32791 tokens 1429.6 tok/s (22.937 s), 131095 tokens 1383.2 tok/s (94.774 s) |
| prefill-thinking | measured: 2098 tokens 1354.4 tok/s (1.549 s), 8239 tokens 1455.9 tok/s (5.659 s), 32815 tokens 1430.9 tok/s (22.933 s), 131122 tokens 1381.7 tok/s (94.898 s) |
| memory-busy | measured: mac: System-wide memory free percentage: 14%; total = 5120.00M  us |

## 2026-10-20 04:35: run `20261020-043551-dsv41-quality-off`

Plan dsv41-quality-off, done; served as `DeepSeek-V4.1-Flash`.

Serving: engine_commit `bfad20ae`; binary_sha256 `9edbd25fa17c85acde00d3adddc35ae4d8f10cc487456a9c37261e840456cfb0`; served_model `{"object": "list", "data": [{"id": "DeepSeek-V4.1-Flash-Abliterated", "object": "model", "`; checkpoint `{'repo': 'deepseek-ai/DeepSeek-V4.1-Flash-1017', 'expert_bits': 2, 'layer_bits': '10-29:3'`; chip `Apple M5 Ultra; 274877906944`; suite_commit `277c842a1481`

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
| tools | 57/60 |
| json | 30/30 |
| ifeval | 130/150 |
| gsm8k | 246/250 |
| mgsm | 217/240 |
| mmlu | 306/342 |
| math500 | 462/500 |

### checks

| check | result |
|---|---|
| memory-idle | measured: mac: System-wide memory free percentage: 94%; total = 5120.00M  us |

## 2026-10-20 04:30: run `20261020-043028-dsv41-speed`

Plan dsv41-speed, done; served as `DeepSeek-V4.1-Flash`.

Serving: engine_commit `bfad20ae`; binary_sha256 `9edbd25fa17c85acde00d3adddc35ae4d8f10cc487456a9c37261e840456cfb0`; served_model `{"object": "list", "data": [{"id": "DeepSeek-V4.1-Flash-Abliterated", "object": "model", "`; checkpoint `{'repo': 'deepseek-ai/DeepSeek-V4.1-Flash-1017', 'expert_bits': 2, 'layer_bits': '10-29:3'`; chip `Apple M5 Ultra; 274877906944`; suite_commit `277c842a1481`

### ruler-streams

| streams | prose total (a stream) | code total (a stream) | structured total (a stream) | list total (a stream) | first token |
|---:|---:|---:|---:|---:|---:|
| 1 | 70.5 (70.5) | 88.5 (88.5) | 80.2 (80.2) | 93.6 (93.6) | 0.10-0.14 s |
| 2 | 88.8 (44.4) | 103.6 (51.8) | 96.2 (48.1) | 117.2 (58.6) | 0.21-0.28 s |
| 4 | 106.9 (26.5) | 120.2 (29.8) | 115.5 (29.2) | 124.0 (30.3) | 0.44-0.58 s |

### checks

| check | result |
|---|---|
| memory-idle | measured: mac: System-wide memory free percentage: 14%; total = 5120.00M  us |

## 2026-10-20 04:25: run `20261020-042547-prefill`

Plan prefill, done; served as `DeepSeek-V4.1-Flash`.

Serving: engine_commit `bfad20ae`; binary_sha256 `9edbd25fa17c85acde00d3adddc35ae4d8f10cc487456a9c37261e840456cfb0`; served_model `{"object": "list", "data": [{"id": "DeepSeek-V4.1-Flash-Abliterated", "object": "model", "`; checkpoint `{'repo': 'deepseek-ai/DeepSeek-V4.1-Flash-1017', 'expert_bits': 2, 'layer_bits': '10-29:3'`; chip `Apple M5 Ultra; 274877906944`; suite_commit `277c842a1481`

### checks

| check | result |
|---|---|
| memory-idle | measured: mac: System-wide memory free percentage: 15%; total = 5120.00M  us |
| prefill-off | measured: 2072 tokens 1219.5 tok/s (1.699 s), 8214 tokens 1445.6 tok/s (5.682 s), 32788 tokens 1422.3 tok/s (23.052 s), 131095 tokens 1376.4 tok/s (95.248 s) |
| prefill-thinking | measured: 2097 tokens 1357.3 tok/s (1.545 s), 8242 tokens 1454.6 tok/s (5.666 s), 32816 tokens 1420.7 tok/s (23.098 s), 131123 tokens 1374.9 tok/s (95.369 s) |
| memory-busy | measured: mac: System-wide memory free percentage: 14%; total = 5120.00M  us |

## 2026-10-19 09:08: run `20261019-090829-dsv41-speed`

Plan dsv41-speed, done; served as `DeepSeek-V4.1-Flash`.

Serving: engine_commit `c4c69219`; binary_sha256 `403a88263359216534fe9cb534063f8e8e2437701eaec9024f2b4fe9c3e0721e`; served_model `{"object": "list", "data": [{"id": "DeepSeek-V4.1-Flash", "object": "model", "created": 17`; checkpoint `{'repo': 'deepseek-ai/DeepSeek-V4.1-Flash-1017', 'expert_bits': 2, 'layer_bits': '10-29:3'`; chip `Apple M5 Ultra; 274877906944`

### ruler-streams

| streams | prose total (a stream) | code total (a stream) | structured total (a stream) | list total (a stream) | first token |
|---:|---:|---:|---:|---:|---:|
| 1 | 70.4 (70.4) | 90.5 (90.5) | 76.8 (76.8) | 88.6 (88.6) | 0.11-0.14 s |
| 2 | 89.3 (44.6) | 104.3 (52.2) | 97.9 (48.9) | 116.7 (58.4) | 0.22-0.28 s |
| 4 | 111.3 (27.9) | 117.5 (30.7) | 116.9 (29.1) | 128.2 (33.5) | 0.45-0.58 s |

### checks

| check | result |
|---|---|
| memory-idle | measured: mac: System-wide memory free percentage: 94%; total = 3072.00M  us |

## 2026-10-19 03:48: run `20261019-034805-dsv41-thinking`

Plan dsv41-thinking, done; served as `DeepSeek-V4.1-Flash`.

Serving: engine_commit `7837387a`; binary_sha256 `c35fad3f18d5efc6c8f1ca9ed81d87579a5507aba2798305ca3a593afbf2d12b`; served_model `{"object": "list", "data": [{"id": "DeepSeek-V4.1-Flash", "object": "model", "created": 17`; checkpoint `{'repo': 'deepseek-ai/DeepSeek-V4.1-Flash-1017', 'expert_bits': 2, 'layer_bits': '10-29:3'`; chip `Apple M5 Ultra; 274877906944`

### checks

| check | result |
|---|---|
| memory-idle | measured: mac: System-wide memory free percentage: 95%; total = 3072.00M  us |
| thinking | pass: thinking on: 10/10 right, 10/10 with reasoning_content, 0 leaks, 0 errors |

## 2026-10-18 20:28: run `20261018-202801-dsv41-quality`

Plan dsv41-quality, done; served as `DeepSeek-V4.1-Flash`.

Serving: engine_commit `269f2447`; binary_sha256 `072334f3cd20bb0bba0c16dceb1a9d92dd5d90b1ce26e3d4f0e4d33ddeb8f70c`; served_model `{"object": "list", "data": [{"id": "DeepSeek-V4.1-Flash", "object": "model", "created": 17`; checkpoint `{'repo': 'deepseek-ai/DeepSeek-V4.1-Flash-1017', 'expert_bits': 2, 'layer_bits': '10-29:3'`; chip `Apple M5 Ultra; 274877906944`

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
| ifeval | 129/150 |
| gsm8k | 247/250 |
| mgsm | 217/240 |
| mmlu | 307/342 |
| math500 | 457/500 |

### suite-thinking

| check | passed |
|---|---:|
| gsm8k | 237/250 |
| ifeval | 129/150 |

### checks

| check | result |
|---|---|
| memory-idle | measured: mac: System-wide memory free percentage: 95%; total = 4096.00M  us |
| thinking | pass: thinking on: 10/10 right, 10/10 with reasoning_content, 0 leaks, 0 errors |

## 2026-10-18 18:44: run `20261018-184411-speed`

Plan speed, done; served as `DeepSeek-V4.1-Flash`.

Serving: engine_commit `6a4d7be7`; binary_sha256 `898befed45888cbb0672978d14890e6565156cdd0f55dc1ecd6ec253c608e211`; served_model `{"object": "list", "data": [{"id": "DeepSeek-V4.1-Flash", "object": "model", "created": 17`; checkpoint `{'repo': 'deepseek-ai/DeepSeek-V4.1-Flash-1017', 'expert_bits': 2, 'layer_bits': '10-29:3'`; chip `Apple M5 Ultra; 274877906944`

### ruler-fresh

| streams | prose total (a stream) | code total (a stream) | structured total (a stream) | list total (a stream) | first token |
|---:|---:|---:|---:|---:|---:|
| 1 | 67.5 (67.5) | 87.5 (87.5) | 77.6 (77.6) | 94.4 (94.4) | 0.11-0.14 s |
| 2 | 145.0 (72.5) | 185.8 (92.9) | 154.4 (77.2) | 214.1 (107.1) | 0.94-1.55 s |

### ruler-after

| streams | prose total (a stream) | code total (a stream) | structured total (a stream) | list total (a stream) | first token |
|---:|---:|---:|---:|---:|---:|
| 1 | 69.1 (69.1) | 93.8 (93.8) | 76.0 (76.0) | 92.0 (92.0) | 0.11-0.14 s |

### checks

| check | result |
|---|---|
| memory-idle | measured: mac: System-wide memory free percentage: 15%; total = 5120.00M  us |
| turns | pass: resumed == again == cold: True; cached 4541 of 4561; ttft resumed 0.134s, cold 0.74s |
| memory-busy | measured: mac: System-wide memory free percentage: 15%; total = 5120.00M  us |

## 2026-10-18 18:39: run `20261018-183907-prefill`

Plan prefill, done; served as `DeepSeek-V4.1-Flash`.

Serving: engine_commit `6a4d7be7`; binary_sha256 `898befed45888cbb0672978d14890e6565156cdd0f55dc1ecd6ec253c608e211`; served_model `{"object": "list", "data": [{"id": "DeepSeek-V4.1-Flash", "object": "model", "created": 17`; checkpoint `{'repo': 'deepseek-ai/DeepSeek-V4.1-Flash-1017', 'expert_bits': 2, 'layer_bits': '10-29:3'`; chip `Apple M5 Ultra; 274877906944`

### checks

| check | result |
|---|---|
| memory-idle | measured: mac: System-wide memory free percentage: 15%; total = 6144.00M  us |
| prefill-off | measured: 2072 tokens 1092.8 tok/s (1.896 s), 8213 tokens 1240.1 tok/s (6.623 s), 32792 tokens 1255.6 tok/s (26.117 s), 131094 tokens 1195.3 tok/s (109.678 s) |
| prefill-thinking | measured: 2095 tokens 1338.7 tok/s (1.565 s), 8240 tokens 1392.4 tok/s (5.918 s), 32818 tokens 1334.2 tok/s (24.598 s), 131122 tokens 1209.8 tok/s (108.38 s) |
| memory-busy | measured: mac: System-wide memory free percentage: 14%; total = 6144.00M  us |

## 2026-10-18 17:24: run `20261018-172408-speed`

Plan speed, done; served as `DeepSeek-V4.1-Flash`.

Serving: engine_commit `6f4617c9`; binary_sha256 `859244df0d5db17f66fd5b10bc9d4b19d334e39c8f8051e20afa9efd3be42c2b`; served_model `{"object": "list", "data": [{"id": "DeepSeek-V4.1-Flash", "object": "model", "created": 17`; checkpoint `{'repo': 'deepseek-ai/DeepSeek-V4.1-Flash-1017', 'expert_bits': 2, 'layer_bits': '10-29:3'`; chip `Apple M5 Ultra; 274877906944`

### ruler-fresh

| streams | prose total (a stream) | code total (a stream) | structured total (a stream) | list total (a stream) | first token |
|---:|---:|---:|---:|---:|---:|
| 1 | 69.5 (69.5) | 92.5 (92.5) | 77.6 (77.6) | 88.1 (88.1) | 0.11-0.14 s |
| 2 | 144.3 (72.2) | 187.3 (93.6) | 158.2 (79.1) | 218.0 (109.0) | 0.91-1.59 s |

### ruler-after

| streams | prose total (a stream) | code total (a stream) | structured total (a stream) | list total (a stream) | first token |
|---:|---:|---:|---:|---:|---:|
| 1 | 72.1 (72.1) | 91.8 (91.8) | 79.1 (79.1) | 95.6 (95.6) | 0.11-0.14 s |

### checks

| check | result |
|---|---|
| memory-idle | measured: mac: System-wide memory free percentage: 16%; total = 3072.00M  us |
| turns | pass: resumed == again == cold: True; cached 4541 of 4561; ttft resumed 0.136s, cold 0.837s |
| memory-busy | measured: mac: System-wide memory free percentage: 15%; total = 3072.00M  us |

## 2026-10-18 17:17: run `20261018-171750-prefill`

Plan prefill, done; served as `DeepSeek-V4.1-Flash`.

Serving: engine_commit `6f4617c9`; binary_sha256 `859244df0d5db17f66fd5b10bc9d4b19d334e39c8f8051e20afa9efd3be42c2b`; served_model `{"object": "list", "data": [{"id": "DeepSeek-V4.1-Flash", "object": "model", "created": 17`; checkpoint `{'repo': 'deepseek-ai/DeepSeek-V4.1-Flash-1017', 'expert_bits': 2, 'layer_bits': '10-29:3'`; chip `Apple M5 Ultra; 274877906944`

### checks

| check | result |
|---|---|
| memory-idle | measured: mac: System-wide memory free percentage: 15%; total = 3072.00M  us |
| prefill-off | measured: 2072 tokens 887.0 tok/s (2.336 s), 8215 tokens 990.0 tok/s (8.298 s), 32791 tokens 992.9 tok/s (33.025 s), 131095 tokens 949.6 tok/s (138.05 s) |
| prefill-thinking | measured: 2095 tokens 1045.9 tok/s (2.003 s), 8241 tokens 1072.8 tok/s (7.682 s), 32820 tokens 1039.0 tok/s (31.587 s), 131122 tokens 965.5 tok/s (135.805 s) |
| memory-busy | measured: mac: System-wide memory free percentage: 15%; total = 3072.00M  us |

## 2026-10-18 16:54: run `20261018-165446-prefill`

Plan prefill, done; served as `DeepSeek-V4.1-Flash`.

Serving: engine_commit `544b3a40`; binary_sha256 `014ddc32e6d9743d5fe408d5000e17b334b20f2206e96f82d6c9acf42ce33c2b`; served_model `{"object": "list", "data": [{"id": "DeepSeek-V4.1-Flash", "object": "model", "created": 17`; checkpoint `{'repo': 'deepseek-ai/DeepSeek-V4.1-Flash-1017', 'expert_bits': 2, 'layer_bits': '10-29:3'`; chip `Apple M5 Ultra; 274877906944`

### checks

| check | result |
|---|---|
| memory-idle | measured: mac: System-wide memory free percentage: 14%; total = 3072.00M  us |
| prefill-off | measured: 2071 tokens 384.4 tok/s (5.387 s), 8218 tokens 398.8 tok/s (20.608 s), 32791 tokens 397.8 tok/s (82.436 s), 131095 tokens 391.4 tok/s (334.925 s) |
| prefill-thinking | measured: 2097 tokens 408.8 tok/s (5.13 s), 8242 tokens 411.7 tok/s (20.018 s), 32816 tokens 407.7 tok/s (80.489 s), 131123 tokens 395.3 tok/s (331.746 s) |
| memory-busy | measured: mac: System-wide memory free percentage: 15%; total = 3072.00M  us |

## 2026-10-18 16:48: run `20261018-164823-prefill`

Plan prefill, done; served as `DeepSeek-V4.1-Flash`.

Serving: engine_commit `544b3a40`; binary_sha256 `014ddc32e6d9743d5fe408d5000e17b334b20f2206e96f82d6c9acf42ce33c2b`; served_model `{"object": "list", "data": [{"id": "DeepSeek-V4.1-Flash", "object": "model", "created": 17`; checkpoint `{'repo': 'deepseek-ai/DeepSeek-V4.1-Flash-1017', 'expert_bits': 2, 'layer_bits': '10-29:3'`; chip `Apple M5 Ultra; 274877906944`

### checks

| check | result |
|---|---|
| memory-idle | measured: mac: System-wide memory free percentage: 14%; total = 3072.00M  us |
| prefill | FAIL: 1563 tokens 371.6 tok/s (4.206 s), 6184 tokens 387.9 tok/s (15.941 s), 24661 tokens 390.2 tok/s (63.197 s), 98572 tokens 392.3 tok/s (251.253 s); not cold or failed: ['32768', '131072'] |
| memory-busy | measured: mac: System-wide memory free percentage: 15%; total = 3072.00M  us |

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

