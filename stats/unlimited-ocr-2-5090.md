# Unlimited-OCR-2, bf16 on 1x NVIDIA RTX 5090 (32 GB), Linux

Target `unlimited-ocr-2-5090`: Unlimited-OCR-2 bf16 as released, TensorFold native CUDA (unlimited-ocr) on one RTX 5090 (131072-token window, one stream). Engine: TensorFold native, CUDA. Rendered from `stats/unlimited-ocr-2-5090.json` (1 runs); aggregate tok/s, total (a stream).

## 2026-11-04 00:18: run `20261104-001831-ocr`

Plan ocr, done; served as `Unlimited-OCR-2`.

Serving: engine_commit `dd7f775f2`; binary_sha256 `2fbcab28edca2e25b7bd78ed8007f12bf47ab949ca9e1619c8557f0efb6534be`; served_model `{"object": "list", "data": [{"id": "Unlimited-OCR-2", "object": "model", "created": 179375`; gpu `NVIDIA GeForce RTX 5090, 615.71.09, 32607 MiB`

### checks

| check | result |
|---|---|
| memory-idle | measured: gpu: 15726 MiB, 32607 MiB |
| ocr | pass: 6/6 cases answered; decode 292-311 tok/s, first token 0.21-1.05 s; 2 at once 224-300 tok/s in all; vs reference: identical 2/6, similarity 0.9971-1.0000, text without boxes identical 5/6, box coords moved 13/284 (at most 2) |
| memory-after | measured: gpu: 15728 MiB, 32607 MiB |

