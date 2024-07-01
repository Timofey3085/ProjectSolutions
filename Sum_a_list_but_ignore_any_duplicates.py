"""
Please write a function that sums a list, but ignores any duplicate items in the list.
For instance, for the list [3, 4, 3, 6] , the function should return 10
and for the list [1, 10, 3, 10, 10] , the function should return 4.
"""
import unittest

import pytest


def sum_no_duplicates(l):
    """My_solution"""
    res = []
    for num in l:
        if l.count(num) == 1:
            res.append(num)
    return sum(res)


def test_sum_no_duplicates():
    """Pytest"""
    assert sum_no_duplicates([1, 2, 3, 1]) == 5
    assert sum_no_duplicates([1, 1, 2, 2, 3]) == 3


def test_if_empy():
    """Pytest"""
    assert sum_no_duplicates([]) == 0


class SumNoDuplicates(unittest.TestCase):

    def test_sum_no_duplicates(self):
        """Unittest"""
        self.assertEqual(sum_no_duplicates([5, 6, 10, 3, 10, 10, 6, 7, 0, 9, 1, 1, 6, 3, 1]), 21)
        self.assertEqual(sum_no_duplicates([0, 10, 8, 9, 7, 3, 3, 9, 3, 6, 0]), 31)
        self.assertEqual(sum_no_duplicates([7, 9, 5, 6, 1, 0, 5, 0, 4, 7, 1, 2, 8, 9, 6, 1]), 14)


if __name__ == '__main__':
    pytest.main()
    unittest.main()


