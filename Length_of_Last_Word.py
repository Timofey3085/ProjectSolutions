"""
Given a string s consisting of words and spaces, return the length of the last word in the string.

A word is a maximal
substring
 consisting of non-space characters only.

 Example 1:

Input: s = "Hello World"
Output: 5
Explanation: The last word is "World" with length 5.
Example 2:

Input: s = "   fly me   to   the moon  "
Output: 4
Explanation: The last word is "moon" with length 4.
Example 3:

Input: s = "luffy is still joyboy"
Output: 6
Explanation: The last word is "joyboy" with length 6.
"""
import unittest

import pytest


def length_of_last_word(s):
    """My_solution"""
    return len(s.split().pop())
    # Or another Solution
    # return len(s.split()[-1])


def test_length_of_last_word():
    """Pytest"""
    assert length_of_last_word("Hello World") == 5
    assert length_of_last_word("Hello my little World") == 5
    assert length_of_last_word("H W") == 1


class LengthOfLastWord(unittest.TestCase):

    def test_length_of_last_word(self):
        """Unittest"""
        assert length_of_last_word("   fly me   to   the moon  "), 4
        assert length_of_last_word("luffy is still joyboy"), 6
        assert length_of_last_word("One"), 3


if __name__ == '__main__':
    pytest.main()
    unittest.main()
