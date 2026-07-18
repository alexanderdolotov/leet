'''
300. Longest Increasing Subsequence
Medium

Topics
premium lock icon
Companies
Given an integer array nums, return the length of the longest strictly increasing subsequence.

 

Example 1:

Input: nums = [10,9,2,5,3,7,101,18]
Output: 4
Explanation: The longest increasing subsequence is [2,3,7,101], therefore the length is 4.
Example 2:

Input: nums = [0,1,0,3,2,3]
Output: 4
Example 3:

Input: nums = [7,7,7,7,7,7,7]
Output: 1
 

Constraints:

1 <= nums.length <= 2500
-104 <= nums[i] <= 104
 

Follow up: Can you come up with an algorithm that runs in O(n log(n)) time complexity?
'''

from typing import List

class Solution:

    imem = {} # keeps memory of already found results for substrings so as not to double check them again

    def sol_rec1(self, nums: List[int], i: int) -> int: 

        # n^2 solution. Accepted. 
        '''
        
        Runtime
        1831
        ms
        Beats
        10.97%

        Memory
        20.01
        MB
        Beats
        10.69%
        '''

        max_len = 1 
        for j in range(i + 1, len(nums)):
            if nums[j] > nums[i]:
                if j in self.imem:
                    next_len = self.imem[j]
                else:
                    next_len = self.sol_rec1(nums, j)
                    self.imem[j] = next_len

                max_len = max(max_len, 1 + next_len)

        self.imem[i] = max_len
        return max_len 


    def n2sol(self, nums: List[int]) -> int:

        self.imem = {}

        # n^2 solution. Accepted. 
        '''
        
        Runtime
        1831
        ms
        Beats
        10.97%

        Memory
        20.01
        MB
        Beats
        10.69%
        '''

        max_len = 0
        for i in range(len(nums)):
            if i not in self.imem:
                curr_len = self.sol_rec1(nums, i)
                max_len = max(max_len, curr_len)
            else:
                max_len = max(max_len, self.imem[i])

        return max_len


    def _fenwick_update(self, pos: int, val: int) -> None:
        while pos <= self._fenwick_size:
            if self._fenwick[pos] < val:
                self._fenwick[pos] = val
            pos += pos & (-pos)

    def _fenwick_query(self, pos: int) -> int:
        result = 0
        while pos > 0:
            if self._fenwick[pos] > result:
                result = self._fenwick[pos]
            pos -= pos & (-pos)
        return result

    def sol_rec2(self, nums: List[int], i: int) -> int:
        # query max DP value among already-inserted js (j > i) with nums[j] > nums[i],
        # via the reverse-rank mapping that turns ">" into a Fenwick prefix query
        q = self._fenwick_query(self._reverse_rank[nums[i]] - 1)
        dp_i = q + 1
        self._fenwick_update(self._reverse_rank[nums[i]], dp_i)
        return dp_i

    def nlognsol(self, nums: List[int]) -> int:

        '''
        
        Runtime
        28
        ms
        Beats
        71.11%


        Memory
        19.63
        MB
        Beats
        15.86%
        '''
        
        sorted_vals = sorted(set(nums))
        m = len(sorted_vals)
        rank = {v: idx + 1 for idx, v in enumerate(sorted_vals)}
        self._reverse_rank = {v: m - rank[v] + 1 for v in sorted_vals}
        self._fenwick = [0] * (m + 1)
        self._fenwick_size = m

        max_len = 0
        # right to left so every j > i is already in the tree when i is queried
        for i in range(len(nums) - 1, -1, -1):
            dp_i = self.sol_rec2(nums, i)
            max_len = max(max_len, dp_i)

        return max_len


    def lengthOfLIS(self, nums: List[int]) -> int:


        return self.nlognsol(nums) 
    
    