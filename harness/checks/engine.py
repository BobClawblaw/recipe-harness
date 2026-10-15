"""The engine's own account of a ruler level, from its server log: rounds, drafts proposed and accepted, tokens.

A TensorFold native server logs one line a finished request, e.g.
``done chatcmpl-… prompt=35 cached=34 … tokens=256 … rounds=55 accepted=200/259``. Summed over one concurrency level
they say how much work each round did (tokens a stream-round, drafts accepted) apart from how long rounds took (the
ruler's per-stream rate over tokens a round). A slower level with the same tokens a round is slower rounds (admission,
the forward, host work); fewer tokens a round is the drafting. ``commands.server_log`` prints the log since $since (Unix
seconds); a target without it gets no engine stats.
"""

from __future__ import annotations

import re

DONE = re.compile(r"\bdone \S+ .*?\bprompt=(\d+)\b.*?\bcached=(\d+)\b.*?\btokens=(\d+)\b.*?\brounds=(\d+) accepted=(\d+)/(\d+)")


def parse(text: str) -> list[dict]:
    """The finished requests' counters in the log text."""
    out = []
    for line in text.splitlines():
        m = DONE.search(line)
        if m:
            prompt, cached, tokens, rounds, accepted, proposed = map(int, m.groups())
            out.append({"prompt": prompt, "cached": cached, "tokens": tokens, "rounds": rounds, "accepted": accepted, "proposed": proposed})
    return out


def level(done: list[dict], per_stream: float | None) -> dict:
    """One concurrency level's totals; ``per_stream`` (the ruler's mean per-stream tok/s) gives ms a round."""
    if not done:
        return {"requests": 0}
    t = {k: sum(d[k] for d in done) for k in ("prompt", "cached", "tokens", "rounds", "accepted", "proposed")}
    tpr = t["tokens"] / t["rounds"] if t["rounds"] else 0.0
    out = {"requests": len(done), **t,
           "tokens_a_round": round(tpr, 3),
           "drafts_a_round": round(t["proposed"] / t["rounds"], 3) if t["rounds"] else 0.0,
           "accept_rate": round(t["accepted"] / t["proposed"], 4) if t["proposed"] else None}
    if per_stream and tpr:
        out["ms_a_round"] = round(1000.0 * tpr / per_stream, 2)
    return out


def summary(levels: dict[int, dict]) -> str:
    parts = []
    for n, s in sorted(levels.items()):
        if not s.get("requests"):
            parts.append(f"c={n} no done lines")
            continue
        rate = f" {s['accept_rate'] * 100:.0f}% accepted" if s.get("accept_rate") is not None else ""
        ms = f", {s['ms_a_round']:.1f} ms a round" if s.get("ms_a_round") else ""
        parts.append(f"c={n} {s['tokens_a_round']:.2f} tokens a round{rate}{ms}")
    return "; ".join(parts)
