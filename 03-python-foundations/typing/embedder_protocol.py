"""Structural typing with Protocol — swap embedding backends without inheritance."""

from __future__ import annotations

from typing import Protocol, runtime_checkable


@runtime_checkable
class Embedder(Protocol):
    def embed(self, texts: list[str]) -> list[list[float]]:
        """Return one embedding vector per input string."""
        ...


class LengthEmbedder:
    """Toy backend: two floats derived from token length."""

    def embed(self, texts: list[str]) -> list[list[float]]:
        return [[float(len(t)), float(t.count(" "))] for t in texts]


def batch_dims(backend: Embedder, corpus: list[str]) -> tuple[int, int]:
    vectors = backend.embed(corpus)
    if not vectors:
        return 0, 0
    return len(vectors), len(vectors[0])


if __name__ == "__main__":
    backend = LengthEmbedder()
    rows, cols = batch_dims(backend, ["chunk one", "chunk-two"])
    print(f"batches: rows={rows}, cols={cols}")
    print("is_embedder?", isinstance(backend, Embedder))
