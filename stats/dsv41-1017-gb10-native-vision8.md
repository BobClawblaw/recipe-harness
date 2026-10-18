# DeepSeek-V4.1-Flash-1017 EXL3 2.9bpw on 2x NVIDIA DGX Spark (GB10, 128 GB unified each), TP=2 over RoCE

Target `dsv41-1017-gb10-native-vision8`: DeepSeek-V4.1-Flash-1017 EXL3 2.9 bpw on native TensorFold (main + the kit engine), native images and video, TP=2 on two DGX Sparks, 8 slots, pool 400K, prefill-dip reserve 2 GiB. Engine: TensorFold native (Zig, CUDA): main 9ccf4727 + the DeepSeek-V4.1 kit engine, vision tower, video as frames, DSpark drafts, 8 slots. Rendered from `stats/dsv41-1017-gb10-native-vision8.json` (1 runs); aggregate tok/s, total (a stream).

## 2026-10-18 09:22: run `20261018-092218-dsv41-speed8`

Plan dsv41-speed8, done; served as `DeepSeek-V4.1-Flash-TF`.

Serving: image `7b3d42e0e5865d34`; pack `778baeaf9fbcd351`

### ruler-streams

| streams | prose total (a stream) | code total (a stream) | structured total (a stream) | list total (a stream) | first token |
|---:|---:|---:|---:|---:|---:|
| 1 | 55.4 (55.4) | 103.5 (103.5) | 62.7 (62.7) | 70.9 (70.9) | 0.19-0.26 s |
| 2 | 81.5 (40.7) | 126.2 (63.1) | 89.4 (44.7) | 142.7 (71.4) | 0.30-0.48 s |
| 4 | 108.8 (26.8) | 163.8 (40.3) | 113.7 (28.4) | 180.4 (44.4) | 0.71-0.85 s |
| 8 | 134.8 (16.7) | 202.7 (25.4) | 143.6 (17.4) | 203.3 (24.8) | 1.35-1.84 s |

### checks

| check | result |
|---|---|
| memory-idle | measured: head 6.3 GiB available |

