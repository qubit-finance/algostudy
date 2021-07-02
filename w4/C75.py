"""
75. Sort Colors

Given an array nums with n objects colored red, white, or blue, sort them in-place so that objects of the same color are adjacent, with the colors in the order red, white, and blue.

We will use the integers 0, 1, and 2 to represent the color red, white, and blue, respectively.

You must solve this problem without using the library's sort function.
"""

class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i]>nums[j]:
                    tmp = nums[i]
                    nums[i] = nums[j]
                    nums[j] = tmp
                    
        return nums

"""
Runtime: 20 ms, faster than 75.53% of Python online submissions for Sort Colors.
Memory Usage: 13.6 MB, less than 11.64% of Python online submissions for Sort Colors.
"""