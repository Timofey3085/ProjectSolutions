"""
We need a function that receives two arguments, a value val , and the exponent of the power,  pow_ ,
and outputs the value that we want to find.
Let'see some cases:
(12385, 3) ==> 13824
(1245678, 5) ==> 1419857
The value, val will be always a positive integer.
The power, pow_ , always higher than 1 .
"""
import pytest


def find_next_power(val, pow_):
    """My_solution"""
    start = 1
    while True:
        result = start ** pow_
        if result > val:
            return result
        start += 1


@pytest.mark.parametrize("val, pow_, result", [
    (12385, 3, 13824),
    (1245678, 5, 1419857),
    (1245678, 6, 1771561),
])
def test_find_next_power(val, pow_, result):
    """Pytest"""
    assert find_next_power(val, pow_) == result


if __name__ == '__main__':
    pytest.main()
