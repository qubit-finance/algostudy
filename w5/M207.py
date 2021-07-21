"""
207. Course Schedule
There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1.
You are given an array prerequisites
where prerequisites[i] = [ai, bi] indicates that you must take course bi first if you want to take course ai.

For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1.
Return true if you can finish all courses. Otherwise, return false.

1 <= numCourses <= 10^5
0 <= prerequisites.length <= 5000
prerequisites[i].length == 2
0 <= ai, bi < numCourses
All the pairs prerequisites[i] are unique.
"""

from typing import List


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        from collections import deque
        from collections import defaultdict

        graph = defaultdict(list)
        nDegree = [0] * numCourses

        # p [1,0] : 1 들으려면 0을 들어야 한다.
        for lst in prerequisites:
            graph[lst[1]].append(lst[0])
            nDegree[lst[0]] += 1

        q = deque()

        # 간선 0 전부 push
        for i in range(numCourses):
            if nDegree[i] == 0:
                q.append(i)

        # 모든 node
        for i in range(numCourses):
            if len(q) == 0:
                return False

            x = q.popleft()

            for j in range(len(graph[x])):
                y = graph[x][j]
                nDegree[y] -= 1
                if nDegree[y] == 0:
                    q.append(y)

        return True


if __name__ == "__main__":
    s = Solution()
    numCourses = 2
    prerequisites = [[1,0]]
    print(s.canFinish(numCourses, prerequisites), True)
    numCourses = 2
    prerequisites = [[1,0],[0,1]]
    print(s.canFinish(numCourses, prerequisites), False)

"""
Runtime: 92 ms, faster than 91.34% of Python3 online submissions for Course Schedule.
Memory Usage: 15.4 MB, less than 84.47% of Python3 online submissions for Course Schedule.
"""