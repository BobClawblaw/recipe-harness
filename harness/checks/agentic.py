"""A long agentic session: the model works through a synthetic repository with tools until it can answer, its context
growing with every file it reads, as a coding agent's does.

Short checks miss what goes wrong late in a long tool session. DeepSeek-V4.1-Flash's 2-bit pack passed the suite and
the tool checks, then, 190k-312k tokens into a real coding session, asked for the same file reads 41 replies in a row
(ashhart/TensorFold#847). This check reproduces that shape: a trail of `hops` modules, each a few thousand tokens of
code, where each superseded definition of RETRY_LIMIT names the module it moved to. The model has `list_files`,
`read_file` and `submit_answer` and no search, so reaching the live value means reading the whole trail: the prompt
grows to about 80% of `context`: the target's window unless the plan caps it.

The repository comes from `seed` alone, so every target gets the same task: run the plan on a quantized checkpoint and
on its release (or a less lossy pack) and compare the two runs.
"""

from __future__ import annotations

import hashlib
import json
import random
import time
from pathlib import Path

from .. import api
from ..config import Target

WORDS = ("account cache client config cursor delta event filter handle index ledger merge node packet queue record "
         "route schema session shard signal socket stream table token vector window worker buffer commit offset").split()
DIRS = ("core", "services", "storage", "net", "util", "jobs", "api", "legacy")

SYSTEM = ("You are a coding agent working in a repository you can only see through your tools. Read what you need, keep "
          "track of what you have already read, and do not read a file again unless you must. When you have the answer, "
          "call submit_answer.")
TASK = ("Find the live value of RETRY_LIMIT, the one app/main.py ends up using. Its definition has moved between modules "
        "several times; each superseded definition says which module it moved to. There is no search tool: follow the "
        "trail with read_file, starting from app/main.py. When you have the live value, call submit_answer with it.")
NUDGE = "Continue with the tools. Call submit_answer when you have the live value of RETRY_LIMIT."

TOOLS = [
    {"type": "function", "function": {"name": "list_files", "description": "List every file in the repository.",
                                      "parameters": {"type": "object", "properties": {}}}},
    {"type": "function", "function": {"name": "read_file", "description": "Read a whole file.",
                                      "parameters": {"type": "object", "properties": {"path": {"type": "string"}}, "required": ["path"]}}},
    {"type": "function", "function": {"name": "submit_answer", "description": "Submit the live value of RETRY_LIMIT.",
                                      "parameters": {"type": "object", "properties": {"value": {"type": "integer"}}, "required": ["value"]}}},
]


def _module(rng: random.Random, tokens: int) -> list[str]:
    """Plausible Python, about `tokens` tokens (code like this runs near 3.1 characters a token in a Qwen tokenizer)."""
    lines, chars = [], 0
    while chars < tokens * 3.1:
        a, b, c = rng.sample(WORDS, 3)
        n = rng.randrange(2, 97)
        block = [f"def {a}_{b}_{n}({c}, limit={n}):",
                 f'    """Return the {b} of a {c}, at most {n} at a time."""',
                 f"    out = [{a}(x) for x in {c}.{b}s[:limit]]",
                 f"    return _{b}_total(out) * {rng.randrange(2, 9)}", ""]
        lines += block
        chars += sum(len(l) + 1 for l in block)
    return lines


