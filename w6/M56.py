"""
56. Merge Intervals
Given an array of intervals where intervals[i] = [starti, endi],
merge all overlapping intervals,
and return an array of the non-overlapping intervals that cover all the intervals in the input.

1 <= intervals.length <= 10^4
intervals[i].length == 2
0 <= starti <= endi <= 10^4
"""

from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        invervs =sorted(intervals, key=lambda x: x[0])
        ans = []
        ans.append(invervs[0])
        for intv in invervs:
            if ans[-1][1] >= intv[0]:
                ans[-1][1] = max(intv[1], ans[-1][1])
            else:
                ans.append(intv)

        return ans

if __name__ == "__main__":
    s = Solution()
    intervals = [[1,4],[4,5]]
    print(s.merge(intervals), [[1,5]])
    intervals = [[1,3],[2,6],[8,10],[15,18]]
    print(s.merge(intervals), [[1,6],[8,10],[15,18]])

"""
Runtime: 84 ms, faster than 75.95% of Python3 online submissions for Merge Intervals.
Memory Usage: 16.2 MB, less than 55.37% of Python3 online submissions for Merge Intervals.
"""