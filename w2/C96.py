"""96. Unique Binary Search Trees

Given an integer n, return the number of structurally unique BST's (binary search trees) which has exactly n nodes of unique values from 1 to n.
"""

class Solution(object):
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """
        memo = {0:1, 1:1} # Memoization to reduce computation on repeated recursions
        def f(x):
            try: # if we've seen such number (in lower level recursion mostly)
                return memo[x] 
            except: # If the given number is the highest level recursion
                res = 0
                for i in range(x):
                    res += f(i)*f(x-i-1) # split left and right (independent)
                memo[x] = res # memoize
                return res
        return f(n)

"""
Runtime: 16 ms, faster than 74.21% of Python online submissions for Unique Binary Search Trees.
Memory Usage: 13.3 MB, less than 60.68% of Python online submissions for Unique Binary Search Trees.
"""