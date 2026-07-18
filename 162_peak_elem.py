'''
162. Find Peak Element
Medium
Topics
premium lock iconCompanies

A peak element is an element that is strictly greater than its neighbors.

Given a 0-indexed integer array nums, find a peak element, and return its index. If the array contains multiple peaks, return the index to any of the peaks.

You may imagine that nums[-1] = nums[n] = -∞. In other words, an element is always considered to be strictly greater than a neighbor that is outside the array.

You must write an algorithm that runs in O(log n) time.

 

Example 1:

Input: nums = [1,2,3,1]
Output: 2
Explanation: 3 is a peak element and your function should return the index number 2.

Example 2:

Input: nums = [1,2,1,3,5,6,4]
Output: 5
Explanation: Your function can return either index number 1 where the peak element is 2, or index number 5 where the peak element is 6.

 

Constraints:

    1 <= nums.length <= 1000
    -231 <= nums[i] <= 231 - 1
    nums[i] != nums[i + 1] for all valid i.


'''

from typing import List


class Solution:

    def _slope(self, nums, istart, iend):
        # check the slope of mid in the indexes 
        if istart >= iend: imid = iend
        else: imid = (iend - istart) // 2 + istart    

        # check if greater than prev val (positive slope)
        slope = ( (nums[imid] - nums[imid-1]) > 0 if imid > 0 else True )

        # exit case, where indexes converge
        if imid == iend:
            if slope: return imid 
            else: return imid-1

        # if slope is positive, higher edge exists to the right, else to the left.
        if slope: return self._slope(nums=nums, istart=imid+1, iend=iend)
        else: return self._slope(nums=nums, istart=istart, iend=imid-1)

        

    def findPeakElement(self, nums: List[int]) -> int:

        # since edges are -inf, by induction, a peak (highest point) in the list must exist. 

        # trivial cases
        if len(nums) == 1: return 0
        if len(nums) == 2: return (0 if nums[0] > nums[1] else 1)
            
        # runs in LogN
        return self._slope(nums, 0, len(nums)-1)

