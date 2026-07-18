

'''
123. Best Time to Buy and Sell Stock III
Hard
Topics
premium lock iconCompanies

You are given an array prices where prices[i] is the price of a given stock on the ith day.

Find the maximum profit you can achieve. You may complete at most two transactions.

Note: You may not engage in multiple transactions simultaneously (i.e., you must sell the stock before you buy again).

 

Example 1:

Input: prices = [3,3,5,0,0,3,1,4]
Output: 6
Explanation: Buy on day 4 (price = 0) and sell on day 6 (price = 3), profit = 3-0 = 3.
Then buy on day 7 (price = 1) and sell on day 8 (price = 4), profit = 4-1 = 3.

Example 2:

Input: prices = [1,2,3,4,5]
Output: 4
Explanation: Buy on day 1 (price = 1) and sell on day 5 (price = 5), profit = 5-1 = 4.
Note that you cannot buy on day 1, buy on day 2 and sell them later, as you are engaging multiple transactions at the same time. You must sell before buying again.

Example 3:

Input: prices = [7,6,4,3,1]
Output: 0
Explanation: In this case, no transaction is done, i.e. max profit = 0.

 

Constraints:

    1 <= prices.length <= 10^5
    0 <= prices[i] <= 10^5



'''


from typing import List 

class Solution:

    def soln2(self, prices: List[int]) -> int:

        '''
        Runtime
        248ms
        Beats35.12%
        Memory
        46.48MB
        Beats25.82%
                
        '''

        mem_start = {} # keep track of best run from every starting point... 

        # run in n^2 by checking every point with every other point 

        best_overall = 0
        best_start = 0
        last_end = 0
        running_max = 0
        for start in range(0, len(prices)):

            if last_end > start:
                # the argmax end from a prior real scan (last_end) is still inside this
                # start's valid window (end > start), so the window's max price hasn't
                # changed -- every value in the window shifts by the same amount, so we
                # can just shift running_max instead of rescanning the whole window
                running_max = running_max + prices[start - 1] - prices[start]
                mem_start[start] = mem_start[start - 1]

            else:
                mem_start[start] = 0
                running_max = 0

                for end in range(start+1, len(prices)):

                    run_total = prices[end] - prices[start]

                    if run_total < 0: # once a run goes negative... there is no point waiting for it to go back up, since we just found a better starting point anyways...
                        # correct as-is: if this row got cut short here, the true global best can't
                        # have started at `start`, since prices[end] < prices[start] would make (end, ...)
                        # strictly better than any (start, ...) pair -- so start won't end up as best_start
                        # do NOT touch mem_start[start] or last_end here -- they already hold the best
                        # confirmed argmax found before the dip, and the dip index itself is not an
                        # argmax, so it must never be used as one by the shortcut above
                        break

                    if run_total >= running_max:
                        # bug fix: this used to be a strict > only, so a tie (prices[end] equal to
                        # the window's current max) never advanced last_end. On a long run of equal
                        # prices that meant every later start had to redo its own full O(n) scan
                        # instead of shortcutting -- O(n^2) overall. A tie still proves the window's
                        # max hasn't changed, so it should extend last_end just like an improvement does.
                        mem_start[start] = end # update a new end of transcation run, if price is net higher...
                        last_end = end
                        running_max = run_total

            if running_max > best_overall:
                best_overall = running_max
                best_start = start


        if best_overall <= 0: # all prices are negative....
            return 0

        # for second best run, either its a disjoint run, or find the biggest dip in the best run, and split the run in two...

        best_end = mem_start[best_start]

        # candidate A: split the best run [best_start, best_end] at its biggest interior dip
        run_len = best_end - best_start + 1

        forward_best = [0] * run_len
        run_min = prices[best_start]
        for i in range(1, run_len):
            idx = best_start + i
            if prices[idx] - run_min > forward_best[i - 1]:
                forward_best[i] = prices[idx] - run_min
            else:
                forward_best[i] = forward_best[i - 1]
            if prices[idx] < run_min:
                run_min = prices[idx]

        backward_best = [0] * run_len
        run_max = prices[best_end]
        for i in range(run_len - 2, -1, -1):
            idx = best_start + i
            if run_max - prices[idx] > backward_best[i + 1]:
                backward_best[i] = run_max - prices[idx]
            else:
                backward_best[i] = backward_best[i + 1]
            if prices[idx] > run_max:
                run_max = prices[idx]

        split_total = 0
        for i in range(run_len):
            if forward_best[i] + backward_best[i] > split_total:
                split_total = forward_best[i] + backward_best[i]

        # candidate B: best run + best disjoint run entirely before best_start or entirely after best_end
        before_best = 0
        if best_start > 0:
            run_min = prices[0]
            for i in range(0, best_start + 1):
                if prices[i] < run_min:
                    run_min = prices[i]
                elif prices[i] - run_min > before_best:
                    before_best = prices[i] - run_min

        after_best = 0
        if best_end < len(prices) - 1:
            run_min = prices[best_end]
            for i in range(best_end, len(prices)):
                if prices[i] < run_min:
                    run_min = prices[i]
                elif prices[i] - run_min > after_best:
                    after_best = prices[i] - run_min

        if before_best > after_best:
            disjoint_total = best_overall + before_best
        else:
            disjoint_total = best_overall + after_best

        if split_total > disjoint_total:
            return split_total
        else:
            return disjoint_total


    def maxProfit(self, prices: List[int]) -> int:
        

        if len(prices) < 2: return 0 

        # need to find best 2 transactions... 

        # idea: find best run, and second best disjoint run....
        # step2: check for every sub-run that could break up the best run, but beat the disjoint run in total... 
        # only need to check dips... 
        # use mem to store best run from every step... can run in n^2...


        return self.soln2(prices)


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

