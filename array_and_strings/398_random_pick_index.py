'''
Given an integer array nums with possible duplicates, randomly output the index of a given target number. You can assume that the given target number must exist in the array.

Implement the Solution class:

Solution(int[] nums) Initializes the object with the array nums.
int pick(int target) Picks a random index i from nums where nums[i] == target. If there are multiple valid i's, then each index should have an equal probability of returning.

'''
# First Solution
import random
class Solution:

    def __init__(self, nums: List[int]):
        self.nums = nums
    def pick(self, target: int) -> int:
        count = 0
        result = None
        for i, num in enumerate(self.nums):
            if num == target:
                count += 1
                if random.randrange(count) == 0:
                    result = i
        return result

# Second Solution:
# Reservoir Sampling
import random
class Solution:

    def __init__(self, nums: List[int]):
        self.nums = nums
    def pick(self, target: int) -> int:
        count = 0
        result = None
        for i, num in enumerate(self.nums):
            if num == target:
                count += 1
                if random.randrange(count) == 0:
                    result = i
        return result
'''
Time Complexity: O(N)
Space Complexity: O(1)
'''
