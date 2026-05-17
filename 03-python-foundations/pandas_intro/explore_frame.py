"""Toy pandas workflow — skips gracefully when pandas is not installed."""

from __future__ import annotations

import sys


def main() -> None:
    try:
        import pandas as pd
    except ImportError:
        print("Optional dependency missing. Install with: pip install pandas")
        sys.exit(0)

    df = pd.DataFrame(
        {
            "batch_tokens": [128, 512, 1024, 2048],
            "latency_ms": [11.2, 28.5, 52.1, 104.3],
        }
    )
    print(df.head())
    print(df.describe())


if __name__ == "__main__":
    main()
