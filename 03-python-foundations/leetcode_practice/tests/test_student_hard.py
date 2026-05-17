"""Run checks against student stubs — hard."""

from __future__ import annotations

import unittest

from leetcode_practice.problems import hard as hard_stub
from leetcode_practice.tests.checks_hard import run_all_hard_checks


class TestHardStudent(unittest.TestCase):
    def test_all(self) -> None:
        run_all_hard_checks(hard_stub)
