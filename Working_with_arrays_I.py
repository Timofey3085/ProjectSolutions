"""
In this kata the function returns an array/list of numbers without its last element.
The function is already written for you and the basic tests pass,
but random tests fail. Your task is to figure out why and fix it.
Good luck!
Hint: watch out for side effects.
"""
import unittest

import pytest


def without_last(lst):
    """MySolution"""
    lst = lst[:-1]
    return lst


def test_without_last():
    """Pytest"""
    assert without_last([1, 2, 3, 4, 5]) == [1, 2, 3, 4]


class Withoutlast(unittest.TestCase):

    def test_without_last(self):
        """UnitTest"""
        self.assertEqual(without_last([9, 7, 6, 9]), [9, 7, 6])


if __name__ == '__main__':
    pytest.main()
    unittest.main()
