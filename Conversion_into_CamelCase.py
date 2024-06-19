"""
Your mission is to convert the name of a function from the Python format (for example "my_function_name")
into CamelCase ("MyFunctionName") where the first char of every word is in uppercase
and all words are concatenated without any intervening characters.
"""
import unittest

import pytest


def to_camel_case(name: str) -> str:
    """My_Solution"""
    new_string = name.replace("_", " ").title()
    string = new_string.replace(" ", "")
    return string


def test_to_camel_case():
    """Pytest"""
    assert to_camel_case("my_function_name") == "MyFunctionName"
    assert to_camel_case("i_phone") == "IPhone"


class ToCamelCase(unittest.TestCase):

    def test_to_camel_case(self):
        """Unittest"""
        self.assertEqual(to_camel_case("need_more"), "NeedMore")
        self.assertEqual(to_camel_case("x_y_z"), "XYZ")


if __name__ == '__main__':
    pytest.main()
    unittest.main()

