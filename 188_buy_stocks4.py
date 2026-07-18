'''
188. Best Time to Buy and Sell Stock IV
Hard
Topics
premium lock iconCompanies

You are given an integer array prices where prices[i] is the price of a given stock on the ith day, and an integer k.

Find the maximum profit you can achieve. You may complete at most k transactions: i.e. you may buy at most k times and sell at most k times.

Note: You may not engage in multiple transactions simultaneously (i.e., you must sell the stock before you buy again).

 

Example 1:

Input: k = 2, prices = [2,4,1]
Output: 2
Explanation: Buy on day 1 (price = 2) and sell on day 2 (price = 4), profit = 4-2 = 2.

Example 2:

Input: k = 2, prices = [3,2,6,5,0,3]
Output: 7
Explanation: Buy on day 2 (price = 2) and sell on day 3 (price = 6), profit = 6-2 = 4. Then buy on day 5 (price = 0) and sell on day 6 (price = 3), profit = 3-0 = 3.

 

Constraints:

    1 <= k <= 100
    1 <= prices.length <= 1000
    0 <= prices[i] <= 1000


'''

from typing import List
from collections import deque

class Solution:


    def soln_state_machine(self, prices: List[int]) -> int:

        # "Textbook" solution: track the best profit achievable so far in each
        # of 4 states, and update all 4 once per day, in this order:
        #   buy1  = holding stock after your FIRST buy
        #   sell1 = cash on hand after your FIRST sell (1 transaction closed)
        #   buy2  = holding stock after your SECOND buy (funded by sell1's cash)
        #   sell2 = cash on hand after your SECOND sell (2 transactions closed)
        #
        # Each variable holds the best (max) value achievable using only the
        # prices seen so far. "Holding stock" is represented as a negative
        # number (cash spent to buy it), so buy1/buy2 start at -infinity
        # (haven't bought yet); sell1/sell2 (no stock, no transaction yet)
        # start at 0.
        #
        # Unlike soln2, this never looks for "runs" or explicit buy/sell
        # indices -- it only ever tracks 4 numbers, updated in a single O(n)
        # pass with O(1) space. It's correct for the same underlying reason
        # soln2 is: buy2/sell2 can only improve on buy1/sell1 by chaining off
        # sell1's cash, so if a second transaction never helps, buy2 and sell2
        # just end up mirroring buy1 and sell1 (buying and selling on the same
        # day nets 0, so sell2 can never fall below sell1).

        buy1 = float('-inf')
        sell1 = 0
        buy2 = float('-inf')
        sell2 = 0

        for price in prices:

            # keep yesterday's best first-buy, or buy today instead
            if -price > buy1:
                buy1 = -price

            # keep yesterday's best first-sell, or sell today using buy1's stock
            if buy1 + price > sell1:
                sell1 = buy1 + price

            # keep yesterday's best second-buy, or buy today using sell1's cash
            if sell1 - price > buy2:
                buy2 = sell1 - price

            # keep yesterday's best second-sell, or sell today using buy2's stock
            if buy2 + price > sell2:
                sell2 = buy2 + price

        # sell2 is the best profit achievable with AT MOST 2 transactions
        # (cast needed because buy1/buy2 start as float('-inf') for the type checker)
        return int(sell2)




    def maxProfit(self, k: int, prices: List[int]) -> int:

        n = len(prices)
        if n < 2 or k == 0:
            return 0

        # If we can afford at least n // 2 transactions, we can buy every local
        # dip and sell every local peak -- more transactions than that can never
        # help, since each one needs 2 distinct days. This degenerates into the
        # unlimited-transactions problem, solvable in O(n), so we don't pay
        # O(n*k) for a k bigger than the array could ever actually use.
        if k >= n // 2:
            total = 0
            for i in range(1, n):
                if prices[i] > prices[i - 1]:
                    total += prices[i] - prices[i - 1]
            return total

        # Same state machine as soln_state_machine in 123_stock3.py, generalized
        # from 4 states to 2k states: buy0, sell0, buy1, sell1, ..., buy(k-1),
        # sell(k-1). Stored as a FIFO queue in exactly that order. Each day we
        # pop every one of the 2k states off the front, update it, and push it
        # straight back onto the tail -- after 2k pop/push cycles the queue is
        # back in its original order, now holding tomorrow's starting values.
        #
        # The dependency: buy[i] needs sell[i-1], and sell[i] needs buy[i] --
        # both of those are always exactly the item popped immediately before
        # the current one, so a single "prev" variable carried across the
        # rotation supplies it without ever needing to look back into the queue.

        queue = deque()
        for i in range(k):
            queue.append(float('-inf'))  # buy[i]: haven't bought yet
            queue.append(0)              # sell[i]: no transaction closed yet

        prev = 0  # tracked outside the day loop so it survives as the final answer

        for price in prices:

            prev = 0            # sell[-1] doesn't exist, so buy0 is funded with 0 cash
            is_buy_turn = True  # queue order alternates buy, sell, buy, sell, ...

            for _ in range(2 * k):
                state = queue.popleft()

                if is_buy_turn:
                    candidate = prev - price
                    if candidate > state:
                        state = candidate
                else:
                    candidate = prev + price
                    if candidate > state:
                        state = candidate

                queue.append(state)
                prev = state
                is_buy_turn = not is_buy_turn

        # after the last day's rotation, prev holds the last state pushed --
        # which is always sell(k-1), i.e. profit after at most k transactions
        return int(prev)

