"""
Find the most common letter (not space) in the string(always lowercase and 2 < words) and replace it with the letter.
If such letters are two or more, choose the one that appears in the string( earlier.
For example:
('my mom loves me as never did', 't') => 'ty tot loves te as never did'
('real talk bro', 'n') => 'neal talk bno'
('great job go ahead', 'k') => 'grekt job go khekd'
"""


import collections

import pytest


def replace_common(st, letter):
    """My_solution"""
    result = []
    count = collections.Counter(st.replace(" ", ""))
    most_common_letter, _ = count.most_common(1)[0]
    for i in st:
        if i == most_common_letter:
            result.append(letter)
        if i != most_common_letter:
            result.append(i)
    return "".join(result)


@pytest.mark.parametrize("st, letter, result", [
    ('my mom loves me as never did', 't', 'ty tot loves te as never did'),
    ('real talk bro', 'n', 'neal talk bno'),
    ('great job go ahead', 'k', 'grekt job go khekd'),
    ('yyyaaa twwww ttt uuu ccca', 'p', 'yyyppp twwww ttt uuu cccp'),
])
def test_replace_common(st, letter, result):
    """Pytest"""
    assert replace_common(st, letter) == result


if __name__ == '__main__':
    pytest.main()
