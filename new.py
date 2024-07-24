"""
There're k square apple boxes full of apples. If a box is of size m, then it contains m × m apples.
You noticed two interesting properties about the boxes:

The smallest box is of size 1,
the next one is of size 2,...,
all the way up to size k.

Boxes that have an odd size contain only yellow apples.
Boxes that have an even size contain only red apples.
Your task is to calculate the difference between the number of red apples and the number of yellow apples.

Example
For k = 5, the output should be -15

There are 1 + 3 × 3 + 5 × 5 = 35 yellow apples and 2 × 2 + 4 × 4 = 20 red apples, thus the answer is 20 - 35 = -15.
"""
import asyncio

import pytest


async def apple_boxes(k):
    """My_solution"""
    even_number = []
    not_even_number = []
    await asyncio.sleep(1)
    for i in range(1, k + 1):
        if i % 2 == 0:
            even_number.append(i * i)
        if i % 2 != 0:
            not_even_number.append(i * i)
    return sum(even_number) - sum(not_even_number)


@pytest.mark.asyncio
@pytest.mark.parametrize("k, expected_result", [
    (18, 171),
    (44, 990),
    (71, -2556),
    (111, -6216),
    (5, -15),
    (15, -120),
    (36, 666),
    (1, -1),
])
async def test_apple_boxes(k, expected_result):
    assert await apple_boxes(k) == expected_result


if __name__ == '__main__':
    pytest.main()


