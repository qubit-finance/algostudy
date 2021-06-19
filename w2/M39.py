"""
39. Combination Sum

Given an array of distinct integers candidates and a target integer target,
return a list of all unique combinations of candidates where the chosen numbers sum to target.
You may return the combinations in any order.

The same number may be chosen from candidates an unlimited number of times.
Two combinations are unique if the frequency of at least one of the chosen numbers is different.

It is guaranteed that the number of unique combinations
that sum up to target is less than 150 combinations for the given input.


1 <= candidates.length <= 30
1 <= candidates[i] <= 200
All elements of candidates are distinct.
1 <= target <= 500
"""

from typing import List
class Solution:
    # def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
    #     from bisect import bisect
    #     # O(n) 짜린가...?
    #     candidates.sort()
    #     answer = []
    #     # 같으면 뒤로감. log n
    #     pos = bisect(candidates, target)
    #     real_candi = candidates[:pos]
    #
    #     if not real_candi:
    #         return []
    #
    #     # if i 를 넣어도 target보다 작으면 append,
    #     # 이 경우 i+1도 시도한다.
    #     # 같아지면 answer에 append
    #     # 더 크면 stop
    #
    #     # 같으면 answer에 넣고 다음꺼 찾음.
    #     candi = real_candi[0]
    #     summation = candi
    #     temp = [candi]
    #     start_index = 0  #  맨 처음꺼 index
    #     index = 0  # 조사중인 거 index
    #
    #     while start_index < len(real_candi):
    #         # 함 더 넣음
    #         if summation < target:
    #             summation += candi
    #             temp.append(candi)
    #
    #         # 같거나 넘어간 경유
    #         else:
    #             # 같은 경우
    #             if summation == target:
    #                 answer.append(temp.copy())
    #             if start_index == len(real_candi)-1:
    #                 break
    #             # 넘어간 경우, 같은 경우 공통
    #             temp.pop()
    #             if len(temp) != 0:
    #                 temp.pop()
    #             if not temp or index == len(real_candi)-1:
    #                 start_index += 1
    #                 index = start_index
    #                 candi = real_candi[index]
    #                 temp = [candi]
    #             else:
    #                 if summation != target and temp[-1] < candi:
    #                     temp.pop()
    #                     temp.append(candi)
    #
    #                 else:
    #                     index += 1
    #                     candi = real_candi[index]
    #                     temp.append(candi)
    #
    #             summation = sum(temp)
    #
    #
    #
    #
    #     return answer
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        from bisect import bisect
        candidates.sort()
        answer = []
        # 같으면 뒤로감. log n
        pos = bisect(candidates, target)
        real_candi = candidates[:pos]
        def dfs(path, remained, index):
            if remained == 0:
                answer.append(path.copy())
                return

            # 앞에꺼 먼저 평가 index 초과 위험 x
            if index < len(real_candi) and real_candi[index]<= remained:
                dfs(path + [real_candi[index]], remained - real_candi[index], index)
                dfs(path, remained, index+1)

        dfs([], target, 0)
        return answer

if __name__ == "__main__":
    s = Solution()
    candidates = [2,3,6,7]
    target = 7
    print(s.combinationSum(candidates, target), "[[2,2,3],[7]]")
    candidates = [2,3,5]
    target = 8
    print(s.combinationSum(candidates, target), "[[2,2,2,2],[2,3,3],[3,5]]")
    candidates = [2]
    target = 1
    print(s.combinationSum(candidates, target), "[]")
    candidates = [1]
    target = 1
    print(s.combinationSum(candidates, target), "[[1]]")
    candidates = [1]
    target = 2
    print(s.combinationSum(candidates, target), "[[1,1]]")


"""

Runtime: 52 ms, faster than 91.70% of Python3 online submissions for Combination Sum.
Memory Usage: 14.3 MB, less than 75.25% of Python3 online submissions for Combination Sum.

"""