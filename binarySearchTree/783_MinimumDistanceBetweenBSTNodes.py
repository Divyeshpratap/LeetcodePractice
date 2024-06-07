'''
Given the root of a Binary Search Tree (BST), return the minimum difference between the values of any two different nodes in the tree.'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDiffInBST(self, root: Optional[TreeNode]) -> int:

        ls = []
        def inorderTraversal(node):
            if node.left:
                inorderTraversal(node.left)

            ls.append(node.val)

            if node.right:
                inorderTraversal(node.right)
            return

        inorderTraversal(root)
        minDist = float('inf')
        for i in range(1, len(ls)):
            if ls[i] - ls[i-1] < minDist:
                minDist = ls[i] - ls[i-1]
        return minDist
'''
Time Complexity: O(N)
Space Complexity: O(N), for storing inorder traversal
*****************************************************
Summary Statistics:
Runtime: 29 ms, faster than 92.58% of Python3 online submissions for Minimum Distance Between BST Nodes.
Memory Usage: 16.5 MB, less than 85.08% of Python3 online submissions for Minimum Distance Between BST Nodes.
'''
