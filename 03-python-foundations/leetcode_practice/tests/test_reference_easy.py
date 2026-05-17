"""Sanity-check reference implementations (`solutions/`)."""

from __future__ import annotations

import unittest

from leetcode_practice.solutions import easy as easy_sol
from leetcode_practice.tests.checks_easy import run_all_easy_checks


class TestEasyReference(unittest.TestCase):
    def test_all(self) -> None:
        run_all_easy_checks(easy_sol)
