'''
Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.
Example:
Input: n = 3
Output: ["((()))","(()())","(())()","()(())","()()()"]
'''
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:

        def validParanthesis(combination):
            stack = []
            for item in combination:
                if item == '(':
                    stack.append(item)
                elif item == ')' and stack:
                    stack.pop()
                elif item ==')' and not stack:
                    return False

            return True if len(stack) == 0 else False

        def backTrack(paranthesis):
            if len(paranthesis) == 2*n:
                if validParanthesis(paranthesis):
                    result.append(''.join(paranthesis))
                return
            else:
                for k in ['(', ')']:
                    paranthesis.append(k)
                    backTrack(paranthesis)
                    paranthesis.pop()

        result = []
        backTrack([])
        return result
'''
Time Complexity: O((2^n).n)
***************************
Summary Statistics:
Runtime: 84 ms, faster than 5.18% of Python3 online submissions for Generate Parentheses.
Memory Usage: 17 MB, less than 11.40% of Python3 online submissions for Generate Parentheses.
'''
