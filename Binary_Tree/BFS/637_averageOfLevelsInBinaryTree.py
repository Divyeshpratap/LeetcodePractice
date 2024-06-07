'''
Given the root of a binary tree, return the average value of the nodes on each level in the form of an array. Answers within 10-5 of the actual answer will be accepted.
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        if not root:
            return

        elementQ = deque()
        elementQ.append(root)
        averages = []

        while elementQ:
            levelLength = len(elementQ)
            total = 0
            for _ in range(levelLength):
                node = elementQ.popleft()
                total  += node.val
                if node.left:
                    elementQ.append(node.left)

                if node.right:
                    elementQ.append(node.right)

            averages.append(total/levelLength)
            total = 0
        return averages
'''
Time Complexity: O(N)
Space Complexity: O(w), where w is the maximum width of the Binary Tree
***********************************************************************
Summary Statistics:
Runtime: 38 ms, faster than 90.71% of Python3 online submissions for Average of Levels in Binary Tree.
Memory Usage: 18.3 MB, less than 96.50% of Python3 online submissions for Average of Levels in Binary Tree.
'''
