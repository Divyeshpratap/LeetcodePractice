'''
Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

You must write an algorithm with O(log n) runtime complexity.
'''
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:

        def binaryTree(start, end):
            if start <= end:
                mid = (start + end)//2
                if target == nums[mid]:
                    return mid
                elif target < (nums[mid]):
                    return binaryTree(start, mid - 1)
                else:
                    return binaryTree(mid + 1, end)
            else:
                return start

        return binaryTree(0, len(nums) - 1)

'''
Time Complexity: O(logn)
Space Complexity: O(logn)
************************
Summary Statistics:
Runtime: 46 ms, faster than 78.04% of Python3 online submissions for Search Insert Position.
Memory Usage: 17.6 MB, less than 16.03% of Python3 online submissions for Search Insert Position.
'''
