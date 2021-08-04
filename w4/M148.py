"""
148. Sort List
Given the head of a linked list, return the list after sorting it in ascending order.

Follow up: Can you sort the linked list in O(n logn) time and O(1) memory (i.e. constant space)?

The number of nodes in the list is in the range [0, 5 * 10^4].
-10^5 <= Node.val <= 10^5
"""

from typing import List


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        if head is None:
            return None

        def mergeSort(start: ListNode, end: ListNode, size: int):

            if size == 0:
                return None
            elif size == 1:
                start.next = None
                return start
            # find mid
            mid = start
            for _ in range(size//2):
                mid = mid.next

            candi1 = mergeSort(start, mid, size//2)
            candi2 = mergeSort(mid, end, size - size//2)
            if candi1 is not None and candi2 is not None:
                if candi1.val <= candi2.val:
                    start = candi1
                    candi1 = candi1.next
                else:
                    start = candi2
                    candi2 = candi2.next

            elif candi2 is None:
                return candi1

            else:
                return candi2

            curr = start
            while candi1 is not None and candi2 is not None:
                if candi1.val <= candi2.val:
                    curr.next = candi1
                    curr = curr.next
                    candi1 = candi1.next

                else:
                    curr.next = candi2
                    curr = curr.next
                    candi2 = candi2.next

            if candi1 is None:
                curr.next = candi2
            else:
                curr.next = candi1
            return start

        last = head
        _size = 1
        while last.next is not None:
            last = last.next
            _size += 1
        return mergeSort(head, last, _size)


if __name__ == "__main__":
    s = Solution()
    head = ListNode(4)
    head.next = ListNode(2)
    head.next.next = ListNode(1)
    head.next.next.next = ListNode(3)
    head = s.sortList(head)
    while head is not None:
        print(head.val)
        head = head.next

"""
Runtime: 404 ms, faster than 72.59% of Python3 online submissions for Sort List.
Memory Usage: 30 MB, less than 91.34% of Python3 online submissions for Sort List.
"""