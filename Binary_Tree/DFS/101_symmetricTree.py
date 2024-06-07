'''
Given the root of a binary tree, check whether it is a mirror of itself (i.e., symmetric around its center).
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:

        def invertRecursive(m, n):
            if not m and not n:
                return True
            if not m or not n:
                return False

            return (m.val==n.val) and invertRecursive(m.left, n.right) and invertRecursive(m.right, n.left)


        return invertRecursive(root.left, root.right)
'''
Time Complexity: O(N) where N is the number of nodes
Space Complexity: O(h) where h is the depth of the tree, and max(h) = N
***********************************************************************
Summary Statistics:
Runtime: 31 ms, faster than 89.79% of Python3 online submissions for Symmetric Tree.
Memory Usage: 16.5 MB, less than 91.76% of Python3 online submissions for Symmetric Tree.
'''
