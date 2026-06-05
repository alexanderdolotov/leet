from dataclasses import dataclass
from typing import List

'''

228. Summary Ranges
Easy
Topics
premium lock iconCompanies

You are given a sorted unique integer array nums.

A range [a,b] is the set of all integers from a to b (inclusive).

Return the smallest sorted list of ranges that cover all the numbers in the array exactly. That is, each element of nums is covered by exactly one of the ranges, and there is no integer x such that x is in one of the ranges but not in nums.

Each range [a,b] in the list should be output as:

    "a->b" if a != b
    "a" if a == b

 

Example 1:

Input: nums = [0,1,2,4,5,7]
Output: ["0->2","4->5","7"]
Explanation: The ranges are:
[0,2] --> "0->2"
[4,5] --> "4->5"
[7,7] --> "7"

Example 2:

Input: nums = [0,2,3,4,6,8,9]
Output: ["0","2->4","6","8->9"]
Explanation: The ranges are:
[0,0] --> "0"
[2,4] --> "2->4"
[6,6] --> "6"
[8,9] --> "8->9"

 

Constraints:

    0 <= nums.length <= 20
    -231 <= nums[i] <= 231 - 1
    All the values of nums are unique.
    nums is sorted in ascending order.

 
'''

class Solution:

    def get_ranges(self, nums: List[int]) -> List[str]:


        sranges = []

        for n in nums:
            if len(sranges) == 0:
                sranges.append([n])
                continue

            nm1 = n-1
            last_arr = sranges[-1]
            last_num = last_arr[-1]
            if nm1 == last_num:
                if len(last_arr) == 1:
                    last_arr.append(n)
                else:
                    last_arr[1] = n

            else:
                sranges.append([n])

        return sranges



    def summaryRanges(self, nums: List[int]) -> List[str]:
        
        sranges = self.get_ranges(nums)

        # pretty print ranges 
        pretty_ranges = []
        for r in sranges:
            if len(r) == 2:
                pretty_ranges.append(  f'{r[0]}->{r[1]}' )
            else:
                pretty_ranges.append( f'{r[0]}' )


        return pretty_ranges


s = Solution()
out = s.summaryRanges([0,1,2,4,5,7])
print(out)
     


