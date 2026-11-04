# Unlimited-OCR-2, bf16 on 1x NVIDIA GB10 (DGX Spark class, 128 GB unified)

Target `unlimited-ocr-2-gb10`: Unlimited-OCR-2 bf16 as released, TensorFold native CUDA (unlimited-ocr) on one GB10 (131072-token window, one stream). Engine: TensorFold native, CUDA. Rendered from `stats/unlimited-ocr-2-gb10.json` (5 runs); aggregate tok/s, total (a stream).

## 2026-11-04 22:00: run `20261104-220009-ocr-match`

Plan ocr-match, done; served as `Unlimited-OCR-2`.

Serving: engine_commit `e1e345a25`; binary_sha256 `6fba85d1e2683085d0dcacd0aac9cd55e148706a257495969c4b8d4b2274a07b`; served_model `{"object": "list", "data": [{"id": "Unlimited-OCR-2", "object": "model", "created": 179382`; gpu `NVIDIA GB10, 580.178.04`

### checks

| check | result |
|---|---|
| memory-idle | measured: server: 15375 MiB; system 98.2 GiB available |
| ocr | pass: 7/7 cases answered; decode 110-117 tok/s, first token 0.62-26.64 s; vs reference: identical 2/6, similarity 0.9960-1.0000, text without boxes identical 6/6, box coords moved 10/288 (at most 5) |
| memory-after | measured: server: 15377 MiB; system 98.0 GiB available |

## 2026-11-04 01:33: run `20261104-013355-ocr-long`

Plan ocr-long, done; served as `Unlimited-OCR-2`.

Serving: engine_commit `5be83bba7`; binary_sha256 `2d73ded9d26be6e37ad2243c04db1ad2599c546fba5b17206df264ef1993def7`; served_model `{"object": "list", "data": [{"id": "Unlimited-OCR-2", "object": "model", "created": 179375`; gpu `NVIDIA GB10, 580.178.04`

### checks

| check | result |
|---|---|
| memory-idle | measured: server: 15375 MiB; system 98.7 GiB available |
| ocr | pass: 1/1 cases answered; decode 108-108 tok/s, first token 34.69-34.69 s |
| memory-after | measured: server: 15377 MiB; system 98.6 GiB available |

## 2026-11-04 01:29: run `20261104-012902-ocr`

Plan ocr, done; served as `Unlimited-OCR-2`.

Serving: engine_commit `5be83bba7`; binary_sha256 `2d73ded9d26be6e37ad2243c04db1ad2599c546fba5b17206df264ef1993def7`; served_model `{"object": "list", "data": [{"id": "Unlimited-OCR-2", "object": "model", "created": 179375`; gpu `NVIDIA GB10, 580.178.04`

### checks

| check | result |
|---|---|
| memory-idle | measured: server: 15375 MiB; system 98.0 GiB available |
| ocr | pass: 6/6 cases answered; decode 114-117 tok/s, first token 0.60-2.90 s; 2 at once 79-113 tok/s in all; vs reference: identical 2/6, similarity 0.9960-1.0000, text without boxes identical 6/6, box coords moved 10/288 (at most 5) |
| memory-after | measured: server: 15377 MiB; system 98.5 GiB available |

## 2026-11-04 00:45: run `20261104-004505-ocr-long`

Plan ocr-long, done; served as `Unlimited-OCR-2`.

Serving: engine_commit `115748f2c`; binary_sha256 `419536e1ecb59adfb89ab0df8aa59905d2e2a27361bd22344ffd31ce692ba592`; served_model `{"object": "list", "data": [{"id": "Unlimited-OCR-2", "object": "model", "created": 179375`; gpu `NVIDIA GB10, 580.178.04`

### checks

| check | result |
|---|---|
| memory-idle | measured: server: 15375 MiB; system 98.9 GiB available |
| ocr | pass: 1/1 cases answered; decode 76-76 tok/s, first token 35.34-35.34 s |
| memory-after | measured: server: 15377 MiB; system 98.6 GiB available |

## 2026-11-04 00:40: run `20261104-004010-ocr`

Plan ocr, done; served as `Unlimited-OCR-2`.

Serving: engine_commit `115748f2c`; binary_sha256 `419536e1ecb59adfb89ab0df8aa59905d2e2a27361bd22344ffd31ce692ba592`; served_model `{"object": "list", "data": [{"id": "Unlimited-OCR-2", "object": "model", "created": 179375`; gpu `NVIDIA GB10, 580.178.04`

### checks

| check | result |
|---|---|
| memory-idle | measured: server: 15375 MiB; system 98.8 GiB available |
| ocr | pass: 6/6 cases answered; decode 113-117 tok/s, first token 0.60-2.90 s; 2 at once 80-113 tok/s in all; vs reference: identical 2/6, similarity 0.9960-1.0000, text without boxes identical 6/6, box coords moved 10/288 (at most 5) |
| memory-after | measured: server: 15377 MiB; system 98.6 GiB available |

