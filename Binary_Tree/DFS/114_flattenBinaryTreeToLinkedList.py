'''
Given the root of a binary tree, flatten the tree into a "linked list":

The "linked list" should use the same TreeNode class where the right child pointer points to the next node in the list and the left child pointer is always null.
The "linked list" should be in the same order as a pre-order traversal of the binary tree.
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """

        def preorder(root):
            if not root:
                return

            leftFlat = preorder(root.left)
            rightFlat = preorder(root.right)

            if root.left:
                leftFlat.right = root.right
                root.right = root.left
                root.left = None

            last = rightFlat or leftFlat or root

            return last

        preorder(root)
'''
Time Complexity: O(N)
Space Complexity: O(1)
**********************
Summary Statistics:
Runtime: 35 ms, faster than 78.41% of Python3 online submissions for Flatten Binary Tree to Linked List.
Memory Usage: 16.6 MB, less than 73.07% of Python3 online submissions for Flatten Binary Tree to Linked List.
'''
