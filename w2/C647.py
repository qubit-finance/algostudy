"""
647. Palindromic Substrings

Given a string s, return the number of palindromic substrings in it.

A string is a palindrome when it reads the same backward as forward.

A substring is a contiguous sequence of characters within the string.
"""
class Solution(object):
    def countSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        from collections import defaultdict
        ans = 0
        def check(st):
            for i in range(len(st)//2):
                if st[i]!=st[len(st)-i-1]:
                    return False
            return True
        idx = defaultdict(list)
        for i, v in enumerate(s):
            if idx[v]:
                for ind in idx[v]:
                    if check(s[ind:i+1]):
                        ans += 1
            idx[v].append(i)
        return ans+len(s)

"""
Time Limit Exceeded
"""


class Solution(object):
    def countSubstrings(self, s):
        ans, n = 0, len(s)

        for i in range(n):
            l, r = i-1, i+1
            while (l>=0 and r<n):
                if s[l]==s[r]:
                    ans += 1
                    l, r = l-1, r+1
                else:
                    break
            
            if s[i]==s[i+1]:
                ans += 1
                l, r = i-1, i+2
                while (l>=0 and r<n):
                    if s[l]==s[r]:
                        ans += 1
                        l, r = l-1, r+1
                    else:
                        break
        return ans + n # Each character is a palindrome

"""
Runtime: 88 ms, faster than 97.88% of Python online submissions for Palindromic Substrings.
Memory Usage: 13.6 MB, less than 63.76% of Python online submissions for Palindromic Substrings.
"""