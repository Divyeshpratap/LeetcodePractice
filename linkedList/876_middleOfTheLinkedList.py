'''
Given the head of a singly linked list, return the middle node of the linked list.

If there are two middle nodes, return the second middle node.
Input: head = [1,2,3,4,5]
Output: [3,4,5]
Explanation: The middle node of the list is node 3.
'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:

        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        return slow
'''
Time Complexity: O(len(linkedList))
Space Complexity: O(1)
**********************
Summary Statistics:
Runtime: 0 ms, faster than 100.00% of Python3 online submissions for Middle of the Linked List.
Memory Usage: 16.7 MB, less than 21.34% of Python3 online submissions for Middle of the Linked List.
'''
