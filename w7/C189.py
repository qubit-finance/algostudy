"""
189. Rotate Array

Given an array, rotate the array to the right by k steps, where k is non-negative.
"""

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n_moves = len(nums)-k if len(nums)>=k else (len(nums)-(k%len(nums)))
        for _ in range(n_moves):
            num = nums.pop(0)
            nums.append(num)

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if k >= len(nums):
            k = k % len(nums)
        if k != 0 and len(nums)>1:
            tmp = nums[:-k]
            nums[:k] = nums[-k:]
            nums[k:] = tmp

"""
Runtime: 220 ms, faster than 69.80% of Python3 online submissions for Rotate Array.
Memory Usage: 25.6 MB, less than 56.78% of Python3 online submissions for Rotate Array.
"""
