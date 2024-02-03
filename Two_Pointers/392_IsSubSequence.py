'''
Given two strings s and t, return true if s is a subsequence of t, or false otherwise.

A subsequence of a string is a new string that is formed from the original string by deleting some (can be none) of the characters without disturbing the relative positions of the remaining characters. (i.e., "ace" is a subsequence of "abcde" while "aec" is not).
'''
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if not s:
            return True
        bigLen = len(t)
        smallLen = len(s)
        i, j = 0, 0
        while i <= smallLen - 1 and j <= bigLen - 1:
            if s[i] == t[j]:
                i = i + 1
                j = j + 1
            else:
                j = j + 1

            if i == smallLen:
                return True

        return False
'''
Time Complexity: O(nigLen)
Space Complexity: O(1)
'''
