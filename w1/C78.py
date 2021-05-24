"""
78. Subsets

Given an integer array nums of unique elements, return all possible subsets (the power set).

The solution set must not contain duplicate subsets. Return the solution in any order.
"""

class Solution(object):
    def subsets(self, nums):
        res = []

        if len(nums)==1:
            res = [[], nums]

        else:
            for subset in self.subsets(nums[1:]):
                res.append([nums[0]]+subset)
                res.append(subset)
        return res

"""
Runtime: 16 ms, faster than 93.45% of Python online submissions for Subsets.
Memory Usage: 13.6 MB, less than 69.89% of Python online submissions for Subsets.
"""

a = Solution()
print(a.subsets([1,2,3]))