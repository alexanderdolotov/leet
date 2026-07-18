'''
53. Maximum Subarray
Medium
Topics
premium lock iconCompanies

Given an integer array nums, find the with the largest sum, and return its sum.



Example 1:

Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
Output: 6
Explanation: The subarray [4,-1,2,1] has the largest sum 6.

Example 2:

Input: nums = [1]
Output: 1
Explanation: The subarray [1] has the largest sum 1.

Example 3:

Input: nums = [5,4,-1,7,8]
Output: 23
Explanation: The subarray [5,4,-1,7,8] has the largest sum 23.



Constraints:

    1 <= nums.length <= 10^5
    -10^4 <= nums[i] <= 10^4



Follow up: If you have figured out the O(n) solution, try coding another solution using the divide and conquer approach, which is more subtle.


'''

from typing import List

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # Kadane's: local_max = best subarray sum ending exactly at this position.
        # At each step, either extend the previous run or start fresh here.
        # Key insight: a positive running sum always helps future elements, so keep it.
        # Only reset when local_max goes negative — it's now a liability, not an asset.
        # Every subarray ends somewhere; evaluating "best ending here" at every index
        # implicitly checks all subarrays in O(n).
        local_max = global_max = nums[0]
        for num in nums[1:]:
            local_max = max(num, local_max + num)
            global_max = max(global_max, local_max)
        return global_max

    def maxSubArray_compress(self, nums: List[int]) -> int:
        # All-negative edge case: best we can do is the least-negative element
        if all(n <= 0 for n in nums):
            return max(nums)

        # Pass 1: collapse consecutive same-sign runs into groups (zeros fold into negatives)
        groups = []
        for num in nums:
            if groups and (groups[-1] > 0) == (num > 0):
                groups[-1] += num
            else:
                groups.append(num)

        # Trim non-positive edges — they can never start or end an optimal subarray
        while groups and groups[0] <= 0:
            groups.pop(0)
        while groups and groups[-1] <= 0:
            groups.pop()

        # Pass 2: hop negative moats when the running sum stays positive
        # compressed array is guaranteed [+, -, +, -, ..., +]
        running = best = 0
        for g in groups:
            running += g
            if running < 0:
                running = 0
            best = max(best, running)
        return best
