"""
49. Group Anagrams

Given an array of strings strs, group the anagrams together. You can return the answer in any order.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.
"""

class Solution(object):
    def groupAnagrams(self, strs):

        from collections import Counter
        ans, aux = [], []
        
        for word in strs:
            # For/Else syntax
            for i, v in enumerate(aux):
                if Counter(word) == v:
                    ans[i].append(word)
                    break
            else:
                ans.append([word])
                aux.append(Counter(word))
        return ans

"""
Time Limit Exceeded
"""

class Solution(object):
    def groupAnagrams(self, strs):

        dic = dict()

        for word in strs:
            key = "".join(sorted(word))
            dic[key] = dic.get(key, []) + [word]
        
        return dic.values()

"""
Runtime: 84 ms, faster than 73.50% of Python online submissions for Group Anagrams.
Memory Usage: 17.5 MB, less than 76.66% of Python online submissions for Group Anagrams.
"""