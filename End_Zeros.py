"""
Try to find out how many zeros a given number has at the end.
"""
import unittest

import pytest


def end_zeros(a):
    """MySolution"""
    count = 0
    b = str(a)
    b = b[::-1]
    for i in b:
        if i == '0':
            count += 1
        else:
            break
    return count


def test_end_zeros():
    """Pytest"""
    assert end_zeros(0) == 1
    assert end_zeros(1) == 0
    assert end_zeros(10) == 1
    assert end_zeros(1000) == 3


class EndZeros(unittest.TestCase):

    def test_end_zeros(self):
        """Unittest"""
        self.assertEqual(end_zeros(101), 0)
        self.assertEqual(end_zeros(245), 0)
        self.assertEqual(end_zeros(100100), 2)


if __name__ == '__main__':
    pytest.main()
    unittest.main()
