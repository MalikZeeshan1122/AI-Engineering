"""Run checks against student stubs (`problems/`)."""

from __future__ import annotations

import unittest

from leetcode_practice.problems import easy as easy_stub
from leetcode_practice.tests.checks_easy import run_all_easy_checks


class TestEasyStudent(unittest.TestCase):
    def test_all(self) -> None:
        run_all_easy_checks(easy_stub)
