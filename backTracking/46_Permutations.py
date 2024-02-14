'''
Given an array nums of distinct integers, return all the possible permutations. You can return the answer in any order.
Example 1:

Input: nums = [1,2,3]
Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
'''
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        length = len(nums)
        result = []
        def backTrack(item, k):
            nonlocal nums
            if k == length:
                result.append(item)
            else:
                for i in nums:
                    if i in set(item):
                        continue
                    else:
                        
                        backTrack(item + [i], k + 1 )
            
                        
        backTrack([], 0)
        return result
'''
Time Complexity: O(n*n!)
Space Complexity: O(n*n!)
'''
