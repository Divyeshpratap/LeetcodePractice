'''
Given two 0-indexed integer arrays nums1 and nums2, return a list answer of size 2 where:

answer[0] is a list of all distinct integers in nums1 which are not present in nums2.
answer[1] is a list of all distinct integers in nums2 which are not present in nums1.
Note that the integers in the lists may be returned in any order.

Example 1:

Input: nums1 = [1,2,3], nums2 = [2,4,6]
Output: [[1,3],[4,6]]
Explanation:
For nums1, nums1[1] = 2 is present at index 0 of nums2, whereas nums1[0] = 1 and nums1[2] = 3 are not present in nums2. Therefore, answer[0] = [1,3].
For nums2, nums2[0] = 2 is present at index 1 of nums1, whereas nums2[1] = 4 and nums2[2] = 6 are not present in nums2. Therefore, answer[1] = [4,6].
'''
class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:

        allNums = nums1 + nums2
        allNums = set(allNums)
        nums1 = set(nums1)
        nums2 = set(nums2)
        first = []
        second = []
        for item in allNums:
            if item not in nums1:
                second.append(item)
            elif item not in nums2:
                first.append(item)

        return [first, second]
'''
Time Complexity: O(len(nums1) + len(nums2))
Space Complexity: O(len(nums1) + len(nums2))
'''
