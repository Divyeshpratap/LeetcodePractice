'''
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

    Open brackets must be closed by the same type of brackets.
    Open brackets must be closed in the correct order.
    Every close bracket has a corresponding open bracket of the same type.
'''
class Solution:
    def isValid(self, s: str) -> bool:
        stack = deque()
        paranthesisDict = {
            '(' : ')',
            '{' : '}',
            '[' : ']'
        }
        for item in s:
            if item in paranthesisDict:
                stack.append(item)
            elif item in paranthesisDict.values():
                if not stack or paranthesisDict[stack.pop()] != item:
                    return False
            else:
                print(f'Invalid item: {item}')
                return False
        if not stack:
            return True
        else:
            return False
'''
Time Complexity: O(N)
Space Complexity: O(N)
**********************
Summary Statistics:
Runtime: 30 ms, faster than 87.76% of Python3 online submissions for Valid Parentheses.
Memory Usage: 16.5 MB, less than 68.46% of Python3 online submissions for Valid Parentheses.
'''
