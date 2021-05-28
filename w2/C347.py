"""
347. Top K Frequent Elements

Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.
"""

class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        from collections import Counter
        return [e for (e, v) in Counter(nums).most_common(k)]

"""
Runtime: 84 ms, faster than 73.65% of Python online submissions for Top K Frequent Elements.
Memory Usage: 16.7 MB, less than 70.26% of Python online submissions for Top K Frequent Elements.
"""