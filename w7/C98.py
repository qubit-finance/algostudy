"""
98. Validate Binary Search Tree

Given the root of a binary tree, determine if it is a valid binary search tree (BST).

A valid BST is defined as follows:

The left subtree of a node contains only nodes with keys less than the node's key.
The right subtree of a node contains only nodes with keys greater than the node's key.
Both the left and right subtrees must also be binary search trees.
"""
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isValidBST(self, root, lowerBound=float("-inf"), upperBound=float("inf")):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True
        if root.val <= lowerBound or root.val >= upperBound:
            return False
        return self.isValidBST(root.left, lowerBound, min(upperBound, root.val)) and self.isValidBST(root.right, max(lowerBound, root.val), upperBound)

"""
Runtime: 32 ms, faster than 84.08% of Python online submissions for Validate Binary Search Tree.
Memory Usage: 18 MB, less than 44.51% of Python online submissions for Validate Binary Search Tree.
"""