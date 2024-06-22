'''
A linked list of length n is given such that each node contains an additional random pointer, which could point to any node in the list, or null.

Construct a deep copy of the list. The deep copy should consist of exactly n brand new nodes, where each new node has its value set to the value of its corresponding original node. Both the next and random pointer of the new nodes should point to new nodes in the copied list such that the pointers in the original list and copied list represent the same list state. None of the pointers in the new list should point to nodes in the original list.

For example, if there are two nodes X and Y in the original list, where X.random --> Y, then for the corresponding two nodes x and y in the copied list, x.random --> y.

Return the head of the copied linked list.

The linked list is represented in the input/output as a list of n nodes. Each node is represented as a pair of [val, random_index] where:

val: an integer representing Node.val
random_index: the index of the node (range from 0 to n-1) that the random pointer points to, or null if it does not point to any node.
Your code will only be given the head of the original linked list.
'''
"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':

        nodeDict = { None: None}
        curr = head
        while curr:
            copy = ListNode(curr.val)
            nodeDict[curr] = copy
            curr = curr.next

        curr = head
        while curr:
            nodeDict[curr].next = nodeDict[curr.next]
            nodeDict[curr].random = nodeDict[curr.random]
            curr = curr.next


        return nodeDict[head]
'''
Time Complexity: O(N)
Space Complexity: O(N)
**********************
Summary Statistics:
Runtime: 32 ms, faster than 90.07% of Python3 online submissions for Copy List with Random Pointer.
Memory Usage: 17.3 MB, less than 65.89% of Python3 online submissions for Copy List with Random Pointer.
'''
