"""
221. Maximal Square

Given an m x n binary matrix filled with 0's and 1's, find the largest square containing only 1's and return its area.
"""

class Solution(object):
    def maximalSquare(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        m, n = len(matrix), len(matrix[0])
        curMax = 0
        memo = [[0]*(n+1) for _ in range(m+1)]
        
        for i in range(m):
            for j in range(n):
                if matrix[i][j]=="1":
                    memo[i+1][j+1] = min(memo[i][j], memo[i][j+1], memo[i+1][j]) + 1
                    curMax = max(curMax, memo[i+1][j+1])
        
        return curMax**2

"""
Runtime: 164 ms, faster than 91.83% of Python online submissions for Maximal Square.
Memory Usage: 22.1 MB, less than 62.36% of Python online submissions for Maximal Square.
"""