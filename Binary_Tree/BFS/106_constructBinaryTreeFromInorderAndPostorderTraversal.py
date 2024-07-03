'''
Given two integer arrays inorder and postorder where inorder is the inorder traversal of a binary tree and postorder is the postorder traversal of the same tree, construct and return the binary tree.
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:

        if not inorder:
            return None

        root = TreeNode(postorder.pop())
        pos = inorder.index(root.val)

        root.right =  self.buildTree(inorder[pos+1:], postorder)
        root.left = self.buildTree(inorder[:pos], postorder)

        return root
'''
Time Complexity: O(n^2)
Space Complexity: O(n^2)
************************
Summary Statistics:
Runtime: 112 ms, faster than 43.80% of Python3 online submissions for Construct Binary Tree from Inorder and Postorder Traversal.
Memory Usage: 52.9 MB, less than 45.04% of Python3 online submissions for Construct Binary Tree from Inorder and Postorder Traversal.
'''
