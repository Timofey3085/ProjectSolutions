"""
Check if the given year is leap year.
A year is a leap year if it is divisible by 4,
except for end-of-century years which must be divisible by 400.
This means that the year 2000 was a leap year, although 1900 was not.
"""
import calendar
import unittest

import pytest


def is_leap_year(year: int) -> bool:
    """MySolution"""
    return calendar.isleap(year)


def test_is_leap_year():
    """Pytest"""
    assert (is_leap_year(2000) is True)
    assert (is_leap_year(1900) is False)
    assert (is_leap_year(2004) is True)
    assert (is_leap_year(2100) is False)


class IsLeapYear(unittest.TestCase):

    def test_is_leap_year(self):
        """Unittest"""
        self.assertEqual(is_leap_year(2020), True)
        self.assertEqual(is_leap_year(2021), False)
        self.assertEqual(is_leap_year(1600), True)
        self.assertEqual(is_leap_year(1985), False)
        self.assertEqual(is_leap_year(2001), False)


if __name__ == '__main__':
    pytest.main()
    unittest.main()
