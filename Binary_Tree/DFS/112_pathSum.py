'''
Given the root of a binary tree and an integer targetSum, return true if the tree has a root-to-leaf path such that adding up all the values along the path equals targetSum.

A leaf is a node with no children.
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False
        def recPathSum(node, total):
            if not node:
                return False
            total += node.val
            if not node.left and not node.right:
                if total == targetSum:
                    return True
                else:
                    False
            else:
                return recPathSum(node.left, total) or recPathSum(node.right, total)

        return recPathSum(root, 0)

'''
Time Complexity: O(N), where N is the number of nodes
Space Complexity: O(h), where h is the depth of the tree, max(h) = N
********************************************************************
Summary Statistics:
Runtime: 43 ms, faster than 42.63% of Python3 online submissions for Path Sum.
Memory Usage: 17.2 MB, less than 97.53% of Python3 online submissions for Path Sum.
'''
