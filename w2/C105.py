"""
105. Construct Binary Tree from Preorder and Inorder Traversal

Given two integer arrays preorder and inorder where preorder is the preorder traversal of a binary tree and inorder is the inorder traversal of the same tree, 
construct and return the binary tree.
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        if inorder:
            tmp = preorder.pop(0) # Root Node
            idx = inorder.index(tmp)
            root = TreeNode(inorder[idx])
            root.left = self.buildTree(preorder, inorder[:idx])
            root.right = self.buildTree(preorder, inorder[idx+1:])
            return root

"""
Runtime: 128 ms, faster than 54.04% of Python online submissions for Construct Binary Tree from Preorder and Inorder Traversal.
Memory Usage: 52.5 MB, less than 42.60% of Python online submissions for Construct Binary Tree from Preorder and Inorder Traversal.
"""