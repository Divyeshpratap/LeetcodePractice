'''
You are given an array prices where prices[i] is the price of a given stock on the ith day.

You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.
'''
'''
*****Greedy Approach*****
'''
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minPrice = prices[0]
        maxProfit = 0
        for i in range(1, len(prices)):
            profit = prices[i] - minPrice
            maxProfit = max(maxProfit, profit)
            minPrice = min(minPrice, prices[i])
        return maxProfit
'''
Time Complexity: O(N)
Space Complexity: O(1)
'''
