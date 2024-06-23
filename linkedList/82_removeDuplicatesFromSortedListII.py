'''
Given the head of a sorted linked list, delete all nodes that have duplicate numbers, leaving only distinct numbers from the original list. Return the linked list sorted as well.
'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        dummy.next = head
        startNode = dummy

        while dummy.next and dummy.next.next:
            if dummy.next.val == dummy.next.next.val:
                tempNode = dummy.next.val
                while dummy.next and dummy.next.val == tempNode:
                    dummy.next = dummy.next.next

            else:
                dummy = dummy.next

        return startNode.next
'''
Time Complexity: O(N)
Space Complexity: O(1)
**********************
Summary Statistics:
Runtime: 34 ms, faster than 88.62% of Python3 online submissions for Remove Duplicates from Sorted List II.
Memory Usage: 16.4 MB, less than 87.53% of Python3 online submissions for Remove Duplicates from Sorted List II.
'''
