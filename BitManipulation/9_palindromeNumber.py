'''
Given an integer x, return true if x is a palindrome, and false otherwise.
'''
class Solution:
    def isPalindrome(self, x: int) -> bool:

        x = str(x)

        return x == x[::-1]
'''
Time Complexity: O(len(x))
Space Complexity: O(len(x))
***************************
Summary Statistics:
Runtime: 50 ms, faster than 72.10% of Python3 online submissions for Palindrome Number.
Memory Usage: 16.5 MB, less than 93.16% of Python3 online submissions for Palindrome Number.
'''

