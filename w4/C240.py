"""
240. Search a 2D Matrix II

Write an efficient algorithm that searches for a target value in an m x n integer matrix. The matrix has the following properties:

Integers in each row are sorted in ascending from left to right.
Integers in each column are sorted in ascending from top to bottom.
"""

class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        
        def helper(i, j, target):
            if i<len(matrix) and j<len(matrix[0]):
                if matrix[i][j]==target:
                    return True
                elif matrix[i][j]<target:
                    return helper(i+1,j,target) or helper(i,j+1,target)
                else:
                    return False
            return False
        
        
        return helper(0,0,target)

"""
Time Limit Exceeded
"""

class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        
        m, n = len(matrix), len(matrix[0])
        
        i, j = 0, n-1
        
        while i<m and j>=0:
            if matrix[i][j]==target:
                return True
            elif matrix[i][j]<target:
                i += 1
            else:
                j -= 1
        return False

"""
Runtime: 148 ms, faster than 24.04% of Python online submissions for Search a 2D Matrix II.
Memory Usage: 19.4 MB, less than 75.43% of Python online submissions for Search a 2D Matrix II.
"""