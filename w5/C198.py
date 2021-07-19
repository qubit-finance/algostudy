"""
198. House Robber

You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed, the only constraint stopping you from robbing each of them is that adjacent houses have security systems connected and it will automatically contact the police if two adjacent houses were broken into on the same night.

Given an integer array nums representing the amount of money of each house, return the maximum amount of money you can rob tonight without alerting the police.
"""

class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        n = len(nums)
        
        if n==0:
            return 0
        elif n==1:
            return nums[0]
        
        res = [0] * (n+1)
        
        res[1] = nums[0]
        res[2] = max(nums[0], nums[1])
        
        for i in range(3, n+1):
            res[i] = max(res[i-2]+nums[i-1], res[i-3]+nums[i-1])
            
        return max(res[-3:])

"""
Runtime: 16 ms, faster than 85.00% of Python online submissions for House Robber.
Memory Usage: 13.4 MB, less than 70.06% of Python online submissions for House Robber.
"""