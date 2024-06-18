"""
You are given list of integers (int).
You should find the sum of the elements with even indexes (0th, 2nd, 4th...).
Then multiply this summed number and the final element of the list together.
Don't forget that the first element has an index of 0.

For an empty list, the result will always be 0 (zero).
"""
import unittest

import pytest


def even_the_last(array: list[int]) -> int:
    """MySolution"""
    if not array:
        return 0
    sum_of_elements_by_index = sum([array[i] for i in range(len(array)) if i % 2 == 0])
    return sum_of_elements_by_index * array[-1]


def test_even_the_last():
    """Pytest"""
    assert even_the_last([0, 1, 2, 3, 4, 5]) == 30
    assert even_the_last([1, 3, 5]) == 30


class EvenTheLast(unittest.TestCase):

    def test_even_the_last(self):
        """Unittest"""
        self.assertEqual(even_the_last([6]), 36)
        self.assertEqual(even_the_last([]), 0)


if __name__ == '__main__':
    pytest.main()
    unittest.main()
