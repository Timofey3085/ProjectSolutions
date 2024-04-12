# 4. Написать программу,
# которая сортирует список строк по длине,
# сначала по возрастанию, а затем по убыванию.

def sortByLength(string):
    '''По длине, по возрастанию'''
    return len(string)


def sortByReverse(string):
    '''По длине, по убыванию'''
    return -len(string)


sortList = ['a', 'cc', 'bbb', 'd']
result_list_1 = sorted(sortList, key=sortByLength)
result_list_2 = sorted(sortList, key=sortByReverse)

print('Список, возрастание:', result_list_1)
print('Список, убывание:', result_list_2)
