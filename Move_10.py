"""
Move every letter in the provided string forward 10 letters through the alphabet.
If it goes past 'z', start again at 'a'.
Input will be a string with length > 0.
"""
import pytest


def move_ten(st):
    """My_solution"""
    alphabet = {
        "a": 0,
        "b": 1,
        "c": 2,
        "d": 3,
        "e": 4,
        "f": 5,
        "g": 6,
        "h": 7,
        "i": 8,
        "j": 9,
        "k": 10,
        "l": 11,
        "m": 12,
        "n": 13,
        "o": 14,
        "p": 15,
        "q": 16,
        "r": 17,
        "s": 18,
        "t": 19,
        "u": 20,
        "v": 21,
        "w": 22,
        "x": 23,
        "y": 24,
        "z": 25,
    }

    result = ""

    for word in st:
        if word in alphabet:
            new_index = (alphabet[word] + 10) % 26
            result += list(alphabet.keys())[new_index]
    return result


@pytest.mark.parametrize("st, result", [
    ("testcase", "docdmkco"),
    ("codewars", "mynogkbc"),
    ("exampletesthere", "ohkwzvodocdrobo"),
    ("returnofthespacecamel", "bodebxypdroczkmomkwov"),
    ("bringonthebootcamp", "lbsxqyxdrolyydmkwz"),
    ("weneedanofficedog", "goxoonkxyppsmonyq"),
])
def test_move_ten(st, result):
    """Pytest"""
    assert move_ten(st) == result


if __name__ == '__main__':
    pytest.main()
