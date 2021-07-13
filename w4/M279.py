"""
279. Perfect Squares

Given an integer n, return the least number of perfect square numbers that sum to n.

A perfect square is an integer that is the square of an integer;
in other words, it is the product of some integer with itself.
For example, 1, 4, 9, and 16 are perfect squares while 3 and 11 are not.

1 <= n <= 10^4

"""

from typing import List


class Solution:
    dp = [-1]*10000
    def numSquares(self, n: int) -> int:
        import math
        if Solution.dp[n-1] != -1:
            return Solution.dp[n-1]

        sqr = math.sqrt(n)
        if sqr == int(sqr):
            Solution.dp[n - 1] = 1
            return 1
        candi = []
        k = 1
        while n >= k*k:
            candi.append(self.numSquares(n - k*k))
            k += 1

        ans = min(candi)+1
        Solution.dp[n-1] = ans
        return ans

if __name__ == "__main__":
    s = Solution()
    n = 12
    print(s.numSquares(n), 3)

    n = 13
    print(s.numSquares(n), 2)
"""
Runtime: 276 ms, faster than 79.51% of Python3 online submissions for Perfect Squares.
Memory Usage: 20.7 MB, less than 14.16% of Python3 online submissions for Perfect Squares.
"""


