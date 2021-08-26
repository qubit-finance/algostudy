"""
146. LRU Cache

Design a data structure that follows the constraints of a
Least Recently Used (LRU) cache.

Implement the LRUCache class:

LRUCache(int capacity)
Initialize the LRU cache with positive size capacity.

int get(int key)
Return the value of the key if the key exists, otherwise return -1.

void put(int key, int value)
Update the value of the key if the key exists. Otherwise, add the key-value pair to the cache.
If the number of keys exceeds the capacity from this operation, evict the least recently used key.
The functions get and put must each run in O(1) average time complexity.


1 <= capacity <= 3000
0 <= key <= 10^4
0 <= value <= 10^5
At most 2 * 10^5 calls will be made to get and put.

"""

from typing import List

class LinkNode:

    def __init__(self, val, key, next=None, prev=None):
        self.val = val
        self.next = next
        self.prev = prev
        self.key = key

    def __repr__(self):
        return str(self.key) + " : " + str(self.val)

class LRUCache:

    def __init__(self, capacity: int):
        self.head = LinkNode(-1, -1)
        self.tail = self.head
        self.k2n = dict()
        self.capa = capacity
        self.size = 0


    def get(self, key: int) -> int:
        node = self.k2n.get(key, -1)
        if node!= -1:
            val = node.val
            self.update(node)
            return val

        return -1

    def put(self, key: int, value: int) -> None:
        node = self.k2n.get(key, -1)
        if node == -1:
            node = LinkNode(value, key)
            if self.size < self.capa:
                self.size += 1

            else:
                # evict node
                self.evict()

            # add node
            self.add(node)

        else:
            node.val = value
            self.update(node)

        self.k2n[key] = node

    def update(self, node):
        if self.tail == node:
            return
        prev = node.prev
        next = node.next

        prev.next = next
        next.prev = prev

        # goto tail
        t = self.tail
        t.next = node
        node.prev = t
        self.tail = node

    def evict(self):
        first = self.head.next
        new_first = first.next
        if new_first is None:
            self.head.next = None
            self.tail = self.head
        else:
            self.head.next = new_first
            new_first.prev = self.head

        del self.k2n[first.key]
        del first

    def add(self, node):
        t = self.tail
        t.next = node
        node.prev = t
        self.tail = node



"""

Runtime: 1351 ms, faster than 13.21% of Python3 online submissions for LRU Cache.
Memory Usage: 76.1 MB, less than 5.29% of Python3 online submissions for LRU Cache.

"""

from collections import OrderedDict
class LRUCache:
    def __init__(self, Capacity):
        self.size = Capacity
        self.cache = OrderedDict()

    def get(self, key):
        if key not in self.cache: return -1
        val = self.cache[key]
        self.cache.move_to_end(key)
        return val

    def put(self, key, val):
        if key in self.cache: del self.cache[key]
        self.cache[key] = val
        if len(self.cache) > self.size:
            self.cache.popitem(last=False)


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)

if __name__ == "__main__":

    lRUCache = LRUCache(2)
    lRUCache.put(1, 1)
    lRUCache.put(2, 2) # // cache is {1 = 1, 2 = 2}

    print(lRUCache.get(1))  # // return 1
    lRUCache.put(3, 3)#  ; // LRU
    # key
    # was
    # 2, evicts
    # key
    # 2, cache is {1 = 1, 3 = 3}
    print(lRUCache.get(2))  #; // returns - 1(not found)
    lRUCache.put(4, 4)  #; // LRU
    # key
    # was
    # 1, evicts
    # key
    # 1, cache is {4 = 4, 3 = 3}
    print(lRUCache.get(1))  #; // return -1(not found)
    print(lRUCache.get(3))  #; // return 3
    print(lRUCache.get(4))  #; // return 4



"""
Runtime: 44 ms, faster than 36.17% of Python3 online submissions for Word Break.
Memory Usage: 14.7 MB, less than 14.46% of Python3 online submissions for Word Break.
"""


