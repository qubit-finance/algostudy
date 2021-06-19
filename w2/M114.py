"""
114. Flatten Binary Tree to Linked List
Given the root of a binary tree, flatten the tree into a "linked list":

The "linked list" should use the same TreeNode class where the right child pointer points to the next node in the list and the left child pointer is always null.
The "linked list" should be in the same order as a pre-order traversal of the binary tree.
The number of nodes in the tree is in the range [0, 2000].
-100 <= Node.val <= 100
Can you flatten the tree in-place (with O(1) extra space)?
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    # O(1)의 메모리를 쓰고 싶다면, 크기가 100보다 작으니까, 1000단위로
    # 원래 자리의 인덱스를 저장해두면 된다. 물론 그 전에 200을 더하고 하면 편하다
    # 그리고 나서 리셋 시킨다음 리턴하면된다. 귀찮으니까 패스스    def flatten(self, root: TreeNode) -> None:
    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if root is None:
            return

        answer = []

        def preorder(node: TreeNode):
            answer.append(node)
            if node.left is not None:
                preorder(node.left)
            if node.right is not None:
                preorder(node.right)

        preorder(root)
        node = root
        for new_node in answer[1:]:
            node.left = None
            node.right = new_node
            node = node.right


def print_LL(root: TreeNode):
    if root is None:
        print([])
    node = root
    print("[", end="")
    while node.right is not None:
        print(node.val, ",", end="")
        node = node.right

    print(node.val, "]")


if __name__ == "__main__":
    root = TreeNode(1)
    root.right = TreeNode(5)
    root.left = TreeNode(2)
    root.right.right = TreeNode(6)
    root.left.left = TreeNode(3)
    root.left.right = TreeNode(4)
    s = Solution()
    s.flatten(root)
    print_LL(root)

"""
Runtime: 36 ms, faster than 76.73% of Python3 online submissions for Flatten Binary Tree to Linked List.
Memory Usage: 15.4 MB, less than 12.77% of Python3 online submissions for Flatten Binary Tree to Linked List.
"""