# Ornith-1.5-122B, 4-bit MLX affine (g64) on 1x Apple M5 Ultra (256 GB unified), macOS

Target `ornith-15-122b-m5`: Ornith-1.5-122B, 4-bit MLX affine with images, vllm-mlx on one M5 Ultra. Engine: vllm-mlx 0.6.0 (mlx-vlm 0.7.9, mlx-lm 0.31.3, mlx 0.32.4). Rendered from `stats/ornith-15-122b-m5.json` (1 runs); aggregate tok/s, total (a stream).

## 2026-10-20 11:17: run `20261020-111724-mlx-speed`

Plan mlx-speed, done; served as `Ornith-1.5-122B`.

Serving: stack `vllm-mlx 0.6.0, mlx-vlm 0.7.9, mlx-lm 0.31.3, mlx 0.32.4`; served_model `{"object":"list","data":[{"id":"Ornith-1.5-122B","object":"model","created":1792513044,"ow`; checkpoint `{'dir': 'Ornith-1.5-122B-MLX-4bit', 'bits': 4, 'group_size': 64, 'mode': 'affine', 'revisi`; chip `Apple M5 Ultra; 274877906944`; suite_commit `277c842a1481`

### ruler-streams

| streams | prose total (a stream) | code total (a stream) | structured total (a stream) | list total (a stream) | first token |
|---:|---:|---:|---:|---:|---:|
| 1 | 66.2 (66.2) | 66.6 (66.6) | 66.4 (66.4) | 66.6 (66.6) | 0.08-0.11 s |
| 2 | 113.4 (56.7) | 113.2 (56.6) | 113.2 (56.6) | 114.0 (57.0) | 0.14-0.19 s |
| 4 | 175.9 (44.0) | 178.1 (44.9) | 177.6 (44.1) | 180.4 (44.9) | 0.25-0.35 s |

### checks

| check | result |
|---|---|
| memory-idle | measured: mac: System-wide memory free percentage: 95%; total = 7168.00M  us |

