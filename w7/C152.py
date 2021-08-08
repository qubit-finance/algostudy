"""
152. Maximum Product Subarray

Given an integer array nums, find a contiguous non-empty subarray within the array that has the largest product, and return the product.

It is guaranteed that the answer will fit in a 32-bit integer.

A subarray is a contiguous subsequence of the array.
"""

class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        def cont_mul(arr): # Factorial
            init = 0
            for num in arr:
                if not init:
                    init = num
                else:
                    init *= num
            return init
            
        def max_subarr(arr): # Returns the maximum continuous product of a "zero-separated" subarray (meaning this subarray contains no zero)
            if len(arr)==0:
                return 0
            if len(arr)==1:
                return arr[0]
            m_cnt = 0 # Number of minus values (if even, just multiply all / if odd, compare maximum between arr[first+1:], arr[:last])
            fir, las = -1, -1
            for i, v in enumerate(arr):
                if v<0:
                    m_cnt += 1
                    if fir == -1:
                        fir = i
            if m_cnt % 2 == 0:
                return cont_mul(arr)
            if m_cnt > 1:
                for i, v in enumerate(arr[::-1]):
                    if v < 0:
                        las = len(arr)-i-1
                        break
            if m_cnt==1:
                las = fir
            return max(cont_mul(arr[fir+1:]), cont_mul(arr[:las]))
            
        res = -10 # lowest possible value
        prev = -1 # position of previous zero
        for i, v in enumerate(nums):
            if v==0:
                res = max(res, 0) # We can get at least 0 for sure
                if prev==-1: # This is the first zero
                    res = max(res, max_subarr(nums[:i]))
                else: # This is not the first zero in nums
                    res = max(res, max_subarr(nums[prev+1:i]))
                prev = i
        res = max(res, max_subarr(nums[prev+1:])) # The contiguous subarray from the last zero (It also covers the case when there is no zero at all)
        return res

"""
Runtime: 40 ms, faster than 61.96% of Python online submissions for Maximum Product Subarray.
Memory Usage: 13.8 MB, less than 63.81% of Python online submissions for Maximum Product Subarray.
"""