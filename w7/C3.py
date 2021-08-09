"""
3. Longest Substring Without Repeating Characters

Given a string s, find the length of the longest substring without repeating characters.
"""
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        curMax = 0
        bag = dict()
        offset = 0
        for i, letter in enumerate(s):
            if bag.get(letter, -1) < offset:
                curMax = max(curMax, i-offset+1)
            else:
                offset = bag[letter]+1
            bag[letter] = i
        return curMax

"""
Runtime: 40 ms, faster than 88.98% of Python online submissions for Longest Substring Without Repeating Characters.
Memory Usage: 13.8 MB, less than 48.10% of Python online submissions for Longest Substring Without Repeating Characters.
"""