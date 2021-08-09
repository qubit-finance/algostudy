"""
15. 3Sum

Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets.
"""
class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if len(nums)<3:
            return []
        res = set()
        nums = sorted(nums)
        for i in range(len(nums)-2):
            if nums[i]>0:
                break
            if i>0 and nums[i]==nums[i-1]:
                continue
            j=i+1
            k=len(nums)-1
            while j<k:
                if nums[i]+nums[j]+nums[k]==0:
                    res.add((nums[i],nums[j],nums[k]))
                    j, k = j+1, k-1
                elif nums[i]+nums[j]+nums[k] < 0:
                    j += 1
                else:
                    k -= 1
        
        return list(res)

"""
Runtime: 732 ms, faster than 63.53% of Python online submissions for 3Sum.
Memory Usage: 16.3 MB, less than 96.00% of Python online submissions for 3Sum.
"""