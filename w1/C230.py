"""
230. Kth Smallest Element in a BST

Given the root of a binary search tree, and an integer k, return the kth (1-indexed) smallest element in the tree.
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def kthSmallest(self, root, k):
        self.vals = []
        def inorder(root):
            if root:
                inorder(root.left)
                self.vals.append(root.val)
                inorder(root.right)
        inorder(root)
        return self.vals[k-1]

"""
Runtime: 44 ms, faster than 65.29% of Python online submissions for Kth Smallest Element in a BST.
Memory Usage: 21.3 MB, less than 38.05% of Python online submissions for Kth Smallest Element in a BST.
"""