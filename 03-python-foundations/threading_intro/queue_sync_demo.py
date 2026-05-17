"""queue.Queue — synchronous FIFO between threads."""

from __future__ import annotations

import queue


def main() -> None:
    q: queue.Queue[str] = queue.Queue()
    for lab in ("shard-a", "shard-b", "shard-c"):
        q.put(lab)
    drained = []
    while not q.empty():
        drained.append(q.get())
    print("drained:", drained)


if __name__ == "__main__":
    main()
