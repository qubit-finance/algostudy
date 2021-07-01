"""
236. Lowest Common Ancestor of a Binary Tree

Given a binary tree, find the lowest common ancestor (LCA) of two given nodes in the tree.

According to the definition of LCA on Wikipedia: “The lowest common ancestor is defined between two nodes p and q as the lowest node in T that has both p and q as descendants (where we allow a node to be a descendant of itself).”
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        def path(root, target):
            if not root:
                return []
            if root.val == target.val:
                return [root]
            res = path(root.left, target)
            if res:
                return [root] + res
            res = path(root.right, target)
            if res:
                return [root] + res
            return []
        
        a = path(root, p)
        b = path(root, q)
        from collections import defaultdict
        ref = defaultdict(int)
        for item in b:
            ref[item.val] += 1
        while len(a)>0:
            tmp = a.pop()
            if ref[tmp.val] == 1:
                return tmp


"""
Runtime: 1200 ms, faster than 5.02% of Python online submissions for Lowest Common Ancestor of a Binary Tree.
Memory Usage: 28 MB, less than 14.28% of Python online submissions for Lowest Common Ancestor of a Binary Tree.
"""

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        if p==q:
            return p
        
        self.LCA, self.depth = None, -1
        
        def dfs(node, depth):
            res = 0
            
            if node and depth > self.depth:
                res = node in (p,q)
                res += dfs(node.left, depth+1)
                res += dfs(node.right, depth+1)
                
                if res == 2 and depth > self.depth:
                    self.LCA = node
                    self.depth = depth
                    
            return res
        
        dfs(root, 0)
        
        return self.LCA

"""
Runtime: 72 ms, faster than 44.74% of Python online submissions for Lowest Common Ancestor of a Binary Tree.
Memory Usage: 28 MB, less than 15.65% of Python online submissions for Lowest Common Ancestor of a Binary Tree.
"""