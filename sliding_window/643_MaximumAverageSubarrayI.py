'''
You are given an integer array nums consisting of n elements, and an integer k.

Find a contiguous subarray whose length is equal to k that has the maximum average value and return this value. Any answer with a calculation error less than 10-5 will be accepted.

Example 1:

Input: nums = [1,12,-5,-6,50,3], k = 4
Output: 12.75000
Explanation: Maximum average is (12 - 5 - 6 + 50) / 4 = 51 / 4 = 12.75
'''
class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:

        maxSum = currSum = sum(nums[:k])
        for i in range(1, len(nums) - k + 1):
            currSum = currSum - nums[i - 1] + nums[i + k - 1]
            maxSum = max(currSum, maxSum)

        return maxSum/k
'''
Time Complexity: O(N)
Space Complexity: O(1)
'''

