'''
You may recall that an array arr is a mountain array if and only if:

arr.length >= 3
There exists some index i (0-indexed) with 0 < i < arr.length - 1 such that:
arr[0] < arr[1] < ... < arr[i - 1] < arr[i]
arr[i] > arr[i + 1] > ... > arr[arr.length - 1]
Given an integer array arr, return the length of the longest subarray, which is a mountain. Return 0 if there is no mountain subarray.



Example 1:

Input: arr = [2,1,4,7,3,2,5]
Output: 5
Explanation: The largest mountain is [1,4,7,3,2] which has length 5.
'''
class Solution:
    def longestMountain(self, arr: List[int]) -> int:

        left, right = 1, 1
        max_len = 0
        for i in range(1, len(arr) - 1):
            left = 0
            while i - left - 1 >= 0 and arr[i - left - 1] < arr[i - left]:
                left += 1
            right = 0
            while i + right + 1< len(arr) and arr[i + right + 1] < arr[i + right]:
                right += 1
            if left == 0 or right == 0:
                curr_len = 0
            else:
                curr_len = right + left + 1
            max_len = max(curr_len, max_len)
        return max_len
'''
Time Complexity: O(n^2)
Space Complexity: O(1)
'''
