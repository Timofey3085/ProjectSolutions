"""
Given a string and an array of integers representing indices, capitalize all letters at the given indices.

For example:

capitalize("abcdef",[1,2,5]) = "aBCdeF"
capitalize("abcdef",[1,2,5,100]) = "aBCdeF". There is no index 100.
The input will be a lowercase string with no spaces and an array of digits.
"""


def capitalize(s, ind):
    """My_solution"""
    lst = []
    for i, k in enumerate(s):
        if i in ind:
            lst.append(k.upper())
        else:
            lst.append(k)
    return "".join(lst)
