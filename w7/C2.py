"""
2. Add Two Numbers

You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.
"""
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        num1, num2 = "", ""
        cur=l1
        while cur:
            num1 = str(cur.val) + num1
            cur = cur.next
        
        cur=l2
        while cur:
            num2 = str(cur.val) + num2
            cur = cur.next
        
        num = str(int(num1)+int(num2))
        
        head = ListNode(val=int(num[-1]))
        cur = head
        num = num[:-1]
        if not num:
            return head
        for n in num[::-1]:
            cur.next = ListNode(val=int(n))
            cur = cur.next
        return head

"""
Runtime: 64 ms, faster than 49.70% of Python online submissions for Add Two Numbers.
Memory Usage: 13.4 MB, less than 91.88% of Python online submissions for Add Two Numbers.
"""