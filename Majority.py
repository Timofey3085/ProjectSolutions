"""
We have a list of logic values (bool). Let's check if the majority of elements are True.

Some cases worth mentioning:
1) an empty list should return False;
2) if True-s and False-s have an equal amount, function should return False.
"""
import unittest

import pytest


def is_majority(items: list[bool]) -> bool:
    """MySolution"""
    count_true = 0
    count_false = 0

    for item in items:
        if item:
            count_true += 1
        else:
            count_false += 1

    return count_true > count_false


def test_is_majority():
    """Pytest"""
    assert is_majority([True, True, False, True, False]) is True
    assert is_majority([True, True, False]) is True
    assert is_majority([True, True, False, False]) is False


class IsMajority(unittest.TestCase):

    def test_is_majority(self):
        """Unittest"""
        self.assertEqual(is_majority([True, True, False, False, False]), False)
        self.assertEqual(is_majority([False]), False)
        self.assertEqual(is_majority([True]), True)
        self.assertEqual(is_majority([]), False)


if __name__ == '__main__':
    pytest.main()
    unittest.main()
