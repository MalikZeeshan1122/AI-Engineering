"""Reference implementations — hard tier."""

from __future__ import annotations

import heapq


def trap_rain_water(height: list[int]) -> int:
    if not height:
        return 0
    lo, hi = 0, len(height) - 1
    left_max = right_max = 0
    water = 0
    while lo < hi:
        if height[lo] < height[hi]:
            left_max = max(left_max, height[lo])
            water += left_max - height[lo]
            lo += 1
        else:
            right_max = max(right_max, height[hi])
            water += right_max - height[hi]
            hi -= 1
    return water


def word_break(s: str, word_dict: list[str]) -> bool:
    words = set(word_dict)
    n = len(s)
    dp = [False] * (n + 1)
    dp[0] = True
    for i in range(1, n + 1):
        for j in range(i):
            if dp[j] and s[j:i] in words:
                dp[i] = True
                break
    return dp[n]


def merge_k_sorted_lists(lists: list[list[int]]) -> list[int]:
    heap: list[tuple[int, int, int]] = []
    for li, lst in enumerate(lists):
        if lst:
            heapq.heappush(heap, (lst[0], li, 0))
    out: list[int] = []
    while heap:
        val, li, idx = heapq.heappop(heap)
        out.append(val)
        nxt = lists[li]
        if idx + 1 < len(nxt):
            heapq.heappush(heap, (nxt[idx + 1], li, idx + 1))
    return out
