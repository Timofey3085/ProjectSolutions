"""
Your task is to create a function that given a sequence and a predicate,
returns True if only some (but not all) the elements in the sequence are True after applying the predicate

Examples
('abcdefg&%$', x -> isLetter(x)) == true
('&%$=', x -> isLetter x) == false
('abcdefg', x -> isLetter x) == false

([4, 1], x -> x > 3) == true
([1, 1], x -> x > 3) == false
([4, 4], x -> x > 3) == false
"""
import pytest


def some_but_not_all(seq, pred):
    """My_solution"""
    true_count = 0
    false_count = 0

    for elem in seq:
        if pred(elem):
            true_count += 1
        else:
            false_count += 1

    return true_count > 0 and false_count > 0


@pytest.mark.parametrize("seq, pred, expected_result", [
    ('abcdefg&%$', str.isalpha, True),
    ('&%$=', str.isalpha, False),
    ('abcdefg', str.isalpha, False),
    ([4, 1], lambda x: x > 3, True),
    ([1, 1], lambda x: x > 3, False),
    ([4, 4], lambda x: x > 3, False),
])
def test_some_but_not_all(seq, pred, expected_result):
    """Pytest"""
    assert some_but_not_all(seq, pred) == expected_result


if __name__ == '__main__':
    pytest.main()
