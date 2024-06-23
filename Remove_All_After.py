"""
Not all of the elements are important.
What you need to do here is to remove all of the elements after the given one from sequence.

example:
For illustration, we have a sequence [1, 2, 3, 4, 5]
and we need to remove all the elements that go after 3 - which are 4 and 5.

We have two edge cases here:
if a cutting element cannot be found, then the sequence shouldn't be changed;
if the sequence is empty, then it should remains empty.
"""
import unittest
from collections.abc import Iterable

import pytest


def remove_all_after(items: list[int], border: int) -> Iterable[int]:
    """My_solution"""
    res = []
    for i in items:
        res.append(i)
        if i == border:
            break
    return res


def test_remove_all_after():
    """Pytest"""
    assert remove_all_after([1, 2, 3, 4, 5], 3) == [1, 2, 3]
    assert remove_all_after([1, 1, 2, 2, 3, 3], 2) == [1, 1, 2]
    assert remove_all_after([1, 1, 2, 4, 2, 3, 4], 2) == [1, 1, 2]


class RemoveAllAfter(unittest.TestCase):

    def test_remove_all_after(self):
        """Unittest"""
        self.assertEqual(remove_all_after([1, 1, 5, 6, 7], 2), [1, 1, 5, 6, 7])
        self.assertEqual(remove_all_after([], 0), [])
        self.assertEqual(remove_all_after([7, 7, 7, 7, 7, 7, 7, 7, 7], 7), [7])


if __name__ == '__main__':
    pytest.main()
    unittest.main()
