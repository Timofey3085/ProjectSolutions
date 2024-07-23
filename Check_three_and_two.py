"""
Given an array with exactly 5 strings "a", "b" or "c" (chars in Java, characters in Fortran),
check if the array contains three and two of the same values.
Examples
["a", "a", "a", "b", "b"] ==> true  // 3x "a" and 2x "b"
["a", "b", "c", "b", "c"] ==> false // 1x "a", 2x "b" and 2x "c"
["a", "a", "a", "a", "a"] ==> false // 5x "a"
"""
import unittest

import pytest


def check_three_and_two(array):
    """My_solution"""
    count_a = array.count('a')
    count_b = array.count('b')
    count_c = array.count('c')

    if count_a == 3 and (count_b == 2 or count_c == 2):
        return True
    elif count_b == 3 and (count_a == 2 or count_c == 2):
        return True
    elif count_c == 3 and (count_a == 2 or count_b == 2):
        return True
    else:
        return False


@pytest.mark.parametrize("array, expected_result", [
    (["a", "a", "a", "b", "b"], True),
    (["a", "c", "a", "c", "b"], False),
    (["a", "a", "a", "a", "a"], False),
    (["b", "b", "b", "a", "a"], True),
    (["c", "c", "c", "a", "a"], True),
    (["b", "b", "b", "c", "c"], True),
])
def test_check_three_and_two(array, expected_result):
    """Pytest"""
    assert check_three_and_two(array) == expected_result


class CheckThreeAndTwo(unittest.TestCase):

    def test_check_three_and_two(self):
        """Unittest"""
        self.assertEqual(check_three_and_two(["a", "b", "c", "a", "b"]), False)
        self.assertEqual(check_three_and_two(["c", "c", "c", "b", "a"]), False)


if __name__ == '__main__':
    pytest.main()
    unittest.main()

