'''
You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
'''
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        firstNode = l1
        secondNode = l2
        newNode = ListNode((firstNode.val + secondNode.val)%10)
        carry = (firstNode.val + secondNode.val)//10
        head = newNode
        firstNode = firstNode.next
        secondNode = secondNode.next
        
        while firstNode and secondNode:
            tempNode = ListNode((firstNode.val + secondNode.val + carry)%10)
            carry = (firstNode.val + secondNode.val + carry)//10
            firstNode = firstNode.next
            secondNode = secondNode.next
            newNode.next = tempNode
            newNode = newNode.next
            
        while firstNode:
            tempNode = ListNode((firstNode.val + carry)%10)
            carry = (firstNode.val + carry)//10
            firstNode = firstNode.next
            newNode.next = tempNode
            newNode = newNode.next
            
        while secondNode:
            tempNode = ListNode((secondNode.val + carry)%10)
            carry = (secondNode.val + carry)//10
            secondNode = secondNode.next
            newNode.next = tempNode
            newNode = newNode.next
        
        if carry > 0:
            newNode.next = ListNode(carry)
        return head
'''
Time Complexity: O(max(lenl1, lenl2))
Space Complexity: O(N)
**********************
Summary Statistics:
Runtime: 54 ms, faster than 62.90% of Python3 online submissions for Add Two Numbers.
Memory Usage: 16.6 MB, less than 75.04% of Python3 online submissions for Add Two Numbers.
'''
