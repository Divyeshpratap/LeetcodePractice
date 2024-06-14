'''
Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets.
'''
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        ls = []
        nums.sort()
        i = 0
        for i in range(len(nums) - 1):
            if i > 0 and nums[i] == nums[i - 1]:
                print(f' nums[i] and nums[i-1] values are {i} and {i-1}')
                continue
            left = i + 1
            right = len(nums) - 1
            while left < right:
                if nums[i] + nums[left] + nums[right] < 0:
                    left = left + 1
                elif nums[i] + nums[left] + nums[right] > 0:
                    right = right - 1

                else:
                    ls.append([nums[i], nums[left], nums[right]])
                    while left < right and nums[left] == nums[left + 1]:
                        left = left + 1
                    while left < right and nums[right] == nums[right - 1]:
                        right = right - 1
                    left += 1
                    right -= 1

        return ls
'''
Time Complexity: O(n^2)
Space Complexity: O(n)
Summary Statistics:
Runtime: 818 ms, faster than 36.10% of Python3 online submissions for 3Sum.
Memory Usage: 20.7 MB, less than 46.09% of Python3 online submissions for 3Sum.
'''
