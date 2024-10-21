"""
Write a function that returns the count of characters that have to be removed in order
to get a string with no consecutive repeats.
Note: This includes any characters
Examples
'abbbbc'  => 'abc'    #  answer: 3
'abbcca'  => 'abca'   #  answer: 2
'ab cca'  => 'ab ca'  #  answer: 1
"""


def count_repeats(txt):
    """My_solution"""
    count = 0
    for i in range(1, len(txt)):
        if txt[i] == txt[i - 1]:
            count += 1
    return count


