"""
138. Copy List with Random Pointer

A linked list of length n is given such that each node contains an additional random pointer,
which could point to any node in the list, or null.

Construct a deep copy of the list.
The deep copy should consist of exactly n brand new nodes,
where each new node has its value set to the value of its corresponding original node.
Both the next and random pointer of the new nodes should point to new nodes in the copied list
such that the pointers in the original list and copied list represent the same list state.
None of the pointers in the new list should point to nodes in the original list.

For example, if there are two nodes X and Y in the original list,
where X.random --> Y, then for the corresponding two nodes x and y in the copied list, x.random --> y.

Return the head of the copied linked list.

The linked list is represented in the input/output as a list of n nodes.
Each node is represented as a pair of [val, random_index] where:

val: an integer representing Node.val
random_index: the index of the node (range from 0 to n-1)
that the random pointer points to, or null if it does not point to any node.
Your code will only be given the head of the original linked list.

0 <= n <= 1000
-10000 <= Node.val <= 10000
Node.random is null or is pointing to some node in the linked list.


"""

from typing import List



# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random

class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        #O(N)
        if head is None:
            return None

        hash = dict()
        i = 0
        curr = head
        ans = Node(head.val)
        node_arr = [curr]
        new_arr = [ans]
        hash[id(curr)] = i
        while curr.next is not None:
            ans.next = Node(curr.next.val)
            ans = ans.next
            curr = curr.next
            node_arr.append(curr)
            new_arr.append(ans)
            i += 1
            hash[id(curr)] = i

        # make random data
        curr = head
        index2rand = []
        while curr is not None:
            if curr.random is None:
                index2rand.append(-1)
            else:
                index2rand.append(hash[id(curr.random)])
            curr = curr.next

        new_arr.append(None)
        for i, randi in enumerate(index2rand):
            new_arr[i].random = new_arr[randi]

        return new_arr[0]





if __name__ == "__main__":
    s = Solution()
    head = Node(7)
    head.next = Node(13)
    curr = head.next
    curr.random = head
    curr.next = Node(11)
    curr = curr.next
    two = curr
    curr.next = Node(10)
    curr = curr.next
    curr.next = Node(1)
    four = curr.next
    two.random = four
    two.next.random = two
    four.random = head
    new_head = s.copyRandomList(head)
    c = new_head
    while c is not None:
        print(c.val)
        c = c.next



"""
Runtime: 36 ms, faster than 64.78% of Python3 online submissions for Copy List with Random Pointer.
Memory Usage: 14.9 MB, less than 83.99% of Python3 online submissions for Copy List with Random Pointer.
"""


