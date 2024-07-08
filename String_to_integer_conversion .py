"""
JavaScript provides a built-in parseInt method.

It can be used like this:

parseInt("10") returns 10
parseInt("10 apples") also returns 10
We would like it to return "NaN" (as a string) for the second case because the input string is not a valid number.

You are asked to write a myParseInt method with the following rules:

It should make the conversion if the given string only contains a single integer value
(and possibly spaces - including tabs, line feeds... - at both ends)
For all other strings (including the ones representing float values), it should return NaN
It should assume that all numbers are not signed and written in base 10
"""
import unittest

import pytest


def my_parse_int(strn):
    """My_solution"""
    strn = strn.strip()  # удаляем лишние пробелы в начале и в конце строки

    if strn.isdigit():  # проверяем, содержит ли строка только цифры
        return int(strn)
    else:
        return "NaN"


def test_my_parse_int():
    """Pytest"""
    assert my_parse_int("1") == 1
    assert my_parse_int("  2 ") == 2
    assert my_parse_int("08") == 8


class MyParseInt(unittest.TestCase):

    def test_my_parse_int(self):
        """Unittest"""
        self.assertEqual(my_parse_int("5 friends"), "NaN")
        self.assertEqual(my_parse_int("16.5"), "NaN")


if __name__ == '__main__':
    pytest.main()
    unittest.main()
