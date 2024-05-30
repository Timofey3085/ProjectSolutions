"""
Two red beads are placed between every two blue beads.
There are N blue beads. After looking at the arrangement below work out the number of red beads.

Implement count_red_beads(n) (in PHP count_red_beads($n);
in Java, Javascript, TypeScript, C, C++ countRedBeads(n)) so that it returns the number of red beads.
If there are less than 2 blue beads return 0.
"""
import unittest

import pytest


def count_red_beads(n):
    """MySolution"""
    if n <= 1:
        return 0
    if n > 1:
        return n * 2 - 2


def test_count_red_beads():
    """PyTest"""
    assert count_red_beads(1) == 0
    assert count_red_beads(3) == 4


class CountRedBeards(unittest.TestCase):

    def test_count_red_beads(self):
        """UnitTest"""
        self.assertEqual(count_red_beads(5), 8)
        self.assertEqual(count_red_beads(6), 10)


if __name__ == '__main__':
    pytest.main()
