'''
Given an integer array nums and an integer k, return true if there are two distinct indices i and j in the array such that nums[i] == nums[j] and abs(i - j) <= k
'''
class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        distinctNum = {}
        for i, item in enumerate(nums):
            if item not in distinctNum:
                distinctNum[item] = i
            else:
                diff = i - distinctNum[item]
                distinctNum[item] = i
                if diff <= k:

                    return True
        return False
'''
Time Complexity: O(N)
Space Complexity: O(N)
'''
