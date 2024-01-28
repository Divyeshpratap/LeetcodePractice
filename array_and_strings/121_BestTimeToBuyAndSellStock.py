'''
You are given an array prices where prices[i] is the price of a given stock on the ith day.

You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.
'''
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxDiff = 0
        minEle = prices[0]
        for index in range(len(prices) - 1):
            diff = prices[index + 1] - minEle
            if diff > maxDiff:
                maxDiff = diff
            if prices[index + 1] < minEle:
                minEle = prices[index + 1]

        if maxDiff < 0:
            return 0
        else:
            return maxDiff
'''
Time Complexity: O(N)
Space Complexity: O(1)
'''
