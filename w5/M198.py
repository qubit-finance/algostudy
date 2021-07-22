"""
198. House Robber
Share
You are a professional robber planning to rob houses along a street.
Each house has a certain amount of money stashed,
the only constraint stopping you from robbing each of them is that adjacent houses have security systems connected
and it will automatically contact the police if two adjacent houses were broken into on the same night.

Given an integer array nums
representing the amount of money of each house,
return the maximum amount of money you can rob tonight without alerting the police.

1 <= nums.length <= 100
0 <= nums[i] <= 400
"""

from typing import List

class Solution:
    def rob(self, nums: List[int]) -> int:
        N = len(nums)
        dp = [-1] * N

        def get_max(i):
            if i >= N:
                return 0
            if i == N-1:
                return nums[N-1]

            if dp[i] != -1:
                return dp[i]

            ans = max(nums[i] + get_max(i+2), get_max(i+1) )
            dp[i] = ans
            return ans

        return get_max(0)

if __name__ == "__main__":
    s = Solution()
    nums = [1,2,3,1]
    print(s.rob(nums), 4)
    nums = [2,7,9,3,1]
    print(s.rob(nums), 12)

"""
Runtime: 32 ms, faster than 67.61% of Python3 online submissions for House Robber.
Memory Usage: 14.3 MB, less than 19.29% of Python3 online submissions for House Robber.
"""