"""Overlap slow I/O-shaped waits with asyncio.gather (compare wall-clock vs sequential)."""

from __future__ import annotations

import asyncio
import time


async def pretend_fetch(name: str, delay_s: float) -> str:
    await asyncio.sleep(delay_s)
    return f"{name}-ok"


async def main() -> None:
    t0 = time.perf_counter()
    one_by_one = []
    for label in ("a", "b", "c"):
        one_by_one.append(await pretend_fetch(label, 0.08))
    sequential_s = time.perf_counter() - t0

    t1 = time.perf_counter()
    parallel = await asyncio.gather(
        pretend_fetch("x", 0.08),
        pretend_fetch("y", 0.08),
        pretend_fetch("z", 0.08),
    )
    parallel_s = time.perf_counter() - t1

    print("sequential:", sequential_s, "s ->", one_by_one)
    print("parallel:  ", parallel_s, "s ->", list(parallel))


if __name__ == "__main__":
    asyncio.run(main())
