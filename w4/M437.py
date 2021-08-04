"""
437. Path Sum III

Given the root of a binary tree and an integer targetSum,
return the number of paths where the sum of the values along the path equals targetSum.

The path does not need to start or end at the root or a leaf, but it must go downwards
(i.e., traveling only from parent nodes to child nodes).

The number of nodes in the tree is in the range [0, 1000].
-10^9 <= Node.val <= 10^9
-1000 <= targetSum <= 1000

"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
from typing import List


class Solution:
    def pathSum(self, root: TreeNode, targetSum: int) -> int:
        if root is None:
            return 0

        self.cnt = 1
        def dfs(lst, node: TreeNode):
            temp = list(map(lambda x: x+ node.val, lst))
            temp += lst
            temp += [node.val]

            for i in range(len(temp)//2):
                if temp[i] == targetSum:
                    self.cnt += 1
            if node.left is not None:
                dfs(temp, node.left)
            if node.right is not None:
                dfs(temp, node.right)


        lst = []
        dfs(lst, root)

        return self.cnt

        # N^2 도 되긴 한다.

if __name__ == "__main__":
    s = Solution()
    root = TreeNode(1)
    root.right = TreeNode(5)
    root.left = TreeNode(2)
    root.right.right = TreeNode(6)
    root.left.left = TreeNode(3)
    root.left.right = TreeNode(4)
    print(s.pathSum(root, 6), 2)

"""
Runtime: 276 ms, faster than 79.51% of Python3 online submissions for Perfect Squares.
Memory Usage: 20.7 MB, less than 14.16% of Python3 online submissions for Perfect Squares.
"""


