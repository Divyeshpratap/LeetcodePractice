'''
Given an m x n grid of characters board and a string word, return true if word exists in the grid.

The word can be constructed from letters of sequentially adjacent cells, where adjacent cells are horizontally or vertically neighboring. The same letter cell may not be used more than once.
'''
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        
        rows, cols = len(board), len(board[0])
        visited = set()
        def backTrack(r, c, pos):
            if len(word) == pos:
                return True
            if (r < 0 or c < 0 or
                r >= rows or c >= cols or 
                (r, c) in visited or 
                board[r][c] != word[pos]):
                return False
            visited.add((r, c))
            res = (backTrack(r + 1, c, pos + 1) or
                backTrack(r - 1, c, pos + 1) or
                backTrack(r, c + 1, pos + 1) or
                backTrack(r, c - 1, pos + 1))
            visited.remove((r, c))
            return res        
            
        for r in range(rows):
            for c in range(cols):
                if backTrack(r, c, 0): return True
        
        return False
'''
Time Complexity: O(n*m*4^n*len(word))
*************************************
Summary Statistics:
Runtime: 4138 ms, faster than 49.37% of Python3 online submissions for Word Search.
Memory Usage: 16.5 MB, less than 45.73% of Python3 online submissions for Word Search.
'''
