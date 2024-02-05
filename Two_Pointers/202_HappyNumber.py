'''
Write an algorithm to determine if a number n is happy.

A happy number is a number defined by the following process:

Starting with any positive integer, replace the number by the sum of the squares of its digits.
Repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1.
Those numbers for which this process ends in 1 are happy.
Return true if n is a happy number, and false if not.
'''
class Solution:
    def isHappy(self, n: int) -> bool:
        total = n
        ls = []
        while total != 1:
            total = sum([int(digit)**2 for digit in str(total)])
            if total in ls:
                return False
            ls.append(total)

            # print(ls)
        return True
'''
Time Complexity: O(1)
Space Complexity: O(Number of Cycles)
****
There is another optimized version of code that implements a fast and slow pointer technique to check for cycles instead of storing a previously encountered number in a list, which has a constant O(1) space complexity. To be implemented in future
****
'''
