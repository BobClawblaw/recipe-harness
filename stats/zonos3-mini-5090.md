# ZONOS3 Mini on 1x NVIDIA RTX 5090 (32 GB), Linux

Target `zonos3-mini-5090`: ZONOS3 Mini as released, fp32 arithmetic, TensorFold native CUDA (zonos3) on one RTX 5090 (text to speech, one request at a time). Engine: TensorFold native, CUDA. Rendered from `stats/zonos3-mini-5090.json` (9 runs); aggregate tok/s, total (a stream).

## 2026-11-17 22:54: run `20261117-225401-speech`

Plan speech, done; served as `zonos3-mini`.

Serving: engine_commit `9b118f77a`; binary_sha256 `6058b1ba2703b912fbb2123e32bc56cc9873fed43316d24a77935043642659a7`; served_model `{"object": "list", "data": [{"id": "zonos3-mini", "object": "model", "created": 1794956054`; gpu `NVIDIA GeForce RTX 5090, 615.71.09, 32607 MiB`

### checks

| check | result |
|---|---|
| memory-idle | measured: gpu: 8551 MiB, 32607 MiB; engine: {"schema_version": 1, "context_window": 4096, "context_fitte |
| speech | pass: 4/4 cases spoken; 7.4-29.2 times real time (32.2 s of audio), streamed first byte 0.03-0.55 s; repeats identical 4/4, streamed identical 4/4; WER 0.000-0.000; 3 at once: statuses [200, 503, 503]; formats mp3, opus, flac served and repeat; refusals 5/5 |
| memory-after | measured: gpu: 14361 MiB, 32607 MiB; engine: {"schema_version": 1, "context_window": 4096, "context_fitte |

## 2026-11-17 22:53: run `20261117-225319-speech-controls`

Plan speech-controls, done; served as `zonos3-mini`.

Serving: engine_commit `9b118f77a`; binary_sha256 `6058b1ba2703b912fbb2123e32bc56cc9873fed43316d24a77935043642659a7`; served_model `{"object": "list", "data": [{"id": "zonos3-mini", "object": "model", "created": 1794956012`; gpu `NVIDIA GeForce RTX 5090, 615.71.09, 32607 MiB`

### checks

| check | result |
|---|---|
| speech | pass: 4/4 cases spoken; 18.0-27.6 times real time (20.5 s of audio), streamed first byte 0.03-0.05 s; repeats identical 4/4, streamed identical 4/4; WER 0.000-0.059; same audio 3/3; refusals 4/4 |

## 2026-11-17 22:52: run `20261117-225257-speech-normalize`

Plan speech-normalize, done; served as `zonos3-mini`.

Serving: engine_commit `9b118f77a`; binary_sha256 `6058b1ba2703b912fbb2123e32bc56cc9873fed43316d24a77935043642659a7`; served_model `{"object": "list", "data": [{"id": "zonos3-mini", "object": "model", "created": 1794955990`; gpu `NVIDIA GeForce RTX 5090, 615.71.09, 32607 MiB`

### checks

| check | result |
|---|---|
| speech | pass: 1/1 cases spoken; 26.2-26.2 times real time (4.1 s of audio), streamed first byte 0.03-0.03 s; repeats identical 1/1, streamed identical 1/1; WER 0.000-0.000; same audio 6/6; refusals 1/1 |

## 2026-11-17 22:11: run `20261117-221158-speech`

Plan speech, done; served as `zonos3-mini`.

Serving: engine_commit `2a4379862`; binary_sha256 `3be1df9fae14edb862512cd75ca4ce3e4c8a720c6e54cc836d0c760c7acece5a`; served_model `{"object": "list", "data": [{"id": "zonos3-mini", "object": "model", "created": 1794953527`; gpu `NVIDIA GeForce RTX 5090, 615.71.09, 32607 MiB`

### checks

| check | result |
|---|---|
| memory-idle | measured: gpu: 8551 MiB, 32607 MiB; engine: {"schema_version": 1, "context_window": 4096, "context_fitte |
| speech | pass: 4/4 cases spoken; 7.4-29.3 times real time (32.2 s of audio), streamed first byte 0.03-0.54 s; repeats identical 4/4, streamed identical 4/4; WER 0.000-0.000; 3 at once: statuses [200, 503, 503]; formats mp3, opus, flac served and repeat; refusals 5/5 |
| memory-after | measured: gpu: 14361 MiB, 32607 MiB; engine: {"schema_version": 1, "context_window": 4096, "context_fitte |

## 2026-11-17 22:11: run `20261117-221109-speech-normalize`

Plan speech-normalize, done; served as `zonos3-mini`.

Serving: engine_commit `2a4379862`; binary_sha256 `3be1df9fae14edb862512cd75ca4ce3e4c8a720c6e54cc836d0c760c7acece5a`; served_model `{"object": "list", "data": [{"id": "zonos3-mini", "object": "model", "created": 1794953477`; gpu `NVIDIA GeForce RTX 5090, 615.71.09, 32607 MiB`

### checks

| check | result |
|---|---|
| speech | pass: 1/1 cases spoken; 26.3-26.3 times real time (4.1 s of audio), streamed first byte 0.03-0.03 s; repeats identical 1/1, streamed identical 1/1; WER 0.000-0.000; same audio 6/6; refusals 1/1 |

## 2026-11-17 22:10: run `20261117-221012-speech`

Plan speech, done; served as `zonos3-mini`.

Serving: engine_commit `2a4379862`; binary_sha256 `3be1df9fae14edb862512cd75ca4ce3e4c8a720c6e54cc836d0c760c7acece5a`; served_model `{"object": "list", "data": [{"id": "zonos3-mini", "object": "model", "created": 1794953425`; gpu `NVIDIA GeForce RTX 5090, 615.71.09, 32607 MiB`

### checks

| check | result |
|---|---|
| memory-idle | measured: gpu: 8551 MiB, 32607 MiB; engine: {"schema_version": 1, "context_window": 4096, "context_fitte |
| speech | pass: 4/4 cases spoken; 7.4-29.3 times real time (32.2 s of audio), streamed first byte 0.03-0.54 s; repeats identical 4/4, streamed identical 4/4; WER 0.000-0.000; 3 at once: statuses [200, 503, 503]; formats mp3, opus, flac served and repeat; refusals 5/5 |
| memory-after | measured: gpu: 14361 MiB, 32607 MiB; engine: {"schema_version": 1, "context_window": 4096, "context_fitte |

## 2026-11-17 19:41: run `20261117-194134-speech`

Plan speech, done; served as `zonos3-mini`.

Serving: engine_commit `9757d2378`; binary_sha256 `54072eb9adb494c513bc15e050233fe26d4fe0862c993fe30e8c3920ab76e643`; served_model `{"object": "list", "data": [{"id": "zonos3-mini", "object": "model", "created": 1794944507`; gpu `NVIDIA GeForce RTX 5090, 615.71.09, 32607 MiB`

### checks

| check | result |
|---|---|
| memory-idle | measured: gpu: 4282 MiB, 32607 MiB; engine: {"schema_version": 1, "context_window": 4096, "context_fitte |
| speech | pass: 4/4 cases spoken; 7.1-29.2 times real time (32.2 s of audio), streamed first byte 0.03-0.58 s; repeats identical 4/4, streamed identical 4/4; WER 0.000-0.000; 3 at once: statuses [200, 503, 503]; formats mp3, opus, flac served and repeat; refusals 5/5 |
| memory-after | measured: gpu: 10092 MiB, 32607 MiB; engine: {"schema_version": 1, "context_window": 4096, "context_fitte |

## 2026-11-17 18:13: run `20261117-181322-speech`

Plan speech, done; served as `zonos3-mini`.

Serving: engine_commit `83f821993`; binary_sha256 `049431a2be1a5b2f9ec71b8b867dfe4f31c2140569fc1d2a943c775bc7d45d32`; served_model `{"object": "list", "data": [{"id": "zonos3-mini", "object": "model", "created": 1794939216`; gpu `NVIDIA GeForce RTX 5090, 615.71.09, 32607 MiB`

### checks

| check | result |
|---|---|
| memory-idle | measured: gpu: 4282 MiB, 32607 MiB; engine: {"schema_version": 1, "context_window": 4096, "context_fitte |
| speech | pass: 4/4 cases spoken; 7.4-29.4 times real time (32.2 s of audio), streamed first byte 0.03-0.55 s; repeats identical 4/4, streamed identical 4/4; WER 0.000-0.000; 3 at once: statuses [200, 503, 503]; refusals 5/5 |
| memory-after | measured: gpu: 10092 MiB, 32607 MiB; engine: {"schema_version": 1, "context_window": 4096, "context_fitte |

## 2026-11-17 18:03: run `20261117-180328-speech`

Plan speech, done; served as `zonos3-mini`.

Serving: engine_commit `fb51fed5d`; binary_sha256 `c67a686b1ae72b876ce8097b6d2eae4630ca164e5fe48701be2451894364260c`; served_model `{"object": "list", "data": [{"id": "zonos3-mini", "object": "model", "created": 1794938621`; gpu `NVIDIA GeForce RTX 5090, 615.71.09, 32607 MiB`

### checks

| check | result |
|---|---|
| memory-idle | measured: gpu: 4282 MiB, 32607 MiB; engine: {"schema_version": 1, "context_window": 4096, "context_fitte |
| speech | pass: 4/4 cases spoken; 7.4-29.3 times real time (32.2 s of audio), streamed first byte 0.03-0.54 s; repeats identical 4/4, streamed identical 4/4; WER 0.000-0.000; 3 at once: statuses [200, 503, 503]; refusals 5/5 |
| memory-after | measured: gpu: 10092 MiB, 32607 MiB; engine: {"schema_version": 1, "context_window": 4096, "context_fitte |

