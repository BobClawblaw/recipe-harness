# Unlimited-OCR-2, bf16 on 1x Apple M5 Ultra (256 GB unified), macOS

Target `unlimited-ocr-2-m5`: Unlimited-OCR-2 bf16 as released, TensorFold native Metal (unlimited-ocr) on one M5 Ultra (131072-token window, one stream). Engine: TensorFold native, Metal. Rendered from `stats/unlimited-ocr-2-m5.json` (15 runs); aggregate tok/s, total (a stream).

## 2026-11-06 10:42: run `20261106-104202-ocr`

Plan ocr, done; served as `Unlimited-OCR-2`.

Serving: engine_commit `f7c686f36`; binary_sha256 `adf4f3c4bb9f45a1501bbf5d41b1bfc1821284d2cb5b7e484846840046c72313`; served_model `{"object": "list", "data": [{"id": "Unlimited-OCR-2", "object": "model", "created": 179398`; chip `Apple M5 Ultra; 274877906944`

### checks

| check | result |
|---|---|
| memory-idle | measured: mac: System-wide memory free percentage: 88% |
| ocr | pass: 6/6 cases answered; decode 303-308 tok/s, first token 0.27-1.45 s; 2 at once 200-296 tok/s in all; vs reference: identical 1/6, similarity 0.9844-1.0000, text without boxes identical 3/6, box coords moved 102/284 (at most 824) |
| memory-after | measured: mac: System-wide memory free percentage: 83% |

## 2026-11-06 10:18: run `20261106-101800-ocr`

Plan ocr, done; served as `Unlimited-OCR-2`.

Serving: engine_commit `3ced46888`; binary_sha256 `9d02efd57e1937f673bb26395c8277c1dcdbfad3631f13cbca750137dd0f7561`; served_model `{"object": "list", "data": [{"id": "Unlimited-OCR-2", "object": "model", "created": 179398`; chip `Apple M5 Ultra; 274877906944`

### checks

| check | result |
|---|---|
| memory-idle | measured: mac: System-wide memory free percentage: 88% |
| ocr | pass: 6/6 cases answered; decode 305-309 tok/s, first token 0.28-1.45 s; 2 at once 201-297 tok/s in all; vs reference: identical 1/6, similarity 0.9844-1.0000, text without boxes identical 3/6, box coords moved 102/284 (at most 824) |
| memory-after | measured: mac: System-wide memory free percentage: 83% |

## 2026-11-05 08:26: run `20261105-082603-ocr`

Plan ocr, done; served as `Unlimited-OCR-2`.

Serving: engine_commit `0af3eb8c8`; binary_sha256 `8b298588bd2754c4a49396e13f40761d933035cc4070f8bb8e53bdd543f12313`; served_model `{"object": "list", "data": [{"id": "Unlimited-OCR-2", "object": "model", "created": 179388`; chip `Apple M5 Ultra; 274877906944`

### checks

| check | result |
|---|---|
| memory-idle | measured: mac: System-wide memory free percentage: 89% |
| ocr | pass: 6/6 cases answered; decode 225-262 tok/s, first token 0.79-3.90 s; 2 at once 108-232 tok/s in all; vs reference: identical 2/6, similarity 0.9973-1.0000, text without boxes identical 6/6, box coords moved 10/288 (at most 10) |
| memory-after | measured: mac: System-wide memory free percentage: 83% |

## 2026-11-05 06:51: run `20261105-065147-ocr`

Plan ocr, done; served as `Unlimited-OCR-2`.

Serving: engine_commit `e2fa967c6`; binary_sha256 `207a1e504c2858dfa7ac21c527293dbd1363f1dbc3b3cbf7e813d6753b80c287`; served_model `{"object": "list", "data": [{"id": "Unlimited-OCR-2", "object": "model", "created": 179388`; chip `Apple M5 Ultra; 274877906944`

### checks

| check | result |
|---|---|
| memory-idle | measured: mac: System-wide memory free percentage: 89% |
| ocr | pass: 6/6 cases answered; decode 228-266 tok/s, first token 0.80-3.92 s; 2 at once 108-233 tok/s in all; vs reference: identical 2/6, similarity 0.9973-1.0000, text without boxes identical 6/6, box coords moved 10/288 (at most 10) |
| memory-after | measured: mac: System-wide memory free percentage: 83% |

## 2026-11-04 09:57: run `20261104-095754-ocr`

Plan ocr, done; served as `Unlimited-OCR-2`.

Serving: engine_commit `11b03ae68`; binary_sha256 `f593da3bce9279449fa79d7fdcb22295b11e90e502330a912a4aa50ce34e10c3`; served_model `{"object": "list", "data": [{"id": "Unlimited-OCR-2", "object": "model", "created": 179380`; chip `Apple M5 Ultra; 274877906944`

### checks

