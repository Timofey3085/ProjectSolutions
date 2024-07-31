"""
Implement a function that accepts 3 integer values a, b, c.
The function should return true if a triangle can be built with the sides of given length and false in any other case.
(In this case, all triangles must have surface greater than 0 to be accepted).

Examples:

Input -> Output
1,2,2 -> true
4,2,3 -> true
2,2,2 -> true
1,2,3 -> false
-5,1,3 -> false
0,2,3 -> false
1,2,9 -> false
"""
import unittest


def is_triangle(a, b, c):
    """My_solution"""
    if a + b > c and b + c > a and a + c > b:
        return True
    else:
        return False


class IsTriangle(unittest.TestCase):

    def test_is_triangle(self):
        """Unittest"""
        self.assertEqual(is_triangle(1, 2, 2), True)
        self.assertEqual(is_triangle(7, 2, 2), False)
        self.assertEqual(is_triangle(1, 2, 3), False)
        self.assertEqual(is_triangle(1, 3, 2), False)
        self.assertEqual(is_triangle(3, 1, 2), False)


if __name__ == '__main__':
    unittest.main()

