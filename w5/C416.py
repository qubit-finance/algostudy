"""
416. Partition Equal Subset Sum

Given a non-empty array nums containing only positive integers, find if the array can be partitioned into two subsets such that the sum of elements in both subsets is equal.
"""

class Solution(object):
    def canPartition(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        Sum = sum(nums)
        if Sum % 2 == 1:
            return False
        res = [True]+[False]*(Sum//2)
        
        for num in nums:
            res = [res[x] or (x>=num and res[x-num]) for x in range(Sum//2+1)]
            if res[Sum//2]:
                return True
        return False

"""
Runtime: 708 ms, faster than 77.97% of Python online submissions for Partition Equal Subset Sum.
Memory Usage: 13.8 MB, less than 79.24% of Python online submissions for Partition Equal Subset Sum.
"""