"""
Create a method that takes an array/list as an input, and outputs the index at which the sole odd number is located.
This method should work with arrays with negative numbers.
If there are no odd numbers in the array, then the method should output -1.
Examples:
odd_one([2,4,6,7,10]) # => 3
odd_one([2,16,98,10,13,78]) # => 4
odd_one([4,-8,98,-12,-7,90,100]) # => 4
odd_one([2,4,6,8]) # => -1
"""


def odd_one(arr):
    for i, v in enumerate(arr):
        """My_solution"""
        if v % 2 != 0:
            return i
        if sum(arr) % 2 == 0:
            return -1
