'''
Given the root of a binary tree, the level of its root is 1, the level of its children is 2, and so on.

Return the smallest level x such that the sum of all the values of nodes at level x is maximal.

Input: root = [1,7,0,7,-8,null,null]
Output: 2
Explanation:
Level 1 sum = 1.
Level 2 sum = 7 + 0 = 7.
Level 3 sum = 7 + -8 = -1.
So we return the level with the maximum sum which is level 2.
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:

        if not root:
            return 0
        q = deque()
        q.append(root)

        maxSum = root.val
        maxLevel = 1
        level = 1
        while q:
            levelSum = 0
            for _ in range(len(q)):
                node = q.popleft()
                if node.left: q.append(node.left)
                if node.right: q.append(node.right)
                levelSum += node.val
            if levelSum > maxSum:
                maxSum = levelSum
                maxLevel = level
            level += 1
        return maxLevel
'''
Time Complexity: O(N)-> O(num(nodes))
Space Complexity: O(N)
'''
