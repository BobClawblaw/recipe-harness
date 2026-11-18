"""Speech editing on /v1/audio/edit (ZONOS3): clips spoken by the server itself, then edited; each edit's reply, how
long it takes, whether it repeats, whether its length is the clip's with each region's fill in place of the region,
how far the audio before the first region stays from the clip's, the word timings of /v1/audio/edit/align, edits
sent while speech is being spoken, the refusals a recipe promises, and, when the target has an `asr` command, each
edit's word error rate against its target text (measured; `max_wer` makes it pass or fail).

clips = [{ name = "line", input = "...", voice = "rupert", seed = 5 }]
cases = [{ name = "by-span", clip = "line", target_text = "...", spans = [[1.2, 1.8]], seed = 3 },
         { name = "by-transcript", clip = "line", target_text = "...", transcript = true, seed = 3 }]
A case's other keys go into the request as they are; `transcript = true` sends the clip's own text as original_text.
align = ["line"] asks /v1/audio/edit/align for each named clip's words, twice.
together = [["by-span", "line"]] sends each list at once (an edit case or a clip's speech request): every reply must
be what it was alone.
refusals = [{ name = "no-target", status = 400, clip = "line", body = { spans = [[0.5, 1.0]] } }]"""

from __future__ import annotations

import base64
import json
import shlex
import struct
import time
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

from .. import api
from ..config import Target
from .speech import WER, wav

OWN = ("name", "clip", "transcript")
FRAME = 2940  # samples of a codec frame at 44.1 kHz
RATE = 15.0  # frames a second


def edit(base: str, body: dict, route: str = "/v1/audio/edit", timeout: float = 600) -> dict:
    """One edit request: status, the reply (takes' audio decoded to PCM bytes under `pcm`), seconds."""
    t0 = time.time()
    status, d = api.request(f"{base}{route}", body, timeout)
    out = {"status": status, "s": round(time.time() - t0, 3)}
    if status != 200 or not isinstance(d, dict):
        out["error"] = d if isinstance(d, str) else json.dumps(d)[:2000]
        return out
    out["reply"] = d
    out["pcm"] = [pcm_of(base64.b64decode(t.pop("audio_base64"))) for t in d.get("takes", [])]
    return out


def pcm_of(data: bytes) -> bytes:
    """The samples of a 16-bit mono WAV file."""
    if data[:4] != b"RIFF" or data[8:12] != b"WAVE":
        return b""
    at = data.find(b"data")
    return data[at + 8:] if at >= 0 else b""


def snr_db(a: bytes, b: bytes) -> float | None:
    """How close two stretches of 16-bit PCM are: the first's power over the difference's, in dB."""
    n = min(len(a), len(b)) // 2
    if n == 0:
        return None
    x, y = struct.unpack(f"<{n}h", a[: 2 * n]), struct.unpack(f"<{n}h", b[: 2 * n])
    signal = sum(v * v for v in x)
    noise = sum((v - w) * (v - w) for v, w in zip(x, y))
    if signal == 0:
        return None
    import math
    return round(10 * math.log10(signal / max(noise, 1e-9)), 1)


def _body(target: Target, case: dict, clips: dict, texts: dict, rate: int) -> dict:
    body = {"model": target.model, "audio_base64": base64.b64encode(wav(clips[case["clip"]], rate)).decode(),
            **{k: v for k, v in case.items() if k not in OWN}}
    if case.get("transcript"):
        body["original_text"] = texts[case["clip"]]
    return body


