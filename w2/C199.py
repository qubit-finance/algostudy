"""
199. Binary Tree Right Side View

Given the root of a binary tree, imagine yourself standing on the right side of it, return the values of the nodes you can see ordered from top to bottom.
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        
        cur, res = [], []

        if root:
            cur.append(root)

        while cur:
            cur2, tmp = [], []
            for node in cur:
                try:
                    tmp.append(node.val)
                    cur2.append(node.left)
                    cur2.append(node.right)
                except:
                    pass
            cur = cur2
            if len(tmp)>0:
                res.append(tmp[-1])

        return res

"""
Runtime: 20 ms, faster than 68.68% of Python online submissions for Binary Tree Right Side View.
Memory Usage: 13.5 MB, less than 49.88% of Python online submissions for Binary Tree Right Side View.
"""