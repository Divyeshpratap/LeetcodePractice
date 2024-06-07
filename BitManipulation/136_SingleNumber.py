'''
Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.

You must implement a solution with a linear runtime complexity and use only constant extra space.
'''
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        temp = 0
        for num in nums:
            temp = temp ^ num

        return temp
'''
Time Complexity: O(nums)
Space Complexity: O(1)
**********************
Summary Statistics:
Runtime: 103 ms, faster than 87.59% of Python3 online submissions for Single Number.
Memory Usage: 19 MB, less than 90.83% of Python3 online submissions for Single Number.
'''
