'''
You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).

Find two lines that together with the x-axis form a container, such that the container contains the most water.

Return the maximum amount of water a container can store.

Notice that you may not slant the container.
'''
class Solution:
    def maxArea(self, height: List[int]) -> int:
        i = 0
        j = len(height) - 1
        currMax = min(height[i], height[j]) * (j - i)
        while i < j:
            if height[i] < height[j]:
                i = i + 1
            else:
                j = j - 1
            if currMax < (min(height[i], height[j]) * (j - i)):
                currMax = min(height[i], height[j]) * (j - i)
        return currMax
'''
Time Complexity: O(N)
Space Complexity: O(1)
'''
