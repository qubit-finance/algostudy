"""
11. Container With Most Water

Given n non-negative integers a1, a2, ..., an , where each represents a point at coordinate (i, ai). n vertical lines are drawn such that the two endpoints of the line i is at (i, ai) and (i, 0). Find two lines, which, together with the x-axis forms a container, such that the container contains the most water.

Notice that you may not slant the container.
"""
class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
                
        l, r = 0, len(height)-1
        cur = 0
        while r>l:
            cur = max(cur, min(height[l], height[r])*(r-l))
            if height[l] <= height[r]:
                l += 1
            else:
                r -= 1
                
                
        return cur

"""
Runtime: 632 ms, faster than 62.18% of Python online submissions for Container With Most Water.
Memory Usage: 24.1 MB, less than 18.91% of Python online submissions for Container With Most Water.
"""