"""
ASC Week 1 Challenge 4 (Medium #1)

Write a function that converts any sentence into a V A P O R W A V E sentence.
a V A P O R W A V E sentence converts all the letters into uppercase,
and adds 2 spaces between each letter (or special character) to create this V A P O R W A V E effect.

Note that spaces should be ignored in this case.

Examples
"Lets go to the movies"       -->  "L  E  T  S  G  O  T  O  T  H  E  M  O  V  I  E  S"
"Why isn't my code working?"  -->  "W  H  Y  I  S  N  '  T  M  Y  C  O  D  E  W  O  R  K  I  N  G  ?"
"""
import pytest


def vaporcode(s):
    """My_solution"""
    new_string = s.replace(" ", "").upper()  # Убираем пробелы и переводим строку в верхний регистр
    result = "  ".join(new_string)  # Добавляем 2 пробела между каждым символом
    return result


@pytest.mark.parametrize("s, result", [
    ("Lets go to the movies", "L  E  T  S  G  O  T  O  T  H  E  M  O  V  I  E  S"),
    ("Why isn't my code working?", "W  H  Y  I  S  N  '  T  M  Y  C  O  D  E  W  O  R  K  I  N  G  ?"),
    ("What is happened", "W  H  A  T  I  S  H  A  P  P  E  N  E  D"),
])
def test_vaporcode(s, result):
    assert vaporcode(s) == result


if __name__ == '__main__':
    pytest.main()
