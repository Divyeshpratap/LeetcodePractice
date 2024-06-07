'''
You are given the heads of two sorted linked lists list1 and list2.

Merge the two lists into one sorted list. The list should be made by splicing together the nodes of the first two lists.

Return the head of the merged linked list.
'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        start = head = ListNode()
        node1 = list1
        node2 = list2
        while node1 and node2:
            if node1.val <= node2.val:
                head.next = node1
                head = head.next
                node1 = node1.next
            else:
                head.next = node2
                head = head.next
                node2 = node2.next

        while node1:
            head.next = node1
            head = head.next
            node1 = node1.next

        while node2:
            head.next = node2
            head = head.next
            node2 = node2.next

        return start.next
'''
Time Complexity: O(N)
Space Complexity: O(1)
**********************
Sumaary Stats:
Runtime: 33 ms, faster than 85.93% of Python3 online submissions for Merge Two Sorted Lists.
Memory Usage: 16.5 MB, less than 91.77% of Python3 online submissions for Merge Two Sorted Lists.
'''
