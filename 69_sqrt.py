'''
69. Sqrt(x)
Easy
Topics
premium lock iconCompanies
Hint

Given a non-negative integer x, return the square root of x rounded down to the nearest integer. The returned integer should be non-negative as well.

You must not use any built-in exponent function or operator.

    For example, do not use pow(x, 0.5) in c++ or x ** 0.5 in python.

 

Example 1:

Input: x = 4
Output: 2
Explanation: The square root of 4 is 2, so we return 2.

Example 2:

Input: x = 8
Output: 2
Explanation: The square root of 8 is 2.82842..., and since we round it down to the nearest integer, 2 is returned.

 

Constraints:

    0 <= x <= 231 - 1

 
'''



import struct

class Solution:

    def dumsol(self, x):
        '''
        Runtime
        1181ms
        Beats12.87%
        Memory
        19.18MB
        Beats87.51%

        
        '''

        # dumbest approach:
        s = 1
        while s*s < x:
            s += 1

        if s*s > x: return s-1

        return s
    

    def sqrt_bit(self, x):

        if x == 0: return 0
        if x == 1: return 1

        '''
        Runtime
        0ms
        Beats100.00%
        Memory
        19.30MB
        Beats23.25%
        '''

        # bit shifting works in max 16 loops
        result = 0
        bit = 1 << (x.bit_length() // 2) # start at halfway of max bit

        # loop down trying every higher bit from mid way
        while bit > 0:
            candidate = result + bit 
            if candidate * candidate <= x: # if bit overshoots, skip it
                result = candidate
            bit >>= 1

        return result


    def mySqrt(self, x: int) -> int:

        if x == 0: return 0

        # can you newtons method
        # can do lookup tables
        # probably some other math heuristic for finding sqrt root algorithmically...

        # can also just do binary method of doubling and halving a number being squared, and taking the error diff. (similar to newtons)

        return self.sqrt_bit(x)



    def quakesqrt(self, x: int) -> int:

        '''
        Runtime
        0ms
        Beats100.00%
        Memory
        19.52MB
        Beats6.29%
        '''

        if x == 0: return 0
        if x == 1: return 1

        # Quake III fast inverse sqrt bit hack: reinterpret the float32 bits as an
        # int, do the magic-number subtract-and-shift, reinterpret back as float32.
        # gives a rough guess at 1/sqrt(x) with no divide and no exponent op.
        y = float(x)
        i = struct.unpack('<i', struct.pack('<f', y))[0]
        i = 0x5f3759df - (i >> 1)
        y = struct.unpack('<f', struct.pack('<i', i))[0]

        x2 = x * 0.5
        y = y * (1.5 - (x2 * y * y))  # newton iteration on the approximation
        y = y * (1.5 - (x2 * y * y))  # second pass, float32 isn't precise enough near 2^31 with just one

        s = int(x * y)  # sqrt(x) = x * invsqrt(x)

        # float32 rounding means s can be off by one, nudge it to the true floor
        while s * s > x: s -= 1
        while (s + 1) * (s + 1) <= x: s += 1

        return s

