'''
Given an array of integers arr, return true if the number of occurrences of each value in the array is unique or false otherwise.

Example 1:

Input: arr = [1,2,2,1,1,3]
Output: true
Explanation: The value 1 has 3 occurrences, 2 has 2 and 3 has 1. No two values have the same number of occurrences.
'''
class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:

        count = {}
        for num in arr:
            count[num] = count.get(num, 0) + 1

        occurrences = list(count.values())
        return len(occurrences) == len(set(occurrences))
'''
Time Complexity: O(len(arr))
Space complexity: O(len(arr))
'''
