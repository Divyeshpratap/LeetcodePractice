'''
Write a function that takes the binary representation of a positive integer and returns the number of set bits it has (also known as the Hamming weight).
'''
class Solution:
    def hammingWeight(self, n: int) -> int:
        count = 0
        while n:
            if (n & 1) == 1:
                count += 1
            n = n >> 1

        return count
'''
Time Complexity: O(n)
Space complexity: O(1)
**********************
Summary Statistics:
Runtime: 37 ms, faster than 45.72% of Python3 online submissions for Number of 1 Bits.
Memory Usage: 16.4 MB, less than 84.49% of Python3 online submissions for Number of 1 Bits.
'''
