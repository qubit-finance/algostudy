"""
22. Generate Parentheses

Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.
"""

class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        self.ans = []
        # Keep track of left and right ('casuse right in cur cannot exceed left)
        def helper(cur, left, right):
            if left:
                helper(cur+"(", left-1, right)
            if right > left:
                helper(cur+")", left, right-1)
            if not right: # When there's no more parenthesis left to add
                self.ans.append(cur)
        helper("", n, n)
        return self.ans
