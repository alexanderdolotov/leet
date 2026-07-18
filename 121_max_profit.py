from typing import List

# 121. Best Time to Buy and Sell Stock
class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        max_profit = 0 
        l = len(prices)
        if l == 0:
            return max_profit 

        if l == 1:
            return max_profit 
  

        if l == 2:
            return max(0, prices[1] - prices[0])

        # first pass 
        buy_idxs = [0]
        running_high = prices[0]
        running_low = prices[0]
        buy_price = prices[0]
        
        for i in range(1, l):

            price = prices[i] 
            if price > running_high:
                running_high = price

            if price < running_low:
                running_low = price 

                # if the last buy index is the previous index, update the last buy index
                if buy_idxs[-1] == i-1:
                    buy_idxs[-1] = i
                # otherwise, add a new buy index
                else:
                    buy_idxs.append(i)  

             
        running_profit = running_high - buy_price
        if running_profit > max_profit:
            max_profit = running_profit

        for buy_idx in buy_idxs:
            buy_price = prices[buy_idx] 
            running_high = buy_price 

            for i in range(buy_idx+1, l):

                price = prices[i] 
                if price > running_high:
                    running_high = price

            running_profit = running_high - buy_price
            if running_profit > max_profit:
                max_profit = running_profit


        return max(0, max_profit)
        

