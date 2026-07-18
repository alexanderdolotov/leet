'''
215. Kth Largest Element in an Array
Medium
Topics
premium lock iconCompanies

Given an integer array nums and an integer k, return the kth largest element in the array.

Note that it is the kth largest element in the sorted order, not the kth distinct element.

Can you solve it without sorting?

 

Example 1:

Input: nums = [3,2,1,5,6,4], k = 2
Output: 5

Example 2:

Input: nums = [3,2,3,1,2,4,5,5,6], k = 4
Output: 4

 

Constraints:

    1 <= k <= nums.length <= 105
    -104 <= nums[i] <= 104



'''

import heapq
import random
from typing import List

class Solution:

    def sortsol(self, nums: List[int], k: int) -> int:

        '''
        Runtime
        48ms
        Beats89.50%
        Memory
        31.14MB
        Beats24.29%
        '''

        nums.sort(reverse=True)

        return nums[k-1]


    def sol_nosort1(self, nums: List[int], k: int) -> int:

        '''
        Runtime
        120ms
        Beats12.89%
        Memory
        31.76MB
        Beats8.28%
        '''

        max_heap = [-num for num in nums]
        heapq.heapify(max_heap)

        largest = heapq.heappop(max_heap)
        for _ in range(k - 1):
            largest = heapq.heappop(max_heap)

        return -largest


    def sol_nosort2(self, nums: List[int], k: int) -> int:

        # keep a rotating min heap of size k. 
        # as new value is added, pop the min. 
        # left with top k values
        # return next min value as top kth largest in min heap 
        '''
        Runtime
        106ms
        Beats24.13%
        Memory
        31.13MB
        Beats24.29%
        '''

        min_heap = []

        for num in nums:
            heapq.heappush(min_heap, num)
            if len(min_heap) > k:
                heapq.heappop(min_heap)

        return min_heap[0]


    def _partition3way(self, nums: List[int], lo: int, hi: int, pivot_idx: int):

        # groups [lo, lt) < pivot, [lt, gt] == pivot, (gt, hi] > pivot
        pivot = nums[pivot_idx]
        lt, gt, i = lo, hi, lo

        while i <= gt:
            if nums[i] < pivot:
                nums[i], nums[lt] = nums[lt], nums[i]
                lt += 1
                i += 1
            elif nums[i] > pivot:
                nums[i], nums[gt] = nums[gt], nums[i]
                gt -= 1
            else:
                i += 1

        return lt, gt


    def sol_nosort3(self, nums: List[int], k: int) -> int:

        '''
        Runtime
        103ms
        Beats30.26%
        Memory
        31.16MB
        Beats24.29%
        '''

        # quick select... same as quicksort, but only recurses into regions that we need to get top k elements. 
        # kth largest == index (n - k) in ascending sorted order
        target = len(nums) - k

        lo, hi = 0, len(nums) - 1
        while lo < hi:
            pivot_idx = random.randint(lo, hi)
            lt, gt = self._partition3way(nums, lo, hi, pivot_idx)

            if target < lt:
                hi = lt - 1
            elif target > gt:
                lo = gt + 1
            else:
                return nums[target]

        return nums[target]


    def findKthLargest(self, nums: List[int], k: int) -> int:
    

        return self.sol_nosort3(nums, k)
    
