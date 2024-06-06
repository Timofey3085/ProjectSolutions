"""
Given an array of numbers,
return a new array of length number containing the last even numbers from the original array (in the same order).
The original array will be not empty and will contain at least "number" even numbers.
For example:
([1, 2, 3, 4, 5, 6, 7, 8, 9], 3) => [4, 6, 8]
([-22, 5, 3, 11, 26, -6, -7, -8, -9, -8, 26], 2) => [-8, 26]
([6, -25, 3, 7, 5, 5, 7, -3, 23], 1) => [6]
"""
import unittest

import pytest


def even_numbers(arr, n):
    """MySolution"""
    res = []
    for i in arr:
        if i % 2 == 0:
            res.append(i)
    return res[-n:]


def test_even_numbers():
    """PyTest"""
    assert even_numbers([1, 2, 3, 4, 5, 6, 7, 8, 9], 3) == [4, 6, 8]
    assert even_numbers([1, 1, 1, 1, 16, 6, 7, 8, 9], 3) == [16, 6, 8]


class EvenNumbers(unittest.TestCase):

    def test_even_numbers(self):
        """Unittest"""
        self.assertEqual(even_numbers([-22, 5, 3, 11, 26, -6, -7, -8, -9, -8, 26], 2), [-8, 26])
        self.assertEqual(even_numbers([6, -25, 3, 7, 5, 5, 7, -3, 23], 1), [6])


if __name__ == '__main__':
    pytest.main()
    unittest.main()
