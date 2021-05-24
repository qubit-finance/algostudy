# 78.Subsets
# Given an integer array nums of unique elements, return all possible subsets (the power set).
#
# The solution set must not contain duplicate subsets. Return the solution in any order.

from typing import List
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        from itertools import combinations

        answer = []
        for i in range(len(nums) + 1):
            answer += list(map(list, combinations(nums, i)))
        return answer

#Runtime: 24 ms, faster than 98.49% of Python3 online submissions for Subsets.
#Memory Usage: 14.3 MB, less than 92.03% of Python3 online submissions for Subsets.
