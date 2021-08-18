"""
438. Find All Anagrams in a String
Given two strings s and p, return an array of all the start indices of p's anagrams in s.
You may return the answer in any order.

1 <= s.length, p.length <= 3 * 10^4
s and p consist of lowercase English letters.
"""

from typing import List


class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        # make dict and set
        Ns = len(s)
        Np = len(p)
        alph_arr = [[0 for _ in range(26)] for _ in range(Ns+1)]
        ans = []

        p_arr = [0 for _ in range(26)]
        for st in p:
            p_arr[ord(st) - ord('a')] += 1

        # 전부 파악
        # alph_arr[ord(s[0])][0] += 1
        for i in range(1, Ns+1):
            for j in range(26):
                alph_arr[i][j] = alph_arr[i-1][j]

            a = s[i-1]
            alph_arr[i][ord(a)- ord('a')] += 1

        for i in range(Np, Ns+1):
            for j in range(26):
                if alph_arr[i][j] - alph_arr[i-Np][j] != p_arr[j]:
                    break
            else:
                ans.append(i-Np)
        return ans
# class Solution:
#     def findAnagrams(self, s: str, p: str) -> List[int]:
#         # make dict and set
#         p_set = set()
#         p_counter = dict()
#         for st in p:
#             p_counter[st] = p_counter.get(st, 0) + 1
#             p_set.add(st)
#         ans = []
#         start = 0
#         while start + len(p) <= len(s):
#             temp_counter = dict()
#             last_char_dict = dict()
#             left_set = p_set.copy()
#             for i in range(len(p)):
#                 t = s[start+i]
#
#                 if t not in p_set:
#                     start += 1 + i
#                     break
#
#                 if temp_counter.get(t, 0) == p_counter[t]:
#                     start = last_char_dict[t] + 1
#                     break
#
#                 temp_counter[t] = temp_counter.get(t, 0) + 1
#                 last_char_dict[t] = start + i
#
#                 if temp_counter[t] == p_counter[t]:
#                     if left_set == {t}:
#                         ans.append(start)
#                         start += 1
#                         break
#                     left_set.remove(t)
#
#         return ans


if __name__ == "__main__":
    sol = Solution()
    s = "cbaebabacd"
    p = "abc"
    print(sol.findAnagrams(s, p),  [0,6])
    s = "abab"
    p = "ab"
    print(sol.findAnagrams(s, p),  [0,1,2])

"""
Runtime: 824 ms, faster than 17.54% of Python3 online submissions for Find All Anagrams in a String.
Memory Usage: 21.8 MB, less than 11.14% of Python3 online submissions for Find All Anagrams in a String.
"""