"""
34. Find First and Last Position of Element in Sorted Array

Given an array of integers nums sorted in ascending order, find the starting and ending position of a given target value.

If target is not found in the array, return [-1, -1].

You must write an algorithm with O(log n) runtime complexity.
"""

class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        
        l, r = 0, len(nums)
        idx = r // 2 # Bisection
        flag = False # Has encountered target
        
        while l < r:
            if nums[idx] > target:
                r = idx 
                idx = (idx-l) // 2
            elif nums[idx] < target:
                l = idx + 1
                idx = idx + (r-idx) // 2
            else:
                flag = True # Has just encountered target value
                break
        
        if flag == False:
            return [-1, -1]
                
        res = []
        
        for i in range(1, len(nums)+1): # To the left
            if idx-i<0 or nums[idx-i] != target:
                res.append(idx-i+1)
                break

        for i in range(1, len(nums)+1): # To the right
            if idx+i>=len(nums) or nums[idx+i] != target :
                res.append(idx+i-1)
                break
                
        return res

"""
Runtime: 56 ms, faster than 99.05% of Python online submissions for Find First and Last Position of Element in Sorted Array.
Memory Usage: 14.9 MB, less than 5.95% of Python online submissions for Find First and Last Position of Element in Sorted Array.
"""