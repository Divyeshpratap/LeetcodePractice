'''
Given the head of a singly linked list and two integers left and right where left <= right, reverse the nodes of the list from position left to position right, and return the reversed list.
'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:

        if not head or (left == right):
            return head
        dummy = ListNode(0)
        prev, curr = dummy, head
        prev.next = head
        pos1 = prev
        pos2 = curr
        for i in range(1, right + 2):
            if i == right + 1:
                pos1.next = prev
                pos2.next = curr
                break
            elif i >= left and i <= right:
                temp = curr.next
                curr.next = prev
                prev = curr
                curr = temp
            else:
                prev = prev.next
                curr = curr.next
                pos1 = prev
                pos2 = curr

        return dummy.next if left > 1 else prev
'''
Time Complexity: O(N)
Space Complexity: O(1)
**********************
Summary Statistics:
Runtime: 34 ms, faster than 68.60% of Python3 online submissions for Reverse Linked List II.
Memory Usage: 16.6 MB, less than 42.48% of Python3 online submissions for Reverse Linked List II.
'''
