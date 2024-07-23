'''
Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.

You must write an algorithm that runs in O(n) time.
'''
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0

        numSet = set(nums)

        currStreak = 0
        maxStreak = 0
        for num in nums:
            if num - 1 not in numSet:
                currNum = num
                currStreak = 1
                while currNum + 1 in numSet:
                    currNum += 1
                    currStreak += 1
                maxStreak = max(currStreak, maxStreak)


        return maxStreak
'''
Time Complexity: O(N)
Space Complexity: O(N)
**********************
Summary Statistics:
Runtime: 5401 ms, faster than 9.35% of Python3 online submissions for Longest Consecutive Sequence.
Memory Usage: 31.6 MB, less than 87.30% of Python3 online submissions for Longest Consecutive Sequence.
'''
