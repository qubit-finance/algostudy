"""
102. Binary Tree Level Order Traversal
Given the root of a binary tree, return the level order traversal of its nodes' values.
(i.e., from left to right, level by level).

The number of nodes in the tree is in the range [0, 2000].
-1000 <= Node.val <= 1000

"""

# Definition for a binary tree node.
from typing import List

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if root is None:
            return []

        answer = []
        def levelTraverse(node: TreeNode, level):
            if len(answer) <= level:
                answer.append([node.val])
            else:
                answer[level].append(node.val)

            if node.left is not None:
                levelTraverse(node.left, level+1)
            if node.right is not None:
                levelTraverse(node.right, level + 1)
        # level을 tracking 하면서 없으면 추가해서 넣는거로.

        levelTraverse(root, 0)
        return answer


if __name__ == "__main__":
    s = Solution()
    root = TreeNode(3)
    root.left = TreeNode(9)
    root.right = TreeNode(20)
    root.right.left = TreeNode(15)
    root.right.right = TreeNode(7)
    print(s.levelOrder(root), "[[3],[9,20],[15,7]]")
    root = TreeNode(1)
    print(s.levelOrder(root), "[[1]]")
    root = None
    print(s.levelOrder(root), "[]")

"""
Runtime: 36 ms, faster than 61.92% of Python3 online submissions for Binary Tree Level Order Traversal.
Memory Usage: 15.2 MB, less than 12.86% of Python3 online submissions for Binary Tree Level Order Traversal.
"""