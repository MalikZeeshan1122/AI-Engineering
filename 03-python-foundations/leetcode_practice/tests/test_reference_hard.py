"""Sanity-check reference implementations — hard."""

from __future__ import annotations

import unittest

from leetcode_practice.solutions import hard as hard_sol
from leetcode_practice.tests.checks_hard import run_all_hard_checks


class TestHardReference(unittest.TestCase):
    def test_all(self) -> None:
        run_all_hard_checks(hard_sol)
