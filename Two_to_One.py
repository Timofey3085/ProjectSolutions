"""
Take 2 strings s1 and s2 including only letters from a to z.
Return a new sorted string (alphabetical ascending),
the longest possible, containing distinct letters - each taken only once - coming from s1 or s2.

Examples:
a = "xyaabbbccccdefww"
b = "xxxxyyyyabklmopq"
longest(a, b) -> "abcdefklmopqwxy"

a = "abcdefghijklmnopqrstuvwxyz"
longest(a, a) -> "abcdefghijklmnopqrstuvwxyz"
"""
import unittest


def longest(a1, a2):
    """My_solution"""
    res = []
    for i in a1:
        if i not in res:
            res.append(i)
        for j in a2:
            if j not in res:
                res.append(j)
    result = "".join(sorted(res))
    return f"{result}"


class Longest(unittest.TestCase):

    def test_longest(self):
        """Unittest"""
        self.assertEqual(longest("aretheyhere", "yestheyarehere"), "aehrsty")
        self.assertEqual(longest("loopingisfunbutdangerous", "lessdangerousthancoding"), "abcdefghilnoprstu")
        self.assertEqual(longest("inmanylanguages", "theresapairoffunctions"), "acefghilmnoprstuy")


if __name__ == '__main__':
    unittest.main()
