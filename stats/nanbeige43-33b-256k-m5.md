# Nanbeige4.3-33B, bf16 on 1x Apple M5 Ultra (256 GB unified), macOS

Target `nanbeige43-33b-256k-m5`: Nanbeige4.3-33B bf16 as released, TensorFold native Metal (llama) on one M5 Ultra (262144-token window, 1 stream: the long-window setting). Engine: TensorFold native, Metal. Rendered from `stats/nanbeige43-33b-256k-m5.json` (4 runs); aggregate tok/s, total (a stream).

## 2026-11-03 04:03: run `20261103-040333-prefill-32k`

Plan prefill-32k, done; served as `nanbeige`.

Serving: engine_commit `c3ee3db24`; binary_sha256 `0d5c5c6b34b6267ae99c4d9182b1c71c2e71af9bbfd2e697cbe487398bf0224f`; served_model `{"object": "list", "data": [{"id": "nanbeige", "object": "model", "created": 1793700226, "`; chip `Apple M5 Ultra; 274877906944`; suite_commit `21db9b23f7be`

### checks

| check | result |
|---|---|
| memory-idle | measured: mac: System-wide memory free percentage: 25%; total = 8192.00M  us |
| prefill-off | measured: 2110 tokens 1240.4 tok/s (1.701 s), 8252 tokens 1283.4 tok/s (6.43 s), 16441 tokens 1206.7 tok/s (13.625 s), 30782 tokens 1046.3 tok/s (29.421 s) |
| prefill-thinking | measured: 2105 tokens 1232.4 tok/s (1.708 s), 8249 tokens 1282.7 tok/s (6.431 s), 16439 tokens 1204.0 tok/s (13.654 s), 30778 tokens 1014.9 tok/s (30.327 s) |
| memory-busy | measured: mac: System-wide memory free percentage: 39%; total = 8192.00M  us |

## 2026-11-03 03:59: run `20261103-035934-prefill-32k`

Plan prefill-32k, done; served as `nanbeige`.

Serving: engine_commit `50fe245ac`; binary_sha256 `c3fcf8cacf289aec9ee53f1eae52fda4fab2f1eeda1bf75b61482542dba4b3d1`; served_model `{"object": "list", "data": [{"id": "nanbeige", "object": "model", "created": 1793699992, "`; chip `Apple M5 Ultra; 274877906944`; suite_commit `21db9b23f7be`

### checks

| check | result |
|---|---|
| memory-idle | measured: mac: System-wide memory free percentage: 16%; total = 8192.00M  us |
| prefill-off | measured: 2110 tokens 878.8 tok/s (2.401 s), 8254 tokens 1006.5 tok/s (8.201 s), 16444 tokens 852.7 tok/s (19.284 s), 30782 tokens 728.4 tok/s (42.261 s) |
| prefill-thinking | measured: 2107 tokens 888.3 tok/s (2.372 s), 8251 tokens 856.4 tok/s (9.635 s), 16442 tokens 792.0 tok/s (20.761 s), 30775 tokens 690.7 tok/s (44.558 s) |
| memory-busy | measured: mac: System-wide memory free percentage: 33%; total = 8192.00M  us |

## 2026-11-03 03:46: run `20261103-034622-prefill`

Plan prefill, done; served as `nanbeige`.

Serving: engine_commit `c3ee3db24`; binary_sha256 `0d5c5c6b34b6267ae99c4d9182b1c71c2e71af9bbfd2e697cbe487398bf0224f`; served_model `{"object": "list", "data": [{"id": "nanbeige", "object": "model", "created": 1793699195, "`; chip `Apple M5 Ultra; 274877906944`; suite_commit `21db9b23f7be`

### checks

| check | result |
|---|---|
| memory-idle | measured: mac: System-wide memory free percentage: 23%; total = 10240.00M  u |
| prefill-off | measured: 2109 tokens 1192.9 tok/s (1.768 s), 8252 tokens 1234.6 tok/s (6.684 s), 32830 tokens 993.4 tok/s (33.048 s), 131132 tokens 466.7 tok/s (280.992 s) |
| prefill-thinking | measured: 2105 tokens 940.2 tok/s (2.239 s), 8249 tokens 928.8 tok/s (8.881 s), 32825 tokens 712.3 tok/s (46.08 s), 131131 tokens 460.2 tok/s (284.965 s) |
| memory-busy | measured: mac: System-wide memory free percentage: 17%; total = 8192.00M  us |

## 2026-10-26 04:35: run `20261026-043526-prefill`

Plan prefill, done; served as `nanbeige`.

Serving: engine_commit `490b6b9a5`; binary_sha256 `f2a9ddfd933ba5b60c5921180b31faeca58b8ac826e09b78911e49d0ef7342a0`; served_model `{"object": "list", "data": [{"id": "nanbeige", "object": "model", "created": 1793007335, "`; chip `Apple M5 Ultra; 274877906944`; suite_commit `277c842a1481`

### checks

| check | result |
|---|---|
| memory-idle | measured: mac: System-wide memory free percentage: 33%; total = 5120.00M  us |
| prefill-off | measured: 2110 tokens 1250.0 tok/s (1.688 s), 8255 tokens 1277.9 tok/s (6.46 s), 32831 tokens 1053.6 tok/s (31.162 s), 131132 tokens 562.6 tok/s (233.095 s) |
| prefill-thinking | measured: 2103 tokens 1229.8 tok/s (1.71 s), 8250 tokens 1298.6 tok/s (6.353 s), 32826 tokens 1029.8 tok/s (31.875 s), 131128 tokens 557.7 tok/s (235.108 s) |
| memory-busy | measured: mac: System-wide memory free percentage: 19%; total = 5120.00M  us |

