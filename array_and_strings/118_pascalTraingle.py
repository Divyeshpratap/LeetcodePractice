'''
Given an integer numRows, return the first numRows of Pascal's triangle.

In Pascal's triangle, each number is the sum of the two numbers directly above it as shown:
Input: numRows = 5
Output: [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]
'''
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:

        if numRows == 1:
            return [[1]]
        pascalTriangle = []
        pascalTriangle.append([1])
        
        for i in range(1, numRows):
            currentTriangle = [0] + pascalTriangle[-1] + [0]
            tempTriangle = []
            for j in range(len(currentTriangle) - 1):
                tempTriangle = tempTriangle + [(currentTriangle[j] + currentTriangle[j + 1])]
            pascalTriangle.append(tempTriangle)
            
        return pascalTriangle
'''
Time Complexity: O(numRows^2)
Space Complexity: O(numRows^2)
******************************
Summary Statistics;
Runtime: 0 ms, faster than 100.00% of Python3 online submissions for Pascal's Triangle.
Memory Usage: 16.6 MB, less than 64.03% of Python3 online submissions for Pascal's Triangle.
'''
