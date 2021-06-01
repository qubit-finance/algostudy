"""
39. Combination Sum

Given an array of distinct integers candidates and a target integer target, return a list of all unique combinations of candidates where the chosen numbers sum to target. You may return the combinations in any order.

The same number may be chosen from candidates an unlimited number of times. Two combinations are unique if the frequency of at least one of the chosen numbers is different.

It is guaranteed that the number of unique combinations that sum up to target is less than 150 combinations for the given input.
"""

class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        self.res = []

        def helper(nums, target, path):
            if target < 0:
                return
            elif target == 0:
                self.res.append(path)
            else:
                for i in range(len(nums)):
                    helper(nums[i:], target-nums[i], path+[nums[i]])                

        helper(candidates, target, [])

        return self.res

"""
Runtime: 88 ms, faster than 46.42% of Python online submissions for Combination Sum.
Memory Usage: 13.7 MB, less than 12.10% of Python online submissions for Combination Sum.
"""