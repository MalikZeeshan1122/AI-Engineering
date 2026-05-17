"""Yield fixed-size batches from any iterable — constant memory for large streams."""

from __future__ import annotations

from collections.abc import Iterable, Iterator
from typing import TypeVar

T = TypeVar("T")


def batched(items: Iterable[T], size: int) -> Iterator[list[T]]:
    if size < 1:
        raise ValueError("size must be positive")
    bucket: list[T] = []
    for item in items:
        bucket.append(item)
        if len(bucket) >= size:
            yield bucket
            bucket = []
    if bucket:
        yield bucket


if __name__ == "__main__":
    seq = range(10)
    for chunk in batched(seq, 3):
        print(chunk)
