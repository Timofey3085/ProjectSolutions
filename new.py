"""
Return the number (count) of vowels in the given string.
We will consider a, e, i o, u y).
The input string will only consist of lower case letters and/or spaces.
"""
import pytest


def get_count(sentence):
    """My_solution"""
    data = ["a", "e", "i", "o", "u"]
    count = 0
    for i in sentence:
        if i in data:
            count += 1
    return count


@pytest.mark.parametrize("sentence, expected_result", [
    ("aeiou", 5)
])
def test_get_count(sentence, expected_result):
    assert get_count(sentence) == expected_result


if __name__ == '__main__':
    pytest.main()
