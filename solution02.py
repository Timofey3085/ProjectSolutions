"""
Написать функцию, которая принимает на вход два целых числа
(минимум и максимум) и возвращает список
всех простых чисел в заданном диапазоне.
"""

def funk_Eratosfena():
    """Решето Эратосфена"""
    n = int(input("n="))
    a = list(range(n + 1))
    a[1] = 0
    lst = []

    i = 2
    while i <= n:
        if a[i] != 0:
            lst.append(a[i])
            for j in range(i, n + 1, i):
                a[j] = 0
        i += 1
    print(lst)


funk_Eratosfena()
