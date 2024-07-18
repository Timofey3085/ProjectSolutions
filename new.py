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
