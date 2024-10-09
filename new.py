"""
Given a string and an array of integers representing indices, capitalize all letters at the given indices.

For example:

capitalize("abcdef",[1,2,5]) = "aBCdeF"
capitalize("abcdef",[1,2,5,100]) = "aBCdeF". There is no index 100.
The input will be a lowercase string with no spaces and an array of digits.
"""
import pytest


def capitalize(s, ind):
    """My_solution"""
    lst = []
    for i, k in enumerate(s):
        if i in ind:
            lst.append(k.upper())
        else:
            lst.append(k)
    return "".join(lst)


@pytest.mark.parametrize("s, ind, expected_result", [
    ("abcdef",[1,2,5],'aBCdeF'),
    ("abcdef",[1,2,5,100],'aBCdeF',),
])
def test_capitalize(s, ind, expected_result):
    assert capitalize(s, ind) == expected_result


if __name__ == '__main__':
    pytest.main()

