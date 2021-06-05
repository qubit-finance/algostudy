"""
102. Binary Tree Level Order Traversal

Given the root of a binary tree, return the level order traversal of its nodes' values. (i.e., from left to right, level by level).
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        res, cur = [], [root] # res: answer / cur: current level nodes

        while len(cur)>0:
            tmp = [] # node vals of current level
            cur2 = []  # duplicate of cur so that we could add left and right siblings on the fly
            for node in cur:
                if node: # if not None
                    tmp.append(node.val)
                    cur2 += [node.left, node.right] # the next level
            cur = cur2 # update cur with next level
            if len(tmp) > 0: # avoid empty array being appended
                res.append(tmp)

        return res

"""
Runtime: 12 ms, faster than 99.63% of Python online submissions for Binary Tree Level Order Traversal.
Memory Usage: 13.9 MB, less than 42.64% of Python online submissions for Binary Tree Level Order Traversal.
"""