"""
139. Word Break

Given a string s and a dictionary of strings wordDict, return true if s can be segmented into a space-separated sequence of one or more dictionary words.

Note that the same word in the dictionary may be reused multiple times in the segmentation.
"""

class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        res = [False]*len(s)

        for i in range(len(s)):
            for word in wordDict:
                if i < len(word)-1:
                    continue
                if s[i-len(word)+1:i+1]==word:
                    if res[i-len(word)] or i-len(word)==-1:
                        res[i] = True
        
        return res[-1]

"""
Runtime: 24 ms, faster than 84.48% of Python online submissions for Word Break.
Memory Usage: 13.7 MB, less than 27.74% of Python online submissions for Word Break.
"""