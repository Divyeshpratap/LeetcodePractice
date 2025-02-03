'''
You are given an integer array nums and an integer k.

In one operation, you can pick two numbers from the array whose sum equals k and remove them from the array.

Return the maximum number of operations you can perform on the array.



Example 1:

Input: nums = [1,2,3,4], k = 5
Output: 2
Explanation: Starting with nums = [1,2,3,4]:
- Remove numbers 1 and 4, then nums = [2,3]
- Remove numbers 2 and 3, then nums = []
There are no more pairs that sum up to 5, hence a total of 2 operations.
'''
class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        nums = sorted(nums)
        start = 0
        end = len(nums) - 1
        count = 0
        while start < end:
            if nums[start] + nums[end] > k:
                end -= 1
            elif nums[start] + nums[end] < k:
                start += 1
            else:
                count += 1
                start += 1
                end -= 1
        return count
'''
Time Complexity: O(N)
Space Complexity: O(1)
'''
