"""
Your mission is to convert the name of a function from CamelCase ("MyFunctionName")
into the Python format ("my_function_name")
where all chars are in lowercase and all words are concatenated with an intervening underscore symbol "_".
"""
import re
import unittest

import pytest


def from_camel_case(name: str) -> str:
    """My_Solution"""
    k = re.findall('.[^A-Z]*', name)
    new_string = "_".join(k).lower()
    return new_string


def test_from_camel_case():
    """Pytest"""
    assert from_camel_case("MyFunctionName") == "my_function_name"
    assert from_camel_case("ThisIsThat") == "this_is_that"


class FromCamelCase(unittest.TestCase):

    def test_from_camel_case(self):
        """Unittest"""
        self.assertEqual(from_camel_case("IPhone"), "i_phone")
        self.assertEqual(from_camel_case("ILovePython"), "i_love_python")


if __name__ == '__main__':
    pytest.main()
    unittest.main()

