"""
35. Search Insert Position
Given a sorted array of distinct integers and a target value, return the index if the target is found.
If not, return the index where it would be if it were inserted in order.

You must write an algorithm with O(log n) runtime complexity.

Example 1:

Input: nums = [1,3,5,6], target = 5
Output: 2
Example 2:

Input: nums = [1,3,5,6], target = 2
Output: 1
Example 3:

Input: nums = [1,3,5,6], target = 7
Output: 4
"""
import pytest


def search_and_insert(nums: list[int], target: int) -> int:
    """My_solution with binary searching method"""
    left: int = 0
    right: int = len(nums) - 1
    while left <= right:
        mid = (left + right) // 2
        if target > nums[mid]:
            left = mid + 1
        else:
            right = mid - 1
    return left


@pytest.mark.parametrize("nums, target, expected_result", [
    ([1, 3, 5, 6], 5, 2),
    ([1, 3, 5, 6], 2, 1),
    ([1, 3, 5, 6], 7, 4),
])
def test_search_and_insert(nums: list[int], target: int, expected_result: int):
    assert search_and_insert(nums, target) == expected_result


if __name__ == '__main__':
    pytest.main()

