"""
Problem Description:

A snail is crawling along a rubber band that has an initial length of x units.
The snail moves at a constant speed of y units per minute.
As the snail crawls from the left end of the rubber band to the right end,
the rubber band increases in length from the right side every minute, adding z units to its length.

The question is: Will the snail be able to reach the right end of the rubber band within 1 year?

Parameters:

x: Initial length of the rubber band (in units), where 0.01 ≤ x ≤ 1,000,000.
y: Speed of the snail (in units per minute), where 0.01 ≤ y ≤ 1,000,000.
z: Amount by which the rubber band increases in length every minute (in units), where 0.01 ≤ z ≤ 1,000,000.
Examples:

Example 1:

Initial length of the rubber band: x = 10 units
Speed of the snail: y = 2 units/minute
Increase rate of the rubber band: z = 1 unit/minute
Outcome: True (The snail will reach the end in 10 minutes.)
Example 2:

Initial length of the rubber band: x = 100 units
Speed of the snail: y = 1 unit/minute
Increase rate of the rubber band: z = 2 units/minute
Outcome: False (The snail will never reach the end.)
Example 3:

Initial length of the rubber band: x = 100,000 units
Speed of the snail: y = 0.1 units/minute
Increase rate of the rubber band: z = 0.05 units/minute
Outcome: False (The snail will not be able to reach the end within one year.)
"""
import pytest


def can_snail_reach_end(length, speed, length_increases):
    """My_solution"""
    result = length / (speed - length_increases)
    if 0 < result < 100000:
        return True
    else:
        return False


@pytest.mark.parametrize("length, speed, length_increases, expected_result", [
    (10, 2, 1, True),
    (100, 10, 5, True),
    (50, 5, 1, True),
    (1000, 100, 10, True),
    (1, 0.1, 0.01, True),
    (100, 1, 2, False),
    (100000, 0.1, 0.05, False),
    (100, 0.5, 1, False),
    (1000, 1, 2, False),
    (500, 5, 10, False),
    (10000, 0.1, 1, False)
])
def test_can_snail_reach_end(length, speed, length_increases, expected_result):
    assert can_snail_reach_end(length, speed, length_increases) == expected_result


if __name__ == '__main__':
    pytest.main()

