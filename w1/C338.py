"""
338. Counting Bits

Given an integer num, return an array of the number of 1's in the binary representation of every number in the range [0, num].
"""

class Solution(object):
    def countBits(self, num):
        """
        :type num: int
        :rtype: List[int]
        """
        
        def get_subarray(order):
            if order == 0:
                return [0]
            return get_subarray(order-1) + [arg+1 for arg in get_subarray(order-1)]

        copy = num
        order = 0
        while copy >= 2:
            copy /= 2
            order += 1

        res = []
        
        for item in range(2**order, num+1):
            subs = bin(item)[2:]
            res.append(sum([int(i) for i in subs]))

            
        return get_subarray(order) + res

"""
Runtime: 184 ms, faster than 16.91% of Python online submissions for Counting Bits.
Memory Usage: 16.2 MB, less than 86.95% of Python online submissions for Counting Bits.
"""

class Solution:
    def countBits(self, num: int) -> List[int]:
        return ['{0:08b}'.format(i).count('1') for i in range(num+1)]

"""
Runtime: 80 ms, faster than 43.75% of Python online submissions for Counting Bits.
Memory Usage: 17.4 MB, less than 22.98% of Python online submissions for Counting Bits.
"""