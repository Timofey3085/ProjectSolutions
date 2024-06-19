"""
An anagram is the result of rearranging the letters of a word to produce a new word (see wikipedia).
Note: anagrams are case-insensitive
Complete the function to return true if the two arguments given are anagrams of each other; return false otherwise.
Examples
"foefet" is an anagram of "toffee"
"Buckethead" is an anagram of "DeathCubeK"
"""
import unittest
from collections import Counter

import pytest


def is_anagram(test, original):
    """My_Solution"""
    return True if Counter(test.lower()) == Counter(original.lower()) else False


def test_is_anagram():
    """Pytest"""
    assert is_anagram("foefet", "toffee") is True
    assert is_anagram("Buckethead", "DeathCubeK") is True
    assert is_anagram("Twoo", "WooT") is True


class IsAnagram(unittest.TestCase):

    def test_is_anagram(self):
        """Unittest"""
        self.assertEqual(is_anagram("dumble", "bumble"), False)
        self.assertEqual(is_anagram("ound", "round"), False)
        self.assertEqual(is_anagram("apple", "pale"), False)


if __name__ == '__main__':
    pytest.main()
    unittest.main()
    help(is_anagram)



