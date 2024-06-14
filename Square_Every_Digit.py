"""
Welcome. In this kata, you are asked to square every digit of a number and concatenate them.
For example, if we run 9119 through the function, 811181 will come out, because 92 is 81 and 12 is 1. (81-1-1-81)
Example #2: An input of 765 will/should return 493625 because 72 is 49, 62 is 36, and 52 is 25. (49-36-25)
Note: The function accepts an integer and returns an integer.
Happy Coding!
"""
import unittest

import pytest


def square_digits(num):
    """MySolution"""
    res = []
    k = [int(i)**2 for i in str(num)]
    j = "".join(str(d) for d in k)
    res.append(j)
    for s in res:
        return int(s)


def test_square_digits():
    """Pytest"""
    assert square_digits(9119) == 811181
    assert square_digits(0) == 0


class SquareDigits(unittest.TestCase):

    def test_square_digits(self):
        """Unittest"""
        self.assertEqual(square_digits(1), 1)
        self.assertEqual(square_digits(555), 252525)


if __name__ == '__main__':
    pytest.main()
    unittest.main()


