"""
Remove Element

Given an integer array nums and an integer val, remove all occurrences of val in nums in-place.
The order of the elements may be changed.
Then return the number of elements in nums which are not equal to val.

Consider the number of elements in nums which are not equal to val be k,
to get accepted, you need to do the following things:

Change the array nums such that the first k elements of nums contain the elements which are not equal to val.
The remaining elements of nums are not important as well as the size of nums.
"""
import pytest


class Solution(object):
    def remove_element(self, nums, val):
        """My_solution"""
        while val in nums:
            nums.remove(val)

        return len(nums)


def test_remove_element():
    """Pytest"""
    solution = Solution()
    assert solution.remove_element([3, 2, 2, 3], 3), [2, 2]
    assert solution.remove_element([0, 1, 2, 2, 3, 0, 4, 2], 2), [0, 1, 3, 0, 4]


if __name__ == '__main__':
    pytest.main()
