"""
739. Daily Temperatures

Given a list of daily temperatures temperatures, return a list such that, for each day in the input, tells you how many days you would have to wait until a warmer temperature. If there is no future day for which this is possible, put 0 instead.

For example, given the list of temperatures temperatures = [73, 74, 75, 71, 69, 72, 76, 73], your output should be [1, 1, 4, 2, 1, 1, 0, 0].

Note: The length of temperatures will be in the range [1, 30000]. Each temperature will be an integer in the range [30, 100].
"""
from typing import List


class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:

        # is O(n) possible?

        answer = [0]*len(temperatures)
        stack = [] # [[]]*71 똑같은 list가 복제됨... !

        # 더 큰놈이 앞에 있으면 그거만 확인하면 뒤에는 끝이남.
        # 그래서 더 큰놈을 찾으면 뒤에거는 pop해도 된다.
        for ri, temp in enumerate(reversed(temperatures)): #O(n)
            index = len(temperatures) - ri - 1
            while stack and temperatures[stack[-1]] <= temp:
                stack.pop()

            if len(stack) != 0:
                answer[index] = stack[-1] - index

            stack.append(index)




        return answer

if __name__ == "__main__":
    s = Solution()
    temperatures = [73, 74, 75, 71, 69, 72, 76, 73]
    ans = [1, 1, 4, 2, 1, 1, 0, 0]

    print(s.dailyTemperatures(temperatures), ans)


"""
Runtime: 556 ms, faster than 20.96% of Python3 online submissions for Daily Temperatures.
Memory Usage: 18.9 MB, less than 32.24% of Python3 online submissions for Daily Temperatures.
"""