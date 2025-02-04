'''
Given a binary array nums, you should delete one element from it.

Return the size of the longest non-empty subarray containing only 1's in the resulting array. Return 0 if there is no such subarray.

Example 1:

Input: nums = [1,1,0,1]
Output: 3
Explanation: After deleting the number in position 2, [1,1,1] contains 3 numbers with value of 1's.
'''
class Solution:
    def longestSubarray(self, nums: List[int]) -> int:

        maxCount =  0
        count = 0
        flag = False
        for i in range(len(nums)):
            if nums[i] == 1:
                count += 1
                maxCount = max(count, maxCount)
            elif nums[i] == 0 and flag == False:
                pos = i
                count += 1
                flag = True
                maxCount = max(count, maxCount)
            elif nums[i] == 0 and flag == True:
                count = i - pos - 1
                count += 1
                pos = i
                flag = True
                maxCount = max(count, maxCount)

        return maxCount - 1
'''
Time Complexity: O(N)
Space Complexity: O(1)
'''
