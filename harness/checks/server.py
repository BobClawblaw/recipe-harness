"""Serving checks beyond a recipe's suite: structured output, sampling determinism, multi-turn resume, media URLs."""

from __future__ import annotations

import json
import random
import re
from concurrent.futures import ThreadPoolExecutor
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
    """Each grammar kind greedy, sampled and with thinking: obeyed, drafted equal to undrafted; a bad grammar is a 400."""
    modes = spec.get("modes", ["greedy", "sampled", "thinking"])
    res, bad = {}, []
    for kind, prompt, extra, ok in STRUCTURED:
        for mode in modes:
            body = {"max_tokens": 400 if mode == "thinking" else 160, "chat_template_kwargs": {"enable_thinking": mode == "thinking"},
                    **extra, **({"temperature": 0.8, "top_k": 20, "top_p": 0.95, "seed": 3} if mode == "sampled" else {"temperature": 0})}
            r = api.chat(target.url, target.model, [{"role": "user", "content": prompt}], **body)
            good = None
            if r["status"] == 200 and r["finish"] == "stop":
                try:
                    good = bool(ok(r["text"].strip()))
                except Exception:
                    good = False
            elif r["status"] != 200:
                good = False
            res[f"{kind}/{mode}"] = {"text": r.get("text", r.get("error")), "finish": r.get("finish"), "ok": good,
                                     "status": r["status"], "usage": r.get("usage"), "seconds": r.get("s"), "prompt": prompt, "request": body}
            if good is False:
                bad.append(f"{kind}/{mode}")
            if mode != "thinking" and target.feature("drafts", True):  # the grammar's reply drafted equals it undrafted
                p = api.chat(target.url, target.model, [{"role": "user", "content": prompt}], **body, draft=False)
                res[f"{kind}/{mode}"].update(plain_text=p.get("text", p.get("error")), plain_seconds=p.get("s"), plain_usage=p.get("usage"))
                if p.get("text") != r.get("text"):
                    bad.append(f"{kind}/{mode} drafted != plain")
    r = api.chat(target.url, target.model, [{"role": "user", "content": "x"}], max_tokens=5, guided_regex="(unclosed")
    res["bad_regex_status"] = r["status"]
    res["bad_regex_error"] = r.get("error")
    _save(run_dir, name, res)
    ok = not bad and r["status"] == 400
    cases = len(res) - 2
    obey = cases - sum(" " not in b for b in bad)
    pairs = sum("plain_text" in v for v in res.values() if isinstance(v, dict))
    same = pairs - sum(b.endswith("drafted != plain") for b in bad)
    return {"ok": ok, "summary": f"{obey}/{cases} obey" + (f", drafted == plain {same}/{pairs}" if pairs else "") + f"; a bad regex -> {r['status']}"
            + (f"; failed {', '.join(bad)}" if bad else ""), "metrics": {"failures": bad, "bad_regex_status": r["status"]}}


def probe_structured(target: Target) -> str:
    """One small json_schema request, for a run that skips structured checks: what the server says to it right now."""
    r = api.chat(target.url, target.model, [{"role": "user", "content": "Invent a person."}], max_tokens=160, temperature=0,
                 chat_template_kwargs={"enable_thinking": False},
                 response_format={"type": "json_schema", "json_schema": {"name": "p", "schema": PERSON}})
    if r["status"] != 200:
        return f"the server refuses json_schema ({r['status']}: {str(r.get('error'))[:160]})"
    try:
        good = set(json.loads(r["text"])) == {"name", "age", "hobbies"}
    except ValueError:
        good = False
    return "the server now obeys json_schema: turn features.structured on" if good else "the server answers json_schema but does not obey it"


CABINS = ("economy", "business", "first")
FLIGHT = {"type": "object", "additionalProperties": False,
          "properties": {"from": {"type": "string"}, "to": {"type": "string"}, "cabin": {"type": "string", "enum": list(CABINS)},
                         "passengers": {"type": "array", "minItems": 1, "items": {
                             "type": "object", "additionalProperties": False,
                             "properties": {"name": {"type": "string"}, "age": {"type": "integer"}}, "required": ["name", "age"]}}},
          "required": ["from", "to", "cabin", "passengers"]}
