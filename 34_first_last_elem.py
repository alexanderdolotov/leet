'''
34. Find First and Last Position of Element in Sorted Array
Medium
Topics
premium lock iconCompanies

Given an array of integers nums sorted in non-decreasing order, find the starting and ending position of a given target value.

If target is not found in the array, return [-1, -1].

You must write an algorithm with O(log n) runtime complexity.

 

Example 1:

Input: nums = [5,7,7,8,8,10], target = 8
Output: [3,4]

Example 2:

Input: nums = [5,7,7,8,8,10], target = 6
Output: [-1,-1]

Example 3:

Input: nums = [], target = 0
Output: [-1,-1]

 

Constraints:

    0 <= nums.length <= 105
    -109 <= nums[i] <= 109
    nums is a non-decreasing array.
    -109 <= target <= 109


'''

from typing import List

class Solution:

    

    def bisearch(self, nums, target)->int:
        lo, hi = 0, len(nums) - 1
        while lo <= hi:
            mid = (lo + hi) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                lo = mid + 1
            else:
                hi = mid - 1
        return -1

    def find_bound(self, nums, target, lo, hi, leftmost)->int:
        result = -1
        while lo <= hi:
            mid = (lo + hi) // 2
            if nums[mid] == target:
                result = mid
                if leftmost:
                    hi = mid - 1
                else:
                    lo = mid + 1
            elif nums[mid] < target:
                lo = mid + 1
            else:
                hi = mid - 1
        return result

    def searchRange(self, nums: List[int], target: int) -> List[int]:

        # first find whether value exists and at which index using bisection search...

        tidx = self.bisearch(nums, target)

        if tidx == -1: return [-1,-1]

        # once a target is found, split into 2 bisection searches:
        # narrow to [0, tidx] for the leftmost occurrence and [tidx, len(nums)-1] for the rightmost
        left = self.find_bound(nums, target, 0, tidx, True)
        right = self.find_bound(nums, target, tidx, len(nums) - 1, False)

        return [left, right]
    

