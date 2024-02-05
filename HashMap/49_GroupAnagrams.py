'''
Given an array of strings strs, group the anagrams together. You can return the answer in any order.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.
'''
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram = {}
        for word in strs:
            tempWord = ''.join(sorted(word))
            if tempWord in anagram:
                anagram[tempWord].append(word)
            else:
                anagram[tempWord] = [word]
        return list(anagram.values())
'''
Time Complexity: O(Nlog(N))
Space Complexity: O(N)
'''
