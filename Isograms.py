"""
An isogram is a word that has no repeating letters, consecutive or non-consecutive.
Implement a function that determines whether a string that contains only letters is an isogram.
Assume the empty string is an isogram. Ignore letter case.

Example: (Input --> Output)
"Dermatoglyphics" --> true
"aba" --> false
"moOse" --> false (ignore letter case)
"""
import unittest

import pytest


def is_isogram(string):
    """MySolution"""
    string = string.lower()
    return len(set(string)) == len(string)


def test_is_isogram():
    """Pytest"""
    assert is_isogram("Dermatoglyphics") is True
    assert is_isogram("isogram") is True
    assert is_isogram("aba") is False


class IsIsogram(unittest.TestCase):

    def test_is_isogram(self):
        """Unittest"""
        self.assertEqual(is_isogram("moOse"), False)
        self.assertEqual(is_isogram("isIsogram"), False)
        self.assertEqual(is_isogram(""), True)


if __name__ == '__main__':
    pytest.main()
    unittest.main()

