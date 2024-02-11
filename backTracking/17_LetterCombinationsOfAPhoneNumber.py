'''
Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent. Return the answer in any order.

A mapping of digits to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.
'''
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        numberCombination = {
            '2': ['a', 'b', 'c'],
            '3': ['d', 'e', 'f'],
            '4': ['g', 'h', 'i'],
            '5': ['j', 'k', 'l'],
            '6': ['m', 'n', 'o'],
            '7': ['p', 'q', 'r', 's'],
            '8': ['t', 'u', 'v'],
            '9': ['w', 'x', 'y', 'z']
        }
        result = []

        def backTrack(i, num):
            if len(num) == len(digits):
                result.append(num)
                return
            else:
                items = numberCombination[digits[i]]
                for item in items:
                    backTrack(i + 1, num + item)

        backTrack(0, "")
        return result
'''
Time Complexity: O(N*4^N)
Space Complexity: O(4^N)
'''
