'''
A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.

Given a string s, return true if it is a palindrome, or false otherwise.
'''
class Solution:
    def isPalindrome(self, s: str) -> bool:
        ls = s.lower()
        phrase = ''
        for item in ls:
            if ord('a') <= ord(item) <= ord('z') or ord('0') <= ord(item) <=ord('9'):
                phrase = phrase + item
        return phrase == phrase[::-1]
'''
Time Complexity = O(N)
Space Complexity =O(N)
'''
