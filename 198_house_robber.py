'''
198. House Robber
Medium
Topics
premium lock iconCompanies

You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed, the only constraint stopping you from robbing each of them is that adjacent houses have security systems connected and it will automatically contact the police if two adjacent houses were broken into on the same night.

Given an integer array nums representing the amount of money of each house, return the maximum amount of money you can rob tonight without alerting the police.

 

Example 1:

Input: nums = [1,2,3,1]
Output: 4
Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
Total amount you can rob = 1 + 3 = 4.

Example 2:

Input: nums = [2,7,9,3,1]
Output: 12
Explanation: Rob house 1 (money = 2), rob house 3 (money = 9) and rob house 5 (money = 1).
Total amount you can rob = 2 + 9 + 1 = 12.

 

Constraints:

    1 <= nums.length <= 100
    0 <= nums[i] <= 400



'''


from typing import List 


class Solution:

    mem = {}

    def robi(self, nums: List[int], i) -> int:

        '''
        Runtime
        0ms
        Beats100.00%
        Memory
        19.24MB
        Beats60.52%

        '''

        if i == -1: return 0
        if i == -2: return 0 

        if i in self.mem: return self.mem[i]

        self.mem[i] = max(self.robi(nums, i-1), self.robi(nums, i-2) + nums[i]) 
        
        return self.mem[i]




    def rob(self, nums: List[int]) -> int:
        
        # somewhat similar to the staircase problem, but now question: jump 1 or 2 spaces between a house, and start from index 0 or 1... 

        # we can follow a stair climbing example, where running max can be either n-2 house running max or n-3 house running max

        # so: f(n) = max(f(n-1), f(n-2) + h[n])

        self.mem = {}


        return self.robi(nums, len(nums)-1)
    
