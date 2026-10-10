"""Serving checks beyond a recipe's suite: structured output, sampling determinism, multi-turn resume, media URLs."""

from __future__ import annotations

import json
import re
from pathlib import Path

from .. import api
from ..config import Target

PERSON = {"type": "object", "properties": {"name": {"type": "string"}, "age": {"type": "integer"},
                                           "hobbies": {"type": "array", "items": {"type": "string"}, "maxItems": 3}},
          "required": ["name", "age", "hobbies"], "additionalProperties": False}

PHONE = r"\(\d{3}\) \d{3}-\d{4}"

STRUCTURED = [
    ("json_object", "Describe a cat as JSON with a few fields.", {"response_format": {"type": "json_object"}},
     lambda t: isinstance(json.loads(t), dict)),
    ("json_schema", "Invent a person.", {"response_format": {"type": "json_schema", "json_schema": {"name": "p", "schema": PERSON}}},
     lambda t: (lambda d: set(d) == {"name", "age", "hobbies"} and isinstance(d["age"], int))(json.loads(t))),
    ("guided_json", "Invent a person who likes the sea.", {"guided_json": PERSON}, lambda t: isinstance(json.loads(t)["age"], int)),
    ("regex", "Give me a US phone number.", {"guided_regex": PHONE}, lambda t: re.fullmatch(PHONE, t)),
    ("choice", "Is the sky green? Answer.", {"guided_choice": ["yes", "no", "it depends"]}, lambda t: t in ("yes", "no", "it depends")),
    ("grammar", "Count to five.", {"guided_grammar": 'root ::= num (", " num)*\nnum ::= [1-9]'},
     lambda t: re.fullmatch(r"[1-9](, [1-9])*", t)),
]


def _save(run_dir: Path, name: str, data) -> None:
    (run_dir / f"{name}.json").write_text(json.dumps(data, indent=1))


def structured(target: Target, spec: dict, run_dir: Path, name: str) -> dict:
    """Each grammar kind greedy, sampled and with thinking: the reply obeys it; a grammar that cannot compile is a 400."""
    modes = spec.get("modes", ["greedy", "sampled", "thinking"])
    res, bad = {}, []
    for kind, prompt, extra, ok in STRUCTURED:
        for mode in modes:
            r = api.chat(target.url, target.model, [{"role": "user", "content": prompt}],
                         max_tokens=400 if mode == "thinking" else 160,
                         chat_template_kwargs={"enable_thinking": mode == "thinking"}, **extra,
                         **({"temperature": 0.8, "top_k": 20, "top_p": 0.95, "seed": 3} if mode == "sampled" else {"temperature": 0}))
            good = None
            if r["status"] == 200 and r["finish"] == "stop":
                try:
                    good = bool(ok(r["text"].strip()))
                except Exception:
                    good = False
            elif r["status"] != 200:
                good = False
            res[f"{kind}/{mode}"] = {"text": r.get("text", r.get("error")), "finish": r.get("finish"), "ok": good}
            if good is False:
                bad.append(f"{kind}/{mode}")
    r = api.chat(target.url, target.model, [{"role": "user", "content": "x"}], max_tokens=5, guided_regex="(unclosed")
    res["bad_regex_status"] = r["status"]
    _save(run_dir, name, res)
    ok = not bad and r["status"] == 400
    return {"ok": ok, "summary": f"{len(res) - 1 - len(bad)}/{len(res) - 1} obey; a bad regex -> {r['status']}"
            + (f"; failed {', '.join(bad)}" if bad else ""), "metrics": {"failures": bad, "bad_regex_status": r["status"]}}


SAMPLING_PROMPTS = ["Write a short poem about the sea.", "Give three creative names for a coffee shop.",
                    "Explain recursion to a child in two sentences."]
SAMPLING_RULES = [{"temperature": 0.8, "top_k": 20, "top_p": 0.95, "seed": 1}, {"temperature": 1.0, "top_p": 0.8, "min_p": 0.05, "seed": 2},
                  {"temperature": 0.7, "top_k": 5, "seed": 3}]


