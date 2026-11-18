# ZONOS3 Mini on 1x NVIDIA RTX 5090 (32 GB), Linux

Target `zonos3-mini-5090`: ZONOS3 Mini as released, fp32 arithmetic, TensorFold native CUDA (zonos3) on one RTX 5090 (text to speech, four requests at once). Engine: TensorFold native, CUDA. Rendered from `stats/zonos3-mini-5090.json` (17 runs); aggregate tok/s, total (a stream).

## 2026-11-18 00:36: run `20261118-003621-speech`

Plan speech, done; served as `zonos3-mini`.

Serving: engine_commit `a158fcdaf`; binary_sha256 `163bf5e64d6030f3632222aa4ffddfc6233b43effab933b20adc0b918bcbc56e`; served_model `{"object": "list", "data": [{"id": "zonos3-mini", "object": "model", "created": 1794962194`; gpu `NVIDIA GeForce RTX 5090, 615.71.09, 32607 MiB`

### checks

| check | result |
|---|---|
| memory-idle | measured: gpu: 21539 MiB, 32607 MiB; engine: {"schema_version": 1, "context_window": 4096, "context_fitte |
| speech | pass: 4/4 cases spoken; 7.4-29.1 times real time (32.2 s of audio), streamed first byte 0.03-0.54 s; repeats identical 4/4, streamed identical 4/4; WER 0.000-0.000; 3 at once: statuses [200, 200, 200]; formats mp3, opus, flac served and repeat; refusals 5/5 |
| memory-after | measured: gpu: 27351 MiB, 32607 MiB; engine: {"schema_version": 1, "context_window": 4096, "context_fitte |

## 2026-11-18 00:35: run `20261118-003516-speech-concurrent`

Plan speech-concurrent, done; served as `zonos3-mini`.

Serving: engine_commit `a158fcdaf`; binary_sha256 `163bf5e64d6030f3632222aa4ffddfc6233b43effab933b20adc0b918bcbc56e`; served_model `{"object": "list", "data": [{"id": "zonos3-mini", "object": "model", "created": 1794962129`; gpu `NVIDIA GeForce RTX 5090, 615.71.09, 32607 MiB`

### checks

| check | result |
|---|---|
| memory-idle | measured: gpu: 21539 MiB, 32607 MiB; engine: {"schema_version": 1, "context_window": 4096, "context_fitte |
| speech | pass: 6/6 cases spoken; 4.2-29.2 times real time (40.0 s of audio), streamed first byte 0.03-0.54 s; repeats identical 6/6, streamed identical 6/6; WER 0.000-0.111; 6 at once: statuses [200, 200, 200, 503, 200, 503]; at once: 18/18 equal to alone in 5 mixes, 11.7-41.7 times real time in total |
| memory-after | measured: gpu: 27399 MiB, 32607 MiB; engine: {"schema_version": 1, "context_window": 4096, "context_fitte |

## 2026-11-18 00:34: run `20261118-003437-speech-controls`

Plan speech-controls, done; served as `zonos3-mini`.

Serving: engine_commit `a158fcdaf`; binary_sha256 `163bf5e64d6030f3632222aa4ffddfc6233b43effab933b20adc0b918bcbc56e`; served_model `{"object": "list", "data": [{"id": "zonos3-mini", "object": "model", "created": 1794962090`; gpu `NVIDIA GeForce RTX 5090, 615.71.09, 32607 MiB`

### checks

| check | result |
|---|---|
| speech | pass: 4/4 cases spoken; 23.9-27.5 times real time (20.5 s of audio), streamed first byte 0.04-0.04 s; repeats identical 4/4, streamed identical 4/4; WER 0.000-0.059; same audio 3/3; refusals 4/4 |

## 2026-11-18 00:34: run `20261118-003416-speech-normalize`

Plan speech-normalize, done; served as `zonos3-mini`.

Serving: engine_commit `a158fcdaf`; binary_sha256 `163bf5e64d6030f3632222aa4ffddfc6233b43effab933b20adc0b918bcbc56e`; served_model `{"object": "list", "data": [{"id": "zonos3-mini", "object": "model", "created": 1794962069`; gpu `NVIDIA GeForce RTX 5090, 615.71.09, 32607 MiB`

### checks

| check | result |
|---|---|
| speech | pass: 1/1 cases spoken; 26.2-26.2 times real time (4.1 s of audio), streamed first byte 0.03-0.03 s; repeats identical 1/1, streamed identical 1/1; WER 0.000-0.000; same audio 6/6; refusals 1/1 |

## 2026-11-17 23:34: run `20261117-233434-speech`

Plan speech, done; served as `zonos3-mini`.

Serving: engine_commit `14a3ccb34`; binary_sha256 `f43394dea56639950389d33b621ef4cb8650748c06b400b320e83785d3af4c62`; served_model `{"object": "list", "data": [{"id": "zonos3-mini", "object": "model", "created": 1794958487`; gpu `NVIDIA GeForce RTX 5090, 615.71.09, 32607 MiB`

### checks

| check | result |
|---|---|
| memory-idle | measured: gpu: 12145 MiB, 32607 MiB; engine: {"schema_version": 1, "context_window": 4096, "context_fitte |
| speech | pass: 4/4 cases spoken; 7.4-29.2 times real time (32.2 s of audio), streamed first byte 0.03-0.55 s; repeats identical 4/4, streamed identical 4/4; WER 0.000-0.000; 3 at once: statuses [200, 200, 200]; formats mp3, opus, flac served and repeat; refusals 5/5 |
| memory-after | measured: gpu: 17957 MiB, 32607 MiB; engine: {"schema_version": 1, "context_window": 4096, "context_fitte |

## 2026-11-17 23:33: run `20261117-233331-speech-concurrent`

Plan speech-concurrent, done; served as `zonos3-mini`.

Serving: engine_commit `14a3ccb34`; binary_sha256 `f43394dea56639950389d33b621ef4cb8650748c06b400b320e83785d3af4c62`; served_model `{"object": "list", "data": [{"id": "zonos3-mini", "object": "model", "created": 1794958420`; gpu `NVIDIA GeForce RTX 5090, 615.71.09, 32607 MiB`

### checks

| check | result |
|---|---|
| memory-idle | measured: gpu: 12145 MiB, 32607 MiB; engine: {"schema_version": 1, "context_window": 4096, "context_fitte |
| speech | pass: 6/6 cases spoken; 4.0-29.2 times real time (40.0 s of audio), streamed first byte 0.03-0.56 s; repeats identical 6/6, streamed identical 6/6; WER 0.000-0.111; 6 at once: statuses [200, 200, 200, 200, 503, 503]; at once: 18/18 equal to alone in 5 mixes, 9.9-29.5 times real time in total |
| memory-after | measured: gpu: 17993 MiB, 32607 MiB; engine: {"schema_version": 1, "context_window": 4096, "context_fitte |

## 2026-11-17 23:32: run `20261117-233254-speech-controls`

Plan speech-controls, done; served as `zonos3-mini`.

Serving: engine_commit `14a3ccb34`; binary_sha256 `f43394dea56639950389d33b621ef4cb8650748c06b400b320e83785d3af4c62`; served_model `{"object": "list", "data": [{"id": "zonos3-mini", "object": "model", "created": 1794958387`; gpu `NVIDIA GeForce RTX 5090, 615.71.09, 32607 MiB`

### checks

| check | result |
|---|---|
| speech | pass: 4/4 cases spoken; 17.9-27.5 times real time (20.5 s of audio), streamed first byte 0.04-0.05 s; repeats identical 4/4, streamed identical 4/4; WER 0.000-0.059; same audio 3/3; refusals 4/4 |

## 2026-11-17 23:32: run `20261117-233232-speech-normalize`

Plan speech-normalize, done; served as `zonos3-mini`.

Serving: engine_commit `14a3ccb34`; binary_sha256 `f43394dea56639950389d33b621ef4cb8650748c06b400b320e83785d3af4c62`; served_model `{"object": "list", "data": [{"id": "zonos3-mini", "object": "model", "created": 1794958365`; gpu `NVIDIA GeForce RTX 5090, 615.71.09, 32607 MiB`

### checks

| check | result |
|---|---|
| speech | pass: 1/1 cases spoken; 26.2-26.2 times real time (4.1 s of audio), streamed first byte 0.03-0.03 s; repeats identical 1/1, streamed identical 1/1; WER 0.000-0.000; same audio 6/6; refusals 1/1 |

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

