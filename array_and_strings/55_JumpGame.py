'''
You are given an integer array nums. You are initially positioned at the array's first index, and each element in the array represents your maximum jump length at that position.

Return true if you can reach the last index, or false otherwise.
'''
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        currMax = nums[0]
        for i in range(1, len(nums)):
            if currMax == 0:
                return False
            currMax = max(currMax - 1, nums[i])
        return True
'''
Time Complexity: O(N)
Space Complexity: O(1)
'''
