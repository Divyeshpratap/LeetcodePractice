'''
Given the root of a Binary Search Tree (BST), return the minimum absolute difference between the values of any two different nodes in the tree.
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:

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
Space Complexity: O(N), list storage of inorder traversal
*********************************************************
Summary Statisitics:
Runtime: 40 ms, faster than 91.07% of Python3 online submissions for Minimum Absolute Difference in BST.
Memory Usage: 18.2 MB, less than 40.21% of Python3 online submissions for Minimum Absolute Difference in BST.
'''
