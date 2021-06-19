"""
215. Kth Largest Element in an Array
Given an integer array nums and an integer k, return the kth largest element in the array.

Note that it is the kth largest element in the sorted order, not the kth distinct element.

1 <= k <= nums.length <= 104
-104 <= nums[i] <= 104
"""
from typing import List

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        import heapq

        return heapq.nlargest(k,nums)[-1]


if __name__ == "__main__":
    s = Solution()
    nums = [3, 2, 1, 5, 6, 4]
    k = 2
    print(s.findKthLargest(nums, k), 5)
    nums = [3, 2, 3, 1, 2, 4, 5, 5, 6]
    k = 4
    print(s.findKthLargest(nums, k), 4)


"""
Runtime: 68 ms, faster than 54.15% of Python3 online submissions for Kth Largest Element in an Array.
Memory Usage: 14.9 MB, less than 98.78% of Python3 online submissions for Kth Largest Element in an Array.
"""