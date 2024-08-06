"""
Count the number of divisors of a positive integer n.
Random tests go up to n = 500000.
Examples (input --> output)
4 --> 3 // we have 3 divisors - 1, 2 and 4
5 --> 2 // we have 2 divisors - 1 and 5
12 --> 6 // we have 6 divisors - 1, 2, 3, 4, 6 and 12
30 --> 8 // we have 8 divisors - 1, 2, 3, 5, 6, 10, 15 and 30
Note you should only return a number, the count of divisors.
The numbers between parentheses are shown only for you to see which numbers are counted in each case.
"""
import asyncio

import pytest


async def divisors(n):
    """My_solution"""
    k = len([i for i in range(1, n + 1) if n % i == 0])
    await asyncio.sleep(1)
    return k


@pytest.mark.asyncio
@pytest.mark.parametrize("n, k", [
    (1, 1),
    (4, 3),
    (5, 2),
    (12, 6),
    (30, 8),
    (4096, 13),
])
async def test_divisors(n, k):
    """Pytest"""
    assert await divisors(n) == k


if __name__ == '__main__':
    pytest.main()
