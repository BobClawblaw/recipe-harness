# Unlimited-OCR-2, bf16 on 1x Apple M5 Ultra (256 GB unified), macOS

Target `unlimited-ocr-2-m5`: Unlimited-OCR-2 bf16 as released, TensorFold native Metal (unlimited-ocr) on one M5 Ultra (131072-token window, one stream). Engine: TensorFold native, Metal. Rendered from `stats/unlimited-ocr-2-m5.json` (1 runs); aggregate tok/s, total (a stream).

## 2026-11-03 15:19: run `20261103-151950-ocr`

Plan ocr, done; served as `Unlimited-OCR-2`.

Serving: engine_commit `b2553e5f9`; binary_sha256 `2a2173f5c64a844fcb34acda6e9d1e631afefb3ffa9b111e005fb4f021936824`; served_model `{"object": "list", "data": [{"id": "Unlimited-OCR-2", "object": "model", "created": 179374`; chip `Apple M5 Ultra; 274877906944`

### checks

| check | result |
|---|---|
| memory-idle | measured: mac: System-wide memory free percentage: 43% |
| ocr | pass: 6/6 cases answered; decode 213-246 tok/s, first token 0.83-4.10 s; 2 at once 102-217 tok/s in all; vs reference: identical 2/6, similarity 0.9973-1.0000, text without boxes identical 6/6, box coords moved 10/288 (at most 10) |
| memory-after | measured: mac: System-wide memory free percentage: 37% |

