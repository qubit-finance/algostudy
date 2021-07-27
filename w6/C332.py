"""
322. Coin Change

You are given an integer array coins representing coins of different denominations and an integer amount representing a total amount of money.

Return the fewest number of coins that you need to make up that amount. If that amount of money cannot be made up by any combination of the coins, return -1.

You may assume that you have an infinite number of each kind of coin.
"""

class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        
        from collections import deque
        
        if amount == 0:
            return 0
        
        coins = sorted(coins)[::-1] # sort in descending order
        level = 1
        cands = []
        cur = deque()
        cur.append(amount)
        
        while cur:
            for _ in range(len(cur)):
                tmp = cur.popleft()
                for coin in coins:
                    if tmp-coin > 0:
                        cur.append(tmp-coin)
                    elif tmp-coin==0:
                        return level
            level += 1
            
        return -1
                
"""
Time Limit Exceeded
"""

class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        
        MAX = 10**4+1 # Largest plausible number under constraint
        memo = [0]+[MAX]*amount # Memo of all numbers smaller than our target
        
        for i in range(1, amount+1): # Linear time
            memo[i] = min([memo[i-coin] for coin in coins if i-coin>=0]+[MAX]) + 1 # n_coins <= 12
            
        return memo[amount] if memo[amount]<=MAX else -1

"""
Runtime: 864 ms, faster than 95.09% of Python online submissions for Coin Change.
Memory Usage: 14.2 MB, less than 42.00% of Python online submissions for Coin Change.
"""