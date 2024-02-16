'''
Given the root of a binary tree, return the level order traversal of its nodes' values. (i.e., from left to right, level by level).
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        queue1 = collections.deque()
        queue2 = collections.deque()
        ls = []
        queue2.append(root)
        count = 1
        while queue2:
            # print(f'queue2 is {queue2}')
            while count > 0:
                queue1.append(queue2.popleft())
                count -= 1
            temp = []
            for item in queue1:
                temp.append(item.val)
            ls.append(temp)
            while queue1:
                currItem = queue1.popleft()
                if currItem.left:
                    queue2.append(currItem.left)
                    count += 1
                if currItem.right:
                    queue2.append(currItem.right)
                    count += 1
        return ls
'''
Time Complexity: O(N)
Space Complexity: O(N)
'''
