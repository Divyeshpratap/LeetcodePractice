'''
You are given the root of a binary search tree (BST) and an integer val.

Find the node in the BST that the node's value equals val and return the subtree rooted with that node. If such a node does not exist, return null.
Input: root = [4,2,7,1,3], val = 2
Output: [2,1,3]
'''
## BFS Solution
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if root is None:
            return
        queue = []
        # result = []
        queue.append(root)
        while len(queue) > 0:
            node =  queue.pop(0)
            if node.val == val:
                return node
            else:
                if node.left is not None:
                    queue.append(node.left)
                if node.right is not None:
                    queue.append(node.right)
        return
'''
Time Complexity: O(N)
Space Complexity: O(N)
'''
## DFS Solution:
class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if not root: return None

        def dfs(node):
            if not node: return
            if node.val == val:
                return node
            else:
                found_node = dfs(node.left) or dfs(node.right)
                
            return found_node

        return dfs(root)
'''
Time Complexity: O(N)
Space Complexity: O(N)
'''
