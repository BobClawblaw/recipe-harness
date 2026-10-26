# Nanbeige4.3-33B, bf16 on 1x Apple M5 Ultra (256 GB unified), macOS

Target `nanbeige43-33b-256k-m5`: Nanbeige4.3-33B bf16 as released, TensorFold native Metal (llama) on one M5 Ultra (262144-token window, 1 stream: the long-window setting). Engine: TensorFold native, Metal. Rendered from `stats/nanbeige43-33b-256k-m5.json` (1 runs); aggregate tok/s, total (a stream).

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

