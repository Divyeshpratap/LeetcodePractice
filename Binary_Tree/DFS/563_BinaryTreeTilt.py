'''
Given the root of a binary tree, return the sum of every tree node's tilt.

The tilt of a tree node is the absolute difference between the sum of all left subtree node values and all right subtree node values. If a node does not have a left child, then the sum of the left subtree node values is treated as 0. The rule is similar if the node does not have a right child.
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTilt(self, root: Optional[TreeNode]) -> int:
        diff = []
        def recursiveDFS(node):
            if not node:
                return 0
            if not node.left and node.right:
                temp = recursiveDFS(node.right)
                diff.append(abs(temp))
                return node.val + temp
            if not node.right and node.left:
                temp = recursiveDFS(node.left)
                diff.append(abs(temp))
                return node.val + temp
            if not node.left and not node.right:
                return node.val
            if node.left and node.right:
                tempLeft = recursiveDFS(node.left)
                tempRight = recursiveDFS(node.right)
                diff.append(abs(tempLeft - tempRight))
                return  tempLeft + tempRight + node.val
        recursiveDFS(root)
        return sum(diff)
'''
Time Complexity: O(N)
Space Complexity: O(N)
'''

