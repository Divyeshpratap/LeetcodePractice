'''
Given the roots of two binary trees p and q, write a function to check if they are the same or not.

Two binary trees are considered the same if they are structurally identical, and the nodes have the same value.
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:

        def recursiveDFSCheck(m, n):

            if not m and not n:
                return True
            if not m and n:
                return False
            if not n and m:
                return False
            if m.val != n.val:
                return False

            return recursiveDFSCheck(m.left, n.left) and recursiveDFSCheck(m.right, n.right)

        return recursiveDFSCheck(p, q)
'''
Time Complexity: O(n) where n is the number of nodes
Space Complexity: O(h) where h is the height of the tree (typically logn)
*************************************************************************
Summary Statistics:
Runtime: 34 ms, faster than 65.19% of Python3 online submissions for Same Tree.
Memory Usage: 16.4 MB, less than 91.24% of Python3 online submissions for Same Tree.
'''
