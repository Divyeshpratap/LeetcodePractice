'''
Given an m x n integer matrix matrix, if an element is 0, set its entire row and column to 0's.

You must do it in place.

Input: matrix = [[1,1,1],[1,0,1],[1,1,1]]
Output: [[1,0,1],[0,0,0],[1,0,1]]
'''
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        zeroPositions = set()

        for row in range(len(matrix)):
            for col in range(len(matrix[0])):
                if matrix[row][col] == 0:
                    zeroPositions.add((row, col))

        for row, col in zeroPositions:
            matrix[row] = [0] * len(matrix[0])
            for i in range(len(matrix)):
                matrix[i][col] = 0
'''
Time Complexity: O(len(rows) * len(cols))
Space Complexity: Worst Case O(len(rows) * len(cols))
*****************************************************
Summary Statistics:
Runtime: 0 ms, faster than 100.00% of Python3 online submissions for Set Matrix Zeroes.
Memory Usage: 17.3 MB, less than 87.78% of Python3 online submissions for Set Matrix Zeroes.
'''
