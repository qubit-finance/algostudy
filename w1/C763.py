"""
763. Partition Labels

A string s of lowercase English letters is given. We want to partition this string into as many parts as possible so that each letter appears in at most one part, and return a list of integers representing the size of these parts.
"""

class Solution(object):
    def partitionLabels(self, s):
        """
        :type s: str
        :rtype: List[int]
        """
        from collections import defaultdict, Counter
        d = defaultdict(list)

        for i, letter in enumerate(s):
            d[letter].append(i)
            
        keys = sorted(d, key = lambda x: d[x][0])
        letters = [key for key in keys if len(d[key])>1]

        dum = list(range(len(s)))
        
        for key in letters:
            dum[d[key][0]:d[key][-1]+1] = [dum[d[key][0]]] * (d[key][-1]-d[key][0]+1)
        
        counts = Counter(dum)

        return [counts[v] for v in sorted(counts)]

"""
Runtime: 40 ms, faster than 16.51% of Python online submissions for Partition Labels.
Memory Usage: 13.5 MB, less than 31.43% of Python online submissions for Partition Labels.
"""