"""
142. Linked List Cycle II

Given a linked list, return the node where the cycle begins. If there is no cycle, return null.

There is a cycle in a linked list if there is some node in the list that can be reached again by continuously following the next pointer. Internally, pos is used to denote the index of the node that tail's next pointer is connected to. Note that pos is not passed as a parameter.

Notice that you should not modify the linked list.
"""
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        seen = dict()
        cur = head
        
        while cur:
            if seen.get(cur, False):
                return cur
            seen[cur] = True
            cur = cur.next
            
        return

"""
Runtime: 44 ms, faster than 58.26% of Python online submissions for Linked List Cycle II.
Memory Usage: 20.7 MB, less than 5.45% of Python online submissions for Linked List Cycle II.
"""