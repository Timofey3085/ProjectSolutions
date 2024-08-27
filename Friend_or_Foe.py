"""
Make a program that filters a list of strings and returns a list with only your friends name in it.

If a name has exactly 4 letters in it,
you can be sure that it has to be a friend of yours! Otherwise, you can be sure he's not...

Input = {"Ryan", "Kieran", "Jason", "Yous"}
Output = {"Ryan", "Yous"}

Input = {"Peter", "Stephen", "Joe"}
Output = {}
Input strings will only contain letters. Note: keep the original order of the names in the output.
"""
import pytest


def friend(x):
    """My_solution"""
    result = []
    for i in x:
        if len(i) == 4:
            result.append(i)
    return result


@pytest.mark.parametrize("x, result", [
    (["Ryan", "Kieran", "Mark"], ["Ryan", "Mark"]),
    (["Ryan", "Jimmy", "abc", "d", "Cool Man"], ["Ryan"]),
    (["Jimm", "Cari", "aret", "truehdnviegkwgvke", "sixtyiscooooool"], ["Jimm", "Cari", "aret"]),
    (["Tima", "Ksenia", "Dima"], ["Tima", "Dima"]),
])
def test_friend(x, result):
    """Pytest"""
    assert friend(x) == result


if __name__ == '__main__':
    pytest.main()
