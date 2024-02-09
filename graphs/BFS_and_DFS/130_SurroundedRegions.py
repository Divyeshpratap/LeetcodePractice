'''
Given an m x n matrix board containing 'X' and 'O', capture all regions that are 4-directionally surrounded by 'X'.

A region is captured by flipping all 'O's into 'X's in that surrounded region.
'''
class Solution:
    def solve(self, board: List[List[str]]) -> None:


        def dfs(x, y):
            if board[x][y] == 'O':
                board[x][y] = 'F'
                if x + 1 < len(board):
                    dfs(x + 1, y)
                if y + 1 < len(board[0]):
                    dfs(x, y + 1)
                if x - 1 > 0:
                    dfs(x - 1, y)
                if y - 1 > 0:
                    dfs(x, y - 1)
            return



        for i in range(len(board)):
            for j in range(len(board[0])):
                if (i == 0 or j == 0 or i == len(board) - 1 or j == len(board[0]) - 1) and board[i][j] == 'O' :
                    dfs(i, j)


        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == 'O':
                    board[i][j] = 'X'

        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == 'F':
                    board[i][j] = 'O'

        return
'''
Time Complexity: O(m*n)
Space Complexity: O(1)
'''