def sampling(target: Target, spec: dict, run_dir: Path, name: str) -> dict:
    """Seeded sampled replies twice (equal), and drafted against undrafted (equal) when the target drafts."""
    res, errors, differ = {}, 0, []
    for i, p in enumerate(SAMPLING_PROMPTS):
        for j, rule in enumerate(SAMPLING_RULES):
            runs = []
            for draft in ([None, None, False] if target.feature("drafts", True) else [None, None]):
                extra = {"draft": False} if draft is False else {}
                r = api.chat(target.url, target.model, [{"role": "user", "content": p}], max_tokens=96,
                             chat_template_kwargs={"enable_thinking": False}, **rule, **extra)
                runs.append(r.get("text") if r["status"] == 200 else None)
                errors += r["status"] != 200
            key = f"{i}/{j}"
            res[key] = runs
            if None in runs or len(set(runs)) != 1:
                differ.append(key)
    _save(run_dir, name, res)
    n = len(res)
    return {"ok": not errors and not differ,
            "summary": f"{n - len(differ)}/{n} seeded replies equal on repeat" + (" and undrafted" if target.feature("drafts", True) else "")
            + f"; {errors} errors", "metrics": {"errors": errors, "differ": differ}}


def turns(target: Target, spec: dict, run_dir: Path, name: str) -> dict:
    """A conversation whose turns resume a kept prompt: the resumed turn equals the same turn sent cold."""
    system = "You are a careful assistant. " + " ".join(f"Rule {i}: answer plainly and keep facts straight about topic {i}."
                                                         for i in range(spec.get("rules", 300)))
    kw = {"max_tokens": 48, "temperature": 0, "chat_template_kwargs": {"enable_thinking": False}}
    ask = lambda msgs: api.stream(target.url, target.model, msgs, **kw)
    conv = [{"role": "system", "content": system}, {"role": "user", "content": "Name three rivers in Europe."}]
    res = {"turn1": ask(conv)}
    conv2 = conv + [{"role": "assistant", "content": res["turn1"].get("text", "")}, {"role": "user", "content": "Which of them is longest?"}]
    res["turn2"] = ask(conv2)
    conv3 = conv2 + [{"role": "assistant", "content": res["turn2"].get("text", "")}, {"role": "user", "content": "And the shortest?"}]
    res["turn3"] = ask(conv3)
    res["turn3_again"] = ask(conv3)
    res["turn3_cold"] = ask([{"role": "system", "content": system + " "}] + conv3[1:])
    _save(run_dir, name, res)
    errs = [k for k, v in res.items() if v.get("status") != 200]
    cached = {k: ((v.get("usage") or {}).get("prompt_tokens_details") or {}).get("cached_tokens") for k, v in res.items()}
    same = res["turn3"].get("text") == res["turn3_again"].get("text") == res["turn3_cold"].get("text")
    t = {k: v.get("ttft") for k, v in res.items()}
    return {"ok": not errs and same,
            "summary": f"resumed == again == cold: {same}; cached {cached.get('turn3')} of {(res['turn3'].get('usage') or {}).get('prompt_tokens')}; "
                       f"ttft resumed {t.get('turn3')}s, cold {t.get('turn3_cold')}s" + (f"; errors in {errs}" if errs else ""),
            "metrics": {"cached": cached, "ttft": t, "equal": same}}


def urls(target: Target, spec: dict, run_dir: Path, name: str) -> dict:
    """A public HTTPS image is answered; a loopback address and plain HTTP are refused with a 400."""
    public = spec.get("public_url", "https://upload.wikimedia.org/wikipedia/commons/4/47/PNG_transparency_demonstration_1.png")
    cases = [("public", public, 200), ("loopback", "https://127.0.0.1/x.png", 400), ("http", "http://example.com/x.png", 400)]
    res, bad = {}, []
    for label, url, want in cases:
        r = api.chat(target.url, target.model, [{"role": "user", "content": [{"type": "image_url", "image_url": {"url": url}},
                                                                           {"type": "text", "text": "What is in this image? One sentence."}]}],
                     max_tokens=40, temperature=0, chat_template_kwargs={"enable_thinking": False}, timeout=300)
        res[label] = {"url": url, "status": r["status"], "text": r.get("text", r.get("error", ""))[:300]}
        if r["status"] != want or (want == 200 and not r.get("text")):
            bad.append(label)
    _save(run_dir, name, res)
    return {"ok": not bad, "summary": "; ".join(f"{k} {v['status']}" for k, v in res.items()) + (f"; unexpected: {bad}" if bad else ""),
            "metrics": {"statuses": {k: v["status"] for k, v in res.items()}}}
