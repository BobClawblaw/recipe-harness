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
        if body.get("response_format") in ("mp3", "flac", "aac"):
            head = {"mp3": b"\xff\xfb", "flac": b"fLaC"}.get(body["response_format"])
            return {"status": 400, "audio": b"", "s": 0.01, "error": "no library"} if head is None else {"status": 200, "audio": head + b"data", "first": 0.1, "s": 0.1}
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

    def test_cases_sent_together_must_each_give_their_lone_audio(self):
        audio = {"hello": b"\x01\x00" * 100, "again": b"\x02\x00" * 200}
        spec = {"sample_rate": RATE, "repeats": 1, "cases": [{"name": "a", "input": "hello"}, {"name": "b", "input": "again"}], "together": [["a", "b", "a"]]}
        res, _ = self.run_check(audio, spec)
        self.assertTrue(res["ok"], res["summary"])
        t = res["metrics"]["together"][0]
        self.assertEqual((t["statuses"], t["identical"], t["audio_s"]), ([200, 200, 200], 3, 4.0))
        self.assertIn("at once: 3/3 equal to alone in 1 mixes", res["summary"])
        # a reply that differs beside others fails: the stand-in gives the first request one audio and later ones another
        res, _ = self.run_check({"hello": [b"\x01\x00" * 100] * 3 + [b"\x05\x00" * 100] * 2, "again": b"\x02\x00" * 200}, spec)
        self.assertFalse(res["ok"])
        self.assertIn("together", res["summary"])

    def test_same_pairs_need_equal_audio_and_another_from_other(self):
        audio = {"hello": b"\x01\x00" * 100, "$5": b"\x02\x00" * 100, "five dollars": b"\x02\x00" * 100, "5 typed": b"\x03\x00" * 100}
        pair = {"name": "dollars", "a": {"input": "$5"}, "b": {"input": "five dollars"}, "other": {"input": "5 typed"}}
        spec = {"sample_rate": RATE, "repeats": 1, "cases": [{"name": "a", "input": "hello"}], "same": [pair]}
        res, _ = self.run_check(audio, spec)
        self.assertTrue(res["ok"], res["summary"])
        self.assertEqual(res["metrics"]["same"]["dollars"], {"statuses": [200, 200, 200], "equal": True, "other_differs": True})
        self.assertIn("same audio 1/1", res["summary"])
        res, _ = self.run_check({**audio, "five dollars": b"\x04\x00" * 100}, spec)
        self.assertFalse(res["ok"])
        res, _ = self.run_check({**audio, "5 typed": b"\x02\x00" * 100}, spec)
        self.assertFalse(res["ok"])
        self.assertIn("same dollars", res["summary"])

    def test_formats_start_as_their_files_do_and_a_refused_one_fails(self):
        spec = {"sample_rate": RATE, "repeats": 1, "formats": ["mp3", "flac", "aac"], "cases": [{"name": "a", "input": "hello"}]}
        res, _ = self.run_check({"hello": b"\x00\x01" * 200}, spec)
        f = res["metrics"]["formats"]
        self.assertEqual((f["mp3"]["starts_as"], f["flac"]["repeat_identical"], f["aac"]["status"]), (True, True, 400))
        self.assertEqual(len(res["metrics"]["failures"]), 1)
        self.assertIn("format aac: status 400", res["metrics"]["failures"][0])

    def test_wer_from_the_asr_command(self):
        spec = {"sample_rate": RATE, "repeats": 1, "max_wer": 0.1, "cases": [{"name": "a", "input": "hello"}]}
        res, _ = self.run_check({"hello": b"\x00\x01" * 200}, spec, {"asr": "echo $wav: 2.0s WER 0.250 for $said"})
        self.assertEqual(res["metrics"]["cases"]["a"]["wer"], 0.25)
        self.assertIn("a: WER 0.25 above 0.1", res["metrics"]["failures"])


if __name__ == "__main__":
    unittest.main()