TOOLS = [{"type": "function", "function": {"name": "book_flight", "description": "Book a flight.", "strict": True, "parameters": FLIGHT}},
         {"type": "function", "function": {"name": "get_weather", "description": "The weather in a city.",
                                           "parameters": {"type": "object", "properties": {"city": {"type": "string"}}, "required": ["city"]}}}]
TOOL_PROMPT = "Book business class from Oslo to Rome for me (Ana, 31) and my son Leo, 6. Also, what's the weather in Rome?"
NAMED = {"type": "function", "function": {"name": "book_flight"}}

# (case, tool_choice, thinking, streamed): auto needs no grammar; required and a named function do (a grammar engine
# refuses them without one, as TensorFold does without lib/libtfgrammar)
TOOL_CASES = [
    ("auto", "auto", False, False),
    ("required", "required", False, False),
    ("named", NAMED, False, False),
    ("named/thinking", NAMED, True, False),
    ("named/stream", NAMED, False, True),
]


def _call_ok(call: dict) -> str | None:
    """None when a call's arguments are the prompt's booking or weather question in its tool's schema, else why not."""
    name = call.get("function", {}).get("name")
    try:
        a = json.loads(call["function"]["arguments"])
    except (KeyError, TypeError, ValueError):
        return f"{name}: arguments are not JSON"
    if name == "get_weather":
        return None if isinstance(a, dict) and isinstance(a.get("city"), str) else f"get_weather: bad arguments {a}"
    if name != "book_flight":
        return f"unknown tool {name!r}"
    if not isinstance(a, dict):
        return f"book_flight: arguments are not an object {a}"
    people = a.get("passengers")
    if (set(a) != set(FLIGHT["required"]) or a["cabin"] not in CABINS or not isinstance(people, list) or not people
            or any(not isinstance(p, dict) or set(p) != {"name", "age"} or type(p["age"]) is not int for p in people)):
        return f"book_flight: arguments outside the schema {a}"
    if a["cabin"] != "business" or sorted(p["age"] for p in people) != [6, 31]:
        return f"book_flight: not the prompt's booking {a}"
    return None


def tools(target: Target, spec: dict, run_dir: Path, name: str) -> dict:
    """Tool calls against a strict nested schema: auto, required, a named function (thinking, streamed); each is a 200 that
    finishes on tool_calls with arguments in the schema; a named call drafted equals it undrafted. Forced calls need a
    grammar, so a target without structured output runs only auto and says so."""
    forced = target.feature("structured")
    res, bad, skipped = {}, [], []
    for case, choice, think, streamed in TOOL_CASES:
        if choice != "auto" and not forced:
            skipped.append(case)
            continue
        body = {"max_tokens": 3000 if think else 600, "temperature": 0, "tools": TOOLS, "tool_choice": choice,
                "chat_template_kwargs": {"enable_thinking": think}}
        msgs = [{"role": "user", "content": TOOL_PROMPT}]
        r = (api.stream if streamed else api.chat)(target.url, target.model, msgs, **body)
        calls = r.get("tool_calls") or []
        why = None
        if r["status"] != 200:
            why = f"{r['status']} {str(r.get('error'))[:200]}"
        elif r.get("finish") != "tool_calls":
            why = f"finish {r.get('finish')}"
        elif not calls or (choice == NAMED and [c["function"]["name"] for c in calls] != ["book_flight"]):
            why = f"calls {[c.get('function', {}).get('name') for c in calls]}"
        else:
            why = next((w for w in map(_call_ok, calls) if w), None)
        res[case] = {"ok": why is None, "why": why, "status": r["status"], "finish": r.get("finish"), "tool_calls": calls,
                     "text": r.get("text", r.get("error")), "usage": r.get("usage"), "seconds": r.get("s"), "request": body}
        if why:
            bad.append(f"{case} ({why})")
        if case == "named" and not why and target.feature("drafts", True):
            p = api.chat(target.url, target.model, msgs, **body, draft=False)
            plain = [c["function"] for c in p.get("tool_calls") or []]
            res[case]["plain_tool_calls"] = p.get("tool_calls")
            if plain != [c["function"] for c in calls]:
                bad.append(f"{case} drafted != plain")
    _save(run_dir, name, res)
    good = sum(v["ok"] for v in res.values())
    summary = f"{good}/{len(res)} tool cases right" + (f"; failed {'; '.join(bad)}" if bad else "")
    if skipped:
        summary += f"; not tested (features.structured = false): {', '.join(skipped)}"
    return {"ok": not bad, "summary": summary, "metrics": {"failures": bad, "skipped": skipped}}


