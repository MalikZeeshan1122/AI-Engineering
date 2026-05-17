"""ThreadPoolExecutor — overlap blocking CPU-ish slices."""

from __future__ import annotations

import time
from concurrent.futures import ThreadPoolExecutor


def slow_square(x: int) -> int:
    time.sleep(0.04)
    return x * x


def main() -> None:
    with ThreadPoolExecutor(max_workers=4) as pool:
        got = list(pool.map(slow_square, range(8)))
    print(got)


if __name__ == "__main__":
    main()
