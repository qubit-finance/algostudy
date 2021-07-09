"""
17. Letter Combinations of a Phone Number

Given a string containing digits from 2-9 inclusive,
return all possible letter combinations that the number could represent.
Return the answer in any order.

A mapping of digit to letters (just like on the telephone buttons) is given below.
Note that 1 does not map to any letters.n == nums.length

0 <= digits.length <= 4
digits[i] is a digit in the range ['2', '9'].

"""

from typing import List

class Solution:
    mapper = {"2" : ['a', 'b','c'],
              "3" : ['d', 'e', 'f'],
              "4" : ['g', 'h', 'i'],
              "5" : ['j', 'k', 'l'],
              "6" : ['m', 'n', 'o'],
              "7" : ['p', 'q', 'r', 's'],
              "8" : ['t', 'u', 'v'],
              "9" : ['w', 'x', 'y', 'z']}

    def letterCombinations(self, digits: str) -> List[str]:
        N = len(digits)
        if N == 0:
            return []

        if N == 1:
            return Solution.mapper[digits]

        answer = []
        if N == 2:
            a = Solution.mapper[digits[0]]
            b = Solution.mapper[digits[1]]
            for i in range(len(a)):
                for j in range(len(b)):
                    answer.append(a[i] + b[j])
        if N == 3:
            a = Solution.mapper[digits[0]]
            b = Solution.mapper[digits[1]]
            c = Solution.mapper[digits[2]]
            for i in range(len(a)):
                for j in range(len(b)):
                    for k in range(len(c)):
                        answer.append(a[i] + b[j] + c[k])
        if N == 4:
            a = Solution.mapper[digits[0]]
            b = Solution.mapper[digits[1]]
            c = Solution.mapper[digits[2]]
            d = Solution.mapper[digits[3]]
            for i in range(len(a)):
                for j in range(len(b)):
                    for k in range(len(c)):
                        for l in range(len(d)):
                            answer.append(a[i] + b[j] + c[k] + d[l])

        return answer



if __name__ == "__main__":
    s = Solution()
    digits = "23"
    print(s.letterCombinations(digits), ["ad","ae","af","bd","be","bf","cd","ce","cf"])

    digits = ""
    print(s.letterCombinations(digits), [])

    digits = "2"
    print(s.letterCombinations(digits), ["a","b","c"])

"""
Runtime: 24 ms, faster than 96.05% of Python3 online submissions for Letter Combinations of a Phone Number.
Memory Usage: 14.4 MB, less than 30.42% of Python3 online submissions for Letter Combinations of a Phone Number.
"""


