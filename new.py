"""
Write a function that takes an integer as input,
and returns the number of bits that are equal to one in the binary representation of that number.
You can guarantee that input is non-negative.
Example: The binary representation of 1234 is 10011010010, so the function should return 5
"""


from collections import Counter

import pytest


def count_bits(n):
    binary = bin(n)[2:]
    return binary.count('1')


@pytest.mark.parametrize("n, result", [
    (0, 0),
    (4, 1),
    (7, 3),
    (9, 2),
    (10, 2),
])
def test_count_bits(n, result):
    """Pytest"""
    assert count_bits(n) == result


if __name__ == '__main__':
    pytest.main()
