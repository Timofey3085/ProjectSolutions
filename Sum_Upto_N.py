"""
Calculate sum of integers from 1 to given N (including).
Examples:
assert sum_upto_n(1) == 1
assert sum_upto_n(2) == 3
assert sum_upto_n(3) == 6
assert sum_upto_n(4) == 10
"""
import unittest

import pytest


def sum_upto_n(n: int) -> int:
    """MySolution"""
    return sum([i for i in range(n + 1)])


def test_sum_upto_n():
    """Pytest"""
    assert sum_upto_n(1) == 1
    assert sum_upto_n(2) == 3
    assert sum_upto_n(3) == 6


class SumUpToN(unittest.TestCase):

    def test_test_sum_upto_n(self):
        """Unittest"""
        self.assertEqual(sum_upto_n(4), 10)
        self.assertEqual(sum_upto_n(5), 15)
        self.assertEqual(sum_upto_n(10), 55)


if __name__ == '__main__':
    pytest.main()
    unittest.main()
