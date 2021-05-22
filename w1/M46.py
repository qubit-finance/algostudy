from typing import List
# 46. Permutations

# Given an array nums of distinct integers, return all the possible permutations. You can return the answer in any order.

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        import itertools

        return itertools.permutations(nums)

# Runtime: 40 ms, faster than 64.22% of Python3 online submissions for Permutations.
# Memory Usage: 14.2 MB, less than 96.86% of Python3 online submissions for Permutations.
