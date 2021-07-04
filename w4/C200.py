"""
200. Number of Islands

Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water), return the number of islands.

An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.
"""

class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        cnt = 0

        def dfs(i, j):
            grid[i][j] = 0
            for (dx,dy) in [(1,0), (-1,0), (0,1), (0,-1)]:
                x, y = i+dx, j+dy
                if 0<=x<len(grid) and 0<=y<len(grid[0]) and grid[x][y]=="1":
                    dfs(x,y)
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]=="1":
                    cnt += 1
                    dfs(i, j)
        

        return cnt

"""
Runtime: 128 ms, faster than 61.43% of Python online submissions for Number of Islands.
Memory Usage: 21.7 MB, less than 17.47% of Python online submissions for Number of Islands.
"""