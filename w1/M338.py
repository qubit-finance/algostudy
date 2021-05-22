"""
Given an integer num, return an array of the number of 1's in the binary representation of every number in the range [0, num].
"""
class Solution:
    def countBits(self, num: int) -> List[int]:
    
        def get_orderSum(number):
            i = 0
            while(number > 0):
                i += (number & 1)
                number = number >> 1
                
                
            return i
        
        return [get_orderSum(x) for x in range(num+1)]
        
        
#Runtime: 216 ms, faster than 11.48% of Python3 online submissions for Counting Bits.
#Memory Usage: 21 MB, less than 41.06% of Python3 online submissions for Counting Bits.
