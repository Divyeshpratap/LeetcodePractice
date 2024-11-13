'''
Given an integer array of size n, find all elements that appear more than ⌊ n/3 ⌋ times.



Example 1:

Input: nums = [3,2,3]
Output: [3]
'''
class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:

        firstMajorEle = float('-inf')
        firstCount = 0
        secondMajorEle = float('-inf')
        secondCount = 0

        for num in nums:
            if firstCount == 0 and secondMajorEle != num:
                firstCount += 1
                firstMajorEle = num
            elif secondCount == 0 and firstMajorEle != num:
                secondCount += 1
                secondMajorEle  = num
            elif firstMajorEle == num:
                firstCount += 1
            elif secondMajorEle == num:
                secondCount += 1
            else:
                firstCount -= 1
                secondCount -= 1

        firstCount = 0
        secondCount = 0
        minCount = len(nums) / 3
        for num in nums:
            if num == firstMajorEle:
                firstCount += 1
            elif secondMajorEle != float('-inf') and num == secondMajorEle:
                secondCount += 1
        ls = []
        if firstCount > minCount:
            ls.append(firstMajorEle)
        if secondCount > minCount:
            ls.append(secondMajorEle)
        return ls
'''
Time Complexity: O(len(nums))
Space Complexity: O(1)
**********************
Summary Statistics:
Runtime: 5 ms, faster than 46.12% of Python3 online submissions for Majority Element II.
Memory Usage: 18.2 MB, less than 21.79% of Python3 online submissions for Majority Element II.
'''
