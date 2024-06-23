'''
Given the head of a linked list, rotate the list to the right by k places.
'''
Given the head of a linked list, rotate the list to the right by k places.
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head:
            return
        dummy = head
        count = 0
        while dummy:
            count += 1
            dummy = dummy.next
        if count == 1:
            return head
        dummy = head
        shiftTimes = k % count
        if shiftTimes == 0:
            return head
        
        for i in range(count - shiftTimes - 1):
            dummy = dummy.next
            
        lastEle = dummy.next
        start = lastEle
        dummy.next = None
        
        while lastEle.next:
            lastEle = lastEle.next
            
        lastEle.next = head
        
        return start
'''
Time Complexity: O(N), worst case
Space Complexity: O(1)
**********************
Summary Statistics:
Runtime: 32 ms, faster than 89.92% of Python3 online submissions for Rotate List.
Memory Usage: 16.5 MB, less than 68.44% of Python3 online submissions for Rotate List.
'''