TEAM = {"type": "array", "minItems": 12, "maxItems": 12, "items": PERSON}

# long replies for decode speed: the same prompt with the grammar off and on
GRAMMAR_SPEED = [
    ("json_schema", "Invent twelve people as a JSON array; each has a name, an age and up to three hobbies.",
     {"response_format": {"type": "json_schema", "json_schema": {"name": "team", "schema": TEAM}}}),
    ("json_object", "Describe five European cities as one JSON object: for each city its country, population, a famous "
                    "sight and a one-sentence history.", {"response_format": {"type": "json_object"}}),
]


def _decode(r: dict) -> float | None:
    """Tokens a second after the first, from a streamed reply."""
    n = (r.get("usage") or {}).get("completion_tokens") or 0
    d = (r.get("s") or 0) - (r.get("ttft") or 0)
    return round((n - 1) / d, 1) if r.get("status") == 200 and n > 1 and d > 0 else None


def structured_speed(target: Target, spec: dict, run_dir: Path, name: str) -> dict:
    """Decode speed with the grammar off and on (greedy, thinking off): one stream; two grammar streams at once; and a
    plain stream beside a grammar stream against beside a plain one. Measured; fails only on an error or a grammar
    reply that is not JSON."""
    kw = {"max_tokens": spec.get("max_tokens", 768), "temperature": 0, "chat_template_kwargs": {"enable_thinking": False}}
    ask = lambda prompt, extra: api.stream(target.url, target.model, [{"role": "user", "content": prompt}], **kw, **extra)
    pair = lambda a, b: list(ThreadPoolExecutor(2).map(lambda f: f(), [a, b]))
    res, bad, parts = {}, [], []
    for kind, prompt, extra in GRAMMAR_SPEED:
        one = {"off": ask(prompt, {}), "on": ask(prompt, extra), "on_undrafted": ask(prompt, {**extra, "draft": False})}
        two = {"off": pair(lambda: ask(prompt, {}), lambda: ask(prompt, {})),
               "on": pair(lambda: ask(prompt, extra), lambda: ask(prompt, extra)),
               "plain_beside_on": pair(lambda: ask(prompt, {}), lambda: ask(prompt, extra))[0]}
        for r in (one["on"], one["on_undrafted"], *two["on"]):
            try:
                json.loads(r["text"])
            except Exception:
                bad.append(kind)
        if any(r.get("status") != 200 for r in [*one.values(), *two["off"], *two["on"], two["plain_beside_on"]]):
            bad.append(f"{kind}: errors")
        m = {"c1_off": _decode(one["off"]), "c1_on": _decode(one["on"]), "c1_on_undrafted": _decode(one["on_undrafted"]),
             "c2_off_total": round(sum(_decode(r) or 0 for r in two["off"]), 1),
             "c2_on_total": round(sum(_decode(r) or 0 for r in two["on"]), 1),
             "c2_plain_beside_plain": _decode(two["off"][0]), "c2_plain_beside_on": _decode(two["plain_beside_on"]),
             "tokens_on": (one["on"].get("usage") or {}).get("completion_tokens")}
        res[kind] = {"metrics": m, "one": one, "two": two}
        parts.append(f"{kind} c=1 off/on {m['c1_off']}/{m['c1_on']} (undrafted {m['c1_on_undrafted']}), "
                     f"c=2 total {m['c2_off_total']}/{m['c2_on_total']}, plain beside plain/grammar "
                     f"{m['c2_plain_beside_plain']}/{m['c2_plain_beside_on']} tok/s")
    _save(run_dir, name, res)
    return {"ok": False if bad else None, "summary": "; ".join(parts) + (f"; failed {', '.join(sorted(set(bad)))}" if bad else ""),
            "metrics": {k: v["metrics"] for k, v in res.items()}}


