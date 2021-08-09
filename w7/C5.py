"""
5. Longest Palindromic Substring

Given a string s, return the longest palindromic substring in s.
"""
class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        if len(s)==0:
            return ""
        if len(s)==1:
            return s[0]
        curMax = s[0]
        for i in range(1, len(s)):
            if s[i-1]==s[i+1]:
                j=0
                while i-j-1>=0 and i+j+1<len(s) and s[i-j-1]==s[i+j+1]:
                    tmp = s[i-j-1:i+j+2]
                    j += 1
                if len(tmp)>len(curMax):
                    curMax = tmp
            if s[i-1]==s[i]:
                j=0
                while i-j-1>=0 and i+j<len(s) and s[i-j-1]==s[i+j]:
                    tmp = s[i-j-1:i+j+1]
                    j += 1
                if len(tmp)>len(curMax):
                    curMax = tmp
        return curMax

"""
Runtime: 1856 ms, faster than 33.18% of Python online submissions for Longest Palindromic Substring.
Memory Usage: 13.8 MB, less than 23.94% of Python online submissions for Longest Palindromic Substring.
"""