"""
438. Find All Anagrams in a String

Given two strings s and p, return an array of all the start indices of p's anagrams in s. You may return the answer in any order.
"""
class Solution(object):
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        from collections import defaultdict
        import copy

        m,n = len(s), len(p)
        res = []
        cnt = defaultdict(int)
        for letter in p:
            cnt[letter] += 1

        def is_anagram(str1):
            dup = copy.deepcopy(cnt)
            for letter in str1:
                if dup[letter]==0:
                    return False
                else:
                    dup[letter] -= 1
            return True

        for i in range(m-n+1):
            if is_anagram(s[i:i+n]):
                res.append(i)

        return res

"""
Time Limit Exceeded
"""

class Solution(object):
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        from collections import defaultdict

        m,n = len(s), len(p)
        res = []
        cnt = defaultdict(int)
        for letter in p:
            cnt[letter] += 1

        for i in range(m-n+1):
            if i == 0:
                for letter in s[i:i+n]:
                    cnt[letter] -= 1
                if all(v==0 for v in cnt.values()):
                    res.append(i)
            else:
                cnt[s[i-1]] += 1
                cnt[s[i+n-1]] -= 1
                if all(v==0 for v in cnt.values()):
                    res.append(i)
        
        return res

"""
Runtime: 180 ms, faster than 28.01% of Python online submissions for Find All Anagrams in a String.
Memory Usage: 14.9 MB, less than 8.26% of Python online submissions for Find All Anagrams in a String.
"""