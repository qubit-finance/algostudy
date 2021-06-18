"""
114. Flatten Binary Tree to Linked List

Given the root of a binary tree, flatten the tree into a "linked list":

The "linked list" should use the same TreeNode class where the right child pointer points to the next node in the list and the left child pointer is always null.
The "linked list" should be in the same order as a pre-order traversal of the binary tree.
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: None Do not return anything, modify root in-place instead.
        """
        
        nodes = []
        
        def preorder(node):
            if node:
                nodes.append(node)
                try:
                    preorder(node.left)
                    preorder(node.right)
                except:
                    pass
        preorder(root)
        nodes = nodes[1:][::-1]
        cur = root
        while nodes:
            node = nodes.pop()
            cur.left = None
            cur.right = node
            cur = cur.right
        
"""
Runtime: 16 ms, faster than 98.87% of Python online submissions for Flatten Binary Tree to Linked List.
Memory Usage: 14.5 MB, less than 25.89% of Python online submissions for Flatten Binary Tree to Linked List.
"""