"""
Write a function, isItLetter or is_it_letter or IsItLetter,
which tells us if a given character is a letter or not.
"""
import unittest

import pytest


def is_it_letter(s):
    """My_Solution"""
    return True if s.isalpha() else False


def test_is_it_letter():
    """PyTest"""
    assert is_it_letter("a") == True
    assert is_it_letter("/") == False


class IsItLetter(unittest.TestCase):

    def test_is_it_letter(self):
        """Unittest"""
        self.assertEqual(is_it_letter("B"), True)
        self.assertEqual(is_it_letter("8"), False)


if __name__ == '__main__':
    pytest.main()
    unittest.main()


