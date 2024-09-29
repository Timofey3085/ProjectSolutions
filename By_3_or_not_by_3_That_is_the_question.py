"""
A trick I learned in elementary school to determine whether or not a number was divisible by three
is to add all of the integers in the number together and to divide the resulting sum by three.
If there is no remainder from dividing the sum by three, then the original number is divisible by three as well.

Given a series of digits as a string, determine if the number represented by the string is divisible by three.

Example:

"123"      -> true
"8409"     -> true
"100853"   -> false
"33333333" -> true
"7"        -> false
Try to avoid using the % (modulo) operator.
"""
import pytest


def divisible_by_three(st: str) -> bool:
    """My_solution"""
    result = sum(int(i) for i in st)
    while result >= 3:
        result -= 3
    return result == 0


def test_divisible_by_three():
    """Pytest"""
    assert divisible_by_three('123') is True
    assert divisible_by_three('153') is True
    assert divisible_by_three('606') is True
    assert divisible_by_three('001') is False
    assert divisible_by_three('121') is False


if __name__ == '__main__':
    pytest.main()
