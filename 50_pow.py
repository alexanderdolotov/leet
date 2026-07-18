'''
50. Pow(x, n)
Medium
Topics
premium lock iconCompanies

Implement pow(x, n), which calculates x raised to the power n (i.e., xn).

 

Example 1:

Input: x = 2.00000, n = 10
Output: 1024.00000

Example 2:

Input: x = 2.10000, n = 3
Output: 9.26100

Example 3:

Input: x = 2.00000, n = -2
Output: 0.25000
Explanation: 2-2 = 1/22 = 1/4 = 0.25

 

Constraints:

    -100.0 < x < 100.0
    -231 <= n <= 231-1
    n is an integer.
    Either x is not zero or n > 0.
    -104 <= xn <= 104

 

'''


class Solution:

    def loopsol(self, x: float, n: int) -> float:

        # Time Limit Exceeded 294 / 307 testcases passed

        if x == 0: return 0
        if n == 0: return 1

        r = 1
        for _ in range(abs(n)):
            r = r*x

        if n < 0: return 1/r

        return r



    def sol2(self, x: float, n: int) -> float:

        '''
        Runtime
        0ms
        Beats100.00%
        Memory
        19.41MB
        Beats53.96%

        '''

        if x == 0: return 0
        if n == 0: return 1

        # x * x * x.... n times... 

        # take out the nearst largest power of 2 from n 
        # x ^ (2^k) = ( x * x ) * x... k times
        # then raise by remainder r = n - 2^k ... 
        # can still improve r and k ... 
        
        # find larget power of 2 using highest bit
        # find remainer

        # loop k times of x * self


        # run remainder

        result = 1
        remaining = abs(n)

        while remaining > 0:
            k = remaining.bit_length() - 1 # find highest power of 2 in n

            power = x
            for _ in range(k):
                power = power * power # x^x function

            result = result * power
            remaining = remaining - (1 << k) # remaining from n where r = n - 2^k

        if n < 0: return 1.0/result

        return result




    def sol3(self, x: float, n: int) -> float:

        if x == 0: return 0
        if n == 0: return 1

        # same bit idea as sol2, but carry the running square forward
        # instead of rebuilding x^(2^k) from scratch each pass

        result = 1
        base = x
        e = abs(n)

        while e > 0:
            if e & 1:
                result = result * base
            base = base * base
            e >>= 1

        if n < 0: return 1.0/result

        return result



    def myPow(self, x: float, n: int) -> float:


        return self.sol3(x,n)
    

