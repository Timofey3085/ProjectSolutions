"""
Given a mixed array of number and string representations of integers,
add up the non-string integers and subtract the total of the string integers.

Return as a number.
"""
import unittest

import pytest


def div_con(x):
    """MySolution"""
    ints = sum([elem for elem in x if int == type(elem)])
    lst = [string for string in x if str == type(string)]
    k = sum([int(i) for i in lst])
    return ints - k


def test_div_con():
    """PyTest"""
    assert div_con([9, 3, '7', '3']) == 2
    assert div_con(['5', '0', 9, 3, 2, 1, '9', 6, 7]) == 14
    assert div_con(['3', 6, 6, 0, '5', 8, 5, '6', 2,'0']) == 13


class DivCon(unittest.TestCase):

    def test_div_con(self):
        """UnitTest"""
        self.assertEqual(div_con(['1', '5', '8', 8, 9, 9, 2, '3']), 11)
        self.assertEqual(div_con([8, 0, 0, 8, 5, 7, 2, 3, 7, 8, 6, 7]), 61)


if __name__ == '__main__':
    pytest.main()
    unittest.main()
