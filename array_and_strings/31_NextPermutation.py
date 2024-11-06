'''
A permutation of an array of integers is an arrangement of its members into a sequence or linear order.

For example, for arr = [1,2,3], the following are all the permutations of arr: [1,2,3], [1,3,2], [2, 1, 3], [2, 3, 1], [3,1,2], [3,2,1].
The next permutation of an array of integers is the next lexicographically greater permutation of its integer. More formally, if all the permutations of the array are sorted in one container according to their lexicographical order, then the next permutation of that array is the permutation that follows it in the sorted container. If such arrangement is not possible, the array must be rearranged as the lowest possible order (i.e., sorted in ascending order).

For example, the next permutation of arr = [1,2,3] is [1,3,2].
Similarly, the next permutation of arr = [2,3,1] is [3,1,2].
While the next permutation of arr = [3,2,1] is [1,2,3] because [3,2,1] does not have a lexicographical larger rearrangement.
Given an array of integers nums, find the next permutation of nums.

The replacement must be in place and use only constant extra memory.



Example 1:

Input: nums = [1,2,3]
Output: [1,3,2]
'''
class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if len(nums) == 1:
            return

        descending  = True
        for i in range(len(nums) - 1, 0 , -1):
            if nums[i - 1] < nums[i]:
                for j in range(len(nums) - 1, i - 1, -1):
                    if nums[j] > nums[i - 1]:
                        temp = nums[j]
                        nums[j] = nums[i - 1]
                        nums[i - 1] = temp
                        nums[i:] = nums[i:][::-1]
                        descending = False
                        break
                if descending == False:
                    break
        if descending == True:
            nums[:] = nums[::-1]
'''
Time Complexity: O(N)
Space Complexity: O(1)
**********************
Summary Statistics:
Runtime: 0 ms, faster than 100.00% of Python3 online submissions for Next Permutation.
Memory Usage: 16.6 MB, less than 27.38% of Python3 online submissions for Next Permutation.
'''