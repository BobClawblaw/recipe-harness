"""The served model, as an OpenAI-compatible client sees it (stdlib urllib)."""

from __future__ import annotations

import json
import time
import urllib.error
import urllib.request


def request(url: str, body: dict | None = None, timeout: float = 600) -> tuple[int, dict | str]:
    """(status, parsed JSON or error text); status -1 when the server could not be reached or dropped the request."""
    data = json.dumps(body).encode() if body is not None else None
    req = urllib.request.Request(url, data, {"Content-Type": "application/json"} if data else {})
    try:
        with urllib.request.urlopen(req, timeout=timeout) as r:
            raw = r.read()
            try:
                return r.status, json.loads(raw)
            except ValueError:
                return r.status, raw.decode(errors="replace")
    except urllib.error.HTTPError as e:
        return e.code, e.read().decode(errors="replace")[:2000]
    except Exception as e:  # refused, reset, timed out
        return -1, repr(e)[:500]


def healthy(base: str, timeout: float = 10) -> bool:
    s1, _ = request(f"{base}/health", timeout=timeout)
    s2, _ = request(f"{base}/v1/models", timeout=timeout)
    return s1 == 200 and s2 == 200


def chat(base: str, model: str, messages: list, timeout: float = 600, **extra) -> dict:
    """One non-streamed completion: status, text, reasoning, finish, usage, seconds (and error when not 200)."""
    body = {"model": model, "messages": messages, **extra}
    t0 = time.time()
    status, d = request(f"{base}/v1/chat/completions", body, timeout)
    out = {"status": status, "s": round(time.time() - t0, 3)}
    if status == 200 and isinstance(d, dict):
        c = d["choices"][0]
        m = c.get("message") or {}
        out.update(text=m.get("content") or "", reasoning=m.get("reasoning_content") or "", finish=c.get("finish_reason"),
                   usage=d.get("usage") or {}, tool_calls=m.get("tool_calls"))
    else:
        out["error"] = d if isinstance(d, str) else json.dumps(d)[:2000]
    return out


def stream(base: str, model: str, messages: list, timeout: float = 600, **extra) -> dict:
    """One streamed completion: text, time to the first content token (and to the first token of any kind), usage,
    finish, and tool calls joined from their deltas."""
    body = {"model": model, "messages": messages, "stream": True, "stream_options": {"include_usage": True}, **extra}
    req = urllib.request.Request(f"{base}/v1/chat/completions", json.dumps(body).encode(), {"Content-Type": "application/json"})
    t0, first, first_any, text, usage, finish, calls = time.time(), None, None, "", {}, None, {}
    try:
        with urllib.request.urlopen(req, timeout=timeout) as r:
            for line in r:
                line = line.decode().strip()
                if not line.startswith("data: ") or line == "data: [DONE]":
                    continue
                d = json.loads(line[6:])
                if d.get("usage"):
                    usage = d["usage"]
                for c in d.get("choices", []):
                    delta = c.get("delta") or {}
                    if first_any is None and (delta.get("content") or delta.get("reasoning_content")):
                        first_any = time.time() - t0
                    piece = delta.get("content")
                    if piece:
                        first = first if first is not None else time.time() - t0
                        text += piece
                    for tc in delta.get("tool_calls") or []:
                        call = calls.setdefault(tc.get("index", 0), {"type": "function", "function": {"name": "", "arguments": ""}})
                        call["id"] = tc.get("id") or call.get("id")
                        f = tc.get("function") or {}
                        call["function"]["name"] += f.get("name") or ""
                        call["function"]["arguments"] += f.get("arguments") or ""
                    finish = c.get("finish_reason") or finish
    except urllib.error.HTTPError as e:
        return {"status": e.code, "error": e.read().decode(errors="replace")[:2000]}
    except Exception as e:
        return {"status": -1, "error": repr(e)[:500]}
    return {"status": 200, "text": text, "ttft": round(first, 3) if first is not None else None,
            "ttft_any": round(first_any, 3) if first_any is not None else None, "usage": usage,
            "s": round(time.time() - t0, 3), "finish": finish, "tool_calls": [calls[i] for i in sorted(calls)] or None}
