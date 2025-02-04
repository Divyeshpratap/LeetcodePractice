'''
Given a binary array nums, return the maximum number of consecutive 1's in the array if you can flip at most one 0.
Example 1:

Input: nums = [1,0,1,1,0]
Output: 4
Explanation:
- If we flip the first zero, nums becomes [1,1,1,1,0] and we have 4 consecutive ones.
- If we flip the second zero, nums becomes [1,0,1,1,1] and we have 3 consecutive ones.
The max number of consecutive ones is 4.
'''
class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        maxCount = 0
        flag = False
        count = 0
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
        return maxCount
'''
Time Complexity: O(N)
Space Complexity: O(1)
**********************
I don't have leetcode premium so couldn't run the test cases but the logic seems correct to me, and I did dry run on a few test cases.
'''

