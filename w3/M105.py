# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:

        def construct_tree(node, preindex, start, end):
            if start >= end:
                return
            node_index = inorder.index(node.val, start,end)
            leftN = node_index - start
            rightN = end - node_index - 1
            # left : start ~ indexk right indexk+1 ~ end
            if leftN > 0:
                node.left = TreeNode(preorder[preindex+1])
                construct_tree(node.left, preindex+1, start, node_index)
            if rightN > 0:
                node.right = TreeNode(preorder[preindex+leftN+1])
                construct_tree(node.right, preindex+leftN+1, node_index+1, end)

        root = TreeNode(preorder[0])
        n = len(preorder)
        construct_tree(root, 0, 0, n)

        return root
      
      
"""
Runtime: 72 ms, faster than 71.10% of Python3 online submissions for Construct Binary Tree from Preorder and Inorder Traversal.
Memory Usage: 19 MB, less than 76.28% of Python3 online submissions for Construct Binary Tree from Preorder and Inorder Traversal.
"""
