'''
You are given a 0-indexed array of integers nums of length n. You are initially positioned at nums[0].

Each element nums[i] represents the maximum length of a forward jump from index i. In other words, if you are at nums[i], you can jump to any nums[i + j] where:

    >>0 <= j <= nums[i] and
    >>i + j < n
Return the minimum number of jumps to reach nums[n - 1]. The test cases are generated such that you can reach nums[n - 1].
'''
class Solution:
    def jump(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 0
        count = 0
        left, right = 0, 0
        furthest = 0 + nums[0]
        right = furthest
        count = 1
        left = 1
        while right < len(nums) - 1:

            for i in range(left, right + 1):
                furthest = max(furthest, nums[i] + i)

            left = right + 1
            right = furthest
            count = count + 1
        return count
'''
Time Complexity: O(N^2)
Space Complexity: O(1)
Summary Statistics:
Runtime: 96 ms, faster than 94.07% of Python3 online submissions for Jump Game II.
Memory Usage: 17.4 MB, less than 91.93% of Python3 online submissions for Jump Game II.
'''
