'''
Given two binary strings a and b, return their sum as a binary string.

Example 1:

Input: a = "11", b = "1"
Output: "100"
'''
class Solution:
    def addBinary(self, a: str, b: str) -> str:

        leftEle = ''
        rightEle = ''
        total = []
        carry = 0
        if len(a) > len(b):
            b = b.zfill(len(a))
        elif len(b) > len(a):
            a = a.zfill(len(b))
        for i in range(len(a)):
                leftEle = int(a[-i-1])
                rightEle = int(b[-i-1])
                if leftEle == 1 and rightEle == 1 and carry == 1:
                    carry = 1
                    total.append(1)
                elif leftEle == 1 and rightEle == 1 and carry == 0:
                    carry = 1
                    total.append(0)
                elif leftEle == 1 and rightEle == 0 and carry == 1:
                    carry = 1
                    total.append(0)
                elif leftEle == 0 and rightEle == 1 and carry == 1:
                    carry = 1
                    total.append(0)
                elif leftEle == 1 and rightEle == 0 and carry == 0:
                    carry = 0
                    total.append(1)
                elif leftEle == 0 and rightEle == 1 and carry == 0:
                    carry = 0
                    total.append(1)
                elif leftEle == 0 and rightEle == 0 and carry == 1:
                    carry = 0
                    total.append(1)
                elif leftEle == 0 and rightEle == 0 and carry == 0:
                    carry = 0
                    total.append(0)

        if carry == 1:
            total.append(str(carry))

        return ''.join(map(str, total[::-1]))
'''
Time Complexity: O(N)
Space Complexity: O(N+M)
************************
Summary Statistics:
Runtime: 35 ms, faster than 71.60% of Python3 online submissions for Add Binary.
Memory Usage: 16.7 MB, less than 10.66% of Python3 online submissions for Add Binary.
'''
