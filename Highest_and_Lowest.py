"""
In this little assignment you are given a string of space separated numbers,
and have to return the highest and lowest number.

Examples
high_and_low("1 2 3 4 5")  # return "5 1"
high_and_low("1 2 -3 4 5") # return "5 -3"
high_and_low("1 9 3 4 -5") # return "9 -5"
"""
import pytest


def high_and_low(numbers):
    """My_solution"""
    num = [int(n) for n in numbers.split(" ")]
    return f'{max(num)} {min(num)}'


@pytest.mark.parametrize("numbers, expected_result", [
    ("1 2 3 4 5", "5 1"),
    ("1 2 -3 4 5", "5 -3"),
    ("1 9 3 4 -5", "9 -5"),
    ("8 3 -5 42 -1 0 0 -9 4 7 4 -4", "42 -9"),
    ("1 2 3", "3 1"),
])
def test_high_and_low(numbers, expected_result):
    """Pytest"""
    assert high_and_low(numbers) == expected_result


if __name__ == '__main__':
    pytest.main()

