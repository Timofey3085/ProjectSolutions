"""
You need to count the number of digits in a given string.
"""
import unittest

import pytest


def count_digits(text: str) -> int:
    """My_solution"""
    text = "".join(text.split())
    count = 0
    for i in text:
        if i.isdigit():
            count += 1
    return count


def test_count_digits():
    """Pytest"""
    assert count_digits("hi") == 0
    assert count_digits("who is 1st here") == 1
    assert count_digits("5 plus 6 is") == 2


class CountDigits(unittest.TestCase):

    def test_count_digits(self):
        """Unittest"""
        self.assertEqual(count_digits("my numbers is 2"), 1)
        self.assertEqual(count_digits("your2 numbers is 2"), 2)
        self.assertEqual(count_digits(""), 0)


if __name__ == '__main__':
    pytest.main()
    unittest.main()
