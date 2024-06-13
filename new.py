"""
A perfect number is a positive integer that is equal to the sum of its proper divisors, excluding itself.
For example, 28 is a perfect number because its divisors are 1, 2, 4, 7, and 14, and their sum is 28.
"""
import unittest

import pytest


def is_perfect(n: int) -> bool:
    """MySolution"""
    res = []
    for i in range(1, n):
        if n % i == 0:
            res.append(i)
    return sum(res) == n


def test_is_perfect():
    """Pytest"""
    assert is_perfect(6) is True
    assert is_perfect(2) is False
    assert is_perfect(28) is True
    assert is_perfect(20) is False


class IsPerfect(unittest.TestCase):

    def test_is_perfect(self):
        """Unittest"""
        self.assertEqual(is_perfect(496), True)
        self.assertEqual(is_perfect(30), False)
        self.assertEqual(is_perfect(8128), True)
        self.assertEqual(is_perfect(100), False)


if __name__ == '__main__':
    pytest.main()
    unittest.main()
