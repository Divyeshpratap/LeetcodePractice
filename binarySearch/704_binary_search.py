'''
Given an array of integers nums which is sorted in ascending order, and an integer target, write a function to search target in nums. If target exists, then return its index. Otherwise, return -1.

You must write an algorithm with O(log n) runtime complexity.

Example 1:

Input: nums = [-1,0,3,5,9,12], target = 9
Output: 4
Explanation: 9 exists in nums and its index is 4
'''
class Solution:
    def search(self, nums: List[int], target: int) -> int:


        def divide_and_conquer(start, end):
            if start > end:
                return -1

            mid = (start + end) // 2

            if target == nums[mid]:
                return mid
            elif target > nums[mid]:
                return divide_and_conquer(mid + 1, end)
            elif target < nums[mid]:
                return divide_and_conquer(start, mid - 1)

        return divide_and_conquer(0, len(nums) - 1)
'''
Time Complexity: O(log(n))
Space Complexity: O(log(n))
'''
