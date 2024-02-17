'''
Determine if a 9 x 9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:

Each row must contain the digits 1-9 without repetition.
Each column must contain the digits 1-9 without repetition.
Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.
Note:

A Sudoku board (partially filled) could be valid but is not necessarily solvable.
Only the filled cells need to be validated according to the mentioned rules.
'''
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in range(9):
            ls = []
            for j in range(9):
                if board[i][j] != '.':
                    ls.append(board[i][j])
            lsUnique = set(ls)
            if len(ls) != len(lsUnique):
                return False

        for j in range(9):
            ls = []
            for i in range(9):
                if board[i][j] != '.':
                    ls.append(board[i][j])
            lsUnique = set(ls)
            if len(ls) != len(lsUnique):
                return False

        for i in range(0, 9, 3):
            for j in range(0, 9, 3):
                ls = []
                for m in range(i, i+3):
                    for n in range(j, j+3):
                        if board[m][n] !='.':
                            ls.append(board[m][n])
                lsUnique = set(ls)
                if len(lsUnique) != len(ls):
                    return False
        return True
'''
Time Complexity: O(M^2)
Space Complexity: O(M)
'''
