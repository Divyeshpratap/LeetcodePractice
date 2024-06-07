'''
You are given a sorted unique integer array nums.

A range [a,b] is the set of all integers from a to b (inclusive).

Return the smallest sorted list of ranges that cover all the numbers in the array exactly. That is, each element of nums is covered by exactly one of the ranges, and there is no integer x such that x is in one of the ranges but not in nums.

Each range [a,b] in the list should be output as:

    "a->b" if a != b
    "a" if a == b
'''
class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        intervalList = []
        continousList = []
        nums.append(float('inf'))
        for i in range(1, len(nums)):
            if nums[i - 1] == nums[i] - 1:
                continousList.append(nums[i - 1])
            else:
                continousList.append(nums[i - 1])
                if len(continousList) > 1:
                    intervalList.append(str(continousList[0])+'->'+str(continousList[-1]))
                else:
                    intervalList.append(str(continousList[0]))
                continousList = []


        return intervalList
'''
Time Complexity: O(N)
Space Complexity: O(N)
****************
Summary Stats:

Runtime: 28 ms, faster than 90.98% of Python3 online submissions for Summary Ranges.
Memory Usage: 16.3 MB, less than 98.07% of Python3 online submissions for Summary Ranges.
'''
