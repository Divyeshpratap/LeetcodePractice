'''
You are a product manager and currently leading a team to develop a new product. Unfortunately, the latest version of your product fails the quality check. Since each version is developed based on the previous version, all the versions after a bad version are also bad.

Suppose you have n versions [1, 2, ..., n] and you want to find out the first bad one, which causes all the following ones to be bad.

You are given an API bool isBadVersion(version) which returns whether version is bad. Implement a function to find the first bad version. You should minimize the number of calls to the API.
'''
# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        if n == 1:
            return 1
        def divide_and_conquer(start, end):

            if isBadVersion(start):
                return start
            if start >= end:
                return None

            mid = (start + end) // 2
            if isBadVersion(mid) and (mid == start or isBadVersion(mid - 1) == False):
                return mid
            if not isBadVersion(mid):
                return divide_and_conquer(mid + 1, end)
            else:
                return divide_and_conquer(start, mid - 1)

        return divide_and_conquer(1, n)
'''
Time Complexity: O(log(n))
Space Complexity: O(log(n))
'''
