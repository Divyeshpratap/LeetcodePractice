'''
You are climbing a staircase. It takes n steps to reach the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?
'''
class Solution:
    def climbStairs(self, n: int) -> int:
        dp = [0 for _ in range(n + 1)]
        dp[0] = 0
        dp[1] = 1
        for i in range(2, n + 1):
            if i == 2:
                dp[i] = 2
            else:
                dp[i] = dp[i - 1] + dp[i - 2]
        return dp[n]
'''
Time Complexity: O(n)
Space Complexity: O(n)
**********************
Summary Statistics:
Runtime: 35 ms, faster than 51.10% of Python3 online submissions for Climbing Stairs.
Memory Usage: 16.4 MB, less than 96.86% of Python3 online submissions for Climbing Stairs.
'''
