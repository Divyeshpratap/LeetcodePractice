'''
Given an m x n matrix, return all elements of the matrix in spiral order.
'''
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:

        flat = []
        left, right = 0, len(matrix[0])
        top, bottom = 0, len(matrix)
        while left < right and top < bottom:
            for i in range(left, right):
                flat.append(matrix[top][i])
            top += 1

            for i in range(top, bottom):
                flat.append(matrix[i][right - 1])
            right -= 1

            if not (left < right and top < bottom):
                break

            for i in range(right - 1, left - 1, -1):
                flat.append(matrix[bottom - 1][i])
            bottom -= 1

            for i in range(bottom - 1, top - 1, -1):
                flat.append(matrix[i][left])
            left += 1

        return flat
'''
Time Complexity: O(rows*columns)
Space Complxity: O(rows*columns)
********************************
Summary Statistics:
Runtime: 32 ms, faster than 76.95% of Python3 online submissions for Spiral Matrix.
Memory Usage: 16.4 MB, less than 86.62% of Python3 online submissions for Spiral Matrix.
'''
