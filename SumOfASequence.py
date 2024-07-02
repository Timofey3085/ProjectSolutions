"""
Your task is to write a function which returns the sum of a sequence of integers.
The sequence is defined by 3 non-negative values: begin, end, step.
If begin value is greater than the end, your function should return 0.
If end is not the result of an integer number of steps, then don't add it to the sum. See the 4th example below.

Examples
2,2,2 --> 2
2,6,2 --> 12 (2 + 4 + 6)
1,5,1 --> 15 (1 + 2 + 3 + 4 + 5)
1,5,3  --> 5 (1 + 4)
"""
import unittest

import pytest


def sequence_sum(begin_number: int, end_number: int, step: int) -> int:
    """My_solution"""
    b: int = begin_number
    e: int = end_number
    s: int = step

    if b > e:
        return 0

    total_sum = 0
    while b <= e:
        total_sum += b
        b += s

    return total_sum


@pytest.mark.parametrize("begin_number, end_number, step, expected_sum", [
    (2, 6, 2, 12),
    (1, 5, 1, 15),
    (1, 5, 3, 5),
    (0, 15, 3, 45),
    (16, 15, 3, 0),
])
def test_sequence_sum(begin_number, end_number, step, expected_sum):
    assert sequence_sum(begin_number, end_number, step) == expected_sum


class SequenceSum(unittest.TestCase):

    def test_sequence_sum(self):
        """Unittest"""
        self.assertEqual(sequence_sum(2, 24, 22), 26)
        self.assertEqual(sequence_sum(2, 2, 2), 2)
        self.assertEqual(sequence_sum(2, 2, 1), 2)
        self.assertEqual(sequence_sum(1, 15, 3), 35)


if __name__ == '__main__':
    pytest.main()
    unittest.main()



