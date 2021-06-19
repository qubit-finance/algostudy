"""
49. Group Anagrams
Given an array of strings strs, group the anagrams together. You can return the answer in any order.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase,
typically using all the original letters exactly once.


1 <= strs.length <= 104
0 <= strs[i].length <= 100
strs[i] consists of lower-case English letters.
"""
from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        from collections import Counter
        from collections import defaultdict

        answer = []
        counter_dict = defaultdict(list)
        for s in strs:
            c = Counter(s)
            hasher = tuple(sorted(c.items()))
            counter_dict[hasher].append(s)

        for value in counter_dict.values():
            answer.append(value)

        return answer



# class Solution:
#     def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
#         from collections import Counter
#         del_lst = [0 for _ in range(len(strs))]
#         answer = []
#         temp = []
#         counter_list = list(map(Counter, strs))
#         for i in range(len(strs)):
#             if del_lst[i] == 1:
#                 continue
#
#             temp.append(strs[i])
#             for j in range(i+1, len(strs)):
#                 if del_lst[j] == 1:
#                     continue
#
#                 if counter_list[i] == counter_list[j]:
#                     temp.append(strs[j])
#                     del_lst[j] = 1
#
#             answer.append(temp.copy())
#             temp = []
#
#         return answer

if __name__ == "__main__":
    s = Solution()
    strs = ["eat","tea","tan","ate","nat","bat"]
    print(s.groupAnagrams(strs), [["bat"],["nat","tan"],["ate","eat","tea"]])

"""
Runtime: 128 ms, faster than 23.77% of Python3 online submissions for Group Anagrams.
Memory Usage: 21.7 MB, less than 8.29% of Python3 online submissions for Group Anagrams.
"""


"""
Runtime: 5728 ms, faster than 5.21% of Python3 online submissions for Group Anagrams.
Memory Usage: 19.7 MB, less than 17.13% of Python3 online submissions for Group Anagrams.
"""