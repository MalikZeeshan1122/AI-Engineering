"""Medium-tier stubs."""

from __future__ import annotations


def group_anagrams(strs: list[str]) -> list[list[str]]:
    """Bucket strings that are anagrams; inner lists any order, outer order any."""
    raise NotImplementedError


def product_except_self(nums: list[int]) -> list[int]:
    """Product of all elements except index i — no division; len(nums) >= 1."""
    raise NotImplementedError


def longest_unique_substring(s: str) -> int:
    """Longest substring without repeating characters."""
    raise NotImplementedError


def top_k_frequent(nums: list[int], k: int) -> list[int]:
    """Return k distinct integers with highest frequency (any order among ties OK here — tests sort)."""
    raise NotImplementedError


def search_in_rotated_sorted(nums: list[int], target: int) -> int:
    """nums ascending rotated unknown pivot; distinct elements; return index or -1."""
    raise NotImplementedError


def coin_change_min_coins(coins: list[int], amount: int) -> int:
    """Fewest coins to make amount (each coin infinite); impossible -> -1."""
    raise NotImplementedError
