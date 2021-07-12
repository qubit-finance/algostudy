"""
300. Longest Increasing Subsequence

Given an integer array nums, return the length of the longest strictly increasing subsequence.

A subsequence is a sequence that can be derived from an array by deleting some or no elements without changing the order of the remaining elements. For example, [3,6,2,7] is a subsequence of the array [0,3,1,6,2,2,7].
"""

class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        res = [1]*len(nums)
        
        for i in range(1, len(nums)):
            for j in range(i):
                if nums[i] > nums[j]:
                    res[i] = max(res[i], res[j]+1)
        
        return max(res)

"""
Runtime: 3440 ms, faster than 33.75% of Python online submissions for Longest Increasing Subsequence.
Memory Usage: 13.7 MB, less than 64.77% of Python online submissions for Longest Increasing Subsequence.
"""

class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        subs = [] # save tails (길이 index까지 가는 subsequence의 가장 작은 마지막 수)

        for num in nums:
            pos, leng = 0, len(subs)
            while pos<=leng:
                if pos==leng:
                    subs.append(num)
                    break
                elif num <= subs[pos]:
                    subs[pos] = num
                    break
                else:
                    pos+= 1

        return len(subs)

"""
Runtime: 344 ms, faster than 73.18% of Python online submissions for Longest Increasing Subsequence.
Memory Usage: 13.8 MB, less than 64.77% of Python online submissions for Longest Increasing Subsequence.
"""