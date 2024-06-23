'''
Given the head of a linked list and a value x, partition it such that all nodes less than x come before nodes greater than or equal to x.

You should preserve the original relative order of the nodes in each of the two partitions.
'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        
        pos = 0
        dummy = head
        smallList = ListNode()
        small = smallList
        largeList = ListNode()
        large = largeList
        while dummy:
            if dummy.val < x:
                smallList.next = dummy
                smallList = smallList.next
            elif dummy.val >= x:
                largeList.next = dummy
                largeList = largeList.next
            dummy = dummy.next
            
        largeList.next = None
        smallList.next = large.next
        
        return small.next
'''
Time Complexity: O(N)
Space Complexity: O(n)
**********************
Summary statistics:
Runtime: 36 ms, faster than 65.48% of Python3 online submissions for Partition List.
Memory Usage: 16.4 MB, less than 86.39% of Python3 online submissions for Partition List.
'''
