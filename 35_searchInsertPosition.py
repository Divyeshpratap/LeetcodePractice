'''
Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

You must write an algorithm with O(log n) runtime complexity.
'''
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:

        def binarySearch(left, right):
            if left <= right:
                mid = (left + right)//2
            # mid = (left + right)//2
                if target == nums[mid]:
                    pos = mid
                elif nums[mid] < target:
                    pos = binarySearch(mid + 1, right)
                elif nums[mid] > target:
                    pos = binarySearch(left, mid - 1)
                return pos
            else:
                return left

        return binarySearch(0, len(nums) - 1)
'''
Time Complexity: O(logn)
Space Complexity: O(logn)
*************************
Summary Statistics:
Runtime: 43 ms, faster than 91.16% of Python3 online submissions for Search Insert Position.
Memory Usage: 17.5 MB, less than 5.97% of Python3 online submissions for Search Insert Position.
'''
