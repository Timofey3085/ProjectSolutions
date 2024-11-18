"""
Trolls are attacking your comment section!
A common way to deal with this situation is to remove all of the vowels from the trolls' comments,
neutralizing the threat.
Your task is to write a function that takes a string and return a new string with all vowels removed.
For example, the string "This website is for losers LOL!" would become "Ths wbst s fr lsrs LL!".
"""
import pytest


def disemvowel(string_):
    """My_solution"""
    res = []
    words = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    for i in string_:
        if i not in words:
            res.append(i)
    return "".join(res)


@pytest.mark.parametrize("string_, result", [
    ("This website is for losers LOL!", "Ths wbst s fr lsrs LL!"),
    ("No offense but,\nYour writing is among the worst I've ever read", "N ffns bt,\nYr wrtng s mng th wrst 'v vr rd"),
    ("What are you, a communist?", "Wht r y,  cmmnst?"),
])
def test_disemvowel(string_, result):
    """Pytest"""
    assert disemvowel(string_) == result


if __name__ == '__main__':
    pytest.main()
