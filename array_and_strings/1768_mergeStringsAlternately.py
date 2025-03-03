'''
You are given two strings word1 and word2. Merge the strings by adding letters in alternating order, starting with word1. If a string is longer than the other, append the additional letters onto the end of the merged string.

Return the merged string.
Example 1:

Input: word1 = "abc", word2 = "pqr"
Output: "apbqcr"
Explanation: The merged string will be merged as so:
word1:  a   b   c
word2:    p   q   r
merged: a p b q c r
'''
class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:

        mergeString = ''
        i, j = 0, 0
        while i < len(word1) and i < len(word2):
            mergeString += word1[i]
            mergeString += word2[i]
            i += 1
        if len(word1) > len(word2):
            mergeString += word1[len(word2):len(word1)]
        elif len(word2) > len(word1):
            mergeString += word2[len(word1):len(word2)]

        return mergeString
'''
Time Complexity: O(len(word1) + len(word2)) -> O(n)
Space Complexity: O(n)
'''

