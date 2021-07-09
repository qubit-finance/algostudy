"""
236. Lowest Common Ancestor of a Binary Tree

Given a binary tree, find the lowest common ancestor (LCA) of two given nodes in the tree.

According to the definition of LCA on Wikipedia:
“The lowest common ancestor is defined between two nodes p and q as the lowest node in T
that has both p and q as descendants (where we allow a node to be a descendant of itself).”

The number of nodes in the tree is in the range [2, 105].
-109 <= Node.val <= 109
All Node.val are unique.
p != q
p and q will exist in the tree.
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        depth = dict()
        parent = dict()
        depth[root.val] = 0
        def calc(node: TreeNode):
            if node.left is not None:
                parent[node.left] = node
                depth[node.left.val] = depth[node.val] + 1
                calc(node.left)

            if node.right is not None:
                parent[node.right] = node
                depth[node.right.val] = depth[node.val] + 1
                calc(node.right)


        calc(root)
        pd = depth[p.val]
        qd = depth[q.val]
        while pd != qd:
            if pd < qd:
                q = parent[q]
                qd = depth[q.val]
            else:
                p = parent[p]
                pd = depth[p.val]

        while p != q:
            p = parent[p]
            q = parent[q]

        return p

"""
Runtime: 92 ms, faster than 18.16% of Python3 online submissions for Lowest Common Ancestor of a Binary Tree.
Memory Usage: 30.7 MB, less than 5.80% of Python3 online submissions for Lowest Common Ancestor of a Binary Tree.
"""


