"""
You are given a positive number. Your function should calculate the product of the digits excluding any zeroes.
For example: The number given is 123405. The result will be 1*2*3*4*5=120 (don't forget to exclude zeroes).
"""
import unittest

import pytest


def digits(number: int) -> int:
    """My_Solution"""
    n = 1
    num = str(number).replace('0', '')
    for i in num:
        n *= int(i)
    return n


def test_digits():
    """Pytest"""
    assert digits(123405) == 120
    assert digits(999) == 729


class Digits(unittest.TestCase):

    def test_digits(self):
        """Unittest"""
        self.assertEqual(digits(1000), 1)
        self.assertEqual(digits(1111), 1)


if __name__ == '__main__':
    pytest.main()
    unittest.main()
