'''
Given an array of distinct integers nums and a target integer target, return the number of possible combinations that add up to target.

The test cases are generated so that the answer can fit in a 32-bit integer.



Example 1:

Input: nums = [1,2,3], target = 4
Output: 7
Explanation:
The possible combination ways are:
(1, 1, 1, 1)
(1, 1, 2)
(1, 2, 1)
(1, 3)
(2, 1, 1)
(2, 2)
(3, 1)
Note that different sequences are counted as different combinations.
'''
class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:

        dp = [0 for _ in range(target + 1)]
        dp[0] = 1
        for total in range(1, target + 1):
            for num in nums:
                if total - num >= 0:
                    dp[total] += dp[total - num]

        return dp[-1]
'''
Time Complexity: O(target*len(nums))
Space Complexity: O(target)
'''
