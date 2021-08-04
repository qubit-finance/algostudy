"""
560. Subarray Sum Equals K

Given an array of integers nums and an integer k,
return the total number of continuous subarrays whose sum equals to k.

1 <= nums.length <= 2 * 10^4
-1000 <= nums[i] <= 1000
-10^7 <= k <= 10^7

"""

# Definition for a binary tree node.


from typing import List


class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        from collections import defaultdict
        if len(nums) == 0:
            return 0

        accsum = [0]
        helper_dict = defaultdict(list)
        helper_dict[0].append(0)
        answer = 0

        for i, num in enumerate(nums):  # O(N)
            accsum.append(num + accsum[-1])
            answer += len(helper_dict[accsum[-1] - k])
            helper_dict[accsum[i + 1]].append(i + 1)

        return answer


if __name__ == "__main__":
    s = Solution()
    nums = [1,1,1]
    k = 2
    print(s.subarraySum(nums, k), 2)
    nums = [1, 2, 3]
    k = 3
    print(s.subarraySum(nums, k), 2)

"""
Runtime: 308 ms, faster than 15.71% of Python3 online submissions for Subarray Sum Equals K.
Memory Usage: 22 MB, less than 8.76% of Python3 online submissions for Subarray Sum Equals K.
"""


