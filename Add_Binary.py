"""
Given two binary strings a and b, return their sum as a binary string.
Example 1:

Input: a = "11", b = "1"
Output: "100"
Example 2:

Input: a = "1010", b = "1011"
Output: "10101"
"""
import unittest

import pytest


def add_binary(a, b):
    """My_solution"""
    decimal_number = int(a, 2)
    decimal_number_2 = int(b, 2)
    sum_of_digits = decimal_number + decimal_number_2
    binary_from_decimal = bin(sum_of_digits)[2:]

    return binary_from_decimal


def test_add_binary():
    """Pytest"""
    assert add_binary("11", "1") == "100"


class AddBinary(unittest.TestCase):

    def test_add_binary(self):
        """Unittest"""
        self.assertEqual(add_binary("1010", "1011"), "10101")


if __name__ == '__main__':
    pytest.main()
    unittest.main()
