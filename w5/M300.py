"""
300. Longest Increasing Subsequence

Given an integer array nums, return the length of the longest strictly increasing subsequence.

A subsequence is a sequence that can be derived from an array by deleting some or no elements
without changing the order of the remaining elements.
For example, [3,6,2,7] is a subsequence of the array [0,3,1,6,2,2,7].

1 <= nums.length <= 2500
-10^4 <= nums[i] <= 10^4


Follow up: Can you come up with an algorithm that runs in O(n log(n)) time complexity?
"""

from typing import List


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        res = []
        for num in nums:
            for i, v in enumerate(res):
                if num <= v:
                    res[i] = num
                    break
            else:
                res.append(num)
        return len(res)

if __name__ == "__main__":
    s = Solution()
    nums = [10,9,2,5,3,7,101,18]
    print(s.lengthOfLIS(nums), 4)

    nums = [0,1,0,3,2,3]
    print(s.lengthOfLIS(nums), 4)

    nums = [7,7,7,7,7,7,7]
    print(s.lengthOfLIS(nums), 1)

    nums = [1, 3, 6, 7, 9, 4, 10, 5, 6]
    print(s.lengthOfLIS(nums), 6)

    nums = [4, 10, 4, 3, 8, 9]
    print(s.lengthOfLIS(nums), 3)


"""
Runtime: 272 ms, faster than 66.37% of Python3 online submissions for Longest Increasing Subsequence.
Memory Usage: 14.5 MB, less than 76.28% of Python3 online submissions for Longest Increasing Subsequence.
"""


