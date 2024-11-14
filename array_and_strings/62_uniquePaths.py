'''
62. Unique Paths
Medium

16930

454

Add to List

Share
There is a robot on an m x n grid. The robot is initially located at the top-left corner (i.e., grid[0][0]). The robot tries to move to the bottom-right corner (i.e., grid[m - 1][n - 1]). The robot can only move either down or right at any point in time.

Given the two integers m and n, return the number of possible unique paths that the robot can take to reach the bottom-right corner.

The test cases are generated so that the answer will be less than or equal to 2 * 109.
'''
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        
        totalSteps = m + n - 2
        downSteps = m - 1
        
        return math.comb(totalSteps, downSteps)
'''
Time Complexity: O(min(m, n))
Space Complexity: O(1)
**********************
Summary Statistics:
Runtime: 0 ms, faster than 100.00% of Python3 online submissions for Unique Paths.
Memory Usage: 16.6 MB, less than 68.82% of Python3 online submissions for Unique Paths.
'''
