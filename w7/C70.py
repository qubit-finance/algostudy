"""
70. Climbing Stairs

You are climbing a staircase. It takes n steps to reach the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?
"""

class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        ways = [1,2]+[0]*(n-2)
        
        for i in range(2, len(ways)):
            ways[i] = ways[i-1]+ways[i-2]
            
        return ways[n-1]

"""
Runtime: 16 ms, faster than 75.35% of Python online submissions for Climbing Stairs.
Memory Usage: 13.4 MB, less than 35.59% of Python online submissions for Climbing Stairs.
"""