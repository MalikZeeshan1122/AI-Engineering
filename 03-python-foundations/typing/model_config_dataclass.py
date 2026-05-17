"""Immutable config objects — safer defaults across pipeline stages."""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True, slots=True)
class ModelConfig:
    name: str
    temperature: float = 0.2
    max_tokens: int = 1024


def summarize(cfg: ModelConfig) -> str:
    return f"{cfg.name} temp={cfg.temperature} max_tokens={cfg.max_tokens}"


if __name__ == "__main__":
    base = ModelConfig(name="demo-mini")
    tuned = ModelConfig(name=base.name, temperature=0.7, max_tokens=2048)
    print(summarize(base))
    print(summarize(tuned))
