"""
Happy Holidays fellow Code Warriors!
It's almost Christmas Eve, so we need to prepare some milk and cookies for Santa!
Wait... when exactly do we need to do that?

Time for Milk and Cookies
Complete the function that accepts a Date object,
and returns true if it's Christmas Eve (December 24th), false otherwise.

Examples
time_for_milk_and_cookies(date(2013, 12, 24))  # True
time_for_milk_and_cookies(date(2013, 1, 23))   # False
time_for_milk_and_cookies(date(3000, 12, 24))  # True
"""
import unittest
import pytest
from datetime import datetime


def time_for_milk_and_cookies(dt):
    """My_solution"""
    if dt.month == 12 and dt.day == 24:
        return True
    else:
        return False


def test_time_for_milk_and_cookies():
    """Pytest"""
    assert time_for_milk_and_cookies(datetime(2013, 12, 24)) is True
    assert time_for_milk_and_cookies(datetime(2013, 10, 24)) is False


class TimeForMilkAndCookies(unittest.TestCase):

    def test_time_for_milk_and_cookies(self):
        """Unittest"""
        self.assertEqual(time_for_milk_and_cookies(datetime(3000, 12, 24)), True)
        self.assertEqual(time_for_milk_and_cookies(datetime(1985, 12, 30)), False)


if __name__ == '__main__':
    pytest.main()
    unittest.main()

