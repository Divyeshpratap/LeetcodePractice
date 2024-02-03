'''
Given two strings s and t, determine if they are isomorphic.

Two strings s and t are isomorphic if the characters in s can be replaced to get t.

All occurrences of a character must be replaced with another character while preserving the order of characters. No two characters may map to the same character, but a character may map to itself.
'''
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        sPos = {}
        tPos = {}
        for sChar, tChar in zip(s, t):
            if sChar not in sPos:
                sPos[sChar] = tChar
            elif sPos[sChar] != tChar:
                return False
            if tChar not in tPos:
                tPos[tChar] = sChar
            elif tPos[tChar] != sChar:
                return False
        return True
'''
Time Complexity: O(N)
Space Complexity: O(N)
'''
