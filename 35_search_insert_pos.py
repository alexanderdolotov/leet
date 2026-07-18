'''
35. Search Insert Position
Easy
Topics
premium lock iconCompanies

Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

You must write an algorithm with O(log n) runtime complexity.

 

Example 1:

Input: nums = [1,3,5,6], target = 5
Output: 2

Example 2:

Input: nums = [1,3,5,6], target = 2
Output: 1

Example 3:

Input: nums = [1,3,5,6], target = 7
Output: 4

 

Constraints:

    1 <= nums.length <= 104
    -104 <= nums[i] <= 104
    nums contains distinct values sorted in ascending order.
    -104 <= target <= 104

 


'''

from typing import List



class Solution:


    def bin_search(self, sorted_unique_nums: List[int], target: int, start_idx:int, end_idx: int):

        '''
        Runtime
        0ms
        Beats100.00%
        Memory
        19.88MB
        Beats80.58%

        '''
        
        if start_idx >= end_idx: return start_idx

        mid_idx = (end_idx-start_idx) // 2 + start_idx

        val = sorted_unique_nums[mid_idx]
        if val == target: return mid_idx

        if target < val:
            return self.bin_search(sorted_unique_nums, target, start_idx, mid_idx)

        else:
            return self.bin_search(sorted_unique_nums, target, mid_idx+1, end_idx)




    def searchInsert(self, nums: List[int], target: int) -> int:
        
        # just binary search.
        return self.bin_search(nums, target, 0, len(nums))

