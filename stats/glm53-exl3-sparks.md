# GLM-5.3-Flash, EXL3 4 bpw on 2x NVIDIA DGX Spark (GB10, 128 GB unified each), TP=2 over RoCE

Target `glm53-exl3-sparks`: GLM-5.3-Flash EXL3 4 bpw, TensorFold native, TP=2 on two DGX Sparks. Engine: TensorFold native, CUDA. Rendered from `stats/glm53-exl3-sparks.json` (3 runs); aggregate tok/s, total (a stream).

## 2026-10-14 00:00: run `evidence/2026-10-14`

Plan published evidence, published; served as `GLM-5.3-Flash-EXL3`.

### ruler-shipped-14fb445e-c1-sampled

| streams | prose total (a stream) | code total (a stream) | structured total (a stream) | list total (a stream) | first token |
|---:|---:|---:|---:|---:|---:|
| 1 | 45.1 (45.2) | 64.6 (65.4) | 56.5 (56.2) | 57.0 (54.9) | 0.18-0.25 s |

### ruler-shipped-14fb445e-c1

| streams | prose total (a stream) | code total (a stream) | structured total (a stream) | list total (a stream) | first token |
|---:|---:|---:|---:|---:|---:|
| 1 | 46.5 (45.4) | 68.7 (69.4) | 57.0 (56.4) | 58.8 (55.3) | 0.18-0.24 s |

### ruler-shipped-14fb445e-c16

| streams | prose total (a stream) | code total (a stream) | structured total (a stream) | list total (a stream) | first token |
|---:|---:|---:|---:|---:|---:|
| 16 | 144.0 (8.9) | 198.3 (12.1) | 180.1 (11.3) | 208.4 (12.5) | 0.91-1.19 s |

### ruler-shipped-14fb445e-c8

| streams | prose total (a stream) | code total (a stream) | structured total (a stream) | list total (a stream) | first token |
|---:|---:|---:|---:|---:|---:|
| 8 | 110.1 (13.6) | 152.5 (18.6) | 138.7 (17.5) | 157.0 (18.7) | 0.49-0.63 s |

### ruler-shipped-f95f2f70-c1-sampled

| streams | prose total (a stream) | code total (a stream) | structured total (a stream) | list total (a stream) | first token |
|---:|---:|---:|---:|---:|---:|
| 1 | 45.4 (45.4) | 65.8 (67.0) | 56.4 (55.9) | 58.1 (55.3) | 0.17-0.23 s |

### ruler-shipped-f95f2f70-c1

| streams | prose total (a stream) | code total (a stream) | structured total (a stream) | list total (a stream) | first token |
|---:|---:|---:|---:|---:|---:|
| 1 | 47.5 (46.5) | 69.5 (69.9) | 58.2 (56.9) | 60.2 (56.8) | 0.16-0.23 s |

### ruler-shipped-f95f2f70-c16

| streams | prose total (a stream) | code total (a stream) | structured total (a stream) | list total (a stream) | first token |
|---:|---:|---:|---:|---:|---:|
| 16 | 144.8 (8.9) | 202.2 (12.3) | 181.4 (11.4) | 207.6 (12.5) | 0.85-1.14 s |

### ruler-shipped-f95f2f70-c8

| streams | prose total (a stream) | code total (a stream) | structured total (a stream) | list total (a stream) | first token |
|---:|---:|---:|---:|---:|---:|
| 8 | 111.1 (13.7) | 154.1 (18.7) | 139.5 (17.2) | 157.3 (18.8) | 0.45-0.60 s |

### ablit/suite

| check | passed |
|---|---:|
| gsm8k | 246/250 |
| mmlu | 292/342 |
| humaneval | 159/164 |
| ifeval | 118/150 |
| tools | 59/60 |
| json | 30/30 |
| mgsm | 221/240 |

### suite-ab

| check | passed |
|---|---:|
| gsm8k | 244/250 |
| mmlu | 292/342 |
| humaneval | 156/164 |
| ifeval | 118/150 |
| tools | 59/60 |
| json | 30/30 |
| mgsm | 223/240 |

## 2026-10-13 00:00: run `evidence/2026-10-13`

Plan published evidence, published; served as `GLM-5.3-Flash-EXL3`.

### ruler-252-c1-sampled

| streams | prose total (a stream) | code total (a stream) | structured total (a stream) | list total (a stream) | first token |
|---:|---:|---:|---:|---:|---:|
| 1 | 44.0 (45.7) | 57.0 (57.4) | 56.6 (57.2) | 56.1 (55.5) | 0.17-0.27 s |

### ruler-252-c1

| streams | prose total (a stream) | code total (a stream) | structured total (a stream) | list total (a stream) | first token |
|---:|---:|---:|---:|---:|---:|
| 1 | 712.7 (45.1) | 1083.6 (69.1) | 962.9 (61.2) | 966.2 (58.3) | 0.18-0.26 s |

