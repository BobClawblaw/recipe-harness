"""OCR serving (a page-image model such as Unlimited-OCR-2): pages in as images, each reply's speed, its page markers,
whether it repeats, whether several streams at once give the same replies, and how close each comes to a reference
transcription (the publisher's own code, made by the recipe; similarity is measured, not passed or failed).

The target's `ocr_dir` holds pages/<page>.png and refs/<case>.txt; a plan's cases name pages in order:
cases = [{ name = "report-1", pages = ["report-1"] }, { name = "document", pages = ["report-1", "report-2"] }]"""

from __future__ import annotations

import base64
import difflib
import json
import re
import time
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

from .. import api
from ..config import Target

PAGE = "<PAGE>"
# a layout block's box, [x0, y0, x1, y1] on the page's 0-999 grid
BOX = re.compile(r"\[(\d+), (\d+), (\d+), (\d+)\]")


def _content(d: Path, pages: list[str], instruction: str) -> list[dict]:
    out = [{"type": "image_url", "image_url": {"url": "data:image/png;base64," + base64.b64encode((d / "pages" / f"{p}.png").read_bytes()).decode()}}
           for p in pages]
    if instruction:
        out.append({"type": "text", "text": instruction})
    return out


def _ask(target: Target, content: list[dict], max_tokens: int | None) -> dict:
    extra = {"temperature": 0, **({"max_tokens": max_tokens} if max_tokens else {})}
    r = api.stream(target.url, target.model, [{"role": "user", "content": content}], timeout=3600, **extra)
    if r["status"] == 200:
        done = (r.get("usage") or {}).get("completion_tokens") or 0
        span = r["s"] - (r["ttft"] or 0)
        r["decode_tps"] = round((done - 1) / span, 1) if done > 1 and span > 0 else None
    return r


def _similarity(a: str, b: str) -> float:
    return round(difflib.SequenceMatcher(None, a, b, autojunk=False).ratio(), 4)


def _boxes(want: str, got: str) -> dict:
    """The reply against the reference with every box taken out (the text alone), and how far the boxes moved."""
    bw, bg = BOX.findall(want), BOX.findall(got)
    moved = [abs(int(a) - int(b)) for x, y in zip(bw, bg) for a, b in zip(x, y)]
    return {"text_identical": BOX.sub("[]", want) == BOX.sub("[]", got), "boxes": [len(bw), len(bg)],
            "coords_moved": sum(1 for m in moved if m), "coords": len(moved), "coord_max_move": max(moved, default=0)}


def run(target: Target, spec: dict, run_dir: Path, name: str) -> dict:
    d = Path(target.expand(spec.get("dir", "$ocr_dir")))
    instruction = spec.get("instruction", "")
    max_tokens = spec.get("max_tokens")
    streams = int(spec.get("streams", 2))
    res, bad = {}, []
    for case in spec["cases"]:
        content = _content(d, case["pages"], instruction)
        r = _ask(target, content, max_tokens)
        entry = {"pages": case["pages"], **{k: r.get(k) for k in ("status", "finish", "ttft", "s", "decode_tps", "usage", "error")}, "text": r.get("text")}
        if r["status"] != 200 or r.get("finish") != "stop":
            bad.append(f"{case['name']}: status {r['status']}, finish {r.get('finish')}")
        else:
            marks = r["text"].count(PAGE)
            entry["page_marks"] = marks
            if marks != len(case["pages"]):
                bad.append(f"{case['name']}: {marks} page markers for {len(case['pages'])} pages")
            ref = d / "refs" / f"{case['name']}.txt"
            if ref.exists():
                want = ref.read_text()
                entry["reference_identical"] = r["text"] == want
                entry["reference_similarity"] = _similarity(want, r["text"])
                entry["reference_boxes"] = _boxes(want, r["text"])
            # the same request again: greedy replies repeat
            again = _ask(target, content, max_tokens)
            entry["repeat_identical"] = again.get("text") == r["text"]
            if not entry["repeat_identical"]:
                bad.append(f"{case['name']}: a second run differs")
            # several at once: each stream's reply equals the lone one
            if streams > 1:
                t0 = time.time()
                with ThreadPoolExecutor(streams) as ex:
                    many = list(ex.map(lambda _: _ask(target, content, max_tokens), range(streams)))
                wall = time.time() - t0
                same = sum(m.get("text") == r["text"] for m in many)
                tokens = sum((m.get("usage") or {}).get("completion_tokens") or 0 for m in many)
                entry["streams"] = {"n": streams, "identical": same, "seconds": round(wall, 2), "tokens_per_s": round(tokens / wall, 1)}
                if same != streams:
                    bad.append(f"{case['name']}: {streams - same} of {streams} concurrent replies differ")
        res[case["name"]] = entry
    (run_dir / f"{name}.json").write_text(json.dumps(res, indent=1))
    ok_cases = [v for v in res.values() if v.get("page_marks") is not None]
    tps = [v["decode_tps"] for v in ok_cases if v.get("decode_tps")]
    ttft = [v["ttft"] for v in ok_cases if v.get("ttft")]
    sims = [v["reference_similarity"] for v in ok_cases if "reference_similarity" in v]
    same = sum(bool(v.get("reference_identical")) for v in ok_cases)
    boxed = [v["reference_boxes"] for v in ok_cases if "reference_boxes" in v]
    text_same = sum(b["text_identical"] for b in boxed)
    moved, coords, worst = sum(b["coords_moved"] for b in boxed), sum(b["coords"] for b in boxed), max((b["coord_max_move"] for b in boxed), default=0)
    agg = [v["streams"]["tokens_per_s"] for v in ok_cases if v.get("streams")]
    summary = (f"{len(ok_cases)}/{len(res)} cases answered"
               + (f"; decode {min(tps):.0f}-{max(tps):.0f} tok/s" if tps else "")
               + (f", first token {min(ttft):.2f}-{max(ttft):.2f} s" if ttft else "")
               + (f"; {streams} at once {min(agg):.0f}-{max(agg):.0f} tok/s in all" if agg else "")
               + (f"; vs reference: identical {same}/{len(sims)}, similarity {min(sims):.4f}-{max(sims):.4f}" if sims else "")
               + (f", text without boxes identical {text_same}/{len(boxed)}, box coords moved {moved}/{coords} (at most {worst})" if boxed else "")
               + (f"; failed {'; '.join(bad)}" if bad else ""))
    metrics = {"cases": {k: {kk: v.get(kk) for kk in ("ttft", "s", "decode_tps", "usage", "page_marks", "reference_identical",
                                                       "reference_similarity", "reference_boxes", "repeat_identical", "streams")} for k, v in res.items()},
               "failures": bad}
    return {"ok": not bad, "summary": summary, "metrics": metrics}
