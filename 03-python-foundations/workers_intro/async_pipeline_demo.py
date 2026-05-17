"""Two-stage async pipeline: ingest docs -> pretend embed."""

from __future__ import annotations

import asyncio
from collections.abc import AsyncIterator


async def ingest_docs() -> AsyncIterator[str]:
    for name in ("wiki:latency", "ticket:884", "runbook:oncall"):
        await asyncio.sleep(0.02)
        yield name


async def pretend_embed(label: str) -> tuple[str, int]:
    await asyncio.sleep(0.02)
    return label, len(label)


async def main() -> None:
    results: list[tuple[str, int]] = []
    async for doc in ingest_docs():
        results.append(await pretend_embed(doc))
    print(results)


if __name__ == "__main__":
    asyncio.run(main())
