"""
Given a non-degenerate triangle with lengths a, b, and c, return

the radius of a circle inscribed in the triangle (r)
the radius of a circle circumscribed on the triangle (R)
Examples:
radii(3, 4, 5) = (1, 2.5) (r = 1, right triangle, thales theorem, so R = 5 / 2 = 2.5)
radii(1, 1, 1) = (sqrt(3) / 6, sqrt(3) / 3)
radii(2, 1, 2) = (0.3872983346207417, 1.032795558988644) (maths, blah blah blah)
No golfing limit for this one, because I felt that this kata wasn't very... golfable.
But if you want to beat me, I got a 74 char solution, and I would really like to see limit being pushed further.
"""


import asyncio
import math

import pytest


async def radii(a, b, c):
    """My_solution"""
    p = (a + b + c) / 2
    r = math.sqrt((p - a) * (p - b) * (p - c) / p)
    R = (a * b * c) / (4 * r * p)
    result = round(r, 10), round(R, 10)
    await asyncio.sleep(1)
    return result


@pytest.mark.asyncio
@pytest.mark.parametrize("a, b, c, result", [
    (3, 4, 5, (1, 2.5)),
    (5, 12, 13, (2, 6.5)),
    (7, 24, 25, (3, 12.5)),
    (2, 1, 2, (0.3872983346, 1.032795559)),
])
async def test_radii(a, b, c, result):
    """Pytest"""
    await asyncio.sleep(1)
    assert await radii(a, b, c) == result


if __name__ == '__main__':
    pytest.main()
