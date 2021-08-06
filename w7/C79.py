"""
79. Word Search

Given an m x n grid of characters board and a string word, return true if word exists in the grid.

The word can be constructed from letters of sequentially adjacent cells, where adjacent cells are horizontally or vertically neighboring. The same letter cell may not be used more than once.
"""

class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        from collections import defaultdict
        
        def check(board, word):
            cnt = defaultdict(int)
            for row in board:
                for letter in row:
                    cnt[letter] += 1
            for letter in word:
                cnt[letter] -= 1
                if cnt[letter] < 0:
                    return False
            return True
        
        def helper(r, c, idx, board):
            if r<0 or c<0 or r>=len(board) or c>=len(board[0]) or board[r][c]!=word[idx]:
                return False
            if idx+1 == len(word):
                return True

            tmp = board[r][c]
            board[r][c] = -1
            res = helper(r-1, c, idx+1, board) or helper(r, c-1, idx+1, board) or helper(r+1, c, idx+1, board) or helper(r, c+1, idx+1, board)
            board[r][c] = tmp
            return res
        
        if not check(board, word):
            return False

        for r in range(len(board)):
            for c in range(len(board[0])):
                if helper(r, c, 0, board):
                    return True
        return False

"""
Runtime: 1564 ms, faster than 96.72% of Python online submissions for Word Search.
Memory Usage: 13.5 MB, less than 40.73% of Python online submissions for Word Search.
"""