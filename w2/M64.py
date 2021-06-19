"""
64. Minimum Path Sum
Given a m x n grid filled with non-negative numbers, find a path from top left to bottom right, which minimizes the sum of all numbers along its path.

Note: You can only move either down or right at any point in time.
m == grid.length
n == grid[i].length
1 <= m, n <= 200
0 <= grid[i][j] <= 100
"""

from typing import List
class Solution:
    answer = float("inf")
    def minPathSum(self, grid: List[List[int]]) -> int:
        from collections import defaultdict
        # top left : 0,0 bottm right : m, n
        # 기본적으로 경우의 수는 (m+n)! / m! n! = m+nCn 이다.
        # 그래서 전체 탐색하면 망한다.

        Solution.answer = float("inf")
        # passed = defaultdict(list)
        m = len(grid)
        n = len(grid[0])

        #  특정점을 지나는 양쪽의 수를 합하면 됨

        # 반드시 지나야 하는 라인이 존재함.

        # 왼쪽 아래 부터 대각선으로 하나씩 올라가는 점은 반드시 지나야함.
        # 이 점들의 개수 : 0,m => n, m-n if m > n else 0,m => m, 0
        # 결국 max(m,n)개가 나온다.
        # 각각을 더하면 sum_r : (m-r + r)Cr = mCr = m!/(m-r)!r! r = 0, max(m,n) <= 2^m
        # 이걸 또 계속 해야 할 수도
        # i,j => x,y로 가는 최소 경로를 찾는 알고를 짜고, 이를 대각선들로 쪼개서 max를 구하면 된다.
        # 좌측 상단에서 하는거랑 우측 하단에서 하는거로 나눈다.

        lefttop = [[0 for j in range(min(m-i,n)) ] for i in range(m)]
        # rigth bottom 골이랑 같은 row가 0으로 취급. 실제랑 m-i-1, n-j-1관계임.
        rightbottom = [[0 for j in range(n - i)] for i in range(m) if n - i > 0]

        def calc_lt(i,j):
            if lefttop[i][j] != 0:
                return lefttop[i][j]

            if j == 0:
                pathsum = 0
                for t in range(i+1):
                    pathsum += grid[t][0]

                lefttop[i][j] = pathsum
                return pathsum

            if i == 0:
                pathsum = sum(grid[0][:j+1])
                lefttop[i][j] = pathsum

                return pathsum

            pathsum = min(calc_lt(i-1,j), calc_lt(i,j-1)) + grid[i][j]
            lefttop[i][j] = pathsum
            return pathsum

        # rigth bottom 골이랑 같은 row가 0으로 취급. 실제랑 m-i-1, n-j-1관계임.
        def calc_rb(i, j):
            if rightbottom[i][j] != 0:
                return rightbottom[i][j]

            if j == 0:
                pathsum = 0
                for t in range(i + 1):
                    pathsum += grid[m-t-1][n-1]

                rightbottom[i][j] = pathsum
                return pathsum

            if i == 0:
                pathsum = sum(grid[m-1][n-j-1:])
                rightbottom[i][j] = pathsum

                return pathsum

            pathsum = min(calc_rb(i - 1, j), calc_rb(i, j - 1)) + grid[m-1-i][n-1-j]
            rightbottom[i][j] = pathsum
            return pathsum


        if len(rightbottom) < len(lefttop):
            candi_points = [(m-i-1, n - len(rightbottom[i])) for i in range(len(rightbottom))]
        else:
            candi_points = [(i, len(lefttop[i]) - 1) for i in range(len(lefttop))]

        test = float("inf")
        for (x, y) in candi_points:
            test = min(test, calc_lt(x,y) + calc_rb(m-x-1, n-y-1) - grid[x][y])

        return test
        # def sumPath(i, j, pathSum):
        #     if passed[(i, j)] == 1:
        #         return
        #     passed[(i,j)] = 1
        #     pathSum += grid[i][j]
        #     if i == m-1 and j == n-1:
        #         if Solution.answer > pathSum:
        #             Solution.answer = pathSum
        #
        #         return
        #     if i < m-1:
        #         sumPath(i+1,j, pathSum)
        #     if j < n-1:
        #         sumPath(i, j+1, pathSum)
        # sumPath(0,0,0)
        # return int(Solution.answer)


if __name__ == "__main__":
    s = Solution()
    grid = [[1, 3, 1], [1, 5, 1], [4, 2, 1]]
    print(s.minPathSum(grid), 7)
    grid = [[1,2,3],[4,5,6]]
    print(s.minPathSum(grid), 12)
    grid = [[1,2],[5,6],[1,1]]
    print(s.minPathSum(grid), 8)
    # 1 2
    # 5 6
    # 1 1 8

"""
Runtime: 124 ms, faster than 23.71% of Python3 online submissions for Minimum Path Sum.
Memory Usage: 16.1 MB, less than 16.26% of Python3 online submissions for Minimum Path Sum.
"""