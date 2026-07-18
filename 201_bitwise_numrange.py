'''
201. Bitwise AND of Numbers Range
Medium
Topics
premium lock iconCompanies

Given two integers left and right that represent the range [left, right], return the bitwise AND of all numbers in this range, inclusive.

 

Example 1:

Input: left = 5, right = 7
Output: 4

Example 2:

Input: left = 0, right = 0
Output: 0

Example 3:

Input: left = 1, right = 2147483647
Output: 0

 

Constraints:

    0 <= left <= right <= 231 - 1

 
'''


class Solution:

    def sol_diff_shift(self, left: int, right: int) -> int:

        # broken: right - left isn't the number of trailing bits that
        # differ between left and right, so shifting by diff over- or
        # undershoots depending on the numbers - fails on e.g. (26, 30)

        # 5: 101  &  6: 110  &  7:  111 only common bit is 100 = 4

        if left == right: return left

        diff = right - left
        bright = right >> diff
        bleft = left >> diff

        a = bright & bleft

        aa = a << diff

        return aa


    def sol_common_prefix(self, left: int, right: int) -> int:

        # O(log right) time, O(1) space
        # shift left and right right by 1 together, counting shifts,
        # until they're equal -> that's their shared binary prefix.
        # every bit that differed gets shifted out and zeroed, so
        # shifting the common prefix back restores it correctly
        # padded with zeros

        shift = 0
        while left < right:
            left >>= 1
            right >>= 1
            shift += 1

        return left << shift


    def rangeBitwiseAnd(self, left: int, right: int) -> int:

        return self.sol_common_prefix(left, right)

