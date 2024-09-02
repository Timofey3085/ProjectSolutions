"""
Create a function that returns the sum of the two lowest positive numbers given an array of minimum 4 positive integers.
No floats or non-positive integers will be passed.
For example, when an array is passed like [19, 5, 42, 2, 77], the output should be 7.
[10, 343445353, 3453445, 3453545353453] should return 3453455.
"""
import pytest


def sum_two_smallest_numbers(numbers):
    """My_solution"""
    num = sorted(numbers)
    return num[0] + num[1]


@pytest.mark.parametrize("numbers, expected_result", [
    ([5, 1, 9, 6], 6),
    ([5, 8, 12, 18, 22], 13),
    ([7, 15, 12, 18, 22], 19),
    ([25, 42, 12, 18, 22], 30),
    ([0, 0, 0, 0], 0),

])
def test_sum_two_smallest_numbers(numbers, expected_result):
    """Pytest"""
    assert sum_two_smallest_numbers(numbers) == expected_result


if __name__ == '__main__':
    pytest.mark()
