"""Reference implementations — medium tier."""

from __future__ import annotations

from collections import Counter, defaultdict
import heapq


def group_anagrams(strs: list[str]) -> list[list[str]]:
    buckets: dict[tuple[str, ...], list[str]] = defaultdict(list)
    for w in strs:
        key = tuple(sorted(w))
        buckets[key].append(w)
    return list(buckets.values())


def product_except_self(nums: list[int]) -> list[int]:
    n = len(nums)
    pref = [1] * n
    suf = [1] * n
    for i in range(1, n):
        pref[i] = pref[i - 1] * nums[i - 1]
    for i in range(n - 2, -1, -1):
        suf[i] = suf[i + 1] * nums[i + 1]
    return [pref[i] * suf[i] for i in range(n)]


def longest_unique_substring(s: str) -> int:
    last: dict[str, int] = {}
    best = 0
    start = 0
    for i, ch in enumerate(s):
        if ch in last and last[ch] >= start:
            start = last[ch] + 1
        last[ch] = i
        best = max(best, i - start + 1)
    return best


def top_k_frequent(nums: list[int], k: int) -> list[int]:
    counts = Counter(nums)
    return heapq.nlargest(k, counts.keys(), key=counts.__getitem__)


def search_in_rotated_sorted(nums: list[int], target: int) -> int:
    lo, hi = 0, len(nums) - 1
    while lo <= hi:
        mid = (lo + hi) // 2
        if nums[mid] == target:
            return mid
        left_sorted = nums[lo] <= nums[mid]
        if left_sorted:
            if nums[lo] <= target < nums[mid]:
                hi = mid - 1
            else:
                lo = mid + 1
        else:
            if nums[mid] < target <= nums[hi]:
                lo = mid + 1
            else:
                hi = mid - 1
    return -1


def coin_change_min_coins(coins: list[int], amount: int) -> int:
    dp = [0] + [10**9] * amount
    for x in range(1, amount + 1):
        for c in coins:
            if c <= x:
                dp[x] = min(dp[x], dp[x - c] + 1)
    return dp[amount] if dp[amount] < 10**9 else -1
