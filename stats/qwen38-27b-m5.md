# Qwen3.8-27B, MLX 4-bit + DFlash2 on 1x Apple M5 Ultra (256 GB unified), macOS

Target `qwen38-27b-m5`: Qwen3.8-27B MLX 4-bit + DFlash2, TensorFold native Metal on one M5 Ultra (262144-token window, 2 streams). Engine: TensorFold native, Metal. Rendered from `stats/qwen38-27b-m5.json` (1 runs); aggregate tok/s, total (a stream).

## 2026-11-13 19:19: run `20261113-191947-agentic`

Plan agentic, done; served as `qwen27`.

Serving: engine_commit `8ff047753`; binary_sha256 `1acce1a163b6e87fe875869f600151b30b400cd13183ead34d4938dda67280b3`; served_model `{"object": "list", "data": [{"id": "qwen27", "object": "model", "created": 1794619351, "ow`; chip `Apple M5 Ultra; 274877906944`; suite_commit `b3b0ef38b8bc`

### checks

| check | result |
|---|---|
| agentic-off | pass: right; 19 replies, 17/17 trail modules read, 0 repeat reads, longest identical run 1, peak prompt 103828 tokens, 104.7 s |
| agentic-thinking | pass: right; 18 replies, 16/16 trail modules read, 0 repeat reads, longest identical run 1, peak prompt 97790 tokens, 120.4 s |

