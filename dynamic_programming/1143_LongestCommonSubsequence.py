'''
Given two strings text1 and text2, return the length of their longest common subsequence. If there is no common subsequence, return 0.

A subsequence of a string is a new string generated from the original string with some characters (can be none) deleted without changing the relative order of the remaining characters.

For example, "ace" is a subsequence of "abcde".
A common subsequence of two strings is a subsequence that is common to both strings.
'''
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:

        str1Len = len(text1)
        str2Len = len(text2)

        dp = [[0 for _ in range(str2Len + 1)] for _ in range(str1Len + 1)]
        for i in range(str1Len + 1):
            for j in range(str2Len + 1):
                if i == 0 or j == 0:
                    dp[i][j] = 0
                else:
                    if text1[i - 1] == text2[j - 1]:
                        dp[i][j] = dp[i-1][j-1] + 1
                    elif text1[i - 1] != text2[j - 1]:
                        dp[i][j] = max(dp[i-1][j], dp[i][j-1])
        return dp[i][j]
'''
Time Complexity: O(len(sting1)*len(string2))
Space Complexity: O(len(string1)*len(string2))
**********************************************
Summary Statistics:
Runtime: 624 ms, faster than 32.88% of Python3 online submissions for Longest Common Subsequence.
Memory Usage: 42.5 MB, less than 35.40% of Python3 online submissions for Longest Common Subsequence.
'''

