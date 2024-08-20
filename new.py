"""
Create a function that takes a number and returns an array of strings containing the number cut off at each digit.

Examples
420 should return ["4", "42", "420"]
2017 should return ["2", "20", "201", "2017"]
2010 should return ["2", "20", "201", "2010"]
4020 should return ["4", "40", "402", "4020"]
80200 should return ["8", "80", "802", "8020", "80200"]
PS: The input is guaranteed to be an integer in the range [0, 1000000]
"""
import pytest


def create_array_of_tiers(n):
    """My_solution"""
    str_num = str(n)
    k = [str_num[:i] for i in range(1, len(str_num) +1)]
    return k


@pytest.mark.parametrize("n, k", [
    (420, ["4", "42", "420"]),
    (2017, ["2", "20", "201", "2017"]),
    (2010, ["2", "20", "201", "2010"]),
    (4020, ["4", "40", "402", "4020"]),
    (80200, ["8", "80", "802", "8020", "80200"]),
])
def test_create_array_of_tiers(n, k):
    """Pytest"""
    assert create_array_of_tiers(n) == k


if __name__ == '__main__':
    pytest.main()
