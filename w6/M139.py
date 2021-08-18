"""
139. Word Break

Given a string s and a dictionary of strings wordDict,
return true if s can be segmented into a space-separated sequence of one or more dictionary words.

Note that the same word in the dictionary may be reused multiple times in the segmentation.

1 <= s.length <= 300
1 <= wordDict.length <= 1000
1 <= wordDict[i].length <= 20
s and wordDict[i] consist of only lowercase English letters.
All the strings of wordDict are unique.


"""

from typing import List


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        wordset = set(wordDict)
        N = len(s)
        dp = [-1]*N
        def dfs(i):
            if i == N:
                return False

            if dp[i] != -1:
                return dp[i]

            _s = s[i:]
            if _s in wordset:
                return True

            temp = ""
            ans = False
            while True:
                if ans:
                    dp[i] = True
                    return True
                if temp in wordset:
                    ans = ans or dfs(i+len(temp))
                elif temp == _s:
                    break
                temp = _s[:len(temp)+1]
            dp[i] = ans
            return ans

        return dfs(0)


if __name__ == "__main__":
    sol = Solution()
    s = "leetcode"
    wordDict = ["leet","code"]
    print(sol.wordBreak(s, wordDict), True)
    s = "applepenapple"
    wordDict = ["apple","pen"]
    print(sol.wordBreak(s, wordDict), True)
    s = "catsandog"
    wordDict = ["cats","dog","sand","and","cat"]
    print(sol.wordBreak(s, wordDict), False)



"""
Runtime: 44 ms, faster than 36.17% of Python3 online submissions for Word Break.
Memory Usage: 14.7 MB, less than 14.46% of Python3 online submissions for Word Break.
"""


