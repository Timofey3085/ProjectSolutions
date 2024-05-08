"""
Your task is to write an update for a lottery machine. 
Its current version produces a sequence of random letters and integers (passed as a string to the function). 
Your code must filter out all letters and return unique integers as a string, 
in their order of first appearance. If there are no integers in the string return "One more run!"
Examples
"hPrBKWDH8yc6Lt5NQZWQ"  -->  "865"
"ynMAisVpHEqpqHBqTrwH"  -->  "One more run!"
"555"                   -->  "5"
"""
import unittest
import pytest


def lottery(s):
    res = ""
    for i in s:
        if i.isdigit() and i not in res:
            res += i
    return res or "One more run!"


def test_lottery():
    """Pytest"""
    assert lottery("wQ8Hy0y5m5oshQPeRCkG") == "805"
    assert lottery("20191224isXmas") == "20194"
    assert lottery("1ghuu2tyujn3hgfvh4iuyg5") == "12345"


class TestLottery(unittest.TestCase):

    def test_lottery(self):
        """Unittest"""
        self.assertEqual(lottery("ffaQtaRFKeGIIBIcSJtg"), "One more run!")
        self.assertEqual(lottery("555"), "5")
        self.assertEqual(lottery("HappyNewYear2020"), "20")


if __name__ == "__main__":
    pytest.main()
    unittest.main()
