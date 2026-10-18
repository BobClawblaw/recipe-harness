# DeepSeek-V4.1-Flash-1017 EXL3 2.9bpw on 2x NVIDIA DGX Spark (GB10, 128 GB unified each), TP=2 over RoCE

Target `dsv41-1017-gb10-native`: DeepSeek-V4.1-Flash-1017 EXL3 2.9 bpw on native TensorFold (main + the deepseek_v41 CUDA family, PRs 667-727), TP=2 on two DGX Sparks, 4 slots, pool 900K. Engine: TensorFold native (Zig, CUDA): main 9ccf4727 + deepseek_v41 series, kit serving profile, DSpark drafts, images as placeholder. Rendered from `stats/dsv41-1017-gb10-native.json` (1 runs); aggregate tok/s, total (a stream).

## 2026-10-18 02:03: run `20261018-020350-dsv41-speed`

Plan dsv41-speed, done; served as `DeepSeek-V4.1-Flash-TF`.

Serving: image `00b298dda4527ad6`; pack `778baeaf9fbcd351`

### ruler-streams

| streams | prose total (a stream) | code total (a stream) | structured total (a stream) | list total (a stream) | first token |
|---:|---:|---:|---:|---:|---:|
| 1 | 53.3 (53.3) | 98.1 (98.1) | 61.0 (61.0) | 69.3 (69.3) | 0.20-0.28 s |
| 2 | 78.4 (39.2) | 121.8 (60.9) | 82.5 (41.3) | 139.0 (69.5) | 0.30-0.42 s |
| 4 | 105.7 (26.2) | 158.5 (39.4) | 110.6 (26.5) | 176.4 (41.4) | 0.75-1.00 s |

### checks

| check | result |
|---|---|
| memory-idle | measured: head 6.3 GiB available |

