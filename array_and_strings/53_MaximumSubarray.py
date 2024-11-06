'''
Given an integer array nums, find the subarray with the largest sum, and return its sum.



Example 1:

Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
Output: 6
Explanation: The subarray [4,-1,2,1] has the largest sum 6.
'''
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:

        current_sum = nums[0]
        max_sum = nums[0]

        for i in range(1, len(nums)):
            current_sum = max(nums[i], current_sum + nums[i])
            max_sum = max(max_sum, current_sum)

        return max_sum
'''
Time Complexity: O(len(nums)
Space complexity: O(1)
**********************
Summary Statistics:
Runtime: 93 ms, faster than 20.51% of Python3 online submissions for Maximum Subarray.
Memory Usage: 31.4 MB, less than 17.46% of Python3 online submissions for Maximum Subarray.
'''
