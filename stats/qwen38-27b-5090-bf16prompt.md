# Qwen3.8-27B, MLX 4-bit, bf16 prompts + DFlash2 on 1x NVIDIA RTX 5090 (32 GB)

Target `qwen38-27b-5090-bf16prompt`: Qwen3.8-27B MLX 4-bit (TensorFold/Qwen3.8-27B-MLX-4bit) + DFlash2 served without --prompt-precision int8, TensorFold native CUDA on one RTX 5090 (bf16 prompts, fp8 KV, the int8-prompt A/B of 2026-11-08). Engine: TensorFold native, CUDA. Rendered from `stats/qwen38-27b-5090-bf16prompt.json` (1 runs); aggregate tok/s, total (a stream).

## 2026-11-08 10:52: run `20261108-105200-quant-compare`

Plan quant-compare, done; served as `qwen38-27b`.

Serving: recipe_commit `a52ff23`; engine_commit `267c5af`; served_model `{"object": "list", "data": [{"id": "qwen38-27b", "object": "model", "created": 1794135120,`; suite_commit `49a346d8899c`

### ruler-fresh

| streams | prose total (a stream) | code total (a stream) | structured total (a stream) | list total (a stream) | first token |
|---:|---:|---:|---:|---:|---:|
| 1 | 275.7 (275.7) | 525.3 (525.3) | 353.9 (353.9) | 331.7 (331.7) | 0.10-0.10 s |

### suite-thinking

| check | passed |
|---|---:|
| gsm8k | 241/250 |

### suite

| check | passed |
|---|---:|
| gsm8k | 240/250 |
| mmlu | 271/342 |
| ifeval | 130/150 |
| humaneval | 151/164 |
| mgsm | 213/240 |

### checks

| check | result |
|---|---|
| memory-idle | measured: gpu: 30850 MiB, 32607 MiB |

