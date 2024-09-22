"""
Your colleagues have been looking over your shoulder. When you should have been doing your boring real job,
you've been using the work computers to smash in endless hours of codewars.
In a team meeting, a terrible, awful person declares to the group that you aren't working.
You're in trouble.
You quickly have to gauge the feeling in the room to decide whether or not you should gather your things and leave.
Given an object ( meet ) containing team member names as keys, and their happiness rating out of 10 as the value,
you need to assess the overall happiness rating of the group.
If <= 5, return 'Get Out Now!'. Else return 'Nice Work Champ!'.
Happiness rating will be total score / number of people in the room.
Note that your boss is in the room ( boss ).
Their score is worth double its face value (but they are still just one person!).
"""
import pytest


def outed(meet, boss):
    """My_solution"""
    total_score = 0
    num_people = 0

    for name, happiness in meet.items():
        if name == boss:
            total_score += happiness * 2  # Босс удваивается
        else:
            total_score += happiness
        num_people += 1  # Увеличиваем количество участников

    # Рейтинг счастья
    average_happiness = total_score / num_people

    if average_happiness <= 5:
        return 'Get Out Now!'
    else:
        return 'Nice Work Champ!'


def test_outed():
    """Pytest"""
    assert outed({'tim': 0,
                  'jim': 2,
                  'randy': 0,
                  'sandy': 7,
                  'andy': 0,
                  'katie': 5,
                  'laura': 1,
                  'saajid': 2,
                  'alex': 3,
                  'john': 2,
                  'mr': 0}, 'laura') == 'Get Out Now!'


if __name__ == '__main__':
    pytest.main()
