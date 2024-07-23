'''
Given two integers n and k, return all possible combinations of k numbers chosen from the range [1, n].

You may return the answer in any order.
Example:
Input: n = 4, k = 2
Output: [[1,2],[1,3],[1,4],[2,3],[2,4],[3,4]]
Explanation: There are 4 choose 2 = 6 total combinations.
Note that combinations are unordered, i.e., [1,2] and [2,1] are considered to be the same combination.
'''
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:

        out = []

        def backTrack(start, combination, end):
            if end == 0:
                out.append(combination[:])
                return

            for i in range(start, n + 1):
                combination.append(i)
                backTrack(i + 1, combination, end - 1)
                combination.pop()


        backTrack(1, [], k)
        return out
'''
Time Complexity: O(n combination k)
Space Complexit: O(k * (n combination k))
*****************************************
Runtime: 701 ms, faster than 67.40% of Python3 online submissions for Combinations.
Memory Usage: 64.8 MB, less than 44.58% of Python3 online submissions for Combinations.
'''
