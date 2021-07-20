"""
560. Subarray Sum Equals K

Given an array of integers nums and an integer k, return the total number of continuous subarrays whose sum equals to k.
"""

class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        
        from collections import defaultdict
        
        cumnums = []
        hashtable = defaultdict(int)
        hashtable[0] = 1
        res = 0
        
        for i in range(len(nums)):
            if i==0:
                cumnums.append(nums[i])
            else:
                cumnums.append(cumnums[i-1]+nums[i])
        
        for idx, val in enumerate(cumnums):
            res += hashtable[val-k]
            hashtable[val] += 1
            
        return res

"""
Runtime: 248 ms, faster than 27.22% of Python online submissions for Subarray Sum Equals K.
Memory Usage: 19.7 MB, less than 6.21% of Python online submissions for Subarray Sum Equals K.
"""