SAMPLING_PROMPTS =["Write a short poem about the sea.", "Give three creative names for a coffee shop.",
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
    """A conversation whose turns resume a kept prompt: the resumed turn equals the same turn sent cold.

    Cold is the same conversation after a restart when the run may restart the server (the same tokens, nothing kept);
    otherwise the system prompt gains a trailing space to miss the kept prefix, which compares only where the template
    and tokenizer leave the prompt's token count unchanged (Flint's keep the space as a token: a different prompt).
    """
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
    restarted = bool(spec.get("restart")) and "up" in target.section("commands")
    if restarted:
        from ..session import bring_up  # the session imports the checks

        bring_up(target)
        res["turn3_cold"] = ask(conv3)
    else:
        res["turn3_cold"] = ask([{"role": "system", "content": system + " "}] + conv3[1:])
    _save(run_dir, name, res)
    errs = [k for k, v in res.items() if v.get("status") != 200]
    cached = {k: ((v.get("usage") or {}).get("prompt_tokens_details") or {}).get("cached_tokens") for k, v in res.items()}
    prompt = {k: (v.get("usage") or {}).get("prompt_tokens") for k, v in res.items()}
    again = res["turn3"].get("text") == res["turn3_again"].get("text")
    # a cold turn that still found kept tokens, or a padded prompt of another length, is not the same request cold
    comparable = prompt["turn3_cold"] == prompt["turn3"] and (not restarted or not cached.get("turn3_cold"))
    cold = res["turn3"].get("text") == res["turn3_cold"].get("text") if comparable else None
    how = "after a restart" if restarted else "padded"
    verdict = (f"cold ({how}): {cold}" if comparable else
               f"cold ({how}) not compared: {prompt['turn3_cold']} prompt tokens (cached {cached.get('turn3_cold')}) against {prompt['turn3']}")
    t = {k: v.get("ttft") for k, v in res.items()}
    ok = False if errs or not again or cold is False else (True if cold else None)
    return {"ok": ok,
            "summary": f"resumed == again: {again}; {verdict}; cached {cached.get('turn3')} of {prompt['turn3']}; "
                       f"ttft resumed {t.get('turn3')}s, cold {t.get('turn3_cold')}s" + (f"; errors in {errs}" if errs else ""),
            "metrics": {"cached": cached, "ttft": t, "equal": again and cold is not False, "again": again, "cold": cold, "cold_restarted": restarted}}


def prefill(target: Target, spec: dict, run_dir: Path, name: str) -> dict:
    """One cold prompt at each size in `tokens`: words no other prompt starts with, timed to the first token (with
    `thinking`, the first reasoning token)."""
    words = "river stone cloud lantern harbor meadow copper violet signal garden orbit candle marble forest thunder".split()
    thinking = bool(spec.get("thinking"))
    kw = {"max_tokens": 8, "temperature": 0, "chat_template_kwargs": {"enable_thinking": thinking}}
    res = {}
    for n in spec.get("tokens", [2048, 8192, 32768, 131072]):
        rng = random.Random(f"{run_dir.name}-{name}-{n}")
        text = f"Document {rng.getrandbits(64):016x}. " + " ".join(rng.choice(words) for _ in range(n))  # a token a word
        r = api.stream(target.url, target.model, [{"role": "user", "content": text + "\n\nSummarize in one sentence."}],
                       timeout=spec.get("timeout", 3600), **kw)
        u = r.get("usage") or {}
        prompt, cached = u.get("prompt_tokens"), (u.get("prompt_tokens_details") or {}).get("cached_tokens")
        first = r.get("ttft_any") if thinking else r.get("ttft")
        res[str(n)] = {"status": r.get("status"), "prompt_tokens": prompt, "cached_tokens": cached, "ttft": first,
                       "tok_s": round(prompt / first, 1) if prompt and first else None, "error": (r.get("error") or "")[:300]}
    _save(run_dir, name, res)
    # the chat template's shared opening may come from the prompt cache; more than that is not a cold prompt
    bad = [k for k, v in res.items() if v["status"] != 200 or v["tok_s"] is None or (v["cached_tokens"] or 0) > spec.get("cached_ok", 64)]
    cells = ", ".join(f"{v['prompt_tokens']} tokens {v['tok_s']} tok/s ({v['ttft']} s)" for v in res.values() if v["tok_s"])
    return {"ok": False if bad else None, "summary": cells + (f"; not cold or failed: {bad}" if bad else ""), "metrics": res}


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
