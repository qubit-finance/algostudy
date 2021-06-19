"""
199. Binary Tree Right Side View
Given the root of a binary tree, imagine yourself standing on the right side of it,
return the values of the nodes you can see ordered from top to bottom.

The number of nodes in the tree is in the range [0, 100].
-100 <= Node.val <= 100
"""


# Definition for a binary tree node.
from typing import List
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        # numbering을 해서
        # root 가 1, left는 p*2, right는 p*2+1
        # 이렇게하면 해당 층은, 그냥 층도 들고 다니쟈
        # answer에 넣어놓고, 더 오른쪽을 찾으면 교체하는 방식
        # 근데 최 우측이 있으면 가고 없으면 그제서야 돌아가는 것도 바쁘지는 않다.
        if root is None:
            return []
        answer = []
        candi_lst = []

        def rightTraverse(node:TreeNode, index, level):
            if len(answer) <= level:
                answer.append(node.val)
                candi_lst.append(index-1)
            else:
                if candi_lst[level] < index-1:
                    answer[level] = node.val
                    candi_lst[level] = index-1

            if node.right is not None:
                rightTraverse(node.right, 2*index+1, level+1)
            if node.left is not None:
                rightTraverse(node.left, 2*index, level+1)

        rightTraverse(root, 1, 0)
        return answer


if __name__ == "__main__":
    s = Solution()
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.right = TreeNode(5)
    root.right.right = TreeNode(4)
    print(s.rightSideView(root), "[1,3,4]")
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.right = TreeNode(5)

    print(s.rightSideView(root), "[1,3,5]")
    root = TreeNode(1)
    root.right = TreeNode(3)
    print(s.rightSideView(root), "[1,3]")
    root = None
    print(s.rightSideView(root), "[]")


"""
Runtime: 24 ms, faster than 97.99% of Python3 online submissions for Binary Tree Right Side View.
Memory Usage: 14.3 MB, less than 18.67% of Python3 online submissions for Binary Tree Right Side View.
"""