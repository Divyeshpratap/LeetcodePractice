'''
Given a pattern and a string s, find if s follows the same pattern.

Here follow means a full match, such that there is a bijection between a letter in pattern and a non-empty word in s.
'''
class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        pattern = list(pattern)
        s = s.split()
        if len(s) != len(pattern):
            return False
        sComplement = {}
        patternComplement = {}
        for pChar, sWord in zip(pattern, s):
            if pChar not in patternComplement:
                patternComplement[pChar] = sWord
            elif patternComplement[pChar] != sWord:
                return False
            if sWord not in sComplement:
                sComplement[sWord] = pChar
            elif sComplement[sWord] != pChar:
                return False
        return True
'''
Time Complexity: O(N)
Space Complexity: O(N)
'''
