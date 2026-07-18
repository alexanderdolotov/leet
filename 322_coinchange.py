'''
322. Coin Change
Medium

Topics
premium lock icon
Companies
You are given an integer array coins representing coins of different denominations and an integer amount representing a total amount of money.

Return the fewest number of coins that you need to make up that amount. If that amount of money cannot be made up by any combination of the coins, return -1.

You may assume that you have an infinite number of each kind of coin.

 

Example 1:

Input: coins = [1,2,5], amount = 11
Output: 3
Explanation: 11 = 5 + 5 + 1
Example 2:

Input: coins = [2], amount = 3
Output: -1
Example 3:

Input: coins = [1], amount = 0
Output: 0
 

Constraints:

1 <= coins.length <= 12
1 <= coins[i] <= 2^31 - 1
0 <= amount <= 10^4
'''


from typing import List
import bisect

class Solution:

    results_found = {} # keeps memory of already found results for substrings so as not to double check them again
    coins_sorted = []

    def coins_rec(self, amount:int) -> int:
        '''
        Accepted
        189 / 189 testcases passed
        alexdolotov
        alexdolotov
        submitted at Jul 09, 2026 15:48

        Runtime
        1451
        ms
        Beats
        5.01%
        '''
        
        if amount == 0:
            return 0 
        
        if amount < 0:
            return -1 
        
        i = bisect.bisect_left(self.coins_sorted, amount)
        if i < len(self.coins_sorted) and self.coins_sorted[i] == amount:
            return 1
        
        if amount in self.results_found: # result has to contain minimum 
            return self.results_found[amount] 
        
        local_results = []
        for c in reversed(self.coins_sorted):
            result = self.coins_rec(amount - c)
            local_results.append(result)

        local_results = [r for r in local_results if r != -1]
        if local_results:
            self.results_found[amount] = min(local_results) + 1
            return min(local_results) + 1
        else:
            self.results_found[amount] = -1

        return -1


    def coinChange(self, coins: List[int], amount: int) -> int:
        self.coins_sorted = sorted(coins, reverse=False)
        self.results_found = {}

        #result = self.coins_rec(amount)
        result = self.coinChange_dp(coins, amount)
        return result

    def coinChange_dp(self, coins: List[int], amount: int) -> int:
        '''
        
        Runtime
        319
        ms
        Beats
        98.73%


        Memory
        19.86
        MB
        Beats
        35.35%
        '''
        # dp[a] = fewest coins to make amount a. amount + 1 is a safe "unreachable"
        # sentinel since the true answer can never exceed amount (using all 1-coins).
        dp = [0] + [amount + 1] * amount # alloc an array of max size 10K + 2 entries. 

        # Build up from smaller amounts so dp[a - c] is already final by the time
        # we use it for a.
        for a in range(1, amount + 1):
            for c in coins:
                if c <= a and dp[a - c] + 1 < dp[a]:
                    dp[a] = dp[a - c] + 1

        # If dp[amount] never dropped below the sentinel, no combination works.
        return dp[amount] if dp[amount] <= amount else -1
    
    