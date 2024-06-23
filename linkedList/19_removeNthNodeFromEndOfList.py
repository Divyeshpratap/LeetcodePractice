'''
Given the head of a linked list, remove the nth node from the end of the list and return its head.
'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        if not head.next:
            return None
        dummy = head
        count = 0
        while dummy:
            count += 1
            dummy = dummy.next

        dummy = ListNode()
        dummy.next = head
        temp = dummy
        for i in range(count - n):
            dummy = dummy.next

        dummy.next = dummy.next.next

        return temp.next
'''
Time Complexity: O(N)
Space Complexity: O(1)
**********************
Summary Statistics:
Runtime: 33 ms, faster than 78.78% of Python3 online submissions for Remove Nth Node From End of List.
Memory Usage: 16.5 MB, less than 74.83% of Python3 online submissions for Remove Nth Node From End of List.
'''
