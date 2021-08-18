"""
416. Partition Equal Subset Sum
Given a non-empty array nums containing only positive integers, find if the array can be partitioned
into two subsets such that the sum of elements in both subsets is equal.

1 <= nums.length <= 200
1 <= nums[i] <= 100
"""

from typing import List


class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        def dfs(nums, target, cache):
            if target < 0: return False
            if target == 0: return True
            if target in cache: return False
            cache.add(target)
            for i, n in enumerate(nums):
                if dfs(nums[i + 1:], target - n, cache): return True
            return False

        s = sum(nums)
        if s % 2 != 0: return False
        return dfs(nums, s // 2, set())


if __name__ == "__main__":
    s = Solution()
    nums = [1,5,11,5]
    print(s.canPartition(nums), True)
    nums = [1,2,5]
    print(s.canPartition(nums), False)

"""
Runtime: 88 ms, faster than 95.84% of Python3 online submissions for Partition Equal Subset Sum.
Memory Usage: 14.6 MB, less than 73.64% of Python3 online submissions for Partition Equal Subset Sum.
"""