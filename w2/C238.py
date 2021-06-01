"""
238. Product of Array Except Self

Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].

The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

You must write an algorithm that runs in O(n) time and without using the division operation.
"""

class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        ans = [1] * len(nums)

        lval, rval = 1, 1

        for lidx, ridx in zip(range(len(nums)-1), range(len(nums)-1, 0, -1)):
            lval *= nums[lidx]
            rval *= nums[ridx]
            ans[lidx+1] *= lval
            ans[ridx-1] *= rval
        return ans

"""
Runtime: 232 ms, faster than 21.29% of Python online submissions for Product of Array Except Self.
Memory Usage: 27.1 MB, less than 5.40% of Python online submissions for Product of Array Except Self.
"""