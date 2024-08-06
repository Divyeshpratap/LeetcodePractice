'''
A peak element is an element that is strictly greater than its neighbors.

Given a 0-indexed integer array nums, find a peak element, and return its index. If the array contains multiple peaks, return the index to any of the peaks.

You may imagine that nums[-1] = nums[n] = -∞. In other words, an element is always considered to be strictly greater than a neighbor that is outside the array.

You must write an algorithm that runs in O(log n) time.
'''
class Solution:
    def findPeakElement(self, nums: List[int]) -> int:

        def binarySearch(left, right):
            if left > right:
                return (left + right)//2
            mid = (left + right)//2

            if (mid > 0) and nums[mid - 1] > nums[mid]:
                pos = binarySearch(left, mid - 1)
            elif (mid < len(nums) - 1) and nums[mid + 1] > nums[mid]:
                pos = binarySearch(mid + 1, right)
            else:
                pos = mid

            return pos

        return binarySearch(0, len(nums) - 1)
'''
Time Complexity: O(log(n))
Space Complexity: O(log(n))
***************************
Summary Statistics:
Runtime: 48 ms, faster than 47.85% of Python3 online submissions for Find Peak Element.
Memory Usage: 17.2 MB, less than 18.76% of Python3 online submissions for Find Peak Element.
'''
