"""
Implement a function that adds two numbers together and returns their sum in binary.
The conversion can be done before, or after the addition.
The binary number returned should be a string.
Examples:(Input1, Input2 --> Output (explanation)))

1, 1 --> "10" (1 + 1 = 2 in decimal or 10 in binary)
5, 9 --> "1110" (5 + 9 = 14 in decimal or 1110 in binary)
"""
import asyncio
import unittest

import pytest


async def add_binary(a, b):
    result = '{:b}'.format(a + b)
    await asyncio.sleep(1)
    return result


@pytest.mark.asyncio
@pytest.mark.parametrize("a, b, result", [
    (1, 1, "10"),
    (0, 1, '1'),
    (1, 0, '1'),
    (0, 0, '0')
])
async def test_add_binary(a, b, result):
    """Pytest"""
    assert await add_binary(a, b) == result


class AddBinary(unittest.TestCase):

    def setUp(self):
        self.loop = asyncio.get_event_loop()

    def test_add_binary(self):
        """Unittest"""
        self.assertEqual(self.loop.run_until_complete(add_binary(2, 2)), '100')
        self.assertEqual(self.loop.run_until_complete(add_binary(51, 12)), '111111')


if __name__ == '__main__':
    pytest.main()
    unittest.main()
