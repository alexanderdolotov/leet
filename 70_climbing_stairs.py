'''
70. Climbing Stairs
Easy
Topics
premium lock iconCompanies
Hint

You are climbing a staircase. It takes n steps to reach the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

 

Example 1:

Input: n = 2
Output: 2
Explanation: There are two ways to climb to the top.
1. 1 step + 1 step
2. 2 steps

Example 2:

Input: n = 3
Output: 3
Explanation: There are three ways to climb to the top.
1. 1 step + 1 step + 1 step
2. 1 step + 2 steps
3. 2 steps + 1 step

 

Constraints:

    1 <= n <= 45

 

'''

from collections import deque
from typing import Optional

class Solution:

    def closed_sol(self, n: int) -> int:


        # there should be some osrt of closed math solution by induction 
        # for the nth stair, it takes n = f(n-1) + f(n-2) steps. which also follows a fibinacci sequence. 
        # where the begining is 1, 2, 3, 5

        # this sequence has a closed solution: 


        sqrt5 = 2.23606797749979
        phi = (1 + sqrt5) / 2
        return round(phi ** (n + 1) / sqrt5) 
    

    def rec_sol(self, n: int) -> int:

        if n == 0: return 1
        if n == 1: return 1
        if n == 2: return 2
        if n == 3: return 3

        # Time Limit Exceeded 21 / 45 testcases passed

        return self.rec_sol(n-1) + self.rec_sol(n-2)


    mem = {}

    def rec_sol_mem(self, n: int) -> int:

        '''
        Runtime
        0ms
        Beats100.00%
        Memory
        19.48MB
        Beats16.44%
        '''

        if n == 0: return 1
        if n == 1: return 1
        if n == 2: return 2
        if n == 3: return 3

        n1 = self.mem[n-1] if n-1 in self.mem else self.rec_sol_mem(n-1)
        n2 = self.mem[n-2] if n-2 in self.mem else self.rec_sol_mem(n-2)

        self.mem[n] = n1 + n2
        return self.mem[n]


    def rec_sol_mem2(self, n: int, i: int = 3, queue: Optional[deque] = None) -> int:

        '''
        Runtime
        0ms
        Beats100.00%
        Memory
        19.34MB
        Beats16.44%
        '''

        if n == 0: return 1
        if n == 1: return 1
        if n == 2: return 2

        if queue is None:
            queue = deque([1, 2], maxlen=2)

        if i > n:
            return queue[-1]

        queue.append(queue[0] + queue[1])
        return self.rec_sol_mem2(n, i + 1, queue)


    def loop_sol(self, n: int) -> int:

        if n == 0: return 1
        if n == 1: return 1
        if n == 2: return 2

        prev2, prev1 = 1, 2
        for _ in range(3, n + 1):
            prev2, prev1 = prev1, prev1 + prev2

        return prev1


    def climbStairs(self, n: int) -> int:

        self.mem = {}

        return self.loop_sol(n)
    

