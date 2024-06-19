"""
The first input array is the key to the correct answers to an exam, like ["a", "a", "b", "d"].
The second one contains a student's submitted answers.
The two arrays are not empty and are the same length.
Return the score for this array of answers, giving +4 for each correct answer,
-1 for each incorrect answer, and +0 for each blank answer,
represented as an empty string (in C the space character is used).
If the score < 0, return 0.
For example:
    Correct answer    |    Student's answer   |   Result
 ---------------------|-----------------------|-----------
 ["a", "a", "b", "b"]   ["a", "c", "b", "d"]  →     6
 ["a", "a", "c", "b"]   ["a", "a", "b", "" ]  →     7
 ["a", "a", "b", "c"]   ["a", "a", "b", "c"]  →     16
 ["b", "c", "b", "a"]   ["" , "a", "a", "c"]  →     0
 """
import unittest
import pytest


def check_exam(arr1,arr2):
    """My_Solution"""
    count = 0
    for i, m in zip(arr1, arr2):
        if m == '':
            continue
        if i == m:
            count += 4
        if i != m:
            count -= 1
    return max(count, 0)


def test_check_exam():
    """PyTest"""
    assert check_exam(["a", "a", "b", "b"], ["a", "c", "b", "d"]) == 6
    assert check_exam(["a", "b", "c", "d"], ["a", "b", "c", "d"]) == 16


class CheckExam(unittest.TestCase):

    def test_check_exam(self):
        """Unittest"""
        self.assertEqual(check_exam(["a", "a", "c", "b"], ["a", "a", "b",  ""]), 7)
        self.assertEqual(check_exam(["b", "c", "b", "a"], ["",  "a", "a", "c"]), 0)


if __name__ == '__main__':
    pytest.main()
    unittest.main()
