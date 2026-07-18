'''
918. Maximum Sum Circular Subarray
Medium
Topics
premium lock iconCompanies
Hint

Given a circular integer array nums of length n, return the maximum possible sum of a non-empty subarray of nums.

A circular array means the end of the array connects to the beginning of the array. Formally, the next element of nums[i] is nums[(i + 1) % n] and the previous element of nums[i] is nums[(i - 1 + n) % n].

A subarray may only include each element of the fixed buffer nums at most once. Formally, for a subarray nums[i], nums[i + 1], ..., nums[j], there does not exist i <= k1, k2 <= j with k1 % n == k2 % n.



Example 1:

Input: nums = [1,-2,3,-2]
Output: 3
Explanation: Subarray [3] has maximum sum 3.

Example 2:

Input: nums = [5,-3,5]
Output: 10
Explanation: Subarray [5,5] has maximum sum 5 + 5 = 10.

Example 3:

Input: nums = [-3,-2,-3]
Output: -2
Explanation: Subarray [-2] has maximum sum -2.



Constraints:

    n == nums.length
    1 <= n <= 3 * 104
    -3 * 104 <= nums[i] <= 3 * 104



'''

from typing import List


class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:

        '''
        Runtime
        41ms
        Beats72.52%
        Memory
        23.94MB
        Beats88.04%

        
        '''

        #Case 1: doesn't wrap   [   ===   ]        → normal Kadane's
        #Case 2: wraps          [==     ==]        → excludes some middle segment, which is by def kadane min

        # [5,-3, 1,7,-10,5] Kadane's first pass = 8. but when keep looping, actual max is 5+5-3+1+7=15
        # wrapped_max = total - min_subarray (minimize the hole to maximize the remainder)
        # Edge: all negative → case 2 gives 0 (empty subarray, invalid), return case 1 directly.

        total = 0
        local_max = local_min = 0
        global_max = global_min = nums[0]

        for num in nums:
            local_max = max(num, local_max + num)
            global_max = max(global_max, local_max)

            local_min = min(num, local_min + num)
            global_min = min(global_min, local_min)

            total += num

        if global_max < 0:
            return global_max

        return max(global_max, total - global_min)
