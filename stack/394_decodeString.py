'''
Given an encoded string, return its decoded string.

The encoding rule is: k[encoded_string], where the encoded_string inside the square brackets is being repeated exactly k times. Note that k is guaranteed to be a positive integer.

You may assume that the input string is always valid; there are no extra white spaces, square brackets are well-formed, etc. Furthermore, you may assume that the original data does not contain any digits and that digits are only for those repeat numbers, k. For example, there will not be input like 3a or 2[4].

The test cases are generated so that the length of the output will never exceed 105.

Example 1:

Input: s = "3[a]2[bc]"
Output: "aaabcbc"
'''
class Solution:
    def decodeString(self, s: str) -> str:

        stack = []
        i = len(s) - 1
        while i >= 0:
            if s[i] != '[':
                stack.append(s[i])
            else:
                ele = ''
                while stack[-1] != ']':
                    ele += stack.pop()
                stack.pop()
                num = ''
                while (i - 1) >= 0 and s[i - 1].isdigit():
                    num += s[i - 1]
                    i -= 1
                ele = int(num[::-1]) * ele
                stack.append(ele)
            i -=1

        k = ''
        while stack:
            k += stack.pop()
        return k
'''
Time Complexity: O(len(s))
Space Complexity: O(len(s))
'''
