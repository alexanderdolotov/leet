'''
46. Permutations
Medium
Topics
premium lock iconCompanies

Given an array nums of distinct integers, return all the possible . You can return the answer in any order.

 

Example 1:

Input: nums = [1,2,3]
Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]

Example 2:

Input: nums = [0,1]
Output: [[0,1],[1,0]]

Example 3:

Input: nums = [1]
Output: [[1]]

 

Constraints:

    1 <= nums.length <= 6
    -10 <= nums[i] <= 10
    All the integers of nums are unique.


'''


class Solution:


    def permute_listbuild(self, nums: List[int]) -> List[List[int]]:
        
        # n! permutations of each number... 
        
        build = []
        for n in nums:
            build.append([n])

        for i in range(len(nums)-1):
            new_build = []
            for b in build:
                for n in nums:
                    if n in b: continue 
                    new_build.append(b + [n])
        

            build = new_build

        return build
    
    def permute_swap(self, nums: List[int]) -> List[List[int]]: # fastest
        result = []

        def backtrack(start):
            if start == len(nums):
                result.append(nums.copy())
                return
            for i in range(start, len(nums)):
                nums[start], nums[i] = nums[i], nums[start] # do one swap
                backtrack(start + 1) # move forward
                nums[start], nums[i] = nums[i], nums[start] # swaps back

        backtrack(0)
        return result

    def permute(self, nums: List[int]) -> List[List[int]]:
        return self.permute_swap(nums)
    
