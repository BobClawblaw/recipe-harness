"""Text to speech on /v1/audio/speech (ZONOS3, Drama): each case's reply as raw PCM, how long it takes against the
audio it holds, whether it repeats, whether the streamed reply carries the same bytes and when its first byte comes,
what a busy server does with more requests, the refusals a recipe promises, and, when the target has an `asr`
command (given `$wav` and the quoted text `$said`, printing `WER <number>`), each reply's word error rate (measured;
`max_wer` makes it pass or fail).

cases = [{ name = "passage", input = "...", voice = "rupert", seed = 11 }, { name = "clone", input = "...", seed = 4, ref_from = "passage" }]
A case's other keys go into the request as they are; `ref_from` sends an earlier case's reply as `ref_audio` (a WAV).
refusals = [{ name = "unknown-voice", status = 400, body = { input = "x", voice = "nobody" } }]
formats = ["mp3", "opus", "aac", "flac"] asks the first case again in each format, twice: a reply that starts as that
format's files do and repeats.
same = [{ name = "dollars", a = { input = "It costs $5." }, b = { input = "It costs five dollars.", text_normalization = false },
          other = { input = "It costs $5.", text_normalization = false } }]
asks `a` and `b`, which must give the same audio (a text normalizer's written and spoken forms), and `other`, when
given, which must not."""

from __future__ import annotations

import base64
import json
import re
import shlex
import struct
import time
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

from .. import api
from ..config import Target

OWN = ("name", "ref_from")
# how a file of each response_format starts
MAGIC = {"mp3": (b"\xff\xfb", b"\xff\xf3", b"\xff\xf2", b"ID3"), "opus": (b"OggS",), "aac": (b"\xff\xf1", b"\xff\xf9"), "flac": (b"fLaC",), "wav": (b"RIFF",)}
WER = re.compile(r"WER\s+([0-9.]+)")


def wav(pcm: bytes, rate: int) -> bytes:
    """16-bit mono PCM in a WAV header."""
    return b"RIFF" + struct.pack("<I4s4sIHHIIHH4sI", 36 + len(pcm), b"WAVE", b"fmt ", 16, 1, 1, rate, rate * 2, 2, 16, b"data", len(pcm)) + pcm


def _span(xs: list[float]) -> list[float]:
    return [round(min(xs), 3), round(max(xs), 3)]


def _case(target: Target, case: dict, replies: dict, rate: int, repeats: int, bad: list[str]) -> tuple[dict, bytes]:
    body = {"model": target.model, "response_format": "pcm", **{k: v for k, v in case.items() if k not in OWN}}
    if "ref_from" in case:
        body["ref_audio"] = base64.b64encode(wav(replies[case["ref_from"]], rate)).decode()
    name = case["name"]
    first = api.speech(target.url, body)
    entry = {"status": first["status"], "first_request_s": first["s"]}
    if first["status"] != 200 or not first["audio"]:
        bad.append(f"{name}: status {first['status']} {first.get('error', '')[:120]}")
        return entry, b""
    pcm = first["audio"]
    whole = [api.speech(target.url, body) for _ in range(repeats)]
    streamed = [api.speech(target.url, {**body, "stream": True}) for _ in range(repeats)]
    audio_s = len(pcm) / (2 * rate)
    entry.update(bytes=len(pcm), audio_s=round(audio_s, 2), whole_s=_span([r["s"] for r in whole]),
                 times_real_time=round(audio_s / min(r["s"] for r in whole), 1),
                 stream_first_byte_s=_span([r["first"] for r in streamed if r.get("first") is not None] or [0]),
                 stream_s=_span([r["s"] for r in streamed]),
                 repeat_identical=all(r.get("audio") == pcm for r in whole),
                 stream_identical=all(r.get("audio") == pcm for r in streamed))
    if not entry["repeat_identical"]:
        bad.append(f"{name}: a repeated request gives other audio")
    if not entry["stream_identical"]:
        bad.append(f"{name}: the streamed reply differs from the whole one")
    return entry, pcm


def _formats(target: Target, case: dict, formats: list[str], run_dir: Path, name: str, bad: list[str]) -> dict:
    """The case in each format, twice: the status, the size, whether it starts as the format does and repeats."""
    body = {"model": target.model, **{k: v for k, v in case.items() if k not in OWN}}
    out = {}
    for fmt in formats:
        a, b = (api.speech(target.url, {**body, "response_format": fmt}) for _ in range(2))
        ok = a["status"] == 200 and a["audio"].startswith(MAGIC.get(fmt, (b"",)))
        out[fmt] = {"status": a["status"], "bytes": len(a["audio"]), "s": a["s"], "starts_as": ok, "repeat_identical": a["audio"] == b.get("audio")}
        if a["status"] == 200:
            (run_dir / f"{name}.{case['name']}.{'ogg' if fmt == 'opus' else fmt}").write_bytes(a["audio"])
        if not ok or not out[fmt]["repeat_identical"]:
            bad.append(f"format {fmt}: status {a['status']}, starts as {fmt} {ok}, repeats {out[fmt]['repeat_identical']} {a.get('error', '')[:120]}")
    return out


