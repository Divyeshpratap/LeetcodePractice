'''
Given a string s which consists of lowercase or uppercase letters, return the length of the longest palindrome that can be built with those letters.

Letters are case sensitive, for example, "Aa" is not considered a palindrome.

 

Example 1:

Input: s = "abccccdd"
Output: 7
Explanation: One longest palindrome that can be built is "dccaccd", whose length is 7.
'''
class Solution:
    def longestPalindrome(self, s: str) -> int:
        
        char_count = {}
        for char in s:
            char_count[char] = char_count.get(char, 0) + 1
        
        odd_flag = False
        num_palindrome_length = 0
        for count in char_count.values():
            num_palindrome_length += (count // 2) * 2
            if (count % 2) == 1:
                odd_flag = True
        
        return num_palindrome_length + 1 if odd_flag else num_palindrome_length
'''
Time Complexity: O(n)
Space complexity: O(n)
'''
