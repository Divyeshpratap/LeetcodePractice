'''
You are given an integer array nums and an integer k. You want to find a subsequence of nums of length k that has the largest sum.

Return any such subsequence as an integer array of length k.

A subsequence is an array that can be derived from another array by deleting some or no elements without changing the order of the remaining elements.



Example 1:

Input: nums = [2,1,3,3], k = 2
Output: [3,3]
Explanation:
The subsequence has the largest sum of 3 + 3 = 6.
'''
class Solution:
    def maxSubsequence(self, nums: List[int], k: int) -> List[int]:
        import heapq
        elements = []
        for i in range(len(nums)):
            if len(elements) < k:
                heapq.heappush(elements, (nums[i], i))
            else:
                if nums[i] > elements[0][0]:
                    heapq.heappop(elements)
                    heapq.heappush(elements, (nums[i], i))

        indices = sorted([index for _, index in elements])

        return [nums[i] for i in indices]
'''
Time Complexity: O(nlog(n))
Space Complexity: O(n)
***************************
Summary Statistics:
Runtime: 4 ms, faster than 50.00% of Python3 online submissions for Find Subsequence of Length K With the Largest Sum.
Memory Usage: 17 MB, less than 23.64% of Python3 online submissions for Find Subsequence of Length K With the Largest Sum.
'''
