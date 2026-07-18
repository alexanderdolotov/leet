'''
172. Factorial Trailing Zeroes
Medium
Topics
premium lock iconCompanies

Given an integer n, return the number of trailing zeroes in n!.

Note that n! = n * (n - 1) * (n - 2) * ... * 3 * 2 * 1.

 

Example 1:

Input: n = 3
Output: 0
Explanation: 3! = 6, no trailing zero.

Example 2:

Input: n = 5
Output: 1
Explanation: 5! = 120, one trailing zero.

Example 3:

Input: n = 0
Output: 0

 

Constraints:

    0 <= n <= 104

 

Follow up: Could you write a solution that works in logarithmic time complexity?
 


'''


class Solution:
    def trailingZeroes(self, n: int) -> int:
        

        # what makes zeros? 10s and 5s X 2 ... 10 is already 5x2...
        # so i want to count powers of 5s and 2s, and take min(2s, 5s)
        # 2s are more abandant than 5s in factorials, so i just need to count powers of 5s...

        '''
        Runtime
        0ms
        Beats100.00%
        Memory
        19.19MB
        Beats89.46%

        '''
        
        count = 0
        power = 5
        while power <= n:
            count += n // power
            power *= 5

        return count
    