### ruler-252-c8

| streams | prose total (a stream) | code total (a stream) | structured total (a stream) | list total (a stream) | first token |
|---:|---:|---:|---:|---:|---:|
| 8 | 347.0 (44.0) | 533.5 (67.7) | 461.2 (57.6) | 514.6 (63.2) | 9.96-20.91 s |

### ruler-deployed-6861d48f-c1-sampled

| streams | prose total (a stream) | code total (a stream) | structured total (a stream) | list total (a stream) | first token |
|---:|---:|---:|---:|---:|---:|
| 1 | 43.8 (44.1) | 63.1 (63.1) | 55.5 (57.4) | 53.1 (54.0) | 0.20-0.29 s |

### ruler-deployed-6861d48f-c1

| streams | prose total (a stream) | code total (a stream) | structured total (a stream) | list total (a stream) | first token |
|---:|---:|---:|---:|---:|---:|
| 1 | 43.9 (44.2) | 63.7 (69.6) | 53.5 (55.4) | 55.4 (55.2) | 0.20-0.29 s |

### ruler-deployed-6861d48f-c8

| streams | prose total (a stream) | code total (a stream) | structured total (a stream) | list total (a stream) | first token |
|---:|---:|---:|---:|---:|---:|
| 8 | 100.9 (12.6) | 125.4 (15.3) | 102.3 (12.5) | 122.3 (14.9) | 0.54-4.29 s |

### ruler-deployed-6861d48f-roce2048-c1

| streams | prose total (a stream) | code total (a stream) | structured total (a stream) | list total (a stream) | first token |
|---:|---:|---:|---:|---:|---:|
| 1 | 46.6 (46.2) | 69.5 (69.8) | 57.7 (56.7) | 59.0 (56.1) | 0.20-0.28 s |

### ruler-deployed-6861d48f-roce2048-c8

| streams | prose total (a stream) | code total (a stream) | structured total (a stream) | list total (a stream) | first token |
|---:|---:|---:|---:|---:|---:|
| 8 | 110.3 (13.7) | 153.5 (18.7) | 136.8 (17.0) | 157.7 (18.8) | 0.54-0.72 s |

### ruler-shipped-6861d48f-c1

| streams | prose total (a stream) | code total (a stream) | structured total (a stream) | list total (a stream) | first token |
|---:|---:|---:|---:|---:|---:|
| 1 | 46.5 (45.9) | 69.3 (69.8) | 57.6 (56.7) | 59.0 (56.1) | 0.19-0.29 s |

### ruler-shipped-6861d48f-c16

| streams | prose total (a stream) | code total (a stream) | structured total (a stream) | list total (a stream) | first token |
|---:|---:|---:|---:|---:|---:|
| 16 | 141.9 (8.7) | 199.0 (12.1) | 178.7 (11.1) | 207.0 (12.4) | 1.00-1.42 s |

### ruler-shipped-6861d48f-c8

| streams | prose total (a stream) | code total (a stream) | structured total (a stream) | list total (a stream) | first token |
|---:|---:|---:|---:|---:|---:|
| 8 | 110.2 (13.7) | 152.3 (18.4) | 138.0 (17.3) | 157.1 (19.0) | 0.54-0.74 s |

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
| tools | 59/60 |
| json | 30/30 |
| ifeval | 118/150 |
| gsm8k | 243/250 |
| mgsm | 217/240 |
| mmlu | 294/342 |
| math500 | 442/500 |
| gpqa | 140/198 |
| humaneval | 157/164 |
| repetition | 8/8 |
| long-context | 42/42 |
| long-tasks | 36/40 |
| soak | 0/60 |
| snapshot | 12/12 |
| vision | 6/6 |
| docvision | 0/0 |
| concurrent | 12/12 |
| vision-concurrent | 16/16 |

### suite-docvision

| check | passed |
|---|---:|
| chartqa | 147/200 |
| docvqa | 112/200 |

### suite-soak

| check | passed |
|---|---:|
| soak | 0/60 |

## 2026-10-12 00:00: run `evidence/2026-10-12`

Plan published evidence, published; served as `GLM-5.3-Flash-EXL3`.

### ruler-deployed-443398c9

| streams | prose total (a stream) | code total (a stream) | structured total (a stream) | list total (a stream) | first token |
|---:|---:|---:|---:|---:|---:|
| 1 | 45.4 (45.4) | 62.8 (62.8) | 55.6 (55.6) | 54.9 (54.9) | 0.11-0.16 s |
| 8 | 112.4 (13.8) | 148.2 (18.3) | 137.4 (17.0) | 167.7 (19.7) | 0.44-0.61 s |
| 16 | 124.7 (7.7) | 169.5 (10.1) | 137.9 (8.5) | 155.4 (9.1) | 0.45-1.19 s |

