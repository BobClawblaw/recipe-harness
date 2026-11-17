# ZONOS3 Mini on 1x Apple M5 Ultra (256 GB), macOS

Target `zonos3-mini-m5`: ZONOS3 Mini as released, fp32 arithmetic, TensorFold native Metal (zonos3) on one M5 Ultra (text to speech, one request at a time). Engine: TensorFold native, Metal. Rendered from `stats/zonos3-mini-m5.json` (3 runs); aggregate tok/s, total (a stream).

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

