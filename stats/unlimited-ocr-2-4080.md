# Unlimited-OCR-2, bf16 on 1x NVIDIA RTX 4080 SUPER (16 GB), Windows 11

Target `unlimited-ocr-2-4080`: Unlimited-OCR-2 bf16 as released, TensorFold native CUDA (unlimited-ocr) on one RTX 4080 SUPER (98304-token window, one stream). Engine: TensorFold native, CUDA. Rendered from `stats/unlimited-ocr-2-4080.json` (2 runs); aggregate tok/s, total (a stream).

## 2026-11-03 18:00: run `20261103-180047-ocr`

Plan ocr, done; served as `Unlimited-OCR-2`.

Serving: engine_commit `5be83bba7`; binary_sha256 `ca344b3798d371d3540258b1a9505ac13dbfa4dd14c771cd0c1c4829360c4d02`; served_model `{"object": "list", "data": [{"id": "Unlimited-OCR-2", "object": "model", "created": 179375`; gpu `NVIDIA GeForce RTX 4080 SUPER, 610.88, 16376 MiB`

### checks

| check | result |
|---|---|
| memory-idle | measured: gpu: 15016 MiB, 16376 MiB |
| ocr | pass: 6/6 cases answered; decode 241-244 tok/s, first token 0.36-1.73 s; 2 at once 157-233 tok/s in all; vs reference: identical 3/6, similarity 0.9965-1.0000, text without boxes identical 5/6, box coords moved 13/284 (at most 5) |
| memory-after | measured: gpu: 15022 MiB, 16376 MiB |

## 2026-11-03 17:29: run `20261103-172907-ocr`

Plan ocr, done; served as `Unlimited-OCR-2`.

Serving: engine_commit `115748f2c`; binary_sha256 `8790ce5c39862d7f9ce979f102f0e1b654b0b0cb81b96925d4399573959fb23f`; served_model `{"object": "list", "data": [{"id": "Unlimited-OCR-2", "object": "model", "created": 179374`; gpu `NVIDIA GeForce RTX 4080 SUPER, 610.88, 16376 MiB`

### checks

| check | result |
|---|---|
| memory-idle | measured: gpu: 15016 MiB, 16376 MiB |
| ocr | pass: 6/6 cases answered; decode 219-240 tok/s, first token 0.36-1.73 s; 2 at once 156-227 tok/s in all; vs reference: identical 3/6, similarity 0.9965-1.0000, text without boxes identical 5/6, box coords moved 13/284 (at most 5) |
| memory-after | measured: gpu: 15022 MiB, 16376 MiB |

