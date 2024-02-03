'''
Given the root of a binary tree, return the length of the diameter of the tree.

The diameter of a binary tree is the length of the longest path between any two nodes in a tree. This path may or may not pass through the root.

The length of a path between two nodes is represented by the number of edges between them.
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        maxDiameter = 0
        def recursiveDFS(node, height):
            nonlocal maxDiameter
            if not node:
                return -1

            nodeHeightLeft = recursiveDFS(node.left, height)
            nodeHeightRight = recursiveDFS(node.right, height)
            diameter = nodeHeightLeft + nodeHeightRight + 2
            nodeHeightLeft += 1
            nodeHeightRight += 1
            height = max(nodeHeightLeft, nodeHeightRight)

            maxDiameter = max(diameter, maxDiameter)

            return height
        recursiveDFS(root, 0)
        return maxDiameter
'''
Time Complexity: O(N)
Space Complexity: O(height of tree)
'''
