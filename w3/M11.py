"""
11. Container With Most Water

Given n non-negative integers a1, a2, ..., an , where each represents a point at coordinate (i, ai).
n vertical lines are drawn such that the two endpoints of the line i is at (i, ai) and (i, 0).
Find two lines, which, together with the x-axis forms a container, such that the container contains the most water.

Notice that you may not slant the container.

n == height.length
2 <= n <= 105
0 <= height[i] <= 104

"""
from typing import List

class Solution:
    def maxArea(self, height: List[int]) -> int:
        # 최악 : O(n^2)
        # 딱보니까 무조건 O(n)해야할 듯
        # (i-j)*min(height[i], height[j])
        answer = 0
        l = 0
        r = len(height)-1

        while l < r:
            answer = max(answer, min(height[l], height[r])*(r-l))

            if height[r] < height[l]:
                r -= 1
            else:
                l += 1

        return answer

if __name__ == "__main__":
    s = Solution()
    height = [1, 8, 6, 2, 5, 4, 8, 3, 7]
    print(s.maxArea(height), 49)
    height = [1, 1]
    print(s.maxArea(height), 1)
    height = [4, 3, 2, 1, 4]
    print(s.maxArea(height), 16)
    height = [1, 2, 1]
    print(s.maxArea(height), 2)