def _case(target: Target, case: dict, clips: dict, texts: dict, rate: int, repeats: int, bad: list[str]) -> tuple[dict, bytes]:
    name = case["name"]
    body = _body(target, case, clips, texts, rate)
    first = edit(target.url, body)
    entry = {"status": first["status"], "first_request_s": first["s"]}
    if first["status"] != 200 or not first.get("pcm") or not first["pcm"][0]:
        bad.append(f"{name}: status {first['status']} {first.get('error', '')[:160]}")
        return entry, b""
    reply, pcm = first["reply"], first["pcm"][0]
    take = reply["takes"][0]
    again = [edit(target.url, body) for _ in range(repeats)]
    clip_frames = len(clips[case["clip"]]) // (2 * FRAME)
    region = sum(round((b - a) * RATE) for a, b in reply["spans"])
    filled = sum(round(s * RATE) for s in take["fill_seconds"])
    want = (clip_frames - region + filled) * FRAME
    before = int(reply["spans"][0][0] * rate) * 2
    entry.update(regions=len(reply["spans"]), spans=reply["spans"], windows=len(reply["contexts"] or []), fill_seconds=take["fill_seconds"],
                 stopped=take["stopped"], audio_s=round(len(pcm) / (2 * rate), 2), edit_s=[round(min(r["s"] for r in again), 3), round(max(r["s"] for r in again), 3)],
                 repeat_identical=all(r.get("pcm") == first["pcm"] for r in again), length_as_planned=len(pcm) // 2 == want,
                 words=len(reply["words"] or []), before_first_region_snr_db=snr_db(clips[case["clip"]][:before], pcm[:before]))
    if not entry["repeat_identical"]:
        bad.append(f"{name}: a repeated edit gives other audio")
    if not entry["length_as_planned"]:
        bad.append(f"{name}: {len(pcm) // 2} samples, the plan gives {want}")
    if not all(take["stopped"]):
        bad.append(f"{name}: a fill ran to its limit instead of ending: stopped {take['stopped']}")
    if len(first["pcm"]) != int(case.get("num_takes", 1)):
        bad.append(f"{name}: {len(first['pcm'])} takes, asked for {case.get('num_takes', 1)}")
    return entry, pcm


def _align(target: Target, name: str, clips: dict, texts: dict, rate: int, bad: list[str]) -> dict:
    body = {"model": target.model, "audio_base64": base64.b64encode(wav(clips[name], rate)).decode(), "text": texts[name]}
    a, b = (edit(target.url, body, "/v1/audio/edit/align") for _ in range(2))
    if a["status"] != 200:
        bad.append(f"align {name}: status {a['status']} {a.get('error', '')[:160]}")
        return {"status": a["status"]}
    words = a["reply"]["words"]
    ordered = all(w["start"] <= w["end"] for w in words) and all(x["end"] <= y["start"] + 1e-9 for x, y in zip(words, words[1:]))
    inside = bool(words) and words[0]["start"] >= 0 and words[-1]["end"] <= a["reply"]["duration"] + 1e-6
    out = {"status": 200, "words": len(words), "said": len(texts[name].split()), "ordered": ordered, "inside_the_clip": inside,
           "repeat_identical": a["reply"] == b.get("reply"), "s": [a["s"], b["s"]], "least_confidence": round(min((w["confidence"] for w in words), default=0), 3)}
    if not (ordered and inside and out["repeat_identical"] and out["words"] == out["said"]):
        bad.append(f"align {name}: {out['words']} of {out['said']} words, ordered {ordered}, inside {inside}, repeats {out['repeat_identical']}")
    return out


def _together(target: Target, mix: list[str], cases: dict, clip_specs: dict, clips: dict, texts: dict, edits: dict, rate: int, bad: list[str]) -> dict:
    """An edit beside speech: each reply against what it was alone."""
    def ask(n: str):
        if n in cases:
            return edit(target.url, _body(target, cases[n], clips, texts, rate)).get("pcm", [b""])[0] == edits[n]
        spec = {k: v for k, v in clip_specs[n].items() if k != "name"}
        return api.speech(target.url, {"model": target.model, "response_format": "pcm", **spec}).get("audio") == clips[n]
    t0 = time.time()
    with ThreadPoolExecutor(len(mix)) as ex:
        same = list(ex.map(ask, mix))
    out = {"cases": mix, "identical": sum(same), "wall_s": round(time.time() - t0, 3)}
    if out["identical"] != len(mix):
        bad.append(f"together {mix}: {out['identical']} of {len(mix)} equal to the lone replies")
    return out