| check | result |
|---|---|
| memory-idle | measured: mac: System-wide memory free percentage: 44% |
| ocr | pass: 6/6 cases answered; decode 216-255 tok/s, first token 0.82-3.93 s; 2 at once 101-230 tok/s in all; vs reference: identical 2/6, similarity 0.9973-1.0000, text without boxes identical 6/6, box coords moved 10/288 (at most 10) |
| memory-after | measured: mac: System-wide memory free percentage: 38% |

## 2026-11-04 05:28: run `20261104-052806-ocr`

Plan ocr, done; served as `Unlimited-OCR-2`.

Serving: engine_commit `a4e444f6a`; binary_sha256 `39c3501d296716215a423a32f4de5834ed574dc24a676c5278140664d5eecdfa`; served_model `{"object": "list", "data": [{"id": "Unlimited-OCR-2", "object": "model", "created": 179379`; chip `Apple M5 Ultra; 274877906944`

### checks

| check | result |
|---|---|
| memory-idle | measured: mac: System-wide memory free percentage: 44% |
| ocr | pass: 6/6 cases answered; decode 202-267 tok/s, first token 0.79-4.08 s; 2 at once 108-207 tok/s in all; vs reference: identical 2/6, similarity 0.9973-1.0000, text without boxes identical 6/6, box coords moved 10/288 (at most 10) |
| memory-after | measured: mac: System-wide memory free percentage: 38% |

## 2026-11-04 05:07: run `20261104-050741-ocr`

Plan ocr, done; served as `Unlimited-OCR-2`.

Serving: engine_commit `641e5c0a4`; binary_sha256 `bbcfb7a45d70b6e0184a433dd410822b38b1b13ea41309ffb7abec722cd421a8`; served_model `{"object": "list", "data": [{"id": "Unlimited-OCR-2", "object": "model", "created": 179379`; chip `Apple M5 Ultra; 274877906944`

### checks

| check | result |
|---|---|
| memory-idle | measured: mac: System-wide memory free percentage: 44% |
| ocr | pass: 6/6 cases answered; decode 227-266 tok/s, first token 0.79-3.90 s; 2 at once 109-234 tok/s in all; vs reference: identical 2/6, similarity 0.9973-1.0000, text without boxes identical 6/6, box coords moved 10/288 (at most 10) |
| memory-after | measured: mac: System-wide memory free percentage: 38% |

## 2026-11-04 04:32: run `20261104-043212-ocr-match`

Plan ocr-match, done; served as `Unlimited-OCR-2`.

Serving: engine_commit `6cad5d7be`; binary_sha256 `49dfc1fb2418dfda88143858bb44dce179e34b7d6fcf43ecef2940ed1a05a172`; served_model `{"object": "list", "data": [{"id": "Unlimited-OCR-2", "object": "model", "created": 179378`; chip `Apple M5 Ultra; 274877906944`

### checks

| check | result |
|---|---|
| memory-idle | measured: mac: System-wide memory free percentage: 43% |
| ocr | pass: 7/7 cases answered; decode 94-265 tok/s, first token 0.80-33.98 s; vs reference: identical 1/6, similarity 0.9850-1.0000, text without boxes identical 5/6, box coords moved 113/284 (at most 824) |
| memory-after | measured: mac: System-wide memory free percentage: 38% |

## 2026-11-03 22:37: run `20261103-223731-ocr`

Plan ocr, done; served as `Unlimited-OCR-2`.

Serving: engine_commit `5b7625066`; binary_sha256 `a0397fa2b7948ca0230ca3e0337f2d037eaf3a3a82bf004914420f2b6557fe92`; served_model `{"object": "list", "data": [{"id": "Unlimited-OCR-2", "object": "model", "created": 179376`; chip `Apple M5 Ultra; 274877906944`

### checks

| check | result |
|---|---|
| memory-idle | measured: mac: System-wide memory free percentage: 45% |
| ocr | pass: 6/6 cases answered; decode 231-271 tok/s, first token 0.79-3.90 s; 2 at once 110-238 tok/s in all; vs reference: identical 2/6, similarity 0.9973-1.0000, text without boxes identical 6/6, box coords moved 10/288 (at most 10) |
| memory-after | measured: mac: System-wide memory free percentage: 39% |

## 2026-11-03 17:51: run `20261103-175105-ocr`

Plan ocr, done; served as `Unlimited-OCR-2`.

Serving: engine_commit `dd7f775f2`; binary_sha256 `b7370f69a8c5d292682fb03bef5348a5f69634ead937293caba6898b8435fb90`; served_model `{"object": "list", "data": [{"id": "Unlimited-OCR-2", "object": "model", "created": 179374`; chip `Apple M5 Ultra; 274877906944`

### checks

| check | result |
|---|---|
| memory-idle | measured: mac: System-wide memory free percentage: 43% |
| ocr | pass: 6/6 cases answered; decode 225-264 tok/s, first token 0.80-3.97 s; 2 at once 108-229 tok/s in all; vs reference: identical 2/6, similarity 0.9973-1.0000, text without boxes identical 6/6, box coords moved 10/288 (at most 10) |
| memory-after | measured: mac: System-wide memory free percentage: 37% |

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

