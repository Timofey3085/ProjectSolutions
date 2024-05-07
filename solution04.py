"""
Написать программу,
которая сортирует список строк по длине,
сначала по возрастанию, а затем по убыванию.
"""


def sort_by_length(string):
    """По длине, по возрастанию"""
    return len(string)


def sort_by_reverse(string):
    """По длине, по убыванию"""
    return -len(string)


sortList = ['a', 'cc', 'bbb', 'd']
result_list_1 = sorted(sortList, key=sort_by_length)
result_list_2 = sorted(sortList, key=sort_by_reverse)

print('Список, возрастание:', result_list_1)
print('Список, убывание:', result_list_2)
