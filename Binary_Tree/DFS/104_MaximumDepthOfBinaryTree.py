'''
Given the root of a binary tree, return its maximum depth.

A binary tree's maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        
        if not root:
            return 0
        def binaryTree(node):
            if not node:
                return
            if not node.left and not node.right:
                return 1
            if node.left and not node.right:
                depth = binaryTree(node.left) + 1
            if node.right and not node.left:
                depth = binaryTree(node.right) + 1
            if node.left and node.right:
                depth = max(binaryTree(node.left), binaryTree(node.right)) + 1

            return depth

        return binaryTree(root)

'''
Time Complexity: O(log(depth of tree))
Space Complexity: O(log(depth olf binary tree))
'''
