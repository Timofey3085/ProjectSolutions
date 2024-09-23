"""
The main idea is to count all the occurring characters in a string.
If you have a string like aba, then the result should be {'a': 2, 'b': 1}.
What if the string is empty? Then the result should be empty object literal, {}.
"""

import collections
import unittest


def count(s):
    """My_solution"""
    result = collections.Counter(s)
    return result


class Count(unittest.TestCase):

    def test_count(self):
        self.assertEqual(count('aba'), {'a': 2, 'b': 1})

    def test_nothing(self):
        self.assertEqual(count(''), {})

    def test_double(self):
        self.assertEqual(count('aa'), {'a': 2})

    def test_random(self):
        self.assertEqual(count('aabbcdddee'), {'a': 2, 'b': 2, 'c': 1, 'd': 3, 'e': 2})


if __name__ == '__main__':
    unittest.main()

