'''
According to Wikipedia's article: "The Game of Life, also known simply as Life, is a cellular automaton devised by the British mathematician John Horton Conway in 1970."

The board is made up of an m x n grid of cells, where each cell has an initial state: live (represented by a 1) or dead (represented by a 0). Each cell interacts with its eight neighbors (horizontal, vertical, diagonal) using the following four rules (taken from the above Wikipedia article):

    Any live cell with fewer than two live neighbors dies as if caused by under-population.
    Any live cell with two or three live neighbors lives on to the next generation.
    Any live cell with more than three live neighbors dies, as if by over-population.
    Any dead cell with exactly three live neighbors becomes a live cell, as if by reproduction.

The next state is created by applying the above rules simultaneously to every cell in the current state, where births and deaths occur simultaneously. Given the current state of the m x n grid board, return the next state.
'''
class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        def checkNeighbors(m, n):

            count = 0
            directions = [(-1,-1), (-1, 0) , (-1, 1), (0, -1), (0, 1), (1,-1), (1,0), (1,1)]
            for direction in directions:
                row, column = m + direction[0], n + direction[1]
                if 0 <= row < len(board) and 0 <= column < len(board[0]) and board[row][column] in [1,3]:
                    count += 1

            return count


        for r in range(len(board)):
            for c in range(len(board[0])):
                nei = checkNeighbors(r, c)
                if board[r][c]:
                    if nei in [2, 3]:
                        board[r][c] = 3
                else:
                    if nei == 3:
                        board[r][c] = 2



        for r in range(len(board)):
            for c in range(len(board[0])):
                if board[r][c] in [2,3]:
                    board[r][c] = 1
                elif board[r][c] == 1:
                    board[r][c] = 0
'''
Time Complexity: O(rows*columns)
Space Complexity: O(1), inplace operation, No new space is taken.
**********************
Summary Statistics:
Runtime: 45 ms, faster than 7.21% of Python3 online submissions for Game of Life.
Memory Usage: 16.5 MB, less than 43.39% of Python3 online submissions for Game of Life.
'''
