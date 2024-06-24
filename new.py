"""
The notorious Captain Schneider has given you a very straightforward mission.
Any data that comes through the system make sure that only non-special characters see the light of day.

Create a function that given a string, retains only the letters A-Z (upper and lowercase),
0-9 digits, and whitespace characters.
Also, returns "Not a string!" if the entry type is not a string.
"""
import unittest

import pytest


def nothing_special(st):
    """My_solution"""
    res = []
    if not isinstance(st, str):
        return "Not a string!"
    for i in st:
        if i.isalpha() or i.isspace() or i.isdigit():
            res.append(i)
    return "".join(res)


def test_nothing_special():
    """Pytest"""
    assert nothing_special("Hello World!") == "Hello World"
    assert nothing_special("%^Take le$ft ##quad%r&a&nt") == "Take left quadrant"


class NothingSpecial(unittest.TestCase):

    def test_nothing_special(self):
        """Unittest"""
        self.assertEqual(nothing_special("M$$$$$$$y ally!!!!!"), "My ally")
        self.assertEqual(nothing_special(25), "Not a string!")


if __name__ == '__main__':
    pytest.main()
    unittest.main()
