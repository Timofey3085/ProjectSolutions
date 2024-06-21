"""
Check to see if a string has the same amount of 'x's and 'o's.
The method must return a boolean and be case-insensitive.
The string can contain any char.

Examples input/output:
XO("ooxx") => true
XO("xooxx") => false
XO("ooxXm") => true
XO("zpzpzpp") => true // when no 'x' and 'o' is present should return true
XO("zzoo") => false
"""
import unittest

import pytest


def xo(s):
    """My_solution"""
    k = s.lower()
    count_x = 0
    count_o = 0
    for i in k:
        if "o" in i:
            count_o += 1
        if "x" in i:
            count_x += 1
    return count_x == count_o


def test_xo():
    """Pytest"""
    assert xo("ooxx") is True
    assert xo("xooxx") is False
    assert xo("ooxXm") is True


class XO(unittest.TestCase):

    def test_xo(self):
        """Unittest"""
        self.assertEqual(xo("zpzpzpp"), True)
        self.assertEqual(xo("zzoo"), False)
        self.assertEqual(xo("oxOx"), True)


if __name__ == '__main__':
    pytest.main()
    unittest.main()
