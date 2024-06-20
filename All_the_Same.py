"""
In this task you should check if all elements in the given sequence are equal.
"""
import unittest
from typing import List, Any

import pytest


def all_the_same(elements: List[Any]) -> bool:
    """My_solution"""
    if len(set(elements)) == 1:
        return True
    if not elements:
        return True
    else:
        return False


def test_all_the_same():
    """Pytest"""
    assert all_the_same([1, 1, 1]) is True
    assert all_the_same([1, 2, 1]) is False
    assert all_the_same([1, "a", 1]) is False


class AllTheSame(unittest.TestCase):

    def test_all_the_same(self):
        """Unittest"""
        self.assertEqual(all_the_same([1, 1, 1, 2]), False)
        self.assertEqual(all_the_same([]), True)
        self.assertEqual(all_the_same([1]), True)


if __name__ == '__main__':
    pytest.main()
    unittest.main()

