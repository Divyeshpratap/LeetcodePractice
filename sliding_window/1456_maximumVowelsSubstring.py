'''
Given a string s and an integer k, return the maximum number of vowel letters in any substring of s with length k.

Vowel letters in English are 'a', 'e', 'i', 'o', and 'u'.

Example 1:

Input: s = "abciiidef", k = 3
Output: 3
Explanation: The substring "iii" contains 3 vowel letters.
'''
class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = {'a', 'e', 'i', 'o', 'u'}

        maxVowel = sum([1 if vowel in vowels else 0 for vowel in s[:k]])
        currVowel = maxVowel
        for i in range(1, len(s) - k + 1):
            currVowel -= (1 if s[i - 1] in vowels else 0)
            currVowel += (1 if s[i + k - 1] in vowels else 0)
            maxVowel = max(maxVowel, currVowel)

        return maxVowel
'''
Time Complexity: O(N)
Space Complexity: O(1)
'''
