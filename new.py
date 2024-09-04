"""
In this kata the aim is to compare each pair of integers from two arrays, and return a new array of large numbers.

Note: Both arrays have the same dimensions.

Example:
arr1 = [13, 64, 15, 17, 88]
arr2 = [23, 14, 53, 17, 80]
get_larger_numbers(arr1, arr2) == [23, 64, 53, 17, 88]
"""
import pytest


def get_larger_numbers(a, b):
    """My_solution"""
    res = []
    for i in range(len(a)):
        if a[i] >= b[i]:
            res.append(a[i])
        else:
            res.append(b[i])
    return res


@pytest.mark.parametrize("a, b, res", [
    ([13, 64, 15, 17, 88], [23, 14, 53, 17, 80], [23, 64, 53, 17, 88]),
    ([34, -64, 15, 17, 88], [23, 14, 53, 17, 80], [34, 14, 53, 17, 88]),
    ([44, 0, 96, 55, 89], [18, 9, 97, 55, 98], [44, 9, 97, 55, 98])
])
def test_get_larger_numbers(a, b, res):
    """Pytest"""
    assert get_larger_numbers(a, b) == res


if __name__ == '__main__':
    pytest.main()
