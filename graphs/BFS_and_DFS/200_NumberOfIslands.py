'''
Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water), return the number of islands.

An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.
'''
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        island = 0
        pos = [[1, 0], [0, 1], [-1, 0], [0, -1]]
        visited = set()

        def bfs(x, y):
            queue = collections.deque()
            visited.add((x, y))
            queue.append((x, y))
            while queue:
                dx, dy = queue[0]
                for i, j in pos:
                    newX, newY = dx + i, dy + j
                    if 0 <= newX < len(grid) and 0 <= newY < len(grid[0]) and (newX, newY) not in visited and grid[newX][newY] == '1':
                        visited.add((newX, newY))
                        queue.append((newX, newY))
                queue.popleft()
            return


        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if (i, j) not in visited and grid[i][j] == '1':
                    bfs(i, j)
                    island += 1
        return island
'''
Time Complexity: O(N*M)
Space Complexity: O(N*M)
************************
Summary Statistics:
Runtime: 290 ms, faster than 22.59% of Python3 online submissions for Number of Islands.
Memory Usage: 24.3 MB, less than 18.91% of Python3 online submissions for Number of Islands.
'''
