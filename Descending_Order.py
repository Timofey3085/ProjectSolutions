"""
Your task is to make a function that can take any non-negative integer as an argument
and return it with its digits in descending order.
Essentially, rearrange the digits to create the highest possible number.

Examples:
Input: 42145 Output: 54421
Input: 145263 Output: 654321
Input: 123456789 Output: 987654321
"""
import unittest

import pytest


def descending_order(num):
    """My_solution"""
    return int("".join((sorted(" ".join(str(num)))[::-1])))


def test_descending_order():
    """Pytest"""
    assert descending_order(15) == 51
    assert descending_order(156) == 651


def test_descending_zero():
    """Pytest"""
    assert descending_order(0) == 0


class DescendingOrder(unittest.TestCase):

    def test_descending_order(self):
        """Unitest"""
        self.assertEqual(descending_order(123456789), 987654321)
        self.assertEqual(descending_order(11223344), 44332211)
        self.assertEqual(descending_order(13579), 97531)


if __name__ == '__main__':
    pytest.main()
    unittest.main()
