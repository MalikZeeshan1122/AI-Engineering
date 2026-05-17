"""Tiny tracemalloc snapshot — complements CURRICULUM letter M."""

from __future__ import annotations

import tracemalloc


def main() -> None:
    tracemalloc.start()
    _scratch = [bytearray(8_192) for _ in range(64)]
    current, peak = tracemalloc.get_traced_memory()
    print(f"current_kb={current / 1024:.1f} peak_kb={peak / 1024:.1f}")
    snapshot = tracemalloc.take_snapshot()
    top = snapshot.statistics("lineno")[:3]
    for stat in top:
        print(stat)
    tracemalloc.stop()


if __name__ == "__main__":
    main()
