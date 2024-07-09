'''
Given the root of a binary tree, determine if it is a valid binary search tree (BST).

A valid BST is defined as follows:

The left subtree of a node contains only nodes with keys less than the node's key.
The right subtree of a node contains only nodes with keys greater than the node's key.
Both the left and right subtrees must also be binary search trees.
'''
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        def bstCheck(node, left, right):
            if not node:
                return True

            if not(node.val > left and node.val < right):
                return False
            else:
                return bstCheck(node.left, left, node.val) and bstCheck(node.right, node.val, right)

        return bstCheck(root, float('-inf'), float('inf'))
'''
Time Complexity: O(N)
Space Complexity: O(1)
**********************
Summary Statistics:
Runtime: 41 ms, faster than 60.27% of Python3 online submissions for Validate Binary Search Tree.
Memory Usage: 18.4 MB, less than 6.47% of Python3 online submissions for Validate Binary Search Tree.
'''
