"""
45. Jump Game II

Given an array of non-negative integers nums, you are initially positioned at the first index of the array.

Each element in the array represents your maximum jump length at that position.

Your goal is to reach the last index in the minimum number of jumps.

You can assume that you can always reach the last index.
"""
class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        lev, prev, curMax = 0, 0, 0
        while curMax < n-1:
            lev += 1
            tmp = curMax
            for i in range(prev, curMax+1):
                curMax = max(i+nums[i], curMax)
            prev = tmp
        return lev
"""
Runtime: 92 ms, faster than 94.93% of Python online submissions for Jump Game II.
Memory Usage: 14.5 MB, less than 35.49% of Python online submissions for Jump Game II.
"""