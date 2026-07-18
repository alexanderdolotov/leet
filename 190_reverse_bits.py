'''
190. Reverse Bits
Easy
Topics
premium lock iconCompanies

Reverse bits of a given 32 bits signed integer.

 

Example 1:

Input: n = 43261596

Output: 964176192

Explanation:
Integer	Binary
43261596	00000010100101000001111010011100
964176192	00111001011110000010100101000000

Example 2:

Input: n = 2147483644

Output: 1073741822

Explanation:
Integer	Binary
2147483644	01111111111111111111111111111100
1073741822	00111111111111111111111111111110

 

Constraints:

    0 <= n <= 231 - 2
    n is even.

 

Follow up: If this function is called many times, how would you optimize it?
 

'''


class Solution:


    def sol1(self, n: int) -> int:

        '''
        Runtime
        48ms
        Beats45.84%
        Memory
        19.26MB
        Beats29.21%
        '''

        bits = [0]*32 

        for i in range(32):

            bits[i] = n%2
            n = n // 2 

        bits.reverse()

        # now create new number by adding multiples of powers of 2 as per bits

        nr = 0 
        cpower = 1
        for i in range(32):
            nr += bits[i] * cpower
            cpower *= 2

        return nr


    def sol2(self, n: int) -> int:
        '''
        The idea: first swap the two 16-bit halves, then the 8-bit halves within each half, then 4-bit, 2-bit, 1-bit — each step doubles how finely you're swapping, and after 5 steps every bit has migrated to its mirrored position. It's O(1) fixed work regardless of input, versus your loop's 32 iterations.
        
        Runtime
        44ms
        Beats70.92%
        Memory
        19.21MB
        Beats29.21%
        '''



        n = (n >> 16) | (n << 16)
        n = ((n & 0xff00ff00) >> 8)  | ((n & 0x00ff00ff) << 8)
        n = ((n & 0xf0f0f0f0) >> 4)  | ((n & 0x0f0f0f0f) << 4)
        n = ((n & 0xcccccccc) >> 2)  | ((n & 0x33333333) << 2)
        n = ((n & 0xaaaaaaaa) >> 1)  | ((n & 0x55555555) << 1)
        return n & 0xFFFFFFFF



    def reverseBits(self, n: int) -> int:
        

        return self.sol2(n)
    

