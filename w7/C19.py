"""
19. Remove Nth Node From End of List

Given the head of a linked list, remove the nth node from the end of the list and return its head.
"""
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        N = 1
        cur = head
        while cur.next:
            cur = cur.next
            N += 1
        if n == N:
            head = head.next
        else:
            cur = head
            for _ in range(N-n-1):
                cur = cur.next  
            cur.next = cur.next.next
        return head

"""
Runtime: 24 ms, faster than 41.52% of Python online submissions for Remove Nth Node From End of List.
Memory Usage: 13.3 MB, less than 71.31% of Python online submissions for Remove Nth Node From End of List.
"""