"""Retry a flaky callable with capped exponential backoff + jitter."""

from __future__ import annotations

import functools
import random
import time
from collections.abc import Callable
from typing import TypeVar

T = TypeVar("T")


def retry_delays(max_attempts: int, base_s: float = 0.05, cap_s: float = 1.0):
    attempts = max(1, max_attempts)

    def deco(fn: Callable[..., T]) -> Callable[..., T]:
        @functools.wraps(fn)
        def wrapper(*args, **kwargs) -> T:
            delay = base_s
            last_exc: BaseException | None = None
            for attempt in range(attempts):
                try:
                    return fn(*args, **kwargs)
                except RuntimeError as exc:
                    last_exc = exc
                    if attempt == attempts - 1:
                        raise
                    jitter = random.uniform(0, delay * 0.2)
                    time.sleep(min(delay + jitter, cap_s))
                    delay = min(delay * 2, cap_s)

            raise AssertionError("unreachable") from last_exc

        return wrapper

    return deco


@retry_delays(max_attempts=4, base_s=0.02)
def flaky_vendor(call_no: list[int]) -> str:
    call_no[0] += 1
    if call_no[0] < 3:
        raise RuntimeError("timeout")
    return "payload"


if __name__ == "__main__":
    counter = [0]
    print(flaky_vendor(counter), "after", counter[0], "calls")
