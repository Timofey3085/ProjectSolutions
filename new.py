"""
Write a function that takes one or more arrays
and returns a new array of unique values in the order of the original provided arrays.

In other words, all values present from all arrays should be included in their original order,
but with no duplicates in the final array.

The unique numbers should be sorted by their original order,
but the final array should not be sorted in numerical order.
"""
import pytest


def unite_unique(*args):
    """Pytest"""
    unique_list = []
    for array in args:
        for value in array:
            if value not in unique_list:
                unique_list.append(value)
    return unique_list


@pytest.mark.parametrize("args, result", [
    (([1, 2], [3, 4]), [1, 2, 3, 4]),
    (([1, 3, 2], [5, 2, 1, 4], [2, 1]), [1, 3, 2, 5, 4])
])
def test_unite_unique(args, result):
    """Pytest"""
    assert unite_unique(*args) == result


if __name__ == '__main__':
    pytest.main()
