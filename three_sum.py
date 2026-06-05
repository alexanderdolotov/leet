from typing import List
import bisect
import datetime
import time

'''
Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets.

 

Example 1:

Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]
Explanation: 
nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
The distinct triplets are [-1,0,1] and [-1,-1,2].
Notice that the order of the output and the order of the triplets does not matter.

Example 2:

Input: nums = [0,1,1]
Output: []
Explanation: The only possible triplet does not sum up to 0.

Example 3:

Input: nums = [0,0,0]
Output: [[0,0,0]]
Explanation: The only possible triplet sums up to 0.

 

Constraints:

    3 <= nums.length <= 3000
    -10^5 <= nums[i] <= 10^5


'''

class Solution:

    def num_neigh(self, nums, idx):

        max_idx = len(nums) - 1
        val = nums[idx]
        #print('checking val neighs', val, str(nums))

        idx1 = idx - 1 
        idx2 = idx - 2 

        idx3 = idx + 1 
        idx4 = idx + 2 

        neighs = 0
        if idx1 >= 0 and nums[idx1] == val:
            neighs += 1 

        if idx2 >= 0 and nums[idx2] == val:
            neighs += 1 

        if idx3 <= max_idx and nums[idx3] == val:
            neighs += 1 

        if idx4 <= max_idx and nums[idx4] == val:
            neighs += 1 

        return neighs



    def binary_search(self, nums: list[int], val: int, num1: int, num2: int) -> bool:
        """nums must be sorted in non-decreasing order."""

        #print('bin search: ', val, num1, num2)

        lo, hi = 0, len(nums) - 1
        while lo <= hi:
            mid = (lo + hi) // 2

            x = nums[mid]
            if x == val:

                if val != num1 and val != num2:
                    #print('no neighs needed')
                    return True 

                if val == num1 and val == num2:
                    if self.num_neigh(nums, mid) > 1:
                        #print('neighs: ', self.num_neigh(nums, mid), 1)
                        return True 
                    else:
                        return False

                if val == num1 or val == num2:
                    # check neighbors
                    if self.num_neigh(nums, mid) > 0:
                        #print('neighs: ', self.num_neigh(nums, mid), 0)
                        return True
                    else:
                        return False


                return True

            if x > val:
                hi = mid - 1
            else:
                lo = mid + 1

        return False

    def binary_search_bisect(self, nums: list[int], val: int, num1: int, num2: int) -> bool:
        """Same behavior as binary_search; locate step uses bisect.bisect_left."""
        mid = bisect.bisect_left(nums, val)
        if mid == len(nums) or nums[mid] != val:
            return False
        if val != num1 and val != num2:
            return True
        if val == num1 and val == num2:
            return self.num_neigh(nums, mid) > 1
        return self.num_neigh(nums, mid) > 0


    def n3_sol(self, nums: list[int]) -> list[list[int]]:

        triplets: set[tuple[int, int, int]] = set()
        nlen = len(nums)

        for i in range(0,nlen):
            for j in range(i, nlen):
                for k in range(j, nlen):
                    if i == j or j == k or i == k:
                        continue 

                    if nums[i] + nums[j] + nums[k] == 0:
                        triplet = [nums[i], nums[j], nums[k]]

                        triplet.sort()
                        triplets.add((triplet[0], triplet[1], triplet[2]))

        return [list(t) for t in sorted(triplets)]


    def remove_more3_occurances(self, sorted_nums:list):

        occurance = 1
        running_num = sorted_nums[0]
        new_nums = [running_num]
        for i in range(1, len(sorted_nums)):
            num = sorted_nums[i]
            if num == running_num:         
                occurance += 1
                if occurance < 4:
                    new_nums.append(num)

            else:
                running_num = num 
                occurance = 1
                new_nums.append(num)


        return new_nums



    def better_sol(self, nums: list[int]) -> list[list[int]]:

        triplets: set[tuple[int, int, int]] = set()
        
        # sort data first 

        nums.sort() # nlogn. max 3000*lg3000

        nlen = len(nums)
        print('nlen1', len(nums))
        nums = self.remove_more3_occurances(nums)

        #print(nums)
        nlen = len(nums)

        print('nlen2', len(nums))

        print('running N^2 logN method')

        min_val = nums[0]
        max_val = nums[-1]

        for i in range(0,nlen):
            for j in range(i+1, nlen):

                running_sum = (nums[i] + nums[j])
                
                running_sum_delta = -running_sum

                if running_sum_delta > max_val:
                    continue 

                if running_sum_delta < min_val:
                    continue

                #print('bin search: ', running_sum_delta, nums[i], nums[j])
                # found = self.binary_search(nums, running_sum_delta, nums[i], nums[j])
                found = self.binary_search_bisect(nums, running_sum_delta, nums[i], nums[j])
                if found:
                    triplet = [nums[i], nums[j], running_sum_delta]

                    triplet.sort()
                    triplets.add((triplet[0], triplet[1], triplet[2]))


        return [list(t) for t in (triplets)]



    def threeSum(self, nums: list[int]) -> list[list[int]]:
        print('nlen', len(nums))
        t0 = time.perf_counter()
        print('before', datetime.datetime.now().isoformat(timespec='milliseconds'))
        out = self.better_sol(nums)
        print('after ', datetime.datetime.now().isoformat(timespec='milliseconds'))
        print('elapsed_s', f'{time.perf_counter() - t0:.6f}')
        return out




s = Solution()
out = s.threeSum([-1,0,1,2,-1,-4])
print(out)

# found = s.binary_search([1,2,3,4,5,6,7,8,9,10], 5)
# print(found)


