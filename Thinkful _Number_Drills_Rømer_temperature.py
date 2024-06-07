"""
You're writing an excruciatingly detailed alternate history novel set in a world
where Daniel Gabriel Fahrenheit was never born.
Since Fahrenheit never lived the world kept on using the Rømer scale,
invented by fellow Dane Ole Rømer to this very day,
skipping over the Fahrenheit and Celsius scales entirely.

Your magnum opus contains several thousand references to temperature,
but those temperatures are all currently in degrees Celsius.
You don't want to convert everything by hand,
so you've decided to write a function,
celsius_to_romer() that takes a temperature in degrees Celsius
and returns the equivalent temperature in degrees Rømer.
For example: celsius_to_romer(24) should return 20.1.
"""
import unittest

import pytest


def celsius_to_romer(temp):
    """MySolution"""
    return temp * (21/40) + 7.5


def test_celsius_to_romer():
    """Pytest"""
    assert celsius_to_romer(24) == 20.1
    assert celsius_to_romer(8) == 11.7


class CelsiusToRomer(unittest.TestCase):

    def test__celsius_to_romer(self):
        """Unittest"""
        self.assertEqual(celsius_to_romer(29), 22.725)


if __name__ in '__main__':
    pytest.main()
    unittest.main()
