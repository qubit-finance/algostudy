"""
19. Remove Nth Node From End of List

Given the head of a linked list,
remove the nth node from the end of the list and return its head.

The number of nodes in the list is sz.
1 <= sz <= 30
0 <= Node.val <= 100
1 <= n <= sz

"""

from typing import Optional, List

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        cnt = 1
        curr = head
        lst = [curr]
        while curr.next is not None:
            cnt += 1
            curr = curr.next
            lst.append(curr)

        lst.append(None)
        index = cnt - n
        if index == 0:
            return head.next
        lst[index-1].next = lst[index+1]

        return head

"""
Runtime: 28 ms, faster than 92.19% of Python3 online submissions for Remove Nth Node From End of List.
Memory Usage: 14 MB, less than 98.80% of Python3 online submissions for Remove Nth Node From End of List.
"""


