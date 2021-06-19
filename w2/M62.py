"""
62. Unique Paths
A robot is located at the top-left corner of a m x n grid (marked 'Start' in the diagram below).

The robot can only move either down or right at any point in time. The robot is trying to reach the bottom-right corner of the grid (marked 'Finish' in the diagram below).

How many possible unique paths are there?

1 <= m, n <= 100
It's guaranteed that the answer will be less than or equal to 2 * 109.
"""


class Solution:
    answer = [[0 for _ in range(j+1)] for j in range(100)]
    def uniquePaths(self, m: int, n: int) -> int:
        # (i,j) 는 answer max-1, min-1 으로 보면 된다.
        i = max(m,n) - 1
        j = min(m,n) - 1
        if m == 1 or n == 1:
            Solution.answer[i][j] = 1
            return 1
        if Solution.answer[i][j] != 0:
            return Solution.answer[i][j]

        Solution.answer[i][j] = self.uniquePaths(m-1, n) + self.uniquePaths(m, n-1)
        return Solution.answer[i][j]


if __name__ == "__main__":
    s = Solution()
    print(s.uniquePaths(3,7), 28)
    print(s.uniquePaths(3, 2), 3)
    print(s.uniquePaths(7, 3), 28)
    print(s.uniquePaths(3, 3), 6)

"""
Runtime: 32 ms, faster than 65.86% of Python3 online submissions for Unique Paths.
Memory Usage: 14.3 MB, less than 64.49% of Python3 online submissions for Unique Paths.
"""