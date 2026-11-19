# ZONOS3 Mini on 1x Apple M5 Ultra (256 GB), macOS

Target `zonos3-mini-m5`: ZONOS3 Mini as released, fp32 arithmetic, TensorFold native Metal (zonos3) on one M5 Ultra (text to speech, four requests at once). Engine: TensorFold native, Metal. Rendered from `stats/zonos3-mini-m5.json` (10 runs); aggregate tok/s, total (a stream).

## 2026-11-19 16:29: run `20261119-162920-speech-edit`

Plan speech-edit, done; served as `zonos3-mini`.

Serving: engine_commit `ef38d3707`; binary_sha256 `5fa056fab0985183e9161d80706e3d7ed39c55f766fca5fe40bb14d47cac5c39`; served_model `{"object": "list", "data": [{"id": "zonos3-mini", "object": "model", "created": 1795127374`; chip `Apple M5 Ultra; 274877906944; 27.2`

### checks

| check | result |
|---|---|
| speech-edit | pass: 6/6 edits made in 1.38-6.62 s each (8 regions); repeats identical 6/6, lengths as planned 6/6; audio before the first region within 7.6-9.8 dB of the clip; aligned 75 words in 2 clips (0.17 s); at once: 5/5 equal to alone; refusals 11/11 |

## 2026-11-19 16:28: run `20261119-162845-speech-laci`

Plan speech-laci, done; served as `zonos3-mini`.

Serving: engine_commit `ef38d3707`; binary_sha256 `5fa056fab0985183e9161d80706e3d7ed39c55f766fca5fe40bb14d47cac5c39`; served_model `{"object": "list", "data": [{"id": "zonos3-mini", "object": "model", "created": 1795127339`; chip `Apple M5 Ultra; 274877906944; 27.2`

### checks

| check | result |
|---|---|
| speech | pass: 9/9 cases spoken; 9.0-18.4 times real time (42.4 s of audio), streamed first byte 0.03-0.38 s; repeats identical 9/9, streamed identical 9/9; same audio 4/4; refusals 10/10 |

## 2026-11-19 16:28: run `20261119-162817-speech-steer`

Plan speech-steer, done; served as `zonos3-mini`.

Serving: engine_commit `ef38d3707`; binary_sha256 `5fa056fab0985183e9161d80706e3d7ed39c55f766fca5fe40bb14d47cac5c39`; served_model `{"object": "list", "data": [{"id": "zonos3-mini", "object": "model", "created": 1795127310`; chip `Apple M5 Ultra; 274877906944; 27.2`

### checks

| check | result |
|---|---|
| speech | pass: 6/6 cases spoken; 16.3-17.9 times real time (31.3 s of audio), streamed first byte 0.03-0.06 s; repeats identical 6/6, streamed identical 6/6; same audio 4/4; refusals 6/6 |

## 2026-11-19 16:27: run `20261119-162729-speech-concurrent`

Plan speech-concurrent, done; served as `zonos3-mini`.

Serving: engine_commit `ef38d3707`; binary_sha256 `5fa056fab0985183e9161d80706e3d7ed39c55f766fca5fe40bb14d47cac5c39`; served_model `{"object": "list", "data": [{"id": "zonos3-mini", "object": "model", "created": 1795127262`; chip `Apple M5 Ultra; 274877906944; 27.2`

### checks

| check | result |
|---|---|
| memory-idle | measured: mac: System-wide memory free percentage: 93%; total = 8192.00M  us; engine: {"schema_version": 1, "context_window": 4096, "context_fitte |
| speech | pass: 6/6 cases spoken; 2.4-18.2 times real time (40.0 s of audio), streamed first byte 0.06-0.96 s; repeats identical 6/6, streamed identical 6/6; 6 at once: statuses [200, 200, 200, 200, 503, 503]; at once: 18/18 equal to alone in 5 mixes, 6.9-29.6 times real time in total |
| memory-after | measured: mac: System-wide memory free percentage: 92%; total = 8192.00M  us; engine: {"schema_version": 1, "context_window": 4096, "context_fitte |

## 2026-11-19 16:26: run `20261119-162652-speech-controls`

Plan speech-controls, done; served as `zonos3-mini`.

Serving: engine_commit `ef38d3707`; binary_sha256 `5fa056fab0985183e9161d80706e3d7ed39c55f766fca5fe40bb14d47cac5c39`; served_model `{"object": "list", "data": [{"id": "zonos3-mini", "object": "model", "created": 1795127225`; chip `Apple M5 Ultra; 274877906944; 27.2`

### checks

| check | result |
|---|---|
| speech | pass: 5/5 cases spoken; 8.2-17.0 times real time (25.9 s of audio), streamed first byte 0.06-0.08 s; repeats identical 5/5, streamed identical 5/5; same audio 4/4; refusals 5/5 |

## 2026-11-19 16:26: run `20261119-162634-speech-normalize`

Plan speech-normalize, done; served as `zonos3-mini`.

Serving: engine_commit `ef38d3707`; binary_sha256 `5fa056fab0985183e9161d80706e3d7ed39c55f766fca5fe40bb14d47cac5c39`; served_model `{"object": "list", "data": [{"id": "zonos3-mini", "object": "model", "created": 1795127207`; chip `Apple M5 Ultra; 274877906944; 27.2`

### checks

| check | result |
|---|---|
| speech | pass: 1/1 cases spoken; 15.8-15.8 times real time (4.1 s of audio), streamed first byte 0.06-0.06 s; repeats identical 1/1, streamed identical 1/1; same audio 6/6; refusals 1/1 |

## 2026-11-19 16:25: run `20261119-162544-speech`

Plan speech, done; served as `zonos3-mini`.

Serving: engine_commit `ef38d3707`; binary_sha256 `5fa056fab0985183e9161d80706e3d7ed39c55f766fca5fe40bb14d47cac5c39`; served_model `{"object": "list", "data": [{"id": "zonos3-mini", "object": "model", "created": 1795127157`; chip `Apple M5 Ultra; 274877906944; 27.2`

### checks

| check | result |
|---|---|
| memory-idle | measured: mac: System-wide memory free percentage: 94%; total = 8192.00M  us; engine: {"schema_version": 1, "context_window": 4096, "context_fitte |
| speech | pass: 4/4 cases spoken; 4.3-18.3 times real time (32.2 s of audio), streamed first byte 0.06-0.97 s; repeats identical 4/4, streamed identical 4/4; 3 at once: statuses [200, 200, 200]; formats mp3, opus, flac served and repeat; refusals 5/5 |
| memory-after | measured: mac: System-wide memory free percentage: 93%; total = 8192.00M  us; engine: {"schema_version": 1, "context_window": 4096, "context_fitte |

## 2026-11-17 15:53: run `20261117-155328-speech`

Plan speech, done; served as `zonos3-mini`.

Serving: engine_commit `52228c3dd`; binary_sha256 `010a6ab1b33b401960009b1e47942b963bb892e199c24fe9179c53e4d079f46d`; served_model `{"object": "list", "data": [{"id": "zonos3-mini", "object": "model", "created": 1794952417`; chip `Apple M5 Ultra; 274877906944; 27.2`

### checks

| check | result |
|---|---|
| memory-idle | measured: mac: System-wide memory free percentage: 94%; total = 11264.00M  u; engine: {"schema_version": 1, "context_window": 4096, "context_fitte |
| speech | pass: 4/4 cases spoken; 3.9-18.9 times real time (32.2 s of audio), streamed first byte 0.06-1.08 s; repeats identical 4/4, streamed identical 4/4; 3 at once: statuses [200, 503, 503]; formats mp3, opus, flac served and repeat; refusals 5/5 |
| memory-after | measured: mac: System-wide memory free percentage: 93%; total = 11264.00M  u; engine: {"schema_version": 1, "context_window": 4096, "context_fitte |

## 2026-11-17 13:45: run `20261117-134557-speech`

Plan speech, done; served as `zonos3-mini`.

Serving: engine_commit `d6f616ec4`; binary_sha256 `0b592be5130e54569995fe8a2c4d23dfb4ce88ebe6bda809371a2dbf1b04ea70`; served_model `{"object": "list", "data": [{"id": "zonos3-mini", "object": "model", "created": 1794944765`; chip `Apple M5 Ultra; 274877906944; 27.2`

### checks

| check | result |
|---|---|
| memory-idle | measured: mac: System-wide memory free percentage: 95%; total = 12288.00M  u; engine: {"schema_version": 1, "context_window": 4096, "context_fitte |
| speech | pass: 4/4 cases spoken; 3.9-19.1 times real time (32.2 s of audio), streamed first byte 0.06-1.07 s; repeats identical 4/4, streamed identical 4/4; 3 at once: statuses [200, 503, 503]; refusals 5/5 |
| memory-after | measured: mac: System-wide memory free percentage: 93%; total = 12288.00M  u; engine: {"schema_version": 1, "context_window": 4096, "context_fitte |

## 2026-11-17 13:19: run `20261117-131940-speech`

Plan speech, done; served as `zonos3-mini`.

Serving: engine_commit `a6820a735`; binary_sha256 `878a2f015f5763c40da17fd25a7ac38af241f7a1fed28602bdb9d9e7cad086c7`; served_model `{"object": "list", "data": [{"id": "zonos3-mini", "object": "model", "created": 1794943189`; chip `Apple M5 Ultra; 274877906944; 27.2`

### checks

| check | result |
|---|---|
| memory-idle | measured: mac: System-wide memory free percentage: 94%; total = 12288.00M  u; engine: {"schema_version": 1, "context_window": 4096, "context_fitte |
| speech | FAIL: 3/4 cases spoken; 14.6-16.3 times real time (27.1 s of audio), streamed first byte 0.06-0.07 s; repeats identical 3/3, streamed identical 3/3; 3 at once: statuses [200, 503, 503]; refusals 5/5; failed clone: status 500 {"error": {"message": "cloning from a clip (ref_audio) is not supported on Metal yet: use a voice or speaker_reference_c |
| memory-after | measured: mac: System-wide memory free percentage: 93%; total = 12288.00M  u; engine: {"schema_version": 1, "context_window": 4096, "context_fitte |

