'''
Given the root of a binary tree, imagine yourself standing on the right side of it, return the values of the nodes you can see ordered from top to bottom.
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return
        val = deque()
        val.append(root)
        stack = []
        i = 0
        while val:
            for i in range(len(val)):
                rightEle = val[0]
                if rightEle.left:
                    val.append(rightEle.left)
                if rightEle.right:
                    val.append(rightEle.right)
                val.popleft()
            stack.append(rightEle.val)

        return stack
'''
Time Complexity: O(N)
Space Complexity: O(N)
**********************
Summary Statistics:
Runtime: 44 ms, faster than 9.34% of Python3 online submissions for Binary Tree Right Side View.
Memory Usage: 16.5 MB, less than 70.17% of Python3 online submissions for Binary Tree Right Side View.
'''
