"""
55. Jump Game

You are given an integer array nums. You are initially positioned at the array's first index, and each element in the array represents your maximum jump length at that position.

Return true if you can reach the last index, or false otherwise.
"""
class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        n = len(nums)
        if n==1:
            return True
        i, curMax = 0, 0
        while i <= curMax:
            curMax = max(i+nums[i], curMax)
            i += 1
            if curMax >= n-1:
                return True
        if curMax < n-1:
            return False

"""
Runtime: 404 ms, faster than 72.67% of Python online submissions for Jump Game.
Memory Usage: 14.4 MB, less than 84.63% of Python online submissions for Jump Game.
"""