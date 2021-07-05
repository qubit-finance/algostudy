"""
437. Path Sum III

Given the root of a binary tree and an integer targetSum, return the number of paths where the sum of the values along the path equals targetSum.

The path does not need to start or end at the root or a leaf, but it must go downwards (i.e., traveling only from parent nodes to child nodes).
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def pathSum(self, root, targetSum):
        """
        :type root: TreeNode
        :type targetSum: int
        :rtype: int
        """
        if not root:
            return 0
        
        self.cnt = 0
        
        def helper(node, arr):
            
            if node:
                if node.val == targetSum:
                    self.cnt += 1
                tmp = [node.val]
                for value in arr:
                    tmp.append(value+node.val)
                    if value+node.val == targetSum:
                        self.cnt += 1
                helper(node.left, tmp)
                helper(node.right, tmp)
            return
        
        helper(root, [])
        
        return self.cnt

"""
Runtime: 452 ms, faster than 38.54% of Python online submissions for Path Sum III.
Memory Usage: 32.5 MB, less than 5.29% of Python online submissions for Path Sum III.
"""