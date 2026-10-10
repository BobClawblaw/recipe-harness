"""Targets and plans: TOML files, a target's committed file overlaid by its git-ignored local file."""

from __future__ import annotations

import os
import string
import tomllib
from dataclasses import dataclass, field
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent


class ConfigError(Exception):
    pass


def merge(base: dict, over: dict) -> dict:
    """``over`` on top of ``base``, tables merged key by key."""
    out = dict(base)
    for k, v in over.items():
        out[k] = merge(out[k], v) if isinstance(v, dict) and isinstance(out.get(k), dict) else v
    return out


def _load(path: Path) -> dict:
    with open(path, "rb") as f:
        return tomllib.load(f)


def find(kind: str, name: str) -> Path:
    """A target or plan by name (targets/<name>.toml) or by path."""
    p = Path(name)
    if p.suffix == ".toml" and p.is_file():
        return p
    p = ROOT / kind / f"{name}.toml"
    if not p.is_file():
        have = sorted(x.stem for x in (ROOT / kind).glob("*.toml") if not x.stem.endswith(".local") and ".example" not in x.stem)
        raise ConfigError(f"no {kind[:-1]} {name!r}; have: {', '.join(have) or 'none'}")
    return p


@dataclass
class Target:
    name: str
    raw: dict
    vars: dict = field(default_factory=dict)

    def __getitem__(self, key):
        return self.raw[key]

    def get(self, key, default=None):
        return self.raw.get(key, default)

    def section(self, key: str) -> dict:
        return self.raw.get(key, {})

    def expand(self, text: str, **extra) -> str:
        """``$name`` placeholders from the target's [vars], its url and model, and ``extra``. Unknown ones fail."""
        values = {**self.vars, "url": self.url, "model": self.model, **{k: str(v) for k, v in extra.items()}}
        try:
            return string.Template(text).substitute(values)
        except KeyError as e:
            raise ConfigError(f"{self.name}: ${e.args[0]} is not set (put it in [vars] of targets/{self.name}.local.toml)") from None

    @property
    def url(self) -> str:
        return string.Template(self.raw["url"]).safe_substitute(self.vars).rstrip("/")

    @property
    def model(self) -> str:
        return self.raw.get("model", "default")

    @property
    def cwd(self) -> str | None:
        c = self.raw.get("cwd")
        return os.path.expanduser(string.Template(c).safe_substitute(self.vars)) if c else None

    def feature(self, name: str, default=True):
        return self.section("features").get(name, default)


def load_target(name: str) -> Target:
    path = find("targets", name)
    raw = _load(path)
    local = path.with_name(path.stem + ".local.toml")
    if local.is_file():
        raw = merge(raw, _load(local))
    for k, v in raw.get("vars", {}).items():
        if isinstance(v, str) and v.startswith("CHANGE-ME"):
            raise ConfigError(f"{path.stem}: [vars] {k} is unset; copy {path.stem}.local.example.toml to {local.name} and fill it")
    t = Target(raw.get("name", path.stem), raw, {k: os.path.expanduser(str(v)) for k, v in raw.get("vars", {}).items()})
    for key in ("url",):
        if key not in raw:
            raise ConfigError(f"{t.name}: '{key}' is required")
    return t


def load_plan(name: str) -> dict:
    plan = _load(find("plans", name))
    if not plan.get("checks"):
        raise ConfigError(f"plan {name}: no [[checks]]")
    return plan


def local_settings() -> dict:
    """harness.local.toml (git-ignored): scrub patterns and other machine-specific values."""
    p = ROOT / "harness.local.toml"
    return _load(p) if p.is_file() else {}
