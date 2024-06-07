'''
Given a non-negative integer x, return the square root of x rounded down to the nearest integer. The returned integer should be non-negative as well.

You must not use any built-in exponent function or operator.

    For example, do not use pow(x, 0.5) in c++ or x ** 0.5 in python.
'''
class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 0 or x == 1:
            return x
        low, high = 1, x
        while low <= high:
            mid = (low + high)//2
            if mid * mid == x:
                return mid
            elif mid * mid < x:
                low = mid + 1
                res = mid
            elif mid * mid > x:
                high = mid - 1

        return res
'''
Time Complexity: O(logn)
Space Complexity: O(1)
**********************
Summary Statistics:
Runtime: 32 ms, faster than 90.31% of Python3 online submissions for Sqrt(x).
Memory Usage: 16.4 MB, less than 97.78% of Python3 online submissions for Sqrt(x).
'''
