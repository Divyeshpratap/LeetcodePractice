'''
Given an input string s, reverse the order of the words.

A word is defined as a sequence of non-space characters. The words in s will be separated by at least one space.

Return a string of the words in reverse order concatenated by a single space.

Note that s may contain leading or trailing spaces or multiple spaces between two words. The returned string should only have a single space separating the words. Do not include any extra spaces.
'''
class Solution:
    def reverseWords(self, s: str) -> str:
        s = s.strip()
        s = s.split()
        s = s[::-1]
        return ' '.join(s)
'''
Time Complexity: O(N)
Space Complexity: O(1)
Runtime: 39 ms, faster than 40.11% of Python3 online submissions for Reverse Words in a String.
Memory Usage: 16.6 MB, less than 66.73% of Python3 online submissions for Reverse Words in a String.
'''
