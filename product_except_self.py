
from typing import List
import math

'''

238. Product of Array Except Self
Medium

Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].

The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

You must write an algorithm that runs in O(n) time and without using the division operation.


Example 1:

Input: nums = [1,2,3,4]
Output: [24,12,8,6]

Example 2:

Input: nums = [-1,1,0,-3,3]
Output: [0,0,9,0,0]


'''

class Solution:

    def n2_sol(self, nums: List[int]) -> List[int]:

        l = len(nums)
        result = [None]*l

        for i in range(0,l):
                  
            running_m = 1
            for j in range(0,l):
                if j != i:
                    num = nums[j]
                    if num == 0:
                        running_m = 0
                        break
                    else:
                        running_m = running_m * nums[j]

            result[i] = running_m

        return result
    

    def lin_sol(self, nums: List[int]) -> List[int]:

        l = len(nums)

        result = [0]*l

        num_zeros = 0
        zero_idx = -1

        for i in range(0,l):            
            num = nums[i]
            if num == 0:
                num_zeros += 1
                zero_idx = i

        if num_zeros > 1:
            return result
        
        if num_zeros == 1:
            v = 1 
            for i in range(0,l):
                if i == zero_idx:
                    continue 

                num = nums[i]
                v = v * num

            result[zero_idx] = v 
            return result 
        
        # convert to logs 
        vlog = 0 
        slog = 1
        for i in range(0,l):
            num = nums[i]
            vlog += math.log(abs(num))
            slog = slog * (1 if num > 0 else -1)


        for i in range(0,l):
            num = nums[i]
            result[i] = int(round(math.exp(vlog - math.log(abs(num))), 0)) * slog * (1 if num > 0 else -1)

        return result
    

    def productExceptSelf(self, nums: List[int]) -> List[int]:

        return self.lin_sol(nums)


s = Solution()
out = s.productExceptSelf([1,2,3,4])
print(out)



