'''
Given two strings s and t, return true if t is an anagram of s, and false otherwise.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.
'''
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        str1 = set(s)
        str2 = set(t)
        if len(s) != len(t):
            return False
        charCount = {}
        for item in s:
            charCount[item] = 1 + charCount.get(item, 0)
        for item in t:
            charCount[item] = charCount.get(item, 0) - 1
        # print(charStr1)
        # print(charStr2)
        for value in charCount.values():
            if value != 0:
                return False
        return True
'''
Time Complexity: O(len(s)+len(t))
Space Complexity: O(len(s)+len(t))
'''
