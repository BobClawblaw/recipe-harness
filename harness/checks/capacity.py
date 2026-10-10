"""N long prompts at once: how many the server holds together, and whether it serves on (a short request after)."""

from __future__ import annotations

import concurrent.futures as cf
import json
import random
from pathlib import Path

from .. import api
from ..config import Target

WORDS = "river stone cloud lantern harbor meadow copper violet signal garden orbit candle marble forest thunder".split()


def run(target: Target, spec: dict, run_dir: Path, name: str) -> dict:
    n, tokens = int(spec.get("streams", 6)), int(spec.get("tokens", 240000))

    def one(i: int) -> dict:
        rng = random.Random(1000 + i)
        text = f"Document {i}. " + " ".join(rng.choice(WORDS) for _ in range(int(tokens / 1.33))) + "\n\nSummarize in one sentence."
        r = api.chat(target.url, target.model, [{"role": "user", "content": text}], timeout=spec.get("timeout", 3600),
                     max_tokens=32, temperature=0, chat_template_kwargs={"enable_thinking": False})
        return {"i": i, "status": r["status"], "s": r["s"], "prompt_tokens": (r.get("usage") or {}).get("prompt_tokens"),
                "finish": r.get("finish"), "error": (r.get("error") or "")[:300]}

    with cf.ThreadPoolExecutor(n) as ex:
        results = list(ex.map(one, range(n)))
    after = api.chat(target.url, target.model, [{"role": "user", "content": "Say hello."}], max_tokens=16, temperature=0,
                     chat_template_kwargs={"enable_thinking": False}, timeout=300)
    answered = sum(r["status"] == 200 for r in results)
    refused = sum(r["status"] not in (200, -1) for r in results)
    lost = sum(r["status"] == -1 for r in results)
    (run_dir / f"{name}.json").write_text(json.dumps({"results": results, "after": after}, indent=1))
    ok = after["status"] == 200 and lost == 0
    return {"ok": ok, "summary": f"{answered}/{n} answered, {refused} refused, {lost} lost (no reply); a short request after: {after['status']}",
            "metrics": {"answered": answered, "refused": refused, "lost": lost, "after": after["status"], "streams": n, "tokens": tokens}}
