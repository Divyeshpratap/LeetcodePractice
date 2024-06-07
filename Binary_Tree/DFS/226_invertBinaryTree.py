'''
Given the root of a binary tree, invert the tree, and return its root.
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None
        def recursiveInvert(node):
            if not node:
                return
            temp = node.left
            node.left = node.right
            node.right = temp
            recursiveInvert(node.left)
            recursiveInvert(node.right)


        recursiveInvert(root)

        return root
'''
Time Complexity: O(n) where n is the number of nodes
Space Complexity: O(h) where h is height of tree, in worst case h = n
*********************************************************************
Summary Statistics:
Runtime: 31 ms, faster than 81.43% of Python3 online submissions for Invert Binary Tree.
Memory Usage: 16.5 MB, less than 79.21% of Python3 online submissions for Invert Binary Tree.
'''
