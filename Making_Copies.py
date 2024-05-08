"""
Write a function that takes a list (in Python) or array (in other languages) of numbers, and makes a copy of it.
Note that you may have troubles if you do not return an actual copy, item by item, just a pointer or an alias for an existing list or array.
If not a list or array is given as a parameter in interpreted languages, the function should raise an error.
Examples:
t = [1, 2, 3, 4]
t_copy = copy_list(t)
t[1] += 5
t = [1, 7, 3, 4]
t_copy = [1, 2, 3, 4]
"""
import pytest


def copy_list(l):
    """My_Solution"""
    return [i for i in l]


def test_copy_list():
    """Pytest"""
    assert copy_list([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]
    assert copy_list([]) == []
    assert copy_list(["Hello World"]) == ["Hello World"]


if __name__ == "__main__":
    pytest.main()
