"""
148. Sort List

Given the head of a linked list, return the list after sorting it in ascending order.

Follow up: Can you sort the linked list in O(n logn) time and O(1) memory (i.e. constant space)?
"""

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return None
        if not head.next:
            return head
                
        cur = head
        n = 1
        while cur.next:
            n += 1
            cur = cur.next
        
        for _ in range(n):
            cur = head
            if cur.val > cur.next.val:
                tmp, tmp2 = cur, cur.next.next
                head = head.next
                head.next = tmp
                head.next.next = tmp2
            while cur.next and cur.next.next:
                if cur.next.val > cur.next.next.val:
                    tmp1, tmp2 = cur.next, cur.next.next.next
                    cur.next = cur.next.next
                    cur.next.next = tmp1
                    cur.next.next.next = tmp2
                cur = cur.next
            
        return head

class Solution(object):
    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        cur = head
        # Store all values in `vals`
        vals = []
        while cur:
            vals.append(cur.val)
            cur = cur.next
        if not vals:
            return None
        # Quicksort vals
        sorvals = sorted(vals)
        # Construct Linked List from vals
        head = ListNode(val=sorvals[0])
        cur = head
        for item in sorvals[1:]:
            cur.next = ListNode(val=item)
            cur = cur.next

        return head

"""
Runtime: 288 ms, faster than 86.73% of Python online submissions for Sort List.
Memory Usage: 63.5 MB, less than 6.55% of Python online submissions for Sort List.
"""