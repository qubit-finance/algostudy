"""
337. House Robber III

The thief has found himself a new place for his thievery again.
There is only one entrance to this area, called root.

Besides the root, each house has one and only one parent house.
After a tour, the smart thief realized that all houses in this place form a binary tree.
It will automatically contact the police if two directly-linked houses were broken into on the same night.

The number of nodes in the tree is in the range [1, 10^4].
0 <= Node.val <= 10^4
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def rob(self, root: TreeNode) -> int:
        val_dict = dict()
        val_dict[None] = [0,0]
        def calc(node: TreeNode):
            if node.left is None and node.right is None:
                val_dict[node] = [0, node.val]
                return

            if node.left not in val_dict:
                calc(node.left)

            if node.right not in val_dict:
                calc(node.right)

            l = val_dict[node.left]
            r = val_dict[node.right]
            val_dict[node] = [max(l) + max(r), node.val + l[0] + r[0]]

        calc(root)
        return max(val_dict[root])

if __name__ == "__main__":
    s = Solution()
    root = TreeNode(3)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.right = TreeNode(3)
    root.right.right = TreeNode(1)

    print(s.rob(root), 7)

    root = TreeNode(3)
    root.left = TreeNode(4)
    root.right = TreeNode(5)
    root.left.right = TreeNode(3)
    root.left.left = TreeNode(1)
    root.right.right = TreeNode(1)
    print(s.rob(root), 9)


"""
Runtime: 48 ms, faster than 77.56% of Python3 online submissions for House Robber III.
Memory Usage: 17.6 MB, less than 16.80% of Python3 online submissions for House Robber III.
"""