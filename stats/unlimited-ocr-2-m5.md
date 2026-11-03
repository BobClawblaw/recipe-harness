# Unlimited-OCR-2, bf16 on 1x Apple M5 Ultra (256 GB unified), macOS

Target `unlimited-ocr-2-m5`: Unlimited-OCR-2 bf16 as released, TensorFold native Metal (unlimited-ocr) on one M5 Ultra (131072-token window, one stream). Engine: TensorFold native, Metal. Rendered from `stats/unlimited-ocr-2-m5.json` (5 runs); aggregate tok/s, total (a stream).

## 2026-11-03 17:17: run `20261103-171755-ocr`

Plan ocr, done; served as `Unlimited-OCR-2`.

Serving: engine_commit `a05fe5c95`; binary_sha256 `db41c164ccc56642d466f9b88568f14f449822c56e99cff91d4bdebde278b5cd`; served_model `{"object": "list", "data": [{"id": "Unlimited-OCR-2", "object": "model", "created": 179374`; chip `Apple M5 Ultra; 274877906944`

### checks

| check | result |
|---|---|
| memory-idle | measured: mac: System-wide memory free percentage: 43% |
| ocr | pass: 6/6 cases answered; decode 224-261 tok/s, first token 0.81-4.00 s; 2 at once 108-220 tok/s in all; vs reference: identical 2/6, similarity 0.9973-1.0000, text without boxes identical 6/6, box coords moved 10/288 (at most 10) |
| memory-after | measured: mac: System-wide memory free percentage: 37% |

## 2026-11-03 17:03: run `20261103-170315-ocr`

Plan ocr, done; served as `Unlimited-OCR-2`.

Serving: engine_commit `b53842b15`; binary_sha256 `e27d6f9f261757add1fe75b7579bbc485e8d44fe6eb6af7869b092ec62a4b7e5`; served_model `{"object": "list", "data": [{"id": "Unlimited-OCR-2", "object": "model", "created": 179374`; chip `Apple M5 Ultra; 274877906944`

### checks

| check | result |
|---|---|
| memory-idle | measured: mac: System-wide memory free percentage: 43% |
| ocr | pass: 6/6 cases answered; decode 222-263 tok/s, first token 0.80-4.11 s; 2 at once 102-220 tok/s in all; vs reference: identical 2/6, similarity 0.9973-1.0000, text without boxes identical 6/6, box coords moved 10/288 (at most 10) |
| memory-after | measured: mac: System-wide memory free percentage: 37% |

## 2026-11-03 16:40: run `20261103-164007-ocr`

Plan ocr, done; served as `Unlimited-OCR-2`.

Serving: engine_commit `2f4814f58`; binary_sha256 `da46cd0a48f3237899a7f74a722bc55b8f9be4fd1529e649c6dfed7dfb85a8ba`; served_model `{"object": "list", "data": [{"id": "Unlimited-OCR-2", "object": "model", "created": 179374`; chip `Apple M5 Ultra; 274877906944`

### checks

| check | result |
|---|---|
| memory-idle | measured: mac: System-wide memory free percentage: 42% |
| ocr | pass: 6/6 cases answered; decode 210-243 tok/s, first token 0.86-4.23 s; 2 at once 100-215 tok/s in all; vs reference: identical 2/6, similarity 0.9973-1.0000, text without boxes identical 6/6, box coords moved 10/288 (at most 10) |
| memory-after | measured: mac: System-wide memory free percentage: 36% |

## 2026-11-03 15:27: run `20261103-152737-ocr`

Plan ocr, done; served as `Unlimited-OCR-2`.

Serving: engine_commit `c94b385e8`; binary_sha256 `35971dfd7d88b48d2dfc901cedb5b0b61c0d5f6f9580b92c0906cfc81de40b19`; served_model `{"object": "list", "data": [{"id": "Unlimited-OCR-2", "object": "model", "created": 179374`; chip `Apple M5 Ultra; 274877906944`

### checks

| check | result |
|---|---|
| memory-idle | measured: mac: System-wide memory free percentage: 43% |
| ocr | pass: 6/6 cases answered; decode 214-249 tok/s, first token 0.84-4.08 s; 2 at once 102-217 tok/s in all; vs reference: identical 2/6, similarity 0.9973-1.0000, text without boxes identical 6/6, box coords moved 10/288 (at most 10) |
| memory-after | measured: mac: System-wide memory free percentage: 37% |

## 2026-11-03 15:19: run `20261103-151950-ocr`

Plan ocr, done; served as `Unlimited-OCR-2`.

Serving: engine_commit `b2553e5f9`; binary_sha256 `2a2173f5c64a844fcb34acda6e9d1e631afefb3ffa9b111e005fb4f021936824`; served_model `{"object": "list", "data": [{"id": "Unlimited-OCR-2", "object": "model", "created": 179374`; chip `Apple M5 Ultra; 274877906944`

### checks

| check | result |
|---|---|
| memory-idle | measured: mac: System-wide memory free percentage: 43% |
| ocr | pass: 6/6 cases answered; decode 213-246 tok/s, first token 0.83-4.10 s; 2 at once 102-217 tok/s in all; vs reference: identical 2/6, similarity 0.9973-1.0000, text without boxes identical 6/6, box coords moved 10/288 (at most 10) |
| memory-after | measured: mac: System-wide memory free percentage: 37% |

