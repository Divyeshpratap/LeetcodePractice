''
You are given an integer array coins representing coins of different denominations and an integer amount representing a total amount of money.

Return the fewest number of coins that you need to make up that amount. If that amount of money cannot be made up by any combination of the coins, return -1.

You may assume that you have an infinite number of each kind of coin.
'''
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [[0 for _ in range(amount + 1)] for _ in range(len(coins) + 1)]
        for i in range(1, amount + 1):
            dp[0][i] = float('inf')
        for i in range(1, len(coins) + 1):
            for j in range(1, amount + 1):
                if coins[i - 1] > j:
                    dp[i][j] = dp[i - 1][j]
                else:
                    dp[i][j] = min(dp[i - 1][j], dp[i][j - coins[i - 1]] + 1)
        if dp[len(coins)][amount] == float('inf'):
            return -1
        else:
            return dp[len(coins)][amount]
'''
Time Complexity: O(len(coins) * len(amount))
Space Complexity: O(len(coins) * len(amount))
'''
