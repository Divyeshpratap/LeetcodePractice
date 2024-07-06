'''

Given a binary tree

struct Node {
  int val;
  Node *left;
  Node *right;
  Node *next;
}
Populate each next pointer to point to its next right node. If there is no next right node, the next pointer should be set to NULL.

Initially, all next pointers are set to NULL.
'''
"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return

        q = deque()
        q.append(root)
        dummy = Node(-999)
        while q:
            levelLen = len(q)
            prev = dummy
            for i in range(levelLen):
                curr = q.popleft()
                if curr.left:
                    q.append(curr.left)
                    prev.next = curr.left
                    prev = prev.next
                if curr.right:
                    q.append(curr.right)
                    prev.next = curr.right
                    prev = prev.next

        return root
'''
Time Complexity: O(N)
Space Complexity: O(1)
**********************
Runtime: 27 ms, faster than 99.75% of Python3 online submissions for Populating Next Right Pointers in Each Node II.
Memory Usage: 17.7 MB, less than 5.63% of Python3 online submissions for Populating Next Right Pointers in Each Node II.
'''
