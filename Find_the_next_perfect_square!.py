"""
You might know some pretty large perfect squares. But what about the NEXT one?
Complete the findNextSquare method that finds the next integral perfect square after the one passed as a parameter.
Recall that an integral perfect square is an integer n such that sqrt(n) is also an integer.
If the argument is itself not a perfect square then return either -1 or an empty value like None or null,
 depending on your language. You may assume the argument is non-negative.

Examples ( Input --> Output )
121 --> 144
625 --> 676
114 --> -1  #  because 114 is not a perfect square
"""
import math

import pytest


def find_next_square(sq):
    """My_solution with using math"""
    x = math.sqrt(sq)
    y = (x - math.floor(x))
    if y == 0:
        return (x + 1) ** 2
    else:
        return -1


@pytest.mark.parametrize("sq, expected_result", [
    (121, 144),
    (625, 676),
    (319225, 320356),
    (15241383936, 15241630849),
    (155, -1),
    (342786627, -1),
    (153, -1)
])
def test_find_next_square(sq, expected_result):
    """Pytest"""
    assert find_next_square(sq) == expected_result


if __name__ == '__main__':
    pytest.main()