def workspace(seed: str, hops: int, file_tokens: int) -> tuple[dict[str, str], list[str], int]:
    """(files, the trail from app/main.py, the live value). Every module on the trail but the last holds a superseded
    RETRY_LIMIT naming the next; the last holds the live one. As many modules again sit off the trail."""
    rng = random.Random(seed)
    names = set()
    while len(names) < 2 * hops:
        names.add(f"{rng.choice(DIRS)}/{rng.choice(WORDS)}_{rng.choice(WORDS)}.py")
    names = sorted(names)
    rng.shuffle(names)
    trail = names[:hops]
    values = rng.sample(range(3, 1000), hops + 1)
    files = {"app/main.py": "\n".join([f"# RETRY_LIMIT moved out of this file; see {trail[0]}", "",
                                       "def main():", "    return run(retries=RETRY_LIMIT)", ""])}
    for i, path in enumerate(names):
        lines = _module(rng, file_tokens)
        if i < hops:
            line = (f"RETRY_LIMIT = {values[i]}  # superseded: the live value moved to {trail[i + 1]}" if i + 1 < hops
                    else f"RETRY_LIMIT = {values[hops]}  # live value, used by app/main.py")
            at = rng.randrange(len(lines) // 5, len(lines))
            lines = lines[:at] + [line, ""] + lines[at:]
        files[path] = "\n".join(lines)
    return files, ["app/main.py", *trail], values[hops]


def _fingerprint(r: dict) -> str:
    calls = [(c.get("function", {}).get("name"), c.get("function", {}).get("arguments")) for c in r.get("tool_calls") or []]
    return hashlib.sha256(json.dumps([r.get("text"), calls]).encode()).hexdigest()[:12]


def run(target: Target, spec: dict, run_dir: Path, name: str) -> dict:
    """Pass: submit_answer gets the live value, without a loop (`loop` identical replies in a row, 3) and without any
    file read more than `max_reads` times (3). Fails on an error, a wrong answer, `max_nudges` (3) replies that call no
    tool, or `max_turns` replies without an answer. `tool_choice` is "auto" (as an agent sends it); "required" makes a
    grammar force every reply to be a call, which tests the long session on a model that rarely calls a tool unforced."""
    # the target's whole window by default (#847's loops began past 190k); a plan's `context` caps it
    served = int(target.vars.get("context", 0) or 0)
    context = min(c for c in (served, int(spec.get("context", 0) or 0)) if c) if served or spec.get("context") else 131072
    file_tokens = int(spec.get("file_tokens", 6000))
    max_tokens = int(spec.get("max_tokens", 8192 if spec.get("thinking") else 1024))
    # the trail fills about 80% of the window, leaving room for replies and a turn's max_tokens
    hops = int(spec.get("hops", max(2, (int(context * 0.8) - max_tokens) // file_tokens)))
    seed = str(spec.get("seed", "agentic-1"))
    files, trail, want = workspace(f"{seed}-{hops}-{file_tokens}", hops, file_tokens)
    max_turns = int(spec.get("max_turns", 3 * len(trail) + 10))
    loop, max_reads, max_nudges = int(spec.get("loop", 3)), int(spec.get("max_reads", 3)), int(spec.get("max_nudges", 3))
    kw = {"max_tokens": max_tokens, "temperature": float(spec.get("temperature", 0)), "tools": TOOLS,
          "tool_choice": spec.get("tool_choice", "auto"), "chat_template_kwargs": {"enable_thinking": bool(spec.get("thinking"))}, **spec.get("extra", {})}
    if "seed_sampling" in spec:
        kw["seed"] = spec["seed_sampling"]

    msgs = [{"role": "system", "content": SYSTEM}, {"role": "user", "content": TASK}]
    turns, reads, prints = [], {}, []
    answer, why, nudges, streak, longest = None, None, 0, 0, 0
    t0 = time.time()
    while answer is None and why is None:
        if len(turns) >= max_turns:
            why = f"no answer after {max_turns} replies"
            break
        r = api.chat(target.url, target.model, msgs, timeout=float(spec.get("timeout", 3600)), **kw)
        u = r.get("usage") or {}
        fp = _fingerprint(r) if r["status"] == 200 else None
        streak = streak + 1 if fp and prints and prints[-1] == fp else 1
        longest = max(longest, streak)
        prints.append(fp)
        calls = r.get("tool_calls") or []
        turns.append({"status": r["status"], "finish": r.get("finish"), "prompt_tokens": u.get("prompt_tokens"),
                      "cached_tokens": (u.get("prompt_tokens_details") or {}).get("cached_tokens"),
                      "completion_tokens": u.get("completion_tokens"), "seconds": r.get("s"), "fingerprint": fp,
                      "text": (r.get("text") or "")[:2000], "reasoning_chars": len(r.get("reasoning") or ""),
                      "calls": [c.get("function") for c in calls], "error": (r.get("error") or "")[:500] or None})
        if r["status"] != 200:
            why = f"turn {len(turns)}: {r['status']} {str(r.get('error'))[:200]}"
            break
        if streak >= loop:
            why = f"{streak} identical replies in a row from turn {len(turns) - streak + 1}"
            break
        if not calls:
            nudges += 1
            if nudges > max_nudges:
                why = f"{nudges} replies called no tool"
                break
            msgs += [{"role": "assistant", "content": r.get("text") or ""}, {"role": "user", "content": NUDGE}]
            continue
        msgs.append({"role": "assistant", "content": r.get("text") or "", "tool_calls": calls})
        for i, c in enumerate(calls):
            f = c.get("function") or {}
            try:
                args = json.loads(f.get("arguments") or "{}")
            except ValueError:
                args = None
            if not isinstance(args, dict):
                out = "error: the arguments are not a JSON object"
            elif f.get("name") == "list_files":
                out = "\n".join(sorted(files))
            elif f.get("name") == "read_file":
                path = str(args.get("path", "")).lstrip("./")
                out = files.get(path, f"error: no file {path!r}")
                if path in files:
                    reads[path] = reads.get(path, 0) + 1
            elif f.get("name") == "submit_answer":
                answer = args.get("value")
                out = "submitted"
            else:
                out = f"error: no tool {f.get('name')!r}"
            msgs.append({"role": "tool", "tool_call_id": c.get("id") or f"call{len(turns)}_{i}", "content": out})
        over = {p: n for p, n in reads.items() if n > max_reads}
        if over and answer is None:
            why = f"read {', '.join(f'{p} {n} times' for p, n in over.items())}"

    try:
        got = int(answer) if answer is not None else None
    except (TypeError, ValueError):
        got = None
    if why is None and got != want:
        why = f"answered {answer!r}, the live value is {want}"
    peak = max((t["prompt_tokens"] or 0 for t in turns), default=0)
    on_trail = sum(p in reads for p in trail[1:])
    repeats = sum(n - 1 for n in reads.values())
    seconds = round(time.time() - t0, 1)
    (run_dir / f"{name}.json").write_text(json.dumps({
        "spec": {"context": context, "hops": hops, "file_tokens": file_tokens, "max_tokens": max_tokens, "seed": seed,
                 "thinking": bool(spec.get("thinking")), "temperature": kw["temperature"], "tool_choice": kw["tool_choice"]},
        "trail": trail, "want": want, "answer": answer, "why": why, "reads": reads, "turns": turns}, indent=1))
    summary = (f"{'right' if why is None else 'FAILED: ' + why}; {len(turns)} replies, {on_trail}/{hops} trail modules read, "
               f"{repeats} repeat reads, longest identical run {longest}, peak prompt {peak} tokens, {seconds} s")
    return {"ok": why is None, "summary": summary,
            "metrics": {"right": got == want, "why": why, "replies": len(turns), "hops": hops, "trail_read": on_trail,
                        "repeat_reads": repeats, "longest_identical": longest, "nudges": nudges, "peak_prompt_tokens": peak,
                        "completion_tokens": sum(t["completion_tokens"] or 0 for t in turns), "seconds": seconds}}
