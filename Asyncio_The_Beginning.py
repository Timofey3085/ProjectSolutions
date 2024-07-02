"""
Story
As you walk the streets with your crush beside you,
you are thinking about the world and how everything works...
Wait!! Your crush? Shit, you are dreaming again.

Task
Now implement a coroutine dreaming which sleeps for n seconds
and then returns m ** n without entirely blocking the execution of other coroutines that might be running.
"""


import asyncio

import pytest


async def dreaming(n, m):
    """My_solution"""
    await asyncio.sleep(n)
    mult = m ** n
    return mult


@pytest.mark.asyncio
@pytest.mark.parametrize("n, m, mult", [
    (1, 3, 3),
    (2, 2, 4),
    (1, 2, 2),
    (3, 3, 27),
    (2, 4, 16),
])
async def test_dreaming(n, m, mult):
    assert await dreaming(n, m) == mult


if __name__ == '__main__':
    pytest.main()

