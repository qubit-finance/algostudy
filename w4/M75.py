"""
75. Sort Colors

Given an array nums with n objects colored red, white, or blue, sort them in-place so that objects of the same color are adjacent, with the colors in the order red, white, and blue.

We will use the integers 0, 1, and 2 to represent the color red, white, and blue, respectively.

You must solve this problem without using the library's sort function.
n == nums.length
1 <= n <= 300
nums[i] is 0, 1, or 2.
"""

from typing import List

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        from collections import Counter
        c = Counter(nums)
        for i in range(c[0]):
            nums[i] = 0
        for j in range(c[0], c[0] + c[1]):
            nums[j] = 1
        for k in range(c[0] + c[1], c[0] + c[1] + c[2]):
            nums[k] = 2


if __name__ == "__main__":
    s = Solution()
    nums = [2,0,2,1,1,0]
    print(s.sortColors(nums), "[0,0,1,1,2,2]")

    nums = [2,0,1]
    print(s.sortColors(nums), "[0,1,2]")

    nums = [0]
    print(s.sortColors(nums), "[0]")

    nums = [1]
    print(s.sortColors(nums), "[1]")


"""
Runtime: 32 ms, faster than 75.82% of Python3 online submissions for Sort Colors.
Memory Usage: 14.3 MB, less than 12.49% of Python3 online submissions for Sort Colors.
"""


