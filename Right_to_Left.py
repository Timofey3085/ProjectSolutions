"""
One of the robots is charged with a simple task:
to join a sequence of strings into one sentence to produce instructions on how to get around the ship.
But this robot is left-handed and has a tendency to joke around and confuse its right-handed friends.

You are given a sequence of strings.
You should join these strings into a chunk of text where the initial strings are separated by commas.
As a joke on the right-handed robots, you should replace all cases of the words "right" with the word "left",
even if it's a part of another word.
All strings are given in lowercase.
"""
import pytest


def left_join(phrases: tuple[str]) -> str:
    """My_solution"""
    join_phrase = ','.join(phrases)
    result = join_phrase.replace('right', 'left')

    return result


def test_left_join():
    """Pytest"""
    assert left_join(("left", "right", "left", "stop")) == "left,left,left,stop"
    assert left_join(("bright aright", "ok")) == "bleft aleft,ok"


if __name__ == '__main__':
    pytest.main()
