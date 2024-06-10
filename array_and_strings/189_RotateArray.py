'''
Given an integer array nums, rotate the array to the right by k steps, where k is non-negative.
'''
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i = k%len(nums)
        if i == 0:
            return
        
        nums[0:0] = nums[-i:]
        
        while i > 0:
            nums.pop()
            i = i - 1      
'''
Time Complexity: O(n)
Space Complexity: O(1)
**********************
Summary Statistics:
Runtime: 153 ms, faster than 78.76% of Python3 online submissions for Rotate Array.
Memory Usage: 28.3 MB, less than 7.95% of Python3 online submissions for Rotate Array.
'''
