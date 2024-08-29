"""
Implement a function that returns the minimal and the maximal value of a list (in this order).
"""
import unittest


def get_min_max(seq: list[int]) -> tuple:
    """My_solution"""
    sorted_seq = sorted(seq)
    return sorted_seq[0], sorted_seq[-1]


class GetMinMax(unittest.TestCase):
    """Unittest"""
    def test_get_min_max(self):
        self.assertEqual(get_min_max([2, 1, 5]), (1, 5))
        self.assertEqual(get_min_max([0, 0, 0]), (0, 0))
        self.assertEqual(get_min_max([100, 5]), (5, 100))


if __name__ == '__main__':
    unittest.main()
