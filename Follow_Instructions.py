"""
You’ve received a letter from a friend whom you haven't seen or heard from for a while.
In this letter he gives you instructions on how to find a hidden treasure!

In this mission you should follow a given list of instructions which will get you to a certain point on the map.
A list of instructions is a string, each letter of this string points you in the direction of your next step.

The letter "f" - tells you to move forward, "b" - backward, "l" - left, and "r" - right.

It means that if the list of your instructions is "fflff" then you should move forward two times,
make one step to the left and then again move two times forward.
Now, let's imagine that you are in the position (0, 0).
If you move forward your position will change to (0, 1).
If you move again it will be (0, 2).
If your next step is to the left then your position will become (-1, 2).
After the next two steps forward your coordinates will be (-1, 4).

Your goal is to find your final coordinates. Like in our case they are (-1, 4).
"""
import unittest

import pytest


def follow(instructions: str) -> tuple[int, int] | list[int]:
    """My_solution"""
    x, y = (0, 0)
    for i in instructions:
        if "f" in i:
            y += 1
        if "b" in i:
            y += -1
        if "l" in i:
            x += -1
        if "r" in i:
            x += 1
    return [x, y]


def test_follow():
    """Pytest"""
    assert follow("fflff") == [-1, 4]
    assert follow("ffrff") == [1, 4]


class Follow(unittest.TestCase):

    def test_follow(self):
        """Unittest"""
        self.assertEqual(follow("fblr"), [0, 0])
        self.assertEqual(follow("lrfb"), [0, 0])


if __name__ == '__main__':
    pytest.main()
    unittest.main()
