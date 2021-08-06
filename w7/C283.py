"""
283. Move Zeroes

Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.

Note that you must do this in-place without making a copy of the array.
"""

class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        r = 0
        for _ in range(len(nums)):
            if nums[r] == 0:
                nums.pop(r)
                nums.append(0)
            else:
                r += 1
                
"""
Runtime: 48 ms, faster than 79.97% of Python3 online submissions for Move Zeroes.
Memory Usage: 15.3 MB, less than 88.67% of Python3 online submissions for Move Zeroes.
"""