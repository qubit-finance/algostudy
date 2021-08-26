"""
142. Linked List Cycle II

Given a linked list, return the node where the cycle begins.
 If there is no cycle, return null.

There is a cycle in a linked list if there is some node in the list that can be reached again
by continuously following the next pointer.
Internally, pos is used to denote the index of the node that tail's next pointer is connected to.
Note that pos is not passed as a parameter.

Notice that you should not modify the linked list.
Follow up: Can you solve it using O(1) (i.e. constant) memory?

The number of the nodes in the list is in the range [0, 10^4].
-10^5 <= Node.val <= 10^5
pos is -1 or a valid index in the linked-list.

"""

from typing import List


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        # 1개, None 처리
        if head is None:
            return None

        if head.next is None or head.next == head:
            return head.next


        one = head
        two = head
        while True:
            if one is None or two.next is None:
                return None
            one = one.next
            two = two.next.next
            if two is None:
                return None

            if one == two:
                break

        one = head
        while one != two:
            one = one.next
            two = two.next


        return one




if __name__ == "__main__":
    sol = Solution()




"""
Runtime: 48 ms, faster than 80.10% of Python3 online submissions for Linked List Cycle II.
Memory Usage: 17.2 MB, less than 82.37% of Python3 online submissions for Linked List Cycle II.
"""


