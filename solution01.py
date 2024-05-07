""" Написать функцию, которая принимает на вход список целых чисел
    и возвращает новый список,
    содержащий только уникальные элементы из исходного списка."""


def unique_numbers(numbers):
    return list(set(numbers))


numbers = [1, 2, 2, 3, 4, 4, 5]
result_list = unique_numbers(numbers)
print(result_list)
