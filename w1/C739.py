"""
739. Daily Temperatures

Given a list of daily temperatures temperatures, return a list such that, for each day in the input, tells you how many days you would have to wait until a warmer temperature. If there is no future day for which this is possible, put 0 instead.

For example, given the list of temperatures temperatures = [73, 74, 75, 71, 69, 72, 76, 73], your output should be [1, 1, 4, 2, 1, 1, 0, 0].

Note: The length of temperatures will be in the range [1, 30000]. Each temperature will be an integer in the range [30, 100].
"""

import collections


class Solution(object):
    def dailyTemperatures(self, temperatures):
        """
        :type temperatures: List[int]
        :rtype: List[int]
        """
        ans = [0] * len(temperatures)
        memo = dict()

        for i, v in enumerate(temperatures):
            for key in memo.keys():
                if memo[key] < v:
                    del memo[key]
                    ans[key] = i-key
            memo[i] = v

        return ans

"""
Time Limit Exceeded
"""

class Solution(object):
    def dailyTemperatures(self, temperatures):
        """
        :type temperatures: List[int]
        :rtype: List[int]
        """

        stack, ans = [], [0]*len(temperatures)

        for i, v in enumerate(temperatures):
            while stack  and temperatures[stack[-1]] < v:
                cur = stack.pop()
                ans[cur] = i-cur
            stack.append(i)

        return ans

"""
Runtime: 452 ms, faster than 85.92% of Python online submissions for Daily Temperatures.
Memory Usage: 17.2 MB, less than 82.60% of Python online submissions for Daily Temperatures.
"""