"""
494. Target Sum

You are given an integer array nums and an integer target.

You want to build an expression out of nums by adding one of the symbols '+' and '-'
before each integer in nums and then concatenate all the integers.

For example, if nums = [2, 1], you can add a '+' before 2 and a '-' before 1
and concatenate them to build the expression "+2-1".
Return the number of different expressions that you can build,
which evaluates to target.

1 <= nums.length <= 20
0 <= nums[i] <= 1000
0 <= sum(nums[i]) <= 1000
-1000 <= target <= 1000

"""

from typing import List


class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        # 일단 dfs로 그냥 무식하게 하는거 확인
        from collections import defaultdict
        dp = defaultdict(dict)

        def dfs(i, cumsum):

            if i == len(nums):
                if cumsum == target:
                    return 1
                else:
                    return 0

            if cumsum in dp[i]:
                return dp[i][cumsum]

            if not cumsum - nums[i] in dp[i+1]:
                dp[i + 1][cumsum - nums[i]] = dfs(i + 1, cumsum - nums[i])

            if not cumsum + nums[i] in dp[i+1]:
                dp[i + 1][cumsum + nums[i]] = dfs(i + 1, cumsum + nums[i])

            dp[i][cumsum] = dp[i + 1][cumsum - nums[i]] + dp[i + 1][cumsum + nums[i]]
            return dp[i][cumsum]

        return dfs(0,0)

if __name__ == "__main__":
    s = Solution()
    nums = [1,1,1,1,1]
    target = 3
    print(s.findTargetSumWays(nums, target), 5)
    nums = [1]
    target = 1
    print(s.findTargetSumWays(nums, target), 1)


"""
Runtime: 496 ms, faster than 16.50% of Python3 online submissions for Target Sum.
Memory Usage: 24.5 MB, less than 28.38% of Python3 online submissions for Target Sum.
"""


