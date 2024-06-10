"""
Write a function that will take a key of X and place it in the middle of Y repeated N times.
Extra challege (not tested): You can complete this with under 70 characters without using regex.
Challenge yourself to do this. It won't be best practices, but it will work.

Rules:
If X cannot be placed in the middle, return X.
N will always be > 0.
Example:
X = 'A';
Y = '*';
N = 10;
Y repeated N times = '**********';
X in the middle of Y repeated N times = '*****A*****';
"""
import unittest

import pytest


def middle_me(N, X, Y):
    """MySolution"""
    if N % 2 != 0:
        return X
    else:
        return f'{Y * (N // 2)}{X}{Y * (N // 2)}'


def test_middle_me():
    """Pytest"""
    assert middle_me(18, 'z', '#') == '#########z#########'
    assert middle_me(20, 'a', '#') == '##########a##########'


class MiddleMe(unittest.TestCase):

    def test_middle_me(self):
        """Unittest"""
        self.assertEqual(middle_me(19, 'z', '#'), 'z')
        self.assertEqual(middle_me(1, 's', '#'), 's')


if __name__ == '__main__':
    pytest.main()
    unittest.main()
