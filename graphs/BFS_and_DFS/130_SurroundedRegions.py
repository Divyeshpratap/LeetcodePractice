'''
Given an m x n matrix board containing 'X' and 'O', capture all regions that are 4-directionally surrounded by 'X'.

A region is captured by flipping all 'O's into 'X's in that surrounded region.
'''
'''
*****DFS Approach*****
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
**********************
Summary Statistics:
Runtime: 121 ms, faster than 51.15% of Python3 online submissions for Surrounded Regions.
Memory Usage: 18 MB, less than 43.35% of Python3 online submissions for Surrounded Regions.
*****BFS Approach*****
'''
class Solution:
    def solve(self, board: List[List[str]]) -> None:


        def BFS(i, j):
            steps = [(0, 1), (0, -1), (1, 0), (-1, 0)]
            q = deque()
            q.append((i, j))
            board[i][j] = 'F'
            while q:
                i, j = q.popleft()
                for sI, sJ in steps:
                    r, c = i + sI, j + sJ
                    if ((r, c) not in visited) and r in range(rows) and c in range(cols) and board[r][c] in ('O', 'F'):
                        visited.add((r, c))
                        board[r][c] = 'F'
                        q.append((r,c))
            return

        rows, cols = len(board), len(board[0])
        visited = set()
        for dr in range(rows):
            for dc in range(cols):
                if (((dr == 0 or dr == rows - 1) and (dc in range(cols))) or ((dc == 0 or dc == cols - 1) and (dr in range(rows)))) and (board[dr][dc] == "O"):
                    visited.add((dr, dc))
                    BFS(dr, dc)

        for dr in range(rows):
            for dc in range(cols):
                # if dr not in (0, rows - 1) and dc not in (0, cols - 1):
                if board[dr][dc] == 'O':
                    board[dr][dc] = 'X'

        for dr in range(rows):
            for dc in range(cols):
                if (board[dr][dc] == "F"):
                    board[dr][dc] = 'O'
        return
'''
Time Complexity: O(M*N)
Space Complexity: O(1)
**********************
Summary Statistics:
Runtime: 116 ms, faster than 74.90% of Python3 online submissions for Surrounded Regions.
Memory Usage: 18 MB, less than 31.09% of Python3 online submissions for Surrounded Regions.
'''
