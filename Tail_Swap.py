"""
You'll be given a list of two strings,
and each will contain exactly one colon (":") in the middle (but not at beginning or end).
The length of the strings, before and after the colon, are random.

Your job is to return a list of two strings (in the same order as the original list),
but with the characters after each colon swapped.

Examples
["abc:123", "cde:456"]  -->  ["abc:456", "cde:123"]
["a:12345", "777:xyz"]  -->  ["a:xyz", "777:12345"]
"""
import unittest


def tail_swap(strings):
    """My_solution"""
    strings = ":".join(strings).split(":")
    a, b, c, d = strings
    return [f"{a}:{d}", f"{c}:{b}"]


def test_tail_swap():
    """Pytest"""
    assert tail_swap(['abc:123', 'cde:456']) == ['abc:456', 'cde:123']


def test_if_zero():
    """Pytest"""
    assert tail_swap(['0:0', '0:0']) == ['0:0', '0:0']


class TailSwap(unittest.TestCase):

    def test_tail_swap(self):
        """Unittest"""
        self.assertEqual(tail_swap((['a:12345', '777:xyz'])), (['a:xyz', '777:12345']))