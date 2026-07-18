'''

502. IPO
Hard
Topics
premium lock iconCompanies

Suppose LeetCode will start its IPO soon. In order to sell a good price of its shares to Venture Capital, LeetCode would like to work on some projects to increase its capital before the IPO. Since it has limited resources, it can only finish at most k distinct projects before the IPO. Help LeetCode design the best way to maximize its total capital after finishing at most k distinct projects.

You are given n projects where the ith project has a pure profit profits[i] and a minimum capital of capital[i] is needed to start it.

Initially, you have w capital. When you finish a project, you will obtain its pure profit and the profit will be added to your total capital.

Pick a list of at most k distinct projects from given projects to maximize your final capital, and return the final maximized capital.

The answer is guaranteed to fit in a 32-bit signed integer.

 

Example 1:

Input: k = 2, w = 0, profits = [1,2,3], capital = [0,1,1]
Output: 4
Explanation: Since your initial capital is 0, you can only start the project indexed 0.
After finishing it you will obtain profit 1 and your capital becomes 1.
With capital 1, you can either start the project indexed 1 or the project indexed 2.
Since you can choose at most 2 projects, you need to finish the project indexed 2 to get the maximum capital.
Therefore, output the final maximized capital, which is 0 + 1 + 3 = 4.

Example 2:

Input: k = 3, w = 0, profits = [1,2,3], capital = [0,1,2]
Output: 6

 

Constraints:

    1 <= k <= 105
    0 <= w <= 109
    n == profits.length
    n == capital.length
    1 <= n <= 105
    0 <= profits[i] <= 104
    0 <= capital[i] <= 109

 
'''

from typing import List
import heapq

class Solution:

    def get_max_profit_maxw(self, max_capital: int, profits: List[int], capital: List[int], completed: List[int]):

        # linear scan with filter

        max_profit = 0 
        best_project = -1

        for project in range(len(profits)):
            if project in completed: continue 

            if capital[project] <= max_capital:
                if profits[project] >= max_profit:
                    max_profit = profits[project]
                    best_project = project


        return best_project



    def sol_n2(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:

        # will time out on lone cases... not leetable...

        total_profits = 0
        completed_projects = []
        for i in range(k):

            best_project = self.get_max_profit_maxw(max_capital=w+total_profits, profits=profits, capital=capital, completed=completed_projects)
            if best_project == -1: return w + total_profits
            
            total_profits += profits[best_project]
            completed_projects.append(best_project)

        return w + total_profits




    def sol_nb(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:

        '''
        Runtime
        243ms
        Beats88.39%
        Memory
        47.78MB
        Beats14.10%
        '''

        # preprocess data for better efficiency 
        # 1st sort all projects by capital cost 

        capital_projects = []
        
        for p in range(len(profits)):
            capital_projects.append( (-profits[p], capital[p]))

        capital_projects.sort(key=lambda proj: proj[1])

        # create a rolling max_profit heap 
        # build initial max_profits heap

        profits_heap = []
        pidx = 0 # keep for continuing later
        while pidx < len(capital_projects) and capital_projects[pidx][1] <= w:
            profits_heap.append(capital_projects[pidx][0])
            pidx += 1

        heapq.heapify(profits_heap)

        total_profits = w
        #completed_projects = set()
        for i in range(k): # has to have k loops for k total projects

            if len(profits_heap) == 0: return total_profits

            best_project = heapq.heappop(profits_heap)
            total_profits += -best_project

            while pidx < len(capital_projects) and capital_projects[pidx][1] <= total_profits:
                heapq.heappush(profits_heap, capital_projects[pidx][0])
                pidx += 1

        return total_profits
    


    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        

        # max k project 
        # w is initial kapital 
        # profits[] from projects with input costs capital[] 

        # seems like to take a greedy approach, we should always do a feasible project capital[i] <= w, with highest payoff where max(p)


        # need to use correct data structure to filter by and get top p where capital[i] <= w 
        # select project from projects where capital <= existing_capital order by profit desc limit 1

        # possible idea that could run in O(sqrtN):
        # make tuple: (project_id, profit, cost) 
        # now make sorted arrays per cost threshold buckets, as per historgram distribution.
        # ex. if 100 projects and H=10, will make buckets of bottom 10 projects with costs < max(bottom10), then bottom20, etc. into 10 buckets (with overlapping projects sorted in desc order)


        # but using heap is better



        return self.sol_nb(k,w, profits, capital)
    

