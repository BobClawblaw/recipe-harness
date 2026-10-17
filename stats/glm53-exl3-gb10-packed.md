# GLM-5.3-Flash EXL3 4bpw on 2x NVIDIA DGX Spark (GB10, 128 GB unified each), TP=2 over RoCE

Target `glm53-exl3-gb10-packed`: GLM-5.3-Flash EXL3 4bpw, families/glm with 4-bit dense / 8-bit head, DFlash2 and 16 streams (PRs 855+979+984 and packing), TP=2 on two DGX Sparks. Engine: TensorFold native, CUDA: families/glm, packed linears (4/8, bf16 freed), DFlash2, 16 streams, prompts one at a time. Rendered from `stats/glm53-exl3-gb10-packed.json` (1 runs); aggregate tok/s, total (a stream).

## 2026-10-17 19:52: run `20261017-195233-glm-ab-ifeval`

Plan glm-ab-ifeval, done; served as `GLM-5.3-Flash-EXL3`.

Serving: binary `cf50867102a60c38`

### suite

| check | passed |
|---|---:|
| ifeval | 103/150 |
| json | 30/30 |

