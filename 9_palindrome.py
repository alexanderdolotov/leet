'''
9. Palindrome Number
Easy
Topics
premium lock iconCompanies
Hint

Given an integer x, return true if x is a , and false otherwise.

 

Example 1:

Input: x = 121
Output: true
Explanation: 121 reads as 121 from left to right and from right to left.

Example 2:

Input: x = -121
Output: false
Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.

Example 3:

Input: x = 10
Output: false
Explanation: Reads 01 from right to left. Therefore it is not a palindrome.

 

Constraints:

    -231 <= x <= 231 - 1

 
Follow up: Could you solve it without converting the integer to a string?
'''


class Solution:

    def stringsol(self, x: int) -> bool:

        '''
        Runtime
        7ms
        Beats63.11%
        Memory
        19.34MB
        Beats17.60%
        
        '''

        xs = str(x)
        xsr = xs[::-1]

        return xs == xsr


    def sol2(self, x: int) -> bool:

        '''
        Runtime
        15ms
        Beats18.21%
        Memory
        19.30MB
        Beats17.60%
        '''

        # stores powers of 10 and compares reversed
        if x < 0:
            return False
        if x == 0:
            return True

        digits = []
        power = 1
        while power <= x:
            digit = (x // power) % 10
            digits.append(digit)
            power *= 10

        return digits == digits[::-1]


    def sol3(self, x: int) -> bool:
        if x < 0 or (x % 10 == 0 and x != 0):
            return False

        reverted = 0
        while x > reverted:
            reverted = reverted * 10 + x % 10
            x //= 10

        return x == reverted or x == reverted // 10



    def isPalindrome(self, x: int) -> bool:
        
        if x < 0: return False # all negative numbers cannot be reversed. 


        return self.sol3(x) 
    
