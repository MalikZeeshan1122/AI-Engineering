"""Overlapping character windows — chunking-shaped iterator for NLP previews."""

from __future__ import annotations

from collections.abc import Iterator


def overlapping_windows(text: str, width: int, stride: int = 1) -> Iterator[str]:
    if width < 1 or stride < 1:
        raise ValueError("width and stride must be positive")
    if len(text) < width:
        yield from ()
        return
    for start in range(0, len(text) - width + 1, stride):
        yield text[start : start + width]


if __name__ == "__main__":
    blob = "retrieval-augmented"
    print(list(overlapping_windows(blob, 6, stride=4)))
