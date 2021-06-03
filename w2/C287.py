"""
287. Find the Duplicate Number

Given an array of integers nums containing n + 1 integers where each integer is in the range [1, n] inclusive.

There is only one repeated number in nums, return this repeated number.

You must solve the problem without modifying the array nums and uses only constant extra space.
"""

class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        arr = sorted(nums)
        
        for i, v in enumerate(arr):
            if arr[i] == arr[i+1]:
                return v

"""
Runtime: 664 ms, faster than 15.68% of Python online submissions for Find the Duplicate Number.
Memory Usage: 25.3 MB, less than 37.86% of Python online submissions for Find the Duplicate Number.
"""

class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        from collections import Counter
        
        return Counter(nums).most_common(1)[0][0]

"""
Runtime: 720 ms, faster than 13.78% of Python online submissions for Find the Duplicate Number.
Memory Usage: 34.6 MB, less than 5.12% of Python online submissions for Find the Duplicate Number.
"""