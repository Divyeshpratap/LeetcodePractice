'''
Given the root of a complete binary tree, return the number of the nodes in the tree.

According to Wikipedia, every level, except possibly the last, is completely filled in a complete binary tree, and all nodes in the last level are as far left as possible. It can have between 1 and 2h nodes inclusive at the last level h.

Design an algorithm that runs in less than O(n) time complexity.
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# BFS implementation
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        elements = deque()
        elements.append(root)
        count = 0
        while elements:
            currNode = elements.popleft()
            if currNode.left:
                elements.append(currNode.left)
            if currNode.right:
                elements.append(currNode.right)
            count += 1

        return count
'''
Time Complexity: O(N), where N is the number of nodes
Space Complexity: O(w), where w is the maximum width of the tree
****************************************************************
Summary Statistics:
Runtime: 53 ms, faster than 73.41% of Python3 online submissions for Count Complete Tree Nodes.
Memory Usage: 21.8 MB, less than 31.53% of Python3 online submissions for Count Complete Tree Nodes.
'''
