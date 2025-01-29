"""
Don Drumphet lives in a nice neighborhood, but one of his neighbors has started to let his house go.
Don Drumphet wants to build a wall between his house and his neighbor’s,
and is trying to get the neighborhood association to pay for it.
He begins to solicit his neighbors to petition to get the association to build the wall.
Unfortunately for Don Drumphet, he cannot read very well, has a very limited attention span,
and can only remember two letters from each of his neighbors’ names.
As he collects signatures, he insists that his neighbors keep truncating their names until two letters remain,
and he can finally read them.

Your code will show Full name of the neighbor and the truncated version of the name as an array.
If the number of the characters in name is less than or equal to two,
it will return an array containing only the name as is.
"""
import pytest


def who_is_paying(name):
    """My_solution"""
    return [name, name[:2]] if len(name) > 2 else [name]


def test_who_is_paying():
    """Pytest"""
    assert who_is_paying("Mexico") == ["Mexico", "Me"]
    assert who_is_paying("Melania") == ["Melania", "Me"]
    assert who_is_paying("Melissa") == ["Melissa", "Me"]


def test_if_two_letters():
    """Pytest"""
    assert who_is_paying("Me") == ["Me"]


if __name__ == '__main__':
    pytest.main()

