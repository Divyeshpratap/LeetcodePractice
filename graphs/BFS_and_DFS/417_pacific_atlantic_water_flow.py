'''
There is an m x n rectangular island that borders both the Pacific Ocean and Atlantic Ocean. The Pacific Ocean touches the island's left and top edges, and the Atlantic Ocean touches the island's right and bottom edges.

The island is partitioned into a grid of square cells. You are given an m x n integer matrix heights where heights[r][c] represents the height above sea level of the cell at coordinate (r, c).

The island receives a lot of rain, and the rain water can flow to neighboring cells directly north, south, east, and west if the neighboring cell's height is less than or equal to the current cell's height. Water can flow from any cell adjacent to an ocean into the ocean.

Return a 2D list of grid coordinates result where result[i] = [ri, ci] denotes that rain water can flow from cell (ri, ci) to both the Pacific and Atlantic oceans.
'''
class Solution:
    def __init__(self):
        self.pacific = set()
        self.atlantic = set()

    def dfs(self, r, c, curr_height, visited):
        if (r,c) in visited or r < 0 or c < 0 or r >= self.rows or c >= self.cols or self.heights[r][c] < curr_height:
            return
        else:
            visited.add((r,c))
            self.dfs(r + 1, c, self.heights[r][c], visited)
            self.dfs(r, c + 1, self.heights[r][c], visited)
            self.dfs(r - 1, c, self.heights[r][c], visited)
            self.dfs(r, c - 1, self.heights[r][c], visited)
            return


    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:

        self.rows = len(heights)
        self.cols = len(heights[0])
        self.heights = heights

        for col in range(self.cols):
            self.dfs(0, col, self.heights[0][col], self.pacific)
            self.dfs(self.rows - 1, col, self.heights[self.rows - 1][col], self.atlantic)

        for row in range(self.rows):
            self.dfs(row, 0, self.heights[row][0], self.pacific)
            self.dfs(row, self.cols - 1, self.heights[row][self.cols - 1], self.atlantic)

        grid_coordinates = []
        for r in range(self.rows):
            for c in range(self.cols):
                if (r, c) in self.pacific and (r,c) in self.atlantic:
                    grid_coordinates.append([r,c])

        return grid_coordinates
'''
Time Complexxity: O(m*n)
Space Complexity: O(m*n)
'''
