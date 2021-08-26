"""
79. Word Search

Given an m x n grid of characters board and a string word,
return true if word exists in the grid.

The word can be constructed from letters of sequentially adjacent cells,
where adjacent cells are horizontally or vertically neighboring.
The same letter cell may not be used more than once.


m == board.length
n = board[i].length
1 <= m, n <= 6
1 <= word.length <= 15
board and word consists of only lowercase and uppercase English letters.

Follow up: Could you use search pruning
to make your solution faster with a larger board?
"""

from typing import List


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        from collections import defaultdict
        M = len(board)
        N = len(board[0])
        L = len(word)
        print(M, N)


        def dfs(ro, co, idx):
            if ro < 0 or ro >= M or co < 0 or co >= N:
                return False

            if board[ro][co] != word[idx]:
                return False

            if idx == L - 1:
                return True

            temp = board[ro][co]
            board[ro][co] = '7'
            u = dfs(ro + 1, co, idx + 1)
            d = dfs(ro - 1, co, idx + 1)
            r = dfs(ro, co + 1, idx + 1)
            l = dfs(ro, co - 1, idx + 1)
            ans = u or d or r or l
            board[ro][co] = temp

            return ans

        fchar = word[0]
        for row in range(M):
            for col in range(N):
                c = board[row][col]
                if c == fchar:
                    temp = dfs(row, col, 0)
                    if temp:
                        return True

        return False


if __name__ == "__main__":
    board = [["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]]
    word = "ABCB"
    s = Solution()
    print(s.exist(board, word), False)
    board = [["A", "B", "C", "E"], ["S", "F", "E", "S"], ["A", "D", "E", "E"]]
    word = "ABCESEEEFS"
    print(s.exist(board, word), True)

"""
Runtime: 7060 ms, faster than 28.86% of Python3 online submissions for Word Search.
Memory Usage: 14.2 MB, less than 89.89% of Python3 online submissions for Word Search.
"""


