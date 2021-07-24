"""
56. Merge Intervals

Given an array of intervals where intervals[i] = [starti, endi], merge all overlapping intervals, and return an array of the non-overlapping intervals that cover all the intervals in the input.
"""

class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        
        intervals = sorted(intervals, key=lambda x: x[0])
        rMax = intervals[0][1]
        tmp = [intervals[0][0], intervals[0][1]]
        ans = []
        
        print(intervals)
        
        for [l, r] in intervals[1:]:
            if l <= rMax:
                rMax = max(rMax, r)
                tmp[1] = rMax
            else:
                ans.append(tmp)
                tmp = [l, r]
                rMax = r
                
        ans.append(tmp)
                
        return ans

"""
Runtime: 84 ms, faster than 26.25% of Python online submissions for Merge Intervals.
Memory Usage: 15.6 MB, less than 96.61% of Python online submissions for Merge Intervals.
"""