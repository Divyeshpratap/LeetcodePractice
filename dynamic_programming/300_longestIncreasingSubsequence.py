'''
Given an integer array nums, return the length of the longest strictly increasing subsequen
ce.
Exapmple 1:
Input: nums = [10,9,2,5,3,7,101,18]
Output: 4
Explanation: The longest increasing subsequence is [2,3,7,101], therefore the length is 4.
'''
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        LIS = [1] * len(nums)

        for i in range(1, len(nums)):
            for j in range(0, i):
                if nums[i] > nums[j] and (1 + LIS[j]) > LIS[i]:
                    LIS[i] = 1 + LIS[j]
        return max(LIS)
'''
Time Complexity: O(len(nums)**2)
Space Complexity: O(len(nums))
******************************
Summary Statistics:
Runtime: 1041 ms, faster than 74.38% of Python3 online submissions for Longest Increasing Subsequence.
Memory Usage: 16.9 MB, less than 28.63% of Python3 online submissions for Longest Increasing Subsequence.
'''
