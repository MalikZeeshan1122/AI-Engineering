"""Async iteration — fake streaming tokens (CURRICULUM letter Y shape)."""

from __future__ import annotations

import asyncio
from collections.abc import AsyncIterator


async def fake_token_stream() -> AsyncIterator[str]:
    for tok in ["The", "model", "streams", "tokens"]:
        await asyncio.sleep(0.04)
        yield tok


async def main() -> None:
    buf: list[str] = []
    async for piece in fake_token_stream():
        buf.append(piece)
        print("chunk:", piece)
    print("joined:", " ".join(buf))


if __name__ == "__main__":
    asyncio.run(main())
