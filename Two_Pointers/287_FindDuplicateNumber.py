'''
Given an array of integers nums containing n + 1 integers where each integer is in the range [1, n] inclusive.

There is only one repeated number in nums, return this repeated number.

You must solve the problem without modifying the array nums and using only constant extra space.
Example 1:

Input: nums = [1,3,4,2,2]
Output: 2
'''
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        
        slow, fast = 0, 0
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break
                
        slowSecond = 0
        
        while True:
            slowSecond = nums[slowSecond]
            slow = nums[slow]
            if slow == slowSecond:
                return slow
'''
Time Complexity: O(len(nums))
Space Complexity: O(1)
**********************
Summary Statistics:
Runtime: 27 ms, faster than 63.35% of Python3 online submissions for Find the Duplicate Number.
Memory Usage: 28.5 MB, less than 77.84% of Python3 online submissions for Find the Duplicate Number
'''

