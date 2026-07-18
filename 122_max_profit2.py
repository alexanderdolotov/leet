from typing import List

# 122. Best Time to Buy and Sell Stock II

'''
You are given an integer array prices where prices[i] is the price of a given stock on the ith day.

On each day, you may decide to buy and/or sell the stock. You can only hold at most one share of the stock at any time. However, you can sell and buy the stock multiple times on the same day, ensuring you never hold more than one share of the stock.

Find and return the maximum profit you can achieve.

Input: prices = [7,1,5,3,6,4]
Output: 7
Explanation: Buy on day 2 (price = 1) and sell on day 3 (price = 5), profit = 5-1 = 4.
Then buy on day 4 (price = 3) and sell on day 5 (price = 6), profit = 6-3 = 3.
Total profit is 4 + 3 = 7.

'''

# beats 100%
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        

        l = len(prices)
        if l == 0 or l == 1:
            return 0 
        
        if l == 2:
            return max(0, prices[1] - prices[0])


        start_price = prices[0] 

        last_price = start_price
        running_profit = 0
        for i in range(1, l):
            curr_price = prices[i]

            if curr_price < last_price:
                # sell before price drop
                profit = last_price - start_price
                if profit > 0:
                    running_profit += profit

                start_price = curr_price

                
            last_price = curr_price

        
        profit = curr_price - start_price
        if profit > 0:
            running_profit += profit

        return running_profit



s = Solution()
out = s.maxProfit(prices=[7,4,3,2,1,3,1,5,3,6,4,5,4,3,2,1,2])
print(out)
