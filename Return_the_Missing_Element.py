"""
Fellow code warrior, we need your help!
We seem to have lost one of our sequence elements, and we need your help to retrieve it!
Our sequence given was supposed to contain all of the integers from 0 to 9 (in no particular order),
but one of them seems to be missing.
Write a function that accepts a sequence of unique integers between 0 and 9 (inclusive), and returns the missing element.

Examples:
[0, 5, 1, 3, 2, 9, 7, 6, 4] --> 8
[9, 2, 4, 5, 7, 0, 8, 6, 1] --> 3
"""
import pytest


def get_missing_element(seq: list[int]) -> int:
    """My_solution"""
    for missing_element in range(0, 10):
        if missing_element not in seq:
            return missing_element


@pytest.mark.parametrize("seq, missing_element", [
    ([0, 5, 1, 3, 2, 9, 7, 6, 4], 8),
    ([9, 2, 4, 5, 7, 0, 8, 6, 1], 3),
    ([9, 2, 3, 5, 7, 0, 8, 6, 1], 4),
])
def test_get_missing_elements(seq, missing_element):
    """Pytest"""
    assert get_missing_element(seq) == missing_element


if __name__ == '__main__':
    pytest.main()
