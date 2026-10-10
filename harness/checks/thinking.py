"""Thinking on: the harness's own word problems with ``enable_thinking: true`` — reasoning arrives in
``reasoning_content``, none leaks into ``content``, and the final answer is right. The recipe's suite can also run
with thinking on through a ``suite`` check whose args turn it on (the qwen suite honours ``--thinking`` for gsm8k only)."""

from __future__ import annotations

import concurrent.futures as cf
import json
import re
from pathlib import Path

from .. import api
from ..config import Target

PROBLEMS = [
    ("A train leaves at 9:40 and arrives at 13:15. How many minutes is the trip?", 215),
    ("A shop sells pens at 3 for $2. How many dollars do 27 pens cost?", 18),
    ("Tom has 5 times as many marbles as Ann. Together they have 84. How many does Tom have?", 70),
    ("A rectangle is 3 times as long as it is wide and its perimeter is 64 cm. What is its area in square cm?", 192),
    ("What is the sum of the first 20 odd numbers?", 400),
    ("A tank fills at 12 litres a minute and leaks 4 litres a minute. How many minutes to fill 200 litres?", 25),
    ("If 7 workers build 7 walls in 7 days, how many days do 14 workers take to build 14 walls?", 7),
    ("A book costs $40 after a 20% discount. What was its price in dollars before the discount?", 50),
    ("How many integers from 1 to 100 are divisible by 3 or 5?", 47),
    ("A clock gains 3 minutes every hour. How many minutes ahead is it after 2 days?", 144),
]


def _answer(text: str) -> int | None:
    m = re.findall(r"answer\s*[:=]\s*\$?(-?\d[\d,]*)", text, re.I) or re.findall(r"(-?\d[\d,]*)", text)
    return int(m[-1].replace(",", "")) if m else None


def run(target: Target, spec: dict, run_dir: Path, name: str) -> dict:
    budget = int(spec.get("max_tokens", 8192))
    extra = spec.get("extra", {})

    def one(item):
        q, want = item
        r = api.chat(target.url, target.model, [{"role": "user", "content": q + " End with 'Answer: <number>'."}],
                     max_tokens=budget, temperature=0, chat_template_kwargs={"enable_thinking": True, **extra}, timeout=1800)
        text = r.get("text", "")
        return {"q": q, "want": want, "status": r["status"], "got": _answer(text), "finish": r.get("finish"),
                "reasoning_chars": len(r.get("reasoning", "")), "leak": "<think>" in text or "</think>" in text,
                "tokens": (r.get("usage") or {}).get("completion_tokens"), "text": text[-300:], "error": r.get("error")}

    with cf.ThreadPoolExecutor(int(spec.get("workers", 1))) as ex:
        res = list(ex.map(one, PROBLEMS[: int(spec.get("n", len(PROBLEMS)))]))
    right = sum(r["got"] == r["want"] for r in res)
    reasoned = sum(r["reasoning_chars"] > 0 for r in res)
    leaks = sum(r["leak"] for r in res)
    errors = sum(r["status"] != 200 for r in res)
    (run_dir / f"{name}.json").write_text(json.dumps(res, indent=1))
    n = len(res)
    return {"ok": errors == 0 and leaks == 0 and reasoned == n and right == n,
            "summary": f"thinking on: {right}/{n} right, {reasoned}/{n} with reasoning_content, {leaks} leaks, {errors} errors",
            "metrics": {"right": right, "n": n, "reasoned": reasoned, "leaks": leaks, "errors": errors}}
