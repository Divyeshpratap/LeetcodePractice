'''
Given a 0-indexed n x n integer matrix grid, return the number of pairs (ri, cj) such that row ri and column cj are equal.

A row and column pair is considered equal if they contain the same elements in the same order (i.e., an equal array).

Input: grid = [[3,2,1],[1,7,6],[2,7,7]]
Output: 1
Explanation: There is 1 equal row and column pair:
- (Row 2, Column 1): [2,7,7]
'''
class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        rowDict = {}
        for rowNum in range(len(grid)):
            row = tuple(grid[rowNum])
            rowDict[row] = rowDict.get(row, 0) + 1

        count = 0
        for colId in range(len(grid)):
            col = tuple([grid[rowId][colId] for rowId in range(len(grid))])
            if col in rowDict:
                count += rowDict.get(col)

        return count
'''
Time Complexity: O(rows*columns)
Space Complexity: O(rows*columns)
'''
