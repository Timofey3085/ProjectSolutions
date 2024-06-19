"""
Write a method that will search an array of strings for all strings
that contain another string, ignoring capitalization.
Then return an array of the found strings.

The method takes two parameters,
the query string and the array of strings to search, and returns an array.

If the string isn't contained in any of the strings in the array,
the method returns an array containing a single string: "Empty" (or Nothing in Haskell, or "None" in Python and C)

Examples
If the string to search for is "me", and the array to search is ["home", "milk", "Mercury", "fish"],
the method should return ["home", "Mercury"].
"""
import unittest

import pytest


def word_search(query, seq):
    """My_solution"""
    query = query.lower()
    result = [i for i in seq if query in i.lower()]

    return result if result else ["None"]


def test_word_search():
    """Pytest"""
    assert word_search("ab", ["za", "ab", "abc", "zab", "zbc"]) == ["ab", "abc", "zab"]
    assert word_search("aB", ["za", "ab", "abc", "zab", "zbc"]) == ["ab", "abc", "zab"]


class WordSearch(unittest.TestCase):

    def test_word_search(self):
        """Unittest"""
        self.assertEqual(word_search("ab", ["za", "aB", "Abc", "zAB", "zbc"]), ["aB", "Abc", "zAB"])
        self.assertEqual(word_search("abcd", ["za", "aB", "Abc", "zAB", "zbc"]), ["None"])


if __name__ == '__main__':
    pytest.main()
    unittest.main()
