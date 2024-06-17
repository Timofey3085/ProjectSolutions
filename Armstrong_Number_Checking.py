"""
In number theory, an Armstrong number (after Michael F. Armstrong)
or narcissistic number in a given number base (10 for this mission)
is a number that is the sum of its own digits each raised to the power of the number of digits.
For example, 153 is an Armstrong number because 1**3 + 5**3 + 3**3 == 153.
"""
import unittest

import pytest


def is_armstrong(num: int) -> bool:
    """MySolution"""
    number = sum([int(item)**len(str(num)) for item in str(num)])
    if number == num:
        return True
    else:
        return False


def test_is_armstrong():
    """Pytest"""
    assert is_armstrong(153) is True
    assert is_armstrong(370) is True
    assert is_armstrong(1634) is True


class IsArmstrong(unittest.TestCase):

    def test_is_armstrong(self):
        """Unittest"""
        self.assertEqual(is_armstrong(947), False)
        self.assertEqual(is_armstrong(8208), True)
        self.assertEqual(is_armstrong(4), True)


if __name__ == '__main__':
    pytest.main()
    unittest.main()

