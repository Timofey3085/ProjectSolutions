"""
Your function should return True or False based on the following criteria.

You should take an umbrella if it's currently raining or if it's cloudy and the chance of rain is over 0.20.
You shouldn't take an umbrella if it's sunny unless it's more likely to rain than not.
The options for the current weather are sunny, cloudy, and rainy.

For example, take_umbrella('sunny', 0.40) should return False.
As an additional challenge, consider solving this kata using only logical operaters and not using any if statements.
"""
import unittest

import pytest


def take_umbrella(weather, rain_chance):
    """MySolution"""
    if weather == 'sunny' and rain_chance <= 0.45:
        return False
    if weather == 'sunny' and rain_chance >= 0.40:
        return True
    if weather == 'rainy':
        return True
    if weather == 'cloudy' and rain_chance <= 0.20:
        return False
    if weather == 'cloudy' and rain_chance >= 0.20:
        return True


def test_take_umbrella():
    """PyTest"""
    assert take_umbrella('sunny', 0.40) is False
    assert take_umbrella('rainy', 0.0) is True


class TakeUmbrella(unittest.TestCase):

    def test_take_umbrella(self):
        """Unittest"""
        self.assertEqual(take_umbrella('cloudy', 0.20), False)


if __name__ == '__main__':
    pytest.main()
    unittest.main()
