"""
Create a method that takes an array/list as an input, and outputs the index at which the sole odd number is located.
This method should work with arrays with negative numbers.
If there are no odd numbers in the array, then the method should output -1.
Examples:
odd_one([2,4,6,7,10]) # => 3
odd_one([2,16,98,10,13,78]) # => 4
odd_one([4,-8,98,-12,-7,90,100]) # => 4
odd_one([2,4,6,8]) # => -1
"""
import pytest


def odd_one(arr):
    """My_solution"""
    for i, v in enumerate(arr):
        if v % 2 != 0:
            return i
        if sum(arr) % 2 == 0:
            return -1


@pytest.mark.parametrize("arr, expected_result", [
    ([2, 4, 6, 7, 10], 3),
    ([2, 16, 98, 10, 13, 78], 4),
    ([4, -8, 98, -12, -7, 90, 100], 4),
    ([2, 4, 6, 8], -1),
    ([10, 100, 1001], 3),
])
def test_odd_one(arr, expected_result):
    """Pytest"""
    assert odd_one(arr) == expected_result


if __name__ == '__main__':
    pytest.main()
