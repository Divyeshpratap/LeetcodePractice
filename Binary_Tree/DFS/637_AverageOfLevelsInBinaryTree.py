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
        levelDict = {}

        def recursiveDFS(node, level):
            if not node:
                return
            elif node.left and not node.right:
                levelDict[level] = levelDict.get(level, [])
                levelDict[level].append(node.val)
                recursiveDFS(node.left, level + 1)
            elif node.right and not node.left:
                levelDict[level] = levelDict.get(level, [])
                levelDict[level].append(node.val)
                recursiveDFS(node.right, level + 1)
            elif node.right and node.left:
                levelDict[level] = levelDict.get(level, [])
                levelDict[level].append(node.val)
                recursiveDFS(node.left, level + 1)
                recursiveDFS(node.right, level + 1)
            elif not node.left and not node.right:
                levelDict[level] = levelDict.get(level, [])
                levelDict[level].append(node.val)
                return
        recursiveDFS(root, 0)
        ls = []
        for value in levelDict.values():
            ls.append(sum(value)/ len(value))
        # print(levelDict)
        return ls
'''
TimeComplexity: O(N)
Space Complexity: O(N)
'''
