'''

137. Single Number II
Medium
Topics
premium lock iconCompanies

Given an integer array nums where every element appears three times except for one, which appears exactly once. Find the single element and return it.

You must implement a solution with a linear runtime complexity and use only constant extra space.

 

Example 1:

Input: nums = [2,2,3,2]
Output: 3

Example 2:

Input: nums = [0,1,0,1,0,1,99]
Output: 99

 

Constraints:

    1 <= nums.length <= 3 * 104
    -231 <= nums[i] <= 231 - 1
    Each element in nums appears exactly three times except for one element which appears once.

 

'''

from typing import List 

class Solution:

    def sol_dict(self, nums: List[int]) -> int:

        # breaks constant memory rule . also runs in O(n)
        '''
        Runtime
        3ms
        Beats71.05%
        Memory
        20.97MB
        Beats15.67%
        '''

        dnums = dict()
        for n in nums:
            if n in dnums: dnums[n] += 1
            else: dnums[n] = 1

        for n, c in dnums.items():
            if c == 1:
                return n
                

        return 0  # should never return 0 
    


    def sol_bitwise(self, nums: List[int]) -> int:

        # O(n) time, O(1) space
        # ones/twos track, per bit position, whether that bit has been
        # seen 1 time or 2 times (mod 3) so far; on the 3rd occurrence
        # the bit is cleared from both, resetting the count to 0

        ones = 0
        twos = 0
        for n in nums:
            # & keeps bits set in both operands: finds bits already flagged
            # "seen once" that are set again in n -> these are now seen twice
            twos |= ones & n 

            # ^ flips bits that are set in n: toggles each bit's membership
            # in the "seen once" set (in if it was out, out if it was in)
            ones ^= n

            # & keeps bits set in both trackers: a bit flagged in both
            # ones and twos has just occurred for the 3rd time
            seen_thrice = ones & twos

            # ~ flips every bit of seen_thrice, so &-ing with it clears
            # exactly the 3rd-occurrence bits, resetting their count to 0
            ones &= ~seen_thrice
            twos &= ~seen_thrice

        return ones


    def singleNumber(self, nums: List[int]) -> int:

        return self.sol_bitwise(nums)
    

