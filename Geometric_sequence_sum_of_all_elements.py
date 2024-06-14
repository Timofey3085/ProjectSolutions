"""
A geometric sequence is a sequence of numbers that scale by a common ratio,
usually denoted as r. To get the next term,
multiply the current term by this value. The first term is provided for this kata.

For example, the first 4 terms of the geometric sequence with first term 2 and ratio 3 is 2, 6, 18, 54.
Notice that, given any term, it is 3 times larger than the last term for this case.

A geometric series is just the first n terms of the sequence summed together.
As an example, the sum of the first 4 terms of the example provided above is 90.

Write a function geometric_sequence_sum(a, r, n), which will help you compute a geometric progression/series.

The parameters provided are as follows:

'a' is the first term
'r' is the common ratio
'n' is the amount of terms

Example:
geometric_sequence_sum(2, 3, 5) should return 242.
"""
import unittest

import pytest


def geometric_sequence_sum(a, r, n):
    """MySolution"""
    return sum([a * r ** (i - 1) for i in range(1, n + 1)])


def test_geometric_sequence_sum():
    """Pytest"""
    assert geometric_sequence_sum(2, 3, 5) == 242
    assert geometric_sequence_sum(1, 1, 2) == 2
    assert geometric_sequence_sum(2, 2, 10) == 2046


class GeometricSequenceSum(unittest.TestCase):

    def test_geometric_sequence_sum(self):
        """Unittest"""
        self.assertEqual(geometric_sequence_sum(1, -2, 10), -341)
        self.assertEqual(geometric_sequence_sum(1, 0.5, 10), 1.998046875)


if __name__ == '__main__':
    pytest.main()
    unittest.main()
