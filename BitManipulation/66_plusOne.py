'''
You are given a large integer represented as an integer array digits, where each digits[i] is the ith digit of the integer. The digits are ordered from most significant to least significant in left-to-right order. The large integer does not contain any leading 0's.

Increment the large integer by one and return the resulting array of digits.
'''
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:

        for i in range(len(digits) - 1, -1, -1):
            if digits[i] != 9:
                digits[i] = digits[i] + 1
                return digits
            digits[i] = 0
        return [1] + digits
'''
Time Complexity: O(len(digits))
Space Complexity: O(1)
**********************
Summary Statistics:
Runtime: 30 ms, faster than 91.21% of Python3 online submissions for Plus One.
Memory Usage: 16.4 MB, less than 79.46% of Python3 online submissions for Plus One.
'''
