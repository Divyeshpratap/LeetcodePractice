'''
152. Maximum Product Subarray
Solved
Medium
Topics
premium lock icon
Companies
Given an integer array nums, find a subarray that has the largest product, and return the product.

The test cases are generated so that the answer will fit in a 32-bit integer.



Example 1:

Input: nums = [2,3,-2,4]
Output: 6
Explanation: [2,3] has the largest product 6.
Example 2:

Input: nums = [-2,0,-1]
Output: 0
Explanation: The result cannot be 2, because [-2,-1] is not a subarray.
'''
class Solution:
    def maxProduct(self, nums: List[int]) -> int:

        max_prod = 1
        min_prod = 1
        res = max(nums)
        for num in nums:
            if num == 0:
                max_prod = 1
                min_prod = 1
            temp = max_prod
            max_prod = max(max_prod * num, min_prod * num, num)
            min_prod = min(temp * num, min_prod * num, num)

            res = max(max_prod, res)

        return res
'''
Time Complexity: O(n)
Space Complexity: O(1)
'''
