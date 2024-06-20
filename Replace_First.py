"""
In a given sequence the first element should become the last one.
An empty sequence or with only one element should stay the same.
"""
import unittest
from collections.abc import Iterable

import pytest


def replace_first(items: list) -> Iterable:
    """My_solution"""
    if items:
        items.append(items.pop(0))
    return items


def test_replace_first():
    """Pytest"""
    assert replace_first([1, 2, 3, 4]) == [2, 3, 4, 1]
    assert replace_first([1, 5, 5, 5]) == [5, 5, 5, 1]


class ReplaceFirst(unittest.TestCase):

    def test_replace_first(self):
        """Unittest"""
        self.assertEqual(replace_first([1]), [1])
        self.assertEqual(replace_first([]), [])


if __name__ == '__main__':
    pytest.main()
    unittest.main()
