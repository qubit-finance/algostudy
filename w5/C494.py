"""
494. Target Sum

You are given an integer array nums and an integer target.

You want to build an expression out of nums by adding one of the symbols '+' and '-' before each integer in nums and then concatenate all the integers.

For example, if nums = [2, 1], you can add a '+' before 2 and a '-' before 1 and concatenate them to build the expression "+2-1".
Return the number of different expressions that you can build, which evaluates to target.
"""

class Solution(object):
    def findTargetSumWays(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        self.cnt = 0
        
        def helper(arr, target):
            if len(arr)==1:
                if arr[0]==0 and target==0:
                    self.cnt += 2
                elif arr[0]==target or -arr[0]==target:
                    self.cnt += 1
            elif len(arr)>1:
                helper(arr[1:], target-arr[0]) 
                helper(arr[1:], target+arr[0])
                
        helper(nums, target)
                
        return self.cnt

"""
Time Limit Exceeded
"""

class Solution(object):
    def findTargetSumWays(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        from collections import defaultdict

        cnt = defaultdict(int)
        cnt[0] = 1

        for new_num in nums:
            tmp = defaultdict(int)
            for prev_num in cnt:
                tmp[prev_num+new_num] += cnt[prev_num]
                tmp[prev_num-new_num] += cnt[prev_num]
            cnt = tmp

        return cnt[target]

"""
Runtime: 156 ms, faster than 78.44% of Python online submissions for Target Sum.
Memory Usage: 13.8 MB, less than 53.91% of Python online submissions for Target Sum.
"""