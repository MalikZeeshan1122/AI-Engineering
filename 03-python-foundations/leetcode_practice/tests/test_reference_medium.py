"""Sanity-check reference implementations — medium."""

from __future__ import annotations

import unittest

from leetcode_practice.solutions import medium as medium_sol
from leetcode_practice.tests.checks_medium import run_all_medium_checks


class TestMediumReference(unittest.TestCase):
    def test_all(self) -> None:
        run_all_medium_checks(medium_sol)
