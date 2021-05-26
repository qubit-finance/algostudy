"""
230. Kth Smallest Element in a BST
Given the root of a binary search tree, and an integer k, return the kth (1-indexed) smallest element in the tree.
"""

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        def inorder_traversal(node, traverse):
            if len(traverse) == k:
                return traverse
            if node.left is not None:
                inorder_traversal(node.left, traverse)

            if len(traverse) == k:
                return traverse

            traverse.append(node.val)
            if len(traverse) == k:
                return traverse

            if node.right is not None:
                inorder_traversal(node.right, traverse)

            return traverse

        return inorder_traversal(root, [])[-1]


if __name__ == "__main__":
    root = TreeNode(3)
    root.left = TreeNode(1)
    root.right = TreeNode(4)
    root.left.right = TreeNode(2)
    s = Solution()
    print(s.kthSmallest(root, 1), 1)
    root = TreeNode(5)
    root.left = TreeNode(3)
    root.right = TreeNode(6)
    root.left.left = TreeNode(2)
    root.left.right = TreeNode(4)
    root.left.left.left = TreeNode(1)
    print(s.kthSmallest(root, 3), 3)

