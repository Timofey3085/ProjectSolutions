"""
Find the difference between the sum of the squares of the first n natural numbers (1 <= n <= 100)
and the square of their sum.
Example
For example, when n = 10:
The square of the sum of the numbers is:
(1 + 2 + 3 + 4 + 5 + 6 + 7 + 8 + 9 + 10)2 = 552 = 3025
The sum of the squares of the numbers is:
12 + 22 + 32 + 42 + 52 + 62 + 72 + 82 + 92 + 102 = 385
Hence, the difference between square of the sum of the first ten natural numbers
and the sum of the squares of those numbs is: 3025 - 385 = 2640
"""
import unittest

import pytest


def difference_of_squares(n):
    """My_Solution"""
    return (sum([i for i in range(n + 1)]) ** 2) - sum([k ** 2 for k in range(n + 1)])


def test_difference_of_squares():
    """PyTest"""
    assert difference_of_squares(5) == 170
    assert difference_of_squares(10) == 2640


class DifferenceOfSquares(unittest.TestCase):

    def test_difference_of_squares(self):
        """UnitTest"""
        self.assertEqual(difference_of_squares(100), 25164150)
        self.assertEqual(difference_of_squares(57), 2669044)


if __name__ == '__main__':
    pytest.main()
    unittest.main()

