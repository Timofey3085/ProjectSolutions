"""
You probably know the "like" system from Facebook and other pages.
People can "like" blog posts, pictures or other items.
We want to create the text that should be displayed next to such an item.
Implement the function which takes an array containing the names of people that like an item.
It must return the display text as shown in the examples:

[]                                -->  "no one likes this"
["Peter"]                         -->  "Peter likes this"
["Jacob", "Alex"]                 -->  "Jacob and Alex like this"
["Max", "John", "Mark"]           -->  "Max, John and Mark like this"
["Alex", "Jacob", "Mark", "Max"]  -->  "Alex, Jacob and 2 others like this"
Note: For 4 or more names, the number in "and 2 others" simply increases.
"""
import unittest

import pytest


def likes(names):
    """My_solution"""
    length = len(names)
    if length == 0:
        return f'no one likes this'
    if length == 1:
        return f'{names[0]} likes this'
    if length == 2:
        return f'{names[0]} and {names[1]} like this'
    if length == 3:
        return f'{names[0]}, {names[1]} and {names[2]} like this'
    if length == 4:
        return f'{names[0]}, {names[1]} and 2 others like this'
    if length > 4:
        return f'{names[0]}, {names[1]} and {length - 2} others like this'


@pytest.mark.parametrize("names, expected_result", [
    ([], 'no one likes this'),
    (['Peter'], 'Peter likes this'),
    (['Jacob', 'Alex'], 'Jacob and Alex like this'),
    (['Max', 'John', 'Mark'], 'Max, John and Mark like this'),
    (['Alex', 'Jacob', 'Mark', 'Max'], 'Alex, Jacob and 2 others like this'),
    (['Sergei', 'Jacob', 'Mark', 'Max', 'Axel', 'Tim'], 'Sergei, Jacob and 4 others like this')
])
def test_likes(names, expected_result):
    """Pytest"""
    assert likes(names) == expected_result


if __name__ == '__main__':
    pytest.main()
