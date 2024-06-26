"""
Colour plays an important role in our lifes.
Most of us like this colour better than another.
User experience specialists believe that certain colours have certain psychological meanings for us.

You are given a 2D array, composed of a colour and its 'common' association in each array element.
The function you will write needs to return the colour as 'key' and association as its 'value'.

For example:
var array = [["white", "goodness"], ...] returns [{'white': 'goodness'}
"""
import pytest


def colour_association(arr):
    """My_solution"""
    return [{k: v} for k, v in arr]


def test_colour_association():
    """Pytest"""
    assert (colour_association([["white", "goodness"], ["blue", "tranquility"]]) == [{'white': "goodness"},
                                                                                     {'blue': "tranquility"}])
    assert colour_association([["red", "energy"], ["yellow", "creativity"],
                               ["brown", "friendly"], ["green", "growth"]]) == [{'red': "energy"},
                                                                                {'yellow': "creativity"},
                                                                                {'brown': "friendly"},
                                                                                {'green': "growth"}]


if __name__ == '__main__':
    pytest.main()
