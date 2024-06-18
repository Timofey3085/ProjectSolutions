"""
Your task in this kata is to implement a function that calculates the sum of the integers inside a string.
For example, in the string "The30quick20brown10f0x1203jumps914ov3r1349the102l4zy dog", the sum of the integers is 3635.
Note: only positive integers will be tested.
"""
import re
import unittest

import pytest


def sum_of_integers_in_string(s):
    """MuSolution"""
    integer = re.findall(r'\d+', s)
    result = list(map(int, integer))
    return sum(result)


def test_sum_of_integers_in_string():
    """Pytest"""
    assert sum_of_integers_in_string("12.4") == 16
    assert sum_of_integers_in_string("h3ll0w0rld") == 3
    assert sum_of_integers_in_string("2 + 3 = ") == 5


class SumOfIntegersInString(unittest.TestCase):

    def test_sum_of_integers_in_string(self):
        """Unittest"""
        self.assertEqual(sum_of_integers_in_string("The Great Depression lasted from 1929 to 1939."), 3868)
        self.assertEqual(sum_of_integers_in_string("Dogs are our best friends."), 0)
        self.assertEqual(sum_of_integers_in_string("C4t5 are 4m4z1ng."), 18)


if __name__ == '__main__':
    pytest.main()
    unittest.main()
