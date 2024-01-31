'''
Given two strings needle and haystack, return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.
'''
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        for i in range(len(haystack) - len(needle) + 1):
            count = 0
            for j in range(len(needle)):
                if needle[j] == haystack[i+j]:
                    count = count + 1
                    if count == len(needle):
                        print("Element found Inside")
                        return i
                else:
                    break

        return -1
'''
Time Complexity: O(N2)
Space Copleity: O(1)
'''
