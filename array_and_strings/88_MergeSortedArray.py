'''
You are given two integer arrays nums1 and nums2, sorted in non-decreasing order, and two integers m and n, representing the number of elements in nums1 and nums2 respectively.

Merge nums1 and nums2 into a single array sorted in non-decreasing order.

The final sorted array should not be returned by the function, but instead be stored inside the array nums1. To accommodate this, nums1 has a length of m + n, where the first m elements denote the elements that should be merged, and the last n elements are set to 0 and should be ignored. nums2 has a length of n.
'''
class Solution(object):
    def merge(self, nums1, m, nums2, n):
        totLen = m + n - 1
        while n - 1 >= 0:
            if m - 1 >= 0 and nums1[m - 1] > nums2[n - 1]:
                nums1[totLen] = nums1[m - 1]
                totLen -= 1
                m -= 1
            else:
                nums1[totLen] = nums2[n - 1]
                totLen -= 1
                n -= 1
'''
Time Complexity: O(n)
Space Complexity: O(1)
'''
