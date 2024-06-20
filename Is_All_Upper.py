"""
The task is to check that all characters of the word are uppercase.
If only the numbers are true.
If it's empty, it's also true.
"""
import unittest

import pytest


def is_all_upper(text: str) -> bool:
    """My_solution"""
    text = "".join(text.split())
    if text.isupper():
        return True
    while text == "" or text.isdigit():
        return True
    else:
        return False


def test_is_all_upper():
    """Pytest"""
    assert is_all_upper("ALL UPPER") is True
    assert is_all_upper("all lower") is False
    assert is_all_upper("mixed UPPER and lower") is False


class IsAllUpper(unittest.TestCase):

    def test_is_all_upper(self):
        """Unittest"""
        self.assertEqual(is_all_upper(""), True)
        self.assertEqual(is_all_upper("444"), True)
        self.assertEqual(is_all_upper("55 55 5"), True)


if __name__ == '__main__':
    pytest.main()
    unittest.main()
