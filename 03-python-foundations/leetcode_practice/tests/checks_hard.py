"""Shared assertions for hard-tier functions."""

from __future__ import annotations


def run_all_hard_checks(mod: object) -> None:
    assert mod.trap_rain_water([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]) == 6

    assert mod.word_break("leetcode", ["leet", "code"]) is True
    assert mod.word_break("catsandog", ["cats", "dog", "sand", "and", "cat"]) is False

    merged = mod.merge_k_sorted_lists([[1, 4, 5], [1, 3, 4], [2, 6]])
    assert merged == [1, 1, 2, 3, 4, 4, 5, 6]
