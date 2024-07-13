"""
Task
Given a string str, reverse it and omit all non-alphabetic characters.
Example
For str = "krishan", the output should be "nahsirk".
For str = "ultr53o?n", the output should be "nortlu".
Input/Output
[input] string str
A string consists of lowercase latin letters, digits and symbols.
[output] a string
"""
import unittest

import pytest


def reverse_letter(st):
    """My_solution"""
    res = []
    for i in st:
        if i.isalpha():
            res.append(i)
    return "".join(res)[::-1]


def test_reverse_letter():
    """Pytest"""
    assert reverse_letter("krishan") == "nahsirk"
    assert reverse_letter("ultr53o?n") == "nortlu"


class ReverseLetter(unittest.TestCase):

    def test_reverse_letter(self):
        """Unittest"""
        self.assertEqual(reverse_letter("ab23c"), "cba")
        self.assertEqual(reverse_letter("krish21an"), "nahsirk")


if __name__ == '__main__':
    pytest.main()
    unittest.main()

