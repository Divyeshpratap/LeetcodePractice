'''
Consider all the leaves of a binary tree, from left to right order, the values of those leaves form a leaf value sequence.
For example, in the given tree above, the leaf value sequence is (6, 7, 4, 9, 8).

Two binary trees are considered leaf-similar if their leaf value sequence is the same.

Return true if and only if the two given trees with head nodes root1 and root2 are leaf-similar.
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:

        leaves1 = []
        leaves2 = []
        def dfs(node, leaves):
            if not node.left and not node.right:
                leaves.append(node.val)
            elif not node.right and node.left:
                dfs(node.left, leaves)
            elif not node.left and node.right:
                dfs(node.right, leaves)
            elif node.left and node.right:
                dfs(node.left, leaves)
                dfs(node.right, leaves)
            return
        dfs(root1, leaves1)
        dfs(root2, leaves2)
        return leaves1 == leaves2
'''
Time Complexity: O(num_nodes)
Space Copmplexity: O(num_nodes), worst case imbalanced tree
'''
