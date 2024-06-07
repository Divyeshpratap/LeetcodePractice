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

**************
2nd Approach (easier to understand)
'''
class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        hashSet = set()
        for i in range(len(nums)):
            if i > k:
                hashSet.remove(nums[i - k - 1])
            if nums[i] in hashSet:
                return True
            else:
                hashSet.add(nums[i])
        return False
'''
Time Complexity: O(N)
Space Complexity: O(k)
'''
