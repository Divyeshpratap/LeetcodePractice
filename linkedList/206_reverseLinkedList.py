'''
Given the head of a singly linked list, reverse the list, and return the reversed list.
'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev, curr = None, head

        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp

        return prev
'''
Time Complexity: O(N)
Space Complexity: O(1)
**********************
Summary Statistics:
Runtime: 36 ms, faster than 66.57% of Python3 online submissions for Reverse Linked List.
Memory Usage: 17.8 MB, less than 6.75% of Python3 online submissions for Reverse Linked List.
'''
