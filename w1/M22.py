# 22. Generate Parentheses
#Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.
from typing import List


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:

        def get_parenthese(lst, t_l, re_l, re_r, answer):
            if t_l <= 0:
                lst.extend([")" for _ in range(re_r)])
                answer.append(lst)

            elif re_l == 0:
                lst.append("(")
                get_parenthese(lst, t_l - 1, re_l + 1, re_r, answer)

            elif re_l > 0:
                lst2 = lst.copy()
                lst.append("(")
                lst2.append(")")
                get_parenthese(lst, t_l - 1, re_l + 1, re_r, answer)
                get_parenthese(lst2, t_l, re_l-1, re_r - 1, answer)

            return answer

        ret = []
        for l in get_parenthese([], n, 0, n,[]):
            ret.append("".join(l))

        return ret

if __name__ == "__main__":
    s = Solution()
    print(s.generateParenthesis(3))

"""
Runtime: 44 ms, faster than 15.26% of Python3 online submissions for Generate Parentheses.
Memory Usage: 14.6 MB, less than 65.22% of Python3 online submissions for Generate Parentheses.
"""