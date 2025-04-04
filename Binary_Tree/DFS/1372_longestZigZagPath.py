'''
You are given the root of a binary tree.

A ZigZag path for a binary tree is defined as follow:

Choose any node in the binary tree and a direction (right or left).
If the current direction is right, move to the right child of the current node; otherwise, move to the left child.
Change the direction from right to left or from left to right.
Repeat the second and third steps until you can't move in the tree.
Zigzag length is defined as the number of nodes visited - 1. (A single node has a length of 0).

Return the longest ZigZag path contained in that tree.

Input: root = [1,null,1,1,1,null,null,1,1,null,1,null,null,null,1]
Output: 3
Explanation: Longest ZigZag path in blue nodes (right -> left -> right).
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.alternateDepth = 0
    def longestZigZag(self, root: Optional[TreeNode]) -> int:

        def zigZagLen(node, left, right):

            if not node:
                return
            self.alternateDepth = max(self.alternateDepth, left, right)

            zigZagLen(node.left, 0, left + 1)
            zigZagLen(node.right, right + 1, 0)

        zigZagLen(root, 0, 0)

        return self.alternateDepth
'''
Time Complexity: O(num_nodes)
Space Complexity: O(num_node)
'''
