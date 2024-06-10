'''
Given an integer array nums sorted in non-decreasing order, remove some duplicates in-place such that each unique element appears at most twice. The relative order of the elements should be kept the same.

Since it is impossible to change the length of the array in some languages, you must instead have the result be placed in the first part of the array nums. More formally, if there are k elements after removing the duplicates, then the first k elements of nums should hold the final result. It does not matter what you leave beyond the first k elements.

Return k after placing the final result in the first k slots of nums.

Do not allocate extra space for another array. You must do this by modifying the input array in-place with O(1) extra memory.
'''
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        currPos = 0
        for item in nums:
            if currPos < 2 or item > nums[currPos - 2]:
                nums[currPos] = item
                currPos = currPos + 1
        return currPos
'''
Time Complexity: O(n)
Space Complexity: O(1)
**********************
Second Simpler but less efficient solution
'''
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:

        for i in reversed(range(2, len(nums))):
            if nums[i] == nums[i - 1] == nums[i - 2]:
                nums.pop(i)
'''
Time Complexity: O(n^2)
Space Complexity: O(1)
**********************
Summary Statistics:
Runtime: 55 ms, faster than 35.03% of Python3 online submissions for Remove Duplicates from Sorted Array II.
Memory Usage: 16.4 MB, less than 93.99% of Python3 online submissions for Remove Duplicates from Sorted Array II.
'''

