'''
Given an array nums of size n, return the majority element.

The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.
'''
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        curr = nums[0]
        count = 1
        for i in range(1, len(nums)):
            if nums[i] == curr:
                count += 1
            else:
                count -= 1

            if count <= 0:
                if i + 1 < len(nums):
                    curr = nums[i + 1]
                    count = 0
        return curr       
'''
Time Complexity: O(n)
Space Complexity: O(1)
'''