def _same(target: Target, pair: dict, bad: list[str]) -> dict:
    """Two requests that must give one audio, and a third that must give another."""
    got = {k: api.speech(target.url, {"model": target.model, "response_format": "pcm", **pair[k]}) for k in ("a", "b", "other") if k in pair}
    a, b = got["a"], got["b"]
    out = {"statuses": [r["status"] for r in got.values()], "equal": a["status"] == 200 and bool(a["audio"]) and a["audio"] == b["audio"]}
    if "other" in got:
        out["other_differs"] = got["other"]["status"] == 200 and got["other"]["audio"] != a["audio"]
    if not out["equal"] or not out.get("other_differs", True):
        bad.append(f"same {pair['name']}: statuses {out['statuses']}, a equals b {out['equal']}, other differs {out.get('other_differs')} {a.get('error', '')[:120]}")
    return out


def _busy(target: Target, case: dict, pcm: bytes, extra: int, bad: list[str]) -> dict:
    """`extra` more requests sent while one is being spoken: each answers the same audio or 503."""
    body = {"model": target.model, "response_format": "pcm", **{k: v for k, v in case.items() if k not in OWN}}
    def ask(i: int) -> dict:
        time.sleep(0.2 if i else 0)
        return api.speech(target.url, body)
    with ThreadPoolExecutor(extra + 1) as ex:
        got = list(ex.map(ask, range(extra + 1)))
    out = {"statuses": [r["status"] for r in got], "identical": sum(r.get("audio") == pcm for r in got)}
    if any(r["status"] not in (200, 503) for r in got) or any(r["status"] == 200 and r.get("audio") != pcm for r in got) or out["identical"] == 0:
        bad.append(f"busy: statuses {out['statuses']}, {out['identical']} equal to the lone reply")
    return out


def run(target: Target, spec: dict, run_dir: Path, name: str) -> dict:
    from ..session import sh
    rate, repeats = int(spec.get("sample_rate", 44100)), int(spec.get("repeats", 3))
    res, replies, bad = {"cases": {}, "refusals": {}}, {}, []
    for case in spec["cases"]:
        entry, pcm = _case(target, case, replies, rate, repeats, bad)
        if pcm:
            replies[case["name"]] = pcm
            path = run_dir / f"{name}.{case['name']}.wav"
            path.write_bytes(wav(pcm, rate))
            asr = target.section("commands").get("asr")
            if asr:
                rc, out = sh(target, asr, timeout=900, wav=path, said=shlex.quote(case["input"]))
                m = WER.search(out)
                entry["wer"] = float(m.group(1)) if m else None
                if m is None:
                    bad.append(f"{case['name']}: asr gave no WER (exit {rc}): {out.strip()[-120:]}")
                elif "max_wer" in spec and entry["wer"] > spec["max_wer"]:
                    bad.append(f"{case['name']}: WER {entry['wer']} above {spec['max_wer']}")
        res["cases"][case["name"]] = entry
    first = spec["cases"][0]
    if spec.get("busy") and first["name"] in replies:
        res["busy"] = _busy(target, first, replies[first["name"]], int(spec["busy"]), bad)
    if spec.get("formats") and first["name"] in replies:
        res["formats"] = _formats(target, first, spec["formats"], run_dir, name, bad)
    if spec.get("same"):
        res["same"] = {pair["name"]: _same(target, pair, bad) for pair in spec["same"]}
    for r in spec.get("refusals", []):
        got = api.speech(target.url, {"model": target.model, **r["body"]})
        res["refusals"][r["name"]] = {"status": got["status"], "message": got.get("error", "")[:200]}
        if got["status"] != r.get("status", 400):
            bad.append(f"refusal {r['name']}: status {got['status']}, expected {r.get('status', 400)}")
    (run_dir / f"{name}.json").write_text(json.dumps(res, indent=1))
    ok = [v for v in res["cases"].values() if "audio_s" in v]
    summary = f"{len(ok)}/{len(res['cases'])} cases spoken"
    if ok:
        x = [v["times_real_time"] for v in ok]
        fb = [t for v in ok for t in v["stream_first_byte_s"]]
        summary += (f"; {min(x):.1f}-{max(x):.1f} times real time ({sum(v['audio_s'] for v in ok):.1f} s of audio)"
                    f", streamed first byte {min(fb):.2f}-{max(fb):.2f} s"
                    f"; repeats identical {sum(v['repeat_identical'] for v in ok)}/{len(ok)}, streamed identical {sum(v['stream_identical'] for v in ok)}/{len(ok)}")
        wers = [v["wer"] for v in ok if v.get("wer") is not None]
        summary += f"; WER {min(wers):.3f}-{max(wers):.3f}" if wers else ""
    if "busy" in res:
        summary += f"; {len(res['busy']['statuses'])} at once: statuses {res['busy']['statuses']}"
    if "formats" in res:
        summary += f"; formats {', '.join(f for f, v in res['formats'].items() if v['starts_as'] and v['repeat_identical'])} served and repeat"
    if "same" in res:
        summary += f"; same audio {sum(v['equal'] and v.get('other_differs', True) for v in res['same'].values())}/{len(res['same'])}"
    if res["refusals"]:
        summary += f"; refusals {sum(v['status'] == r.get('status', 400) for v, r in zip(res['refusals'].values(), spec['refusals']))}/{len(res['refusals'])}"
    summary += f"; failed {'; '.join(bad)}" if bad else ""
    return {"ok": not bad, "summary": summary, "metrics": {**res, "failures": bad}}
