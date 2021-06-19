"""
96. Unique Binary Search Trees
Given an integer n, return the number of structurally unique BST's
(binary search trees) which has exactly n nodes of unique values from 1 to n.
1 <= n <= 19
"""
class Solution:
    answer = [0 for _ in range(20)]
    def numTrees(self, n: int) -> int:
        Solution.answer = [0 for _ in range(20)]
        # dynamic으로 풀기.
        def dynamic(i):
            if Solution.answer[i] != 0:
                return Solution.answer[i]
            if i <= 1:
                Solution.answer[i] = 1
                return 1

            # 좌 우 분배
            total = 0
            for leftSize in range(i):
                rightSize = i-1-leftSize
                total += dynamic(leftSize)*dynamic(rightSize)

            Solution.answer[i] = total
            return total

        return dynamic(n)



if __name__ == "__main__":
    s = Solution()
    n = 3
    print(s.numTrees(n), 5)
    n = 1
    print(s.numTrees(n), 1)

"""
Runtime: 32 ms, faster than 56.46% of Python3 online submissions for Unique Binary Search Trees.
Memory Usage: 14 MB, less than 97.53% of Python3 online submissions for Unique Binary Search Trees.
"""