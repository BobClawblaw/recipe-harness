import base64
import tempfile
import unittest
from pathlib import Path
from unittest import mock

from harness import config
from harness.checks import speech_edit
from harness.checks.speech import wav

FRAME = speech_edit.FRAME


def target() -> config.Target:
    return config.Target("t", {"url": "http://h", "model": "m", "commands": {}}, {})


def clip(frames: int, value: int = 100) -> bytes:
    return (value).to_bytes(2, "little", signed=True) * (frames * FRAME)


def server(fill_frames: int = 12, drift: bool = False):
    """Stand-ins for api.speech and api.request: a 60-frame clip; an edit that swaps each region for `fill_frames`."""
    state = {"edits": 0}

    def speak(url, body, timeout=None):
        return {"status": 200, "audio": clip(60), "first": 0.1, "s": 0.2}

    def post(url, body, timeout=None):
        if url.endswith("/align"):
            if "text" not in body:
                return 400, "text is required"
            words = body["text"].split()
            return 200, {"text": body["text"], "duration": 4.0, "words": [{"word": w, "start": i * 0.2, "end": i * 0.2 + 0.2, "confidence": 0.9, "tokens": [w.upper()]} for i, w in enumerate(words)]}
        if "target_text" not in body or "audio_base64" not in body:
            return 400, "target_text is required"
        spans = body.get("spans") or [[1.0, 2.0]]
        state["edits"] += 1
        frames = 60 - sum(round((b - a) * 15) for a, b in spans) + fill_frames * len(spans)
        audio = clip(frames, 100 + (state["edits"] if drift else 0))
        take = {"seed": 1, "audio_base64": base64.b64encode(wav(audio, 44100)).decode(), "duration": frames / 15, "edited_regions": spans,
                "fill_seconds": [fill_frames / 15] * len(spans), "stopped": [True] * len(spans), "verify": None, "words": None}
        return 200, {"sample_rate": 44100, "spans": spans, "contexts": None, "expected_seconds": [1.0] * len(spans), "words": None,
                     "takes": [dict(take) for _ in range(int(body.get("num_takes", 1)))]}
    return speak, post


SPEC = {
    "clips": [{"name": "line", "input": "one two three", "seed": 1}],
    "cases": [{"name": "by-span", "clip": "line", "target_text": "one two four", "spans": [[1.0, 2.0]]},
              {"name": "by-text", "clip": "line", "target_text": "one two four", "transcript": True, "num_takes": 2}],
    "align": ["line"],
    "together": [["by-span", "line"]],
    "refusals": [{"name": "no-target", "status": 400, "clip": "line", "body": {}},
                 {"name": "align-without-text", "status": 400, "clip": "line", "route": "/v1/audio/edit/align", "body": {}}],
}


class Edit(unittest.TestCase):
    def run_spec(self, speak, post, spec=SPEC):
        with tempfile.TemporaryDirectory() as d, mock.patch("harness.api.speech", speak), mock.patch("harness.api.request", post):
            return speech_edit.run(target(), spec, Path(d), "speech-edit")

    def test_passes_and_measures(self):
        speak, post = server()
        got = self.run_spec(speak, post)
        self.assertTrue(got["ok"], got["summary"])
        case = got["metrics"]["cases"]["by-span"]
        self.assertTrue(case["repeat_identical"] and case["length_as_planned"])
        self.assertEqual(case["audio_s"], round((60 - 15 + 12) * FRAME / 44100, 2))
        self.assertEqual(got["metrics"]["align"]["line"]["words"], 3)
        self.assertEqual(got["metrics"]["together"][0]["identical"], 2)
        self.assertIn("refusals 2/2", got["summary"])

    def test_an_edit_that_does_not_repeat_fails(self):
        speak, post = server(drift=True)
        got = self.run_spec(speak, post)
        self.assertFalse(got["ok"])
        self.assertIn("a repeated edit gives other audio", got["summary"])

    def test_a_reply_of_the_wrong_length_fails(self):
        speak, post = server()

        def short(url, body, timeout=None):
            status, d = post(url, body, timeout)
            if status == 200 and "takes" in d:
                for take in d["takes"]:
                    take["fill_seconds"] = [1.0] * len(take["fill_seconds"])
            return status, d
        got = self.run_spec(speak, short)
        self.assertFalse(got["ok"])
        self.assertIn("the plan gives", got["summary"])

    def test_snr_and_wav_reading(self):
        a = clip(1)
        self.assertEqual(speech_edit.pcm_of(wav(a, 44100)), a)
        self.assertEqual(speech_edit.pcm_of(b"not a wav"), b"")
        self.assertGreater(speech_edit.snr_db(a, a), 100)
        self.assertIsNone(speech_edit.snr_db(b"", b""))


if __name__ == "__main__":
    unittest.main()
