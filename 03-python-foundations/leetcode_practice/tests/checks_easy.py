"""Shared assertions for easy-tier functions."""

from __future__ import annotations


def run_all_easy_checks(mod: object) -> None:
    two_sum = mod.two_sum
    idx = sorted(two_sum([2, 7, 11, 15], 9))
    assert idx == [0, 1], idx
    idx = sorted(two_sum([3, 3], 6))
    assert idx == [0, 1], idx

    vp = mod.is_valid_parentheses
    assert vp("") is True
    assert vp("()") is True
    assert vp("(]") is False
    assert vp("([{}])") is True

    assert mod.merge_sorted_lists([1, 3, 5], [2, 4, 6]) == [1, 2, 3, 4, 5, 6]

    assert mod.max_subarray_sum([-2, 1, -3, 4, -1, 2, 1, -5, 4]) == 6

    assert mod.max_profit_one_transaction([7, 1, 5, 3, 6, 4]) == 5
    assert mod.max_profit_one_transaction([7, 6, 4, 3, 1]) == 0

    assert mod.contains_duplicate([1, 2, 3, 1]) is True
    assert mod.contains_duplicate([1, 2, 3]) is False

    assert mod.is_anagram("anagram", "nagaram") is True
    assert mod.is_anagram("rat", "car") is False

    assert mod.binary_search([-1, 0, 3, 5, 9, 12], 9) == 4
    assert mod.binary_search([-1, 0, 3, 5, 9, 12], 2) == -1

    assert mod.single_number_xor([4, 1, 2, 1, 2]) == 4

    assert mod.climb_stairs(5) == 8
