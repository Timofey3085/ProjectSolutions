"""
Find the difference between two collections.
The difference means that either the character is present in one collection or it is present in other, but not in both.
Return a sorted list with the difference.

The collections can contain any character and can contain duplicates.
Example
A = [a, a, t, e, f, i, j]
B = [t, g, g, i, k, f]
difference = [a, e, g, j, k]
"""
import unittest

import pytest


def diff(a, b):
    """My_solution"""
    a = set(a)
    b = set(b)
    return sorted((a - b) | (b - a))


def test_diff():
    """Pytest"""
    assert diff(['a', 'b', 'z', 'd', 'e', 'd'], ['a', 'b', 'j', 'j']) == ['d', 'e', 'j', 'z']
    assert diff(['a', 'b'], ['a', 'b']) == []


class Diff(unittest.TestCase):

    def test_diff(self):
        """Unittest"""
        self.assertEqual(diff(['a', 'b', 'z'], ['a', 'b']), ['z'])
        self.assertEqual(diff([], ['a', 'b']), ['a', 'b'])

    def test_empy(self):
        """Unittest"""
        self.assertEqual(diff([], []), [])


if __name__ == '__main__':
    pytest.main()
    unittest.main()


