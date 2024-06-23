'''
Given the head of a sorted linked list, delete all duplicates such that each element appears only once. Return the linked list sorted as well
'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return
        # dummy = ListNode()
        dummy = head

        while dummy.next:
            while dummy.val == dummy.next.val:
                dummy.next = dummy.next.next
                if not dummy.next:
                    break
            if dummy.next:
                dummy = dummy.next

        return head
'''
Time Complexity: O(N)
Space Complexity: O(1)
**********************
Summary Statistics:
Runtime: 40 ms, faster than 55.75% of Python3 online submissions for Remove Duplicates from Sorted List.
Memory Usage: 16.5 MB, less than 85.02% of Python3 online submissions for Remove Duplicates from Sorted List.
'''
