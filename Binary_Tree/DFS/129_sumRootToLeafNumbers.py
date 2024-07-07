'''
You are given the root of a binary tree containing digits from 0 to 9 only.

Each root-to-leaf path in the tree represents a number.

For example, the root-to-leaf path 1 -> 2 -> 3 represents the number 123.
Return the total sum of all root-to-leaf numbers. Test cases are generated so that the answer will fit in a 32-bit integer.

A leaf node is a node with no children
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:

        ls = []
        def dfs(node, total):
            if not node:
                return
            elif not node.left and not node.right:
                total = total + str(node.val)
                ls.append(int(total))
            else:
                total = total + str(node.val)
                dfs(node.left, total)
                dfs(node.right, total)

            return

        dfs(root, '')
        return sum(ls)
'''
Time COmplexity: O(N)
Space Complexity: O(N)
**********************
Runtime: 32 ms, faster than 77.18% of Python3 online submissions for Sum Root to Leaf Numbers.
Memory Usage: 16.6 MB, less than 11.45% of Python3 online submissions for Sum Root to Leaf Numbers.
'''
