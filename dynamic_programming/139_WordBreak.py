'''
Given a string s and a dictionary of strings wordDict, return true if s can be segmented into a space-separated sequence of one or more dictionary words.

Note that the same word in the dictionary may be reused multiple times in the segmentation.
'''
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = [False for _ in range(len(s) + 1)]
        dp[0] = True
        i = 0
        for i in range(len(s)):
            if dp[i] == True:
                for word in wordDict:
                    if s[i: i + len(word)] == word:
                        dp[i + len(word)] = True
        return dp[-1]
'''
Time Complexity: O(N)
Space Complexity: O(N)
**********************
Summary Statistics:
Runtime: 37 ms, faster than 76.06% of Python3 online submissions for Word Break.
Memory Usage: 16.4 MB, less than 97.56% of Python3 online submissions for Word Break.
'''
