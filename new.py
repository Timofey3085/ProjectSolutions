"""
Write a small function that returns the values of an array that are not odd.
All values in the array will be integers. Return the good values in the order they are given.
"""
import pytest


def no_odds(values):
    """My_solution"""
    return [result for result in values if result % 2 == 0]


@pytest.mark.parametrize("values, result", [
    ([0, 1], [0]),
    ([0, 1, 2, 3], [0, 2]),
    ([1, 3, 5, 7, 9], []),
])
def test_no_odds(values, result):
    assert no_odds(values) == result


if __name__ == '__main__':
    pytest.main()
