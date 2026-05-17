"""Offload blocking work with asyncio.to_thread (pairs with exercises/09-async-io.ipynb)."""

from __future__ import annotations

import asyncio
import time


def blocking_sum(n: int) -> int:
    time.sleep(0.05)
    return sum(range(n))


async def main() -> None:
    t0 = time.perf_counter()
    total = await asyncio.to_thread(blocking_sum, 80_000)
    ms = (time.perf_counter() - t0) * 1000
    print("sum:", total, "elapsed_ms:", round(ms, 2))


if __name__ == "__main__":
    asyncio.run(main())
