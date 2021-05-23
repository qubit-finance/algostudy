"""
46. Permutations

Given an array nums of distinct integers, return all the possible permutations. You can return the answer in any order.
"""

class Solution(object):
    def permute(self, nums):

        res = []

        if len(nums)==1: # Boundary Condition
            res = [nums]
        else:
            for i in range(len(nums)): # Each letter can come first
                for subp in self.permute(nums[:i]+nums[i+1:]): # Every ensuing sub-permutation
                    res.append(nums[i:i+1]+subp)

        return res

"""
Runtime: 28 ms, faster than 64.57% of Python online submissions for Permutations.
Memory Usage: 13.5 MB, less than 86.38% of Python online submissions for Permutations.
"""