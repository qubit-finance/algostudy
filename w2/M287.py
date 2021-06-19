"""
287. Find the Duplicate Number
Given an array of integers nums containing n + 1 integers where each integer is in the range [1, n] inclusive.

There is only one repeated number in nums, return this repeated number.

You must solve the problem without modifying the array nums and uses only constant extra space.
"""

from typing import List
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        from collections import Counter

        return Counter(nums).most_common(1)[0][0]


"""
Runtime: 608 ms, faster than 63.38% of Python3 online submissions for Find the Duplicate Number.
Memory Usage: 36.1 MB, less than 6.69% of Python3 online submissions for Find the Duplicate Number.
"""