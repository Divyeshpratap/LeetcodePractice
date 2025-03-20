'''
Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.



Example 1:

Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]
Example 2:

Input: nums = [1], k = 1
Output: [1]
'''
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        nums_dict = {}
        for num in nums:
            nums_dict[num] = nums_dict.get(num, 0) + 1

        freq_list = [[] for _ in range(len(nums))]

        for num, count in nums_dict.items():
            freq_list[count - 1].append(num)

        result = []
        for item in reversed(freq_list):
            for num in item:
                result.append(num)
                if len(result) == k:
                    return result
        return result
'''
Time Complexity: O(N)
Space Complexity: O(N)
'''
