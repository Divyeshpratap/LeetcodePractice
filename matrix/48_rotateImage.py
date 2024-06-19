'''
You are given an n x n 2D matrix representing an image, rotate the image by 90 degrees (clockwise).

You have to rotate the image in-place, which means you have to modify the input 2D matrix directly. DO NOT allocate another 2D matrix and do the rotation.
'''
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        left, right = 0, len(matrix[0]) - 1

        while left < right:
            for i in range(right - left):
                top, bottom = left, right
                topLeft = matrix[top][left + i]
                matrix[top][left + i] = matrix[bottom - i][left]
                matrix[bottom - i][left] = matrix[bottom][right - i]
                matrix[bottom][right - i] = matrix[top + i][right]
                matrix[top + i][right] = topLeft

            left = left + 1
            right = right - 1
'''
Time Complexity: O(rows*columns)
Space Complexity: O(1)
**********************
Summary Statistics:
Runtime: 33 ms, faster than 87.11% of Python3 online submissions for Rotate Image.
Memory Usage: 16.6 MB, less than 50.81% of Python3 online submissions for Rotate Image.
'''
