"""
Story
Bear the Freelancer charges clients on the hour,
but he adjusts his rate depending on how close friends he is with his clients.
For close friends, he charges $25 per hour, for his other friends he charges $50,
for his acquaintances his hourly rate is $100, reaching $125 for all his other clients.

Input
You’ll receive a list of lists, representing all the jobs Bear the Freelancer carried out for the month.
Each array within the outer list is comprised of the number of hours worked,
and the proximity to the client as a string, the possible values being 'Close Friend', 'Friend', 'Acquaintance',
or any other string for the rest of his clients.
The recognition of those three strings ('Close Friend', 'Friend', and 'Acquaintance') should be case insensitive.

Example
[[10, 'Close Friend'], [3, 'Acquaintance'], [7, 'Lead from web'], [6, 'Friend'], [2, 'From advertisements']]
In this example, he'll be charging 10 hours at $25, 3 hours at $100, 7 hours at $125, 6 hours at $50, and 2 hours at $125, for a total of $1975.

Expected Output
The total amount of dollars Bear the Freelancer has invoiced for his work. For an empty array, return 0.

Example
1975
"""
import pytest


def bear_dollars(jobs):
    """My_solution"""
    total_payment = 0

    for job in jobs:
        hours_worked = job[0]
        client_type = job[1].lower()

        if client_type == 'close friend':
            total_payment += hours_worked * 25
        elif client_type == 'friend':
            total_payment += hours_worked * 50
        elif client_type == 'acquaintance':
            total_payment += hours_worked * 100
        else:
            total_payment += hours_worked * 125

    return total_payment


@pytest.mark.parametrize("jobs, total_payment", [
    ((10, 'Close Friend'), 250),
    ((5, 'Friend'), 250),
    ((3, 'Acquaintance'), 300),
    ((7, 'Lead from web'), 875),
    ((2, 'From advertisements'), 250)
])
def test_bear_dollars(jobs, total_payment):
    """Pytest"""
    assert bear_dollars([jobs]) == total_payment


if __name__ == '__main__':
    pytest.main()
