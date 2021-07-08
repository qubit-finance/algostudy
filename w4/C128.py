"""
128. Longest Consecutive Sequence

Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.

You must write an algorithm that runs in O(n) time.
"""

class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        if not nums:
            return 0
        
        from collections import defaultdict
        
        dic = defaultdict(int)
        
        for num in set(nums):
            dic[num] += 1
            l, r = dic[num-1], dic[num+1]
            if dic[num-1]:
                dic[num-1] += (1+r)
                for i in range(2, len(nums)+1):
                    if dic[num-i]==0:
                        break
                    dic[num-i] = dic[num-1]
            if dic[num+1]:
                dic[num+1] += (1+l)
                for i in range(2, len(nums)+1):
                    if dic[num+i]==0:
                        break
                    dic[num+i] = dic[num+1]
            dic[num] += (l+r)
                
            
        return max(dic.values())

"""
Time Limits Exceeded
"""

class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        nums = set(nums)
        curmax = 0
        
        if not nums:
            return 0
        
        while nums:
            num = nums.pop()
            i, j, l, r = 1, 1, 0, 0
            while num-i in nums: # Set에서 in Operation은 Hash (O(1))
                nums.remove(num-i) # 핵심: 각 원소를 한번만 살핌으로써 O(n) 유지 <- 없으면 Time Limit 초과
                i += 1
                l += 1
            while num+j in nums: # Set에서 in Operation은 Hash (O(1))
                nums.remove(num+j) # 핵심: 각 원소를 한번만 살핌으로써 O(n) 유지 <- 없으면 Time Limit 초과
                j += 1
                r += 1
            curmax = max(curmax, l+r+1)
            
        return curmax

"""
Runtime: 160 ms, faster than 73.49% of Python online submissions for Longest Consecutive Sequence.
Memory Usage: 26.2 MB, less than 21.35% of Python online submissions for Longest Consecutive Sequence.
"""