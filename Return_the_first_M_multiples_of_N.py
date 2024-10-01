"""
Implement a function, multiples(m, n), which returns an array of the first m multiples of the real number n.
Assume that m is a positive integer.
Ex.
multiples(3, 5.0)
should return
[5.0, 10.0, 15.0]
"""
import pytest


def multiples(m, n):
    """My_solution"""
    return [n * i for i in range(1, m + 1)]


def test_multiples():
    """Pytest"""
    assert multiples(3, 5) == [5, 10, 15]
    assert multiples(2, 3) == [3, 6]


if __name__ == '__main__':
    pytest.main()
