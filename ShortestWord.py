"""
Simple, given a string of words, return the length of the shortest word(s).
String will never be empty, and you do not need to account for different data types.
"""

import pytest


def find_short(s):
    """My_Solution"""
    return min(len(l) for l in s.split())


def test_find_short():
    """Pytest"""
    assert find_short("Hello World") == 5
    assert find_short("Hello my friend") == 2
    assert find_short("Это тест") == 3


if __name__ == "__main__":
    pytest.main()
