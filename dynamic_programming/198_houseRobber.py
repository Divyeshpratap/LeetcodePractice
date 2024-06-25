'''
You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed, the only constraint stopping you from robbing each of them is that adjacent houses have security systems connected and it will automatically contact the police if two adjacent houses were broken into on the same night.

Given an integer array nums representing the amount of money of each house, return the maximum amount of money you can rob tonight without alerting the police.
'''
class Solution:
    def rob(self, nums: List[int]) -> int:

        dp = [0] * (len(nums) + 1)
        if len(nums) == 1:
            return nums[0]
        print(f'dp is {dp}')
        dp[0] = 0
        dp[1] = nums[0]
        for i in range(1, len(nums)):
            dp[i + 1] = max(dp[i-1] + nums[i], dp[i])

        return max(dp[-1], dp[- 2])
'''
Time Complexity: O(N)
Space Complexity: O(N)
'''
