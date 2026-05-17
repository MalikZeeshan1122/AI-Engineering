"""Tiny producer-consumer using asyncio.Queue + sentinel shutdown."""

from __future__ import annotations

import asyncio

_SENTINEL = object()


async def producer(queue: asyncio.Queue[str | object], labels: list[str]) -> None:
    for lab in labels:
        await asyncio.sleep(0.02)
        await queue.put(lab)
    await queue.put(_SENTINEL)


async def main() -> None:
    q: asyncio.Queue[str | object] = asyncio.Queue(maxsize=3)

    async def drain() -> list[str]:
        out: list[str] = []
        while True:
            item = await q.get()
            try:
                if item is _SENTINEL:
                    break
                out.append(str(item))
            finally:
                q.task_done()
        return out

    worker = asyncio.create_task(drain())
    await producer(q, ["chunk-1", "chunk-2", "chunk-3"])
    await q.join()
    got = await worker
    print("drained:", got)


if __name__ == "__main__":
    asyncio.run(main())
