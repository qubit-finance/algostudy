"""
31. Next Permutation

Implement next permutation, which rearranges numbers into the lexicographically next greater permutation of numbers.

If such an arrangement is not possible, it must rearrange it as the lowest possible order (i.e., sorted in ascending order).

The replacement must be in place and use only constant extra memory.
"""
class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        def partial_permute(part): # grab the next largest permuation in the subarray
            if len(part)==2:
                return reversed(part)
            refs = sorted(part[1:])
            for i, n in enumerate(refs):
                if n > part[0]:
                    refs[i] = part[0]
                    return [n] + refs
        n = len(nums)
        if n > 1:
            flag = False
            i = n-1
            while i > 0:
                if nums[i] > nums[i-1]:
                    nums[i-1:] = partial_permute(nums[i-1:])
                    flag = True
                    break
                i -= 1
            if not flag: # This is indeed the largest permutation
                hi, lo = n-1, 0
                while lo < hi:
                    tmp = nums[hi]
                    nums[hi] = nums[lo]
                    nums[lo] = tmp
                    hi -= 1
                    lo += 1

"""
Runtime: 28 ms, faster than 69.56% of Python online submissions for Next Permutation.
Memory Usage: 13.4 MB, less than 68.86% of Python online submissions for Next Permutation.
"""