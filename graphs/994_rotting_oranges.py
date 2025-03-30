'''
You are given an m x n grid where each cell can have one of three values:

0 representing an empty cell,
1 representing a fresh orange, or
2 representing a rotten orange.
Every minute, any fresh orange that is 4-directionally adjacent to a rotten orange becomes rotten.

Return the minimum number of minutes that must elapse until no cell has a fresh orange. If this is impossible, return -1.
Example 1:
Input: grid = [[2,1,1],[1,1,0],[0,1,1]]
Output: 4
Example 2:

Input: grid = [[2,1,1],[0,1,1],[1,0,1]]
Output: -1
Explanation: The orange in the bottom left corner (row 2, column 0) is never rotten, because rotting only happens 4-directionally


'''
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        num_ones = set()
        num_twos = set()
        fresh_count = 0
        q = deque()
        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 1:
                    fresh_count += 1
                elif grid[row][col] == 2:
                    q.append((row, col))
        if fresh_count == 0:
            return 0
        movements = [(1,0), (0, 1), (-1, 0), (0, -1)]
        minutes = 0
        while q:
            rotted_this_minute = False
            for _ in range(len(q)):
                x, y = q.popleft()
                for x_shift, y_shift in movements:
                    if x + x_shift < rows and x + x_shift >= 0 and y + y_shift < cols and y + y_shift >= 0 and grid[x + x_shift][y + y_shift] == 1:
                        fresh_count -= 1
                        grid[x + x_shift][y + y_shift] = 2
                        q.append((x + x_shift, y + y_shift))
                        rotted_this_minute = True
            if rotted_this_minute:
'''
Time Complexity: O(rows*cols)
Space Complexity: O(rows*cols)
'''

