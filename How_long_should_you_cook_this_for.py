"""
You've purchased a ready-meal from the supermarket.
The packaging says that you should microwave it for 4 minutes and 20 seconds, based on a 600W microwave.
Oh no, your microwave is 800W! How long should you cook this for?!

Input
You'll be given 4 arguments:

1. needed power
The power of the needed microwave.
Example: "600W"

2. minutes
The number of minutes shown on the package.
Example: 4

3. seconds
The number of seconds shown on the package.
Example: 20

4. power
The power of your microwave.
Example: "800W"

Output
The amount of time you should cook the meal for formatted as a string.
Example: "3 minutes 15 seconds"

Note: the result should be rounded up.

59.2 sec  -->  60 sec  -->  return "1 minutes 0 seconds"
"""
import math
import unittest

import pytest


def cooking_time(needed_power, minutes, seconds, power):
    """MySolution"""
    new_power = int(needed_power.replace('W', ''))
    all_seconds = minutes * 60 + seconds
    my_power = int(power.replace('W', ''))
    result_seconds = math.ceil((new_power * all_seconds) / my_power)
    result_minutes = result_seconds // 60
    result_seconds %= 60

    return f"{result_minutes} minutes {result_seconds} seconds"


def test_cooking_time():
    """PyTest"""
    assert cooking_time("600W", 4, 20, "800W") == "3 minutes 15 seconds"
    assert cooking_time("800W", 3, 0, "1200W") == "2 minutes 0 seconds"
    assert cooking_time("100W", 8, 45, "50W") == "17 minutes 30 seconds"


class CookingTime(unittest.TestCase):

    def test_cooking_time(self):
        """Unittest"""
        self.assertEqual(cooking_time("7500W", 0, 5, "600W"), "1 minutes 3 seconds")
        self.assertEqual(cooking_time("450W", 3, 25, "950W"), "1 minutes 38 seconds")
        self.assertEqual(cooking_time("21W", 64, 88, "25W"), "55 minutes 0 seconds")


if __name__ == '__main__':
    pytest.main()
    unittest.main()
