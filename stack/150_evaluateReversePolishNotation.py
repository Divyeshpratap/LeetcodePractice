'''
You are given an array of strings tokens that represents an arithmetic expression in a Reverse Polish Notation.

Evaluate the expression. Return an integer that represents the value of the expression.

Note that:

The valid operators are '+', '-', '*', and '/'.
Each operand may be an integer or another expression.
The division between two integers always truncates toward zero.
There will not be any division by zero.
The input represents a valid arithmetic expression in a reverse polish notation.
The answer and all the intermediate calculations can be represented in a 32-bit integer.
'''
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operatorSet = {'+', '-', '*', '/'}
        stack = []
        for item in tokens:
            if item not in operatorSet:
                stack.append(int(item))
            else:

                a = stack.pop()
                b = stack.pop()
                if item == '+':
                    stack.append(b + a)
                elif item == '-':
                    stack.append(b - a)
                elif item == '*':
                    stack.append(b*a)
                elif item == '/':
                    stack.append(int(b/a))

        return stack[0]
'''
Time Complexity: O(N)
Space Complexity: O(1)
**********************
Summary Statistcs:
Runtime: 53 ms, faster than 98.35% of Python3 online submissions for Evaluate Reverse Polish Notation.
Memory Usage: 17.1 MB, less than 67.58% of Python3 online submissions for Evaluate Reverse Polish Notation.
'''
