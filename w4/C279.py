"""
279. Perfect Squares

Given an integer n, return the least number of perfect square numbers that sum to n.

A perfect square is an integer that is the square of an integer; in other words, it is the product of some integer with itself. For example, 1, 4, 9, and 16 are perfect squares while 3 and 11 are not.
"""

class Solution(object):
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        import math
        self.cnts = []
        
        def recur(num, cnt):
            if num==0:
                self.cnts.append(cnt)
                return
            t1, t2, t3 = int(sqrt(num)), int(sqrt(num))-1, int(sqrt(num))-2
            if num-t1**2 >= 0 and t1 > 0:
                recur(num-t1**2, cnt+1)
            if num-t2**2 >= 0 and t2 > 0:
                recur(num-t2**2, cnt+1)
            if num-t3**2 >= 0 and t3 > 0:
                recur(num-t3**2, cnt+1)
            
    
            
        recur(n, 0)
                
        return min(self.cnts)
                

class Solution(object):
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        import math
        cnt = 0
        
        tmp1 = {n}
        lst = [k**2 for k in range(int(math.sqrt(n))+1)]
        
        while tmp1:
            cnt += 1
            tmp2 = set()
            for x in tmp1:
                for y in lst:
                    if x==y:
                        return cnt
                    if x<y:
                        break
                    tmp2.add(x-y)
            tmp1 = tmp2
            
        return cnt


"""
Runtime: 176 ms, faster than 87.94% of Python online submissions for Perfect Squares.
Memory Usage: 14.3 MB, less than 31.27% of Python online submissions for Perfect Squares.
"""