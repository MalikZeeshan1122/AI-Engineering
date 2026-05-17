"""Shared assertions for medium-tier functions."""

from __future__ import annotations


def _norm_groups(groups: list[list[str]]) -> list[list[str]]:
    inner = [sorted(bucket) for bucket in groups]
    inner.sort(key=lambda b: (len(b), b))
    return inner


def run_all_medium_checks(mod: object) -> None:
    got = mod.group_anagrams(["eat", "tea", "tan", "ate", "nat", "bat"])
    exp = _norm_groups([["bat"], ["nat", "tan"], ["ate", "eat", "tea"]])
    assert _norm_groups(got) == exp

    assert mod.product_except_self([1, 2, 3, 4]) == [24, 12, 8, 6]

    assert mod.longest_unique_substring("abcabcbb") == 3
    assert mod.longest_unique_substring("bbbbbb") == 1

    tf = mod.top_k_frequent([1, 1, 1, 2, 2, 3], 2)
    assert sorted(tf) == sorted([1, 2])

    assert mod.search_in_rotated_sorted([4, 5, 6, 7, 0, 1, 2], 0) == 4
    assert mod.search_in_rotated_sorted([4, 5, 6, 7, 0, 1, 2], 3) == -1

    assert mod.coin_change_min_coins([1, 2, 5], 11) == 3
    assert mod.coin_change_min_coins([2], 3) == -1
