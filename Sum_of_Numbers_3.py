"""
Given two integers a and b, which can be positive or negative,
find the sum of all the integers between and including them and return it.
If the two numbers are equal return a or b.
Note: a and b are not ordered!
Examples (a, b) --> output (explanation)
(1, 0) --> 1 (1 + 0 = 1)
(1, 2) --> 3 (1 + 2 = 3)
(0, 1) --> 1 (0 + 1 = 1)
(1, 1) --> 1 (1 since both are same)
(-1, 0) --> -1 (-1 + 0 = -1)
(-1, 2) --> 2 (-1 + 0 + 1 + 2 = 2)
Your function should only return a number, not the explanation about how you get that number.
"""
import unittest

import pytest


def get_sum(a, b):
    """MySolution"""
    min_num = min(a, b)
    max_num = max(a, b)
    return sum(range(min_num, max_num + 1))


def test_get_sum():
    """Pytest"""
    assert get_sum(0, 1) == 1
    assert get_sum(0, -1) == -1
    assert get_sum(1, 2) == 3


class GetSum(unittest.TestCase):

    def test_get_sum(self):
        """Unittest"""
        self.assertEqual(get_sum(1, 1), 1)
        self.assertEqual(get_sum(-1, 2), 2)
        self.assertEqual(get_sum(-1, 3), 5)


if __name__ == '__main__':
    pytest.main()
    unittest.main()

