'''
1004. Max Consecutive Ones III
Given a binary array nums and an integer k, return the maximum number of consecutive 1's in the array if you can flip at most k 0's.

Example 1:

Input: nums = [1,1,1,0,0,0,1,1,1,1,0], k = 2
Output: 6
Explanation: [1,1,1,0,0,1,1,1,1,1,1]
Bolded numbers were flipped from 0 to 1. The longest subarray is underlined.
'''
class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        maxCount = 0
        count = 0
        flippedCount = 0
        posList = deque()
        for i in range(len(nums)):
            if nums[i] == 1:
                count += 1
                maxCount = max(count, maxCount)
            elif nums[i] == 0 and flippedCount < k:
                posList.append(i)
                count += 1
                maxCount = max(count, maxCount)
                flippedCount += 1
            elif nums[i] == 0 and flippedCount >= k:
                if k != 0:
                    count = i - posList.popleft() - 1
                    count += 1
                    maxCount  = max(count, maxCount)
                    posList.append(i)
                else:
                    count = 0

        return maxCount
'''
Time Complexity: O(N)
Space Complexity: O(k)
'''
