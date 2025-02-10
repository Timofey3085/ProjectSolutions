"""
There is a sentence that has a mistake in its ordering.

The part with a capital letter should be the first word.

Please write a function to re-order the words, so that the word starting with a capital letter is moved to the front.

Each word in the string is separated by a single space.

In the string, there will always be exactly one word with a capital letter in it.
"""
import pytest


def re_ordering(text):
    """My_solution"""
    res = []
    r = []
    t = text.split()
    for i in t:
        if i[0].isupper():
            res.append(i)
        else:
            r.append(i)
    return ' '.join(res + r)


@pytest.mark.parametrize("text, result", [
    ('ming Yao', 'Yao ming'),
    ('Mano donowana', 'Mano donowana'),
    ('wario LoBan hello', 'LoBan wario hello'),
    ('bull color pig Patrick', 'Patrick bull color pig'),
    ('jojo ddjajdiojdwo ana G nnibiial', 'G jojo ddjajdiojdwo ana nnibiial'),

])
def test_re_ordering(text, result):
    """Pytest"""
    assert re_ordering(text) == result


if __name__ == '__main__':
    pytest.main()
