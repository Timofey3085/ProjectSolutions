"""
You are going to be given a word.
Your job is to return the middle character of the word.
If the word's length is odd, return the middle character.
If the word's length is even, return the middle 2 characters.

#Examples:
Kata.getMiddle("test") should return "es"
Kata.getMiddle("testing") should return "t"
Kata.getMiddle("middle") should return "dd"
Kata.getMiddle("A") should return "A"
#Input
A word (string) of length 0 < str < 1000
(In javascript you may get slightly more than 1000 in some test cases due to an error in the test cases).
You do not need to test for this.
This is only here to tell you that you do not need to worry about your solution timing out.

#Output
The middle character(s) of the word represented as a string.
"""
import unittest

import pytest


def get_middle(s):
    """My_solution"""
    if len(s) % 2 == 1:
        mid = len(s) // 2
        return s[mid]
    else:
        mid = len(s) // 2
        return s[mid - 1: mid + 1]


def test_get_middle():
    """Pytest"""
    assert get_middle("test") == "es"
    assert get_middle("apple") == "p"
    assert get_middle("Python") == "th"


class GetMiddle(unittest.TestCase):

    def test_get_middle(self):
        """Unittest"""
        self.assertEqual(get_middle("name"), "am")
        self.assertEqual(get_middle("password"), "sw")
        self.assertEqual(get_middle("sun"), "u")


if __name__ == '__main__':
    pytest.main()
    unittest.main()
