
from typing import List

'''
219. Contains Duplicate II
Easy
Topics
premium lock iconCompanies

Given an integer array nums and an integer k, return true if there are two distinct indices i and j in the array such that nums[i] == nums[j] and abs(i - j) <= k.

 

Example 1:

Input: nums = [1,2,3,1], k = 3
Output: true

Example 2:

Input: nums = [1,0,1,1], k = 1
Output: true

Example 3:

Input: nums = [1,2,3,1,2,3], k = 2
Output: false

 

Constraints:

    1 <= nums.length <= 105
    -109 <= nums[i] <= 109
    0 <= k <= 105



'''

class Solution:

    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        
        nums_ranges = {}
        for i in range(len(nums)):
            num = nums[i]
            if num in nums_ranges:
                nums_ranges[num].append(i)
            else:
                nums_ranges[num] = [i]


        for nr in nums_ranges.keys():
            r = nums_ranges[nr]
            if len(r) > 1:
                r.sort()
                for ri in range(len(r)-1):
                    diff = abs(r[ri] - r[ri+1])
                    if diff <= k:
                        return True


        return False


s = Solution()
out = s.containsNearbyDuplicate([1,2,3,1,2,3], 1 )
print(out)
     