def run(target: Target, spec: dict, run_dir: Path, name: str) -> dict:
    from ..session import sh
    rate, repeats = int(spec.get("sample_rate", 44100)), int(spec.get("repeats", 2))
    res, clips, texts, edits, bad = {"clips": {}, "cases": {}, "refusals": {}}, {}, {}, {}, []
    for clip in spec["clips"]:
        got = api.speech(target.url, {"model": target.model, "response_format": "pcm", **{k: v for k, v in clip.items() if k != "name"}})
        res["clips"][clip["name"]] = {"status": got["status"], "audio_s": round(len(got["audio"]) / (2 * rate), 2)}
        if got["status"] != 200 or not got["audio"]:
            bad.append(f"clip {clip['name']}: status {got['status']} {got.get('error', '')[:120]}")
            continue
        clips[clip["name"]], texts[clip["name"]] = got["audio"], clip["input"]
        (run_dir / f"{name}.clip.{clip['name']}.wav").write_bytes(wav(got["audio"], rate))
    for case in spec["cases"]:
        if case["clip"] not in clips:
            bad.append(f"{case['name']}: its clip was not spoken")
            continue
        entry, pcm = _case(target, case, clips, texts, rate, repeats, bad)
        res["cases"][case["name"]] = entry
        if pcm:
            edits[case["name"]] = pcm
            path = run_dir / f"{name}.{case['name']}.wav"
            path.write_bytes(wav(pcm, rate))
            asr = target.section("commands").get("asr")
            if asr:
                rc, out = sh(target, asr, timeout=900, wav=path, said=shlex.quote(case["target_text"]))
                m = WER.search(out)
                entry["wer"] = float(m.group(1)) if m else None
                if m is None:
                    bad.append(f"{case['name']}: asr gave no WER (exit {rc}): {out.strip()[-120:]}")
                elif "max_wer" in spec and entry["wer"] > spec["max_wer"]:
                    bad.append(f"{case['name']}: WER {entry['wer']} above {spec['max_wer']}")
    if spec.get("align"):
        res["align"] = {n: _align(target, n, clips, texts, rate, bad) for n in spec["align"] if n in clips}
    if spec.get("together"):
        by_name = {c["name"]: c for c in spec["cases"]}
        clip_specs = {c["name"]: c for c in spec["clips"]}
        res["together"] = [_together(target, mix, by_name, clip_specs, clips, texts, edits, rate, bad) for mix in spec["together"] if all(n in edits or n in clips for n in mix)]
    for r in spec.get("refusals", []):
        body = {"model": target.model, **r["body"]}
        if r.get("clip") in clips:
            body["audio_base64"] = base64.b64encode(wav(clips[r["clip"]], rate)).decode()
        got = edit(target.url, body, r.get("route", "/v1/audio/edit"))
        res["refusals"][r["name"]] = {"status": got["status"], "message": got.get("error", "")[:200]}
        if got["status"] != r.get("status", 400):
            bad.append(f"refusal {r['name']}: status {got['status']}, expected {r.get('status', 400)}")
    (run_dir / f"{name}.json").write_text(json.dumps(res, indent=1))
    ok = [v for v in res["cases"].values() if "audio_s" in v]
    summary = f"{len(ok)}/{len(spec['cases'])} edits made"
    if ok:
        summary += (f" in {min(v['edit_s'][0] for v in ok):.2f}-{max(v['edit_s'][1] for v in ok):.2f} s each ({sum(v['regions'] for v in ok)} regions)"
                    f"; repeats identical {sum(v['repeat_identical'] for v in ok)}/{len(ok)}, lengths as planned {sum(v['length_as_planned'] for v in ok)}/{len(ok)}")
        wers = [v["wer"] for v in ok if v.get("wer") is not None]
        summary += f"; WER against the target {min(wers):.3f}-{max(wers):.3f}" if wers else ""
        near = [v["before_first_region_snr_db"] for v in ok if v["before_first_region_snr_db"] is not None]
        summary += f"; audio before the first region within {min(near):.1f}-{max(near):.1f} dB of the clip" if near else ""
    if res.get("align"):
        a = [v for v in res["align"].values() if v.get("status") == 200]
        summary += f"; aligned {sum(v['words'] for v in a)} words in {len(a)} clips ({min((min(v['s']) for v in a), default=0):.2f} s)"
    if res.get("together"):
        t = res["together"]
        summary += f"; at once: {sum(v['identical'] for v in t)}/{sum(len(v['cases']) for v in t)} equal to alone"
    if res["refusals"]:
        summary += f"; refusals {sum(v['status'] == r.get('status', 400) for v, r in zip(res['refusals'].values(), spec['refusals']))}/{len(res['refusals'])}"
    summary += f"; failed {'; '.join(bad)}" if bad else ""
    return {"ok": not bad, "summary": summary, "metrics": {**res, "failures": bad}}
