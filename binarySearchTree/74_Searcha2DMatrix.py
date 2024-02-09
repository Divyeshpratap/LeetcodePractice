'''
You are given an m x n integer matrix matrix with the following two properties:

Each row is sorted in non-decreasing order.
The first integer of each row is greater than the last integer of the previous row.
Given an integer target, return true if target is in matrix or false otherwise.

You must write a solution in O(log(m * n)) time complexity.
'''
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        def binarySearch(ls, item):
            start = 0
            end = len(ls) - 1
            # print(f'ls list is {ls}')
            while start <= end:
                mid = (start + end)//2

                if item < ls[mid]:
                    end = mid
                    return binarySearch(ls[start:end], item)
                elif item == ls[mid]:
                    return True
                else:
                    start = mid + 1
                    return binarySearch(ls[start:end+1], item)

        if matrix[0][0] <= target <= matrix[len(matrix) - 1][len(matrix[0]) - 1]:
            columns = len(matrix[0]) - 1
            for i in range(len(matrix)):
                if matrix[i][0] <= target <= matrix[i][columns]:
                    # print(f'Item may be in {i}th row')
                    return binarySearch(matrix[i], target)
        else:
            return False

        return False
'''
Time Complexity: O(m*log(n))
Space Complexity: O(log(n))
'''
