"""
"Sometimes, zeros resemble very tasty donut.
And every time we finish a donut, we want another, and then another, and then another..."

You are given list of integers (int).
Your task in this mission is to duplicate (..., 🍩, ... --> ..., 🍩, 🍩, ...) all zeros (think about donuts ;-P)
and return the result as any Iterable. Let's look on the example:
1. [0, 0, 0, 0] == [0, 0, 0, 0, 0, 0, 0, 0]
2. [100, 10, 0, 101, 1000] == [100, 10, 0, 0, 101, 1000]
"""
import unittest
from collections.abc import Iterable

import pytest


def duplicate_zeros(donuts: list[int]) -> Iterable[int]:
    """MySolution"""
    res = []
    for i in donuts:
        res.append(i)
        if i == 0:
            res.append(i * 2)
    return res


def test_duplicate_zeros():
    """Pytest"""
    assert duplicate_zeros([0, 0, 0, 0]) == [0, 0, 0, 0, 0, 0, 0, 0]
    assert duplicate_zeros([1, 2, 3, 0]) == [1, 2, 3, 0, 0]
    assert duplicate_zeros([1, 2, 3, 4]) == [1, 2, 3, 4]


class DuplicateZeros(unittest.TestCase):

    def test_duplicate_zeros(self):
        """Unittest"""
        self.assertEqual(duplicate_zeros([100, 10, 0, 101, 1000]), [100, 10, 0, 0, 101, 1000])
        self.assertEqual(duplicate_zeros([100, 10, 1, 101, 1000]), [100, 10, 1, 101, 1000])
        self.assertEqual(duplicate_zeros([1, 0, 0]), [1, 0, 0, 0, 0])


if __name__ == '__main__':
    pytest.main()
    unittest.main()
