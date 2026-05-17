"""Run checks against student stubs — medium."""

from __future__ import annotations

import unittest

from leetcode_practice.problems import medium as medium_stub
from leetcode_practice.tests.checks_medium import run_all_medium_checks


class TestMediumStudent(unittest.TestCase):
    def test_all(self) -> None:
        run_all_medium_checks(medium_stub)
