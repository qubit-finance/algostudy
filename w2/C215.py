"""
215. Kth Largest Element in an Array

Given an integer array nums and an integer k, return the kth largest element in the array.

Note that it is the kth largest element in the sorted order, not the kth distinct element.
"""

class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        return sorted(nums)[-k]

"""
Runtime: 52 ms, faster than 64.21% of Python online submissions for Kth Largest Element in an Array.
Memory Usage: 14.1 MB, less than 77.25% of Python online submissions for Kth Largest Element in an Array.
"""