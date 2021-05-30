"""
48. Rotate Image

You are given an n x n 2D matrix representing an image, rotate the image by 90 degrees (clockwise).

You have to rotate the image in-place, which means you have to modify the input 2D matrix directly. DO NOT allocate another 2D matrix and do the rotation.
"""

class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        # Rotate by taking each column and replace row
        tmp = [[]] # First column can be just transposed (hence empty list for its first element)
        for i in range(1, len(matrix)):
            tmp.append([matrix[j][i] for j in range(len(matrix)) if i>j]) # These elements will be altered in in-place operation, so keep them (upper triangle entries)
        for i in range(len(matrix)):
            col = [row[i] for row in matrix] # grab each column
            col[:i] = tmp[i] # replace elements that has previously been altered by in-place opoeration
            matrix[i] = col[::-1] # inverse order
        return matrix

"""
Runtime: 20 ms, faster than 79.08% of Python online submissions for Rotate Image.
Memory Usage: 13.2 MB, less than 91.09% of Python online submissions for Rotate Image.
"""