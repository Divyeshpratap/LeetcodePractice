'''
Given a binary tree, find the lowest common ancestor (LCA) of two given nodes in the tree.

According to the definition of LCA on Wikipedia: “The lowest common ancestor is defined between two nodes p and q as the lowest node in T that has both p and q as descendants (where we allow a node to be a descendant of itself).”
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':

        def dfs(node):
            if not node:
                return None
            if node == p or node == q:
                return node

            l = dfs(node.left)
            r = dfs(node.right)
            if l and r:
                return node
            else:
                return l or r

        return dfs(root)
'''
Time Complexity: O(N)
Space Complexity: O(1)
***********************
Summary Statistics:
Runtime: 46 ms, faster than 79.68% of Python3 online submissions for Lowest Common Ancestor of a Binary Tree.
Memory Usage: 21 MB, less than 62.26% of Python3 online submissions for Lowest Common Ancestor of a Binary Tree.
'''
