"""
 Написать функцию, которая принимает на вход список целых чисел
и возвращает новый список,
содержащий только уникальные элементы из исходного списка.
"""
import pytest


def unique_numbers(numbers):
    """My_solution"""
    return list(set(numbers))


numbers = [1, 2, 2, 3, 4, 4, 5]
result_list = unique_numbers(numbers)
print(result_list)


def test_unique_numbers():
    """Pytest"""
    assert unique_numbers([1, 2, 2, 3, 4, 4, 5]) == [1, 2, 3, 4, 5]


def test_zero_numbers():
    """Pytest"""
    assert unique_numbers([0]) == [0]


def test_empy():
    """Pytest"""
    assert unique_numbers([]) == []


if __name__ == '__main__':
    pytest.main()

