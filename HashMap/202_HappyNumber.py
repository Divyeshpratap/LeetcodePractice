'''
Write an algorithm to determine if a number n is happy.

A happy number is a number defined by the following process:

    Starting with any positive integer, replace the number by the sum of the squares of its digits.
    Repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1.
    Those numbers for which this process ends in 1 are happy.

Return true if n is a happy number, and false if no
'''
class Solution:
    def isHappy(self, n: int) -> bool:
        if n == 1:
            return True
        num = set()

        while n not in num:
            num.add(n)
            total = 0
            while n!=0:
                rem  = n%10
                n = n//10
                total = total + rem**2
            if total == 1:
                return True
            n = total
        return False
'''
Time Complexity: O(d*logn) where d is the number of iterations until a repeat or 1 is detected, n is the number of digits in each iteration (usually small)
Space Complexity: O(d)
'''
