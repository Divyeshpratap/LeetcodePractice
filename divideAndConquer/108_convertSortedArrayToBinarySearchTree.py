'''
Given an integer array nums where the elements are sorted in ascending order, convert it to a height-balanced binary search tree.
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        
        def helper(l, r):
            if l <= r:
                mid = (l + r)//2
                # print(f'mid element is {mid}, and left value is {l}, and right value is {r}')
                midNode = TreeNode(nums[mid])
                midNode.left = helper(l, mid - 1)
                midNode.right = helper(mid + 1, r)
                return midNode
            else:
                return None
            
        return helper(0, len(nums) - 1)
'''
Time Complexity: O(N) where N is the number of nodes
Space Complexity: O(log(N))
***************************
Summary Statistics:
Runtime: 55 ms, faster than 51.65% of Python3 online submissions for Convert Sorted Array to Binary Search Tree.
Memory Usage: 17.7 MB, less than 76.81% of Python3 online submissions for Convert Sorted Array to Binary Search Tree.
'''
