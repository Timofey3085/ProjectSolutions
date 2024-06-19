"""
Oh, no!
Some really funny web dev gave you a sequence of numbers from his API response as an sequence of strings!
You need to cast the whole array to the correct type.
Create the function that takes as a parameter a sequence of numbers represented as strings
and outputs a sequence of numbers.

ie:["1", "2", "3"] to [1, 2, 3]

Note that you can receive floats as well.
"""
import pytest


def to_float_array(arr):
    """My_Solution"""
    return [float(item) for item in arr]


def test_to_float_array():
    """PyTest"""
    assert to_float_array(["1.1", "2.2", "3.3"]) == [1.1, 2.2, 3.3]


if __name__ == '__main__':
    pytest.main()
