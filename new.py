"""
There is a sentence that has a mistake in its ordering.

The part with a capital letter should be the first word.

Please write a function to re-order the words, so that the word starting with a capital letter is moved to the front.

Each word in the string is separated by a single space.

In the string, there will always be exactly one word with a capital letter in it.
"""


def re_ordering(text):
    res = []
    r = []
    t = text.split()
    for i in t:
        if i[0].isupper():
            res.append(i)
        else:
            r.append(i)
    return ' '.join(res + r)
