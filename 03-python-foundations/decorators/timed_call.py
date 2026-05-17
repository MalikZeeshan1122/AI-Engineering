"""Wrap a function to print wall-clock duration (minimal @timed decorator)."""

from __future__ import annotations

import functools
import time
from collections.abc import Callable
from typing import Any


def timed(fn: Callable[..., Any]) -> Callable[..., Any]:
    @functools.wraps(fn)
    def wrapper(*args: Any, **kwargs: Any) -> Any:
        t0 = time.perf_counter()
        try:
            return fn(*args, **kwargs)
        finally:
            ms = (time.perf_counter() - t0) * 1000
            print(f"{fn.__name__} took {ms:.2f} ms")

    return wrapper


@timed
def fake_embed_batch(texts: list[str]) -> int:
    time.sleep(0.05)
    return sum(len(t) for t in texts)


if __name__ == "__main__":
    n = fake_embed_batch(["rag", "agents", "pipelines"])
    print("chars:", n)
