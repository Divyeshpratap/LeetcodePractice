'''
Given an array of positive integers nums and a positive integer target, return the minimal length of a subarray whose sum is greater than or equal to target. If there is no such subarray, return 0 instead.



Example 1:

Input: target = 7, nums = [2,3,1,2,4,3]
Output: 2
Explanation: The subarray [4,3] has the minimal length under the problem constraint.
'''
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left, right = 0, 0
        minLen = len(nums) + 1
        total = 0
        while right < len(nums):
            total += nums[right]
            while total >= target:
                currLen = right - left + 1
                total -= nums[left]
                left += 1
                minLen = min(currLen, minLen)

            right += 1
        return minLen if minLen!= len(nums) + 1 else 0
'''
Time Complexity: O(len(nums))
Space Complexity: O(1)
**********************
Summary Statistics:
Runtime: 11 ms, faster than 55.24% of Python3 online submissions for Minimum Size Subarray Sum.
Memory Usage: 27.4 MB, less than 86.17% of Python3 online submissions for Minimum Size Subarray Sum.
'''
