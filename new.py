"""
Write a small function that returns the values of an array that are not odd.
All values in the array will be integers. Return the good values in the order they are given.
"""


def no_odds(values):
    """My_solution"""
    return [result for result in values if result % 2 == 0]
