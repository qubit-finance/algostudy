"""
621. Task Scheduler

Given a characters array tasks, representing the tasks a CPU needs to do,
where each letter represents a different task.
Tasks could be done in any order. Each task is done in one unit of time.
For each unit of time, the CPU could complete either one task or just be idle.

However, there is a non-negative integer n that represents the cooldown period between two same tasks
(the same letter in the array), that is that there must be at least n units of time between any two same tasks.

Return the least number of units of times that the CPU will take to finish all the given tasks.

1 <= task.length <= 104
tasks[i] is upper-case English letter.
The integer n is in the range [0, 100].
"""

from typing import List

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        from collections import Counter
        # 일단 사실 문자에는 연관이 없다.
        # counter가 나오고,
        # 제일 많은 놈이 마지막에 남거나, 중간에 죽어서 끝나거나.
        # 하한은 len(tasks)
        #       N <= x <= n*(k-1) + p
        # 개수가 같은 종류들이 t1, ... tm 이라고 해보자.
        # n*k < N 이면 문제가 생긴다. 즉 종류가 n에 커버되지 못하는 경우임.
        # O(n)
        # O(n)
        c = Counter(tasks)
        vals = c.values()
        k = max(vals)
        N = len(tasks)
        p = 0
        for val in vals:
            if val == k:
                p += 1

        print(N, (n+1)*(k-1) + p, k, p)
        return max(N, (n+1)*(k-1) + p)



if __name__ == "__main__":
    s = Solution()
    tasks = ["A","A","A","B","B","B"]
    n = 2

    print(s.leastInterval(tasks, n), 8)
    tasks = ["A", "A", "A", "B", "B", "B"]
    n = 0
    print(s.leastInterval(tasks, n), 6)

    tasks = ["A","A","A","A","A","A","B","C","D","E","F","G"]
    n = 2
    print(s.leastInterval(tasks, n), 16)

    tasks = ["A", "A", "B", "B", "C", "C", "D", "D", "E", "E", "F", "F", "G", "G", "H", "H", "I", "I", "J", "J", "K", "K", "L",
     "L", "M", "M", "N", "N", "O", "O", "P", "P", "Q", "Q", "R", "R", "S", "S", "T", "T", "U", "U", "V", "V", "W", "W",
     "X", "X", "Y", "Y", "Z", "Z"]
    n = 2
    print(s.leastInterval(tasks, n), 52)

    tasks = ["A", "A", "A", "A", "A", "A", "B", "C", "D", "E", "F", "G"]
    n= 2
    print(s.leastInterval(tasks, n), 16)



"""
Runtime: 396 ms, faster than 74.35% of Python3 online submissions for Task Scheduler.
Memory Usage: 14.9 MB, less than 24.07% of Python3 online submissions for Task Scheduler.
"""