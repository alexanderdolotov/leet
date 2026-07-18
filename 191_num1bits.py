'''
191. Number of 1 Bits
Easy
Topics
premium lock iconCompanies

Given a positive integer n, write a function that returns the number of in its binary representation (also known as the Hamming weight).

 

Example 1:

Input: n = 11

Output: 3

Explanation:

The input binary string 1011 has a total of three set bits.

Example 2:

Input: n = 128

Output: 1

Explanation:

The input binary string 10000000 has a total of one set bit.

Example 3:

Input: n = 2147483645

Output: 30

Explanation:

The input binary string 1111111111111111111111111111101 has a total of thirty set bits.

 

Constraints:

    1 <= n <= 231 - 1

 
Follow up: If this function is called many times, how would you optimize it?
'''


class Solution:
    def hammingWeight(self, n: int) -> int:
        
        '''
        Runtime
        0ms
        Beats100.00%
        Memory
        19.09MB
        Beats97.62%

        '''

        bits = 0 
        for i in range(32):
            if n%2:
                bits += 1 

            n = n // 2


        return bits
    