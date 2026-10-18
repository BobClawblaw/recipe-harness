# DeepSeek-V4.1-Flash-1017 EXL3 2.9bpw on 2x NVIDIA DGX Spark (GB10, 128 GB unified each), TP=2 over RoCE

Target `dsv41-1017-gb10-native-vision`: DeepSeek-V4.1-Flash-1017 EXL3 2.9 bpw on native TensorFold (main + jayleaton's kit engine 9131e10a ported onto it), native images and video, TP=2 on two DGX Sparks, 4 slots, pool 200K. Engine: TensorFold native (Zig, CUDA): main 9ccf4727 + the DeepSeek-V4.1 kit engine, vision tower (TF_DSV41_IMAGES=native), video as sampled frames, DSpark drafts. Rendered from `stats/dsv41-1017-gb10-native-vision.json` (1 runs); aggregate tok/s, total (a stream).

## 2026-10-18 03:24: run `20261018-032401-dsv41-speed`

Plan dsv41-speed, done; served as `DeepSeek-V4.1-Flash-TF`.

Serving: image `7b3d42e0e5865d34`; pack `778baeaf9fbcd351`

### ruler-streams

| streams | prose total (a stream) | code total (a stream) | structured total (a stream) | list total (a stream) | first token |
|---:|---:|---:|---:|---:|---:|
| 1 | 55.2 (55.2) | 100.4 (100.4) | 62.5 (62.5) | 71.4 (71.4) | 0.19-0.26 s |
| 2 | 81.0 (40.5) | 124.9 (62.5) | 84.2 (42.1) | 143.6 (71.8) | 0.31-0.40 s |
| 4 | 106.5 (26.4) | 161.6 (40.0) | 111.9 (26.9) | 178.7 (43.1) | 0.73-0.99 s |

### checks

| check | result |
|---|---|
| memory-idle | measured: head 6.6 GiB available |

