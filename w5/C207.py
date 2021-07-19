"""
207. Course Schedule

There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1. You are given an array prerequisites where prerequisites[i] = [ai, bi] indicates that you must take course bi first if you want to take course ai.

For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1.
Return true if you can finish all courses. Otherwise, return false.
"""

class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        
        if not prerequisites:
            return True
        
        from collections import defaultdict
        ref = defaultdict(list)
        for [p,q] in prerequisites:
            ref[p].append(q)

        def helper(cur, trace):
            for item in ref[cur]:
                if item in trace:
                    return False
            trace.add(cur)
            if ref[cur]:
                for item in ref[cur]:
                    return helper(item, trace)
            else:
                return True
                    
        ans = helper(prerequisites[0][0], set())
        for [k,v] in prerequisites[1:]:
            ans = ans and helper(k, set())
        
        return ans

"""
Runtime: 1132 ms, faster than 5.04% of Python online submissions for Course Schedule.
Memory Usage: 16.9 MB, less than 10.13% of Python online submissions for Course Schedule.
"""