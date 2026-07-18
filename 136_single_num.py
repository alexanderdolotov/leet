'''
136. Single Number
Easy
Topics
premium lock iconCompanies
Hint

Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.

You must implement a solution with a linear runtime complexity and use only constant extra space.

 

Example 1:

Input: nums = [2,2,1]

Output: 1

Example 2:

Input: nums = [4,1,2,1,2]

Output: 4

Example 3:

Input: nums = [1]

Output: 1

 

Constraints:

    1 <= nums.length <= 3 * 104
    -3 * 104 <= nums[i] <= 3 * 104
    Each element in the array appears twice except for one element which appears only once.



'''

from typing import List

class Solution:

    def sol_dict(self, nums: List[int]) -> int:

        # breaks constant memory rule . also runs in O(n)
        '''
        Runtime
        0ms
        Beats100.00%
        Memory
        21.87MB
        Beats10.46%
        '''

        dnums = set()
        for n in nums:
            if n in dnums: dnums.remove(n)
            else: dnums.add(n)

        return dnums.pop()


    def sol_xor(self, nums: List[int]) -> int:

        # O(n) time, O(1) space: a^a=0 and a^0=a, so XOR-ing everything
        # cancels the pairs and leaves the single number
        '''
        Runtime
        0ms
        Beats100.00%
        Memory
        21.17MB
        Beats43.49%
        '''

        result = 0
        for n in nums:
            result ^= n

        return result


    def singleNumber(self, nums: List[int]) -> int:

        return self.sol_xor(nums)
    
