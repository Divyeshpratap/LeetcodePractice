'''
Given two integer arrays preorder and inorder where preorder is the preorder traversal of a binary tree and inorder is the inorder traversal of the same tree, construct and return the binary tree.
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:

        if not preorder or not inorder:
            return None

        root = TreeNode(preorder[0])
        separation = inorder.index(preorder[0])
        root.left = self.buildTree(preorder[1:separation+1], inorder[:separation])
        root.right = self.buildTree(preorder[separation+1:], inorder[separation+1:])

        return root
'''
Time Complexity: O(n^2)
Space Complexity: O(n^2)
************************
Summary Statistics:
Runtime: 127 ms, faster than 47.64% of Python3 online submissions for Construct Binary Tree from Preorder and Inorder Traversal.
Memory Usage: 88.1 MB, less than 31.71% of Python3 online submissions for Construct Binary Tree from Preorder and Inorder Traversal.
'''
