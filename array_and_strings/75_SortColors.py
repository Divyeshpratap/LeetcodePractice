'''
Given an array nums with n objects colored red, white, or blue, sort them in-place so that objects of the same color are adjacent, with the colors in the order red, white, and blue.

We will use the integers 0, 1, and 2 to represent the color red, white, and blue, respectively.

You must solve this problem without using the library's sort function.



Example 1:

Input: nums = [2,0,2,1,1,0]
Output: [0,0,1,1,2,2]
'''
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        def swap(i, j):
            temp = nums[i]
            nums[i] = nums[j]
            nums[j] = temp

        left, right = 0 , len(nums) - 1
        i = 0
        while i <= right:
            if nums[i] == 0:
                swap(left, i)
                left += 1
            elif nums[i] == 2:
                swap(i, right)
                right -= 1
                i -= 1
            i += 1
'''
Time Complexity: O(len(nums))
Space Complexity: O(1)
**********************
Summary statistics:
Runtime: 0 ms, faster than 100.00% of Python3 online submissions for Sort Colors.
Memory Usage: 16.7 MB, less than 19.29% of Python3 online submissions for Sort Colors.
'''
