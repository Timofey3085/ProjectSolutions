"""
Given three integers, determine which one is the largest.
Examples:
(1, 2, 3) == 3
(3, 2, 1) == 3
(-1, -3, -2) == -1
(0, 0, 0) == 0
"""
import unittest

import pytest


def max_of_three(a: int, b: int, c: int) -> int:
    """MySolution"""
    return max(a, b, c)


def test_max_of_three():
    """Pytest"""
    assert max_of_three(1, 2, 3) == 3
    assert max_of_three(4, 5, 6) == 6
    assert max_of_three(-1, -2, -3) == -1


class MaxOfThree(unittest.TestCase):

    def test_max_of_three(self):
        """UnitTest"""
        self.assertEqual(max_of_three(7, 8, 9), 9)
        self.assertEqual(max_of_three(-7, -8, -9), -7)
        self.assertEqual(max_of_three(-7, 8, 1), 8)


if __name__ == '__main__':
    pytest.main()
    unittest.main()
