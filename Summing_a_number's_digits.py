"""
Write a function named sumDigits which takes a number as input
and returns the sum of the absolute value of each of the number's decimal digits.

For example: (Input --> Output)
10 --> 1
99 --> 18
-32 --> 5
Let's assume that all numbers in the input will be integer values.
"""
import unittest

import pytest


def sum_digits(number: int) -> int:
    """My_solution"""
    sum_d = sum([int(i) for i in str(abs(number))])
    return sum_d


@pytest.mark.parametrize("numbers, sum_d", [
    (10, 1),
    (99, 18),
    (101, 2),
    (-32, 5),
    (123456789, 45),
    (1, 1),
    (555, 15),
    (646464, 30),
    (11111, 5),
    (0, 0),
])
def test_sum_digits(numbers: int, sum_d: int):
    """Pytest"""
    assert sum_digits(numbers) == sum_d


class SumDigits(unittest.TestCase):

    def test_sum_digits(self):
        """Unittest"""
        self.assertEqual(sum_digits(999), 27)
        self.assertEqual(sum_digits(751), 13)
        self.assertEqual(sum_digits(-66), 12)


if __name__ == '__main__':
    pytest.main()
    unittest.main()
