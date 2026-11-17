import tempfile
import unittest
from pathlib import Path
from unittest import mock

from harness import config
from harness.checks import speech

RATE = 100


def target(commands: dict | None = None) -> config.Target:
    return config.Target("t", {"url": "http://h", "model": "m", "commands": commands or {}}, {})


def server(audio: dict, busy_status: int = 503):
    """api.speech's stand-in: a reply by input, 400 for an unknown voice, and one request at a time when asked twice at once."""
    calls = []

    def ask(url, body, timeout=None):
        calls.append(body)
        if body.get("voice") == "nobody":
            return {"status": 400, "audio": b"", "s": 0.01, "error": "unknown voice"}
        pcm = audio[body["input"]]
        pcm = pcm.pop(0) if isinstance(pcm, list) else pcm
        return {"status": 200, "audio": pcm, "first": 0.05 if body.get("stream") else 0.5, "s": 0.5}
    return ask, calls


class Wav(unittest.TestCase):
    def test_header_sizes(self):
        w = speech.wav(b"\x01\x00" * 50, RATE)
        self.assertEqual((w[:4], w[8:12], len(w)), (b"RIFF", b"WAVE", 144))
        self.assertEqual(int.from_bytes(w[4:8], "little"), 136)
        self.assertEqual(int.from_bytes(w[40:44], "little"), 100)


class Check(unittest.TestCase):
    spec = {"sample_rate": RATE, "repeats": 2, "cases": [{"name": "a", "input": "hello", "seed": 1}, {"name": "c", "input": "again", "ref_from": "a"}],
            "refusals": [{"name": "voice", "status": 400, "body": {"input": "x", "voice": "nobody"}}]}

    def run_check(self, audio, spec=None, commands=None):
        ask, calls = server(audio)
        with tempfile.TemporaryDirectory() as d, mock.patch("harness.api.speech", ask):
            return speech.run(target(commands), spec or self.spec, Path(d), "speech"), calls

    def test_speed_repeats_streams_and_the_clone_carries_the_first_reply(self):
        res, calls = self.run_check({"hello": b"\x00\x01" * 200, "again": b"\x02\x03" * 100})
        self.assertTrue(res["ok"], res["summary"])
        a = res["metrics"]["cases"]["a"]
        self.assertEqual((a["audio_s"], a["times_real_time"], a["repeat_identical"], a["stream_identical"]), (2.0, 4.0, True, True))
        clone = next(c for c in calls if c["input"] == "again")
        self.assertEqual(speech.base64.b64decode(clone["ref_audio"]), speech.wav(b"\x00\x01" * 200, RATE))
        self.assertNotIn("ref_from", clone)
        self.assertEqual(res["metrics"]["refusals"]["voice"]["status"], 400)

    def test_a_repeat_that_differs_fails(self):
        res, _ = self.run_check({"hello": [b"\x00\x01" * 200, b"\x00\x01" * 200, b"\x09\x09" * 200, b"\x00\x01" * 200, b"\x00\x01" * 200], "again": b"\x02\x03" * 100})
        self.assertFalse(res["ok"])
        self.assertIn("a: a repeated request gives other audio", res["metrics"]["failures"])

    def test_a_refusal_that_answers_fails(self):
        spec = {**self.spec, "refusals": [{"name": "plain", "status": 400, "body": {"input": "hello"}}]}
        res, _ = self.run_check({"hello": b"\x00\x01" * 200, "again": b"\x02\x03" * 100}, spec)
        self.assertIn("refusal plain: status 200, expected 400", res["metrics"]["failures"])

    def test_busy_takes_the_same_audio_or_503(self):
        spec = {"sample_rate": RATE, "repeats": 1, "busy": 2, "cases": [{"name": "a", "input": "hello"}]}
        res, _ = self.run_check({"hello": b"\x00\x01" * 200}, spec)
        self.assertTrue(res["ok"], res["summary"])
        self.assertEqual(res["metrics"]["busy"], {"statuses": [200, 200, 200], "identical": 3})

    def test_wer_from_the_asr_command(self):
        spec = {"sample_rate": RATE, "repeats": 1, "max_wer": 0.1, "cases": [{"name": "a", "input": "hello"}]}
        res, _ = self.run_check({"hello": b"\x00\x01" * 200}, spec, {"asr": "echo $wav: 2.0s WER 0.250 for $said"})
        self.assertEqual(res["metrics"]["cases"]["a"]["wer"], 0.25)
        self.assertIn("a: WER 0.25 above 0.1", res["metrics"]["failures"])


if __name__ == "__main__":
    unittest.main()
