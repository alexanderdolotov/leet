
from typing import List
import math

'''
209. Minimum Size Subarray Sum
Medium
Topics
premium lock iconCompanies

Given an array of positive integers nums and a positive integer target, return the minimal length of a whose sum is greater than or equal to target. If there is no such subarray, return 0 instead.

 

Example 1:

Input: target = 7, nums = [2,3,1,2,4,3]
Output: 2
Explanation: The subarray [4,3] has the minimal length under the problem constraint.

Example 2:

Input: target = 4, nums = [1,4,4]
Output: 1

Example 3:

Input: target = 11, nums = [1,1,1,1,1,1,1,1]
Output: 0

 

Constraints:

    1 <= target <= 10^9
    1 <= nums.length <= 10^5
    1 <= nums[i] <= 10^4




'''

class Solution:

    def sort_and_merge(self, target: int, nums: List[int]) -> int:

        # this results in sub-sequence, not subarray, so not the correct answer
        nums.sort(reverse=True)

        print(nums)
        running_sum = 0
        running_count = 0
        for n in nums:
            running_sum += n 
            running_count += 1

            print(running_count, n, running_sum, target)
            if running_sum >= target:
                return  running_count

        return 0

    def all_subarrays(self, target: int, nums: List[int]) -> int:


        builds = []

        possible_subs = []


        for n in nums:

            if n >= target:
                return 1

            new_builds = []
            for b in builds:
                s = sum(b) + n 
                if s < target:
                    new_builds.append(b)
                    new_builds.append(b + [n])
                else:
                    possible_subs.append(b + [n])

            builds = new_builds

            builds.append([n])
            

    def sliding_window_sub_greedy(self, target: int, nums: List[int]) -> int:

        
        total_len = len(nums)
       

        if total_len == 0:
            return 0 

        if total_len == 1:
            return (1 if nums[0] >= target else 0)


        total_sum = sum(nums)
        print('total_sum', total_sum)
        if total_sum < target:
            return 0

        l = total_len
        i = 0
        j = total_len-1

        index_visits = {}

        while l > 0:
            inum = nums[i]
            jnum = nums[j]

            print(i, j, 'nums:', inum, jnum, ' sum, len:', total_sum, l)

            if inum >= target or jnum >= target:
                return 1

            if inum < jnum:
                total_sum -= inum
                i += 1
                l -=1 
                if i in index_visits:
                    index_visits[i] += 1

                    if index_visits[i] > 2:
                        return l+1

                else:
                    index_visits[i] = 1

            else:
                total_sum -= jnum
                j -= 1
                l -=1 

                if j in index_visits:
                    index_visits[j] += 1

                    if index_visits[j] > 2:
                        return l+1

                else:
                    index_visits[j] = 1
                
            if total_sum < target:

                inum = nums[i]
                jnum = nums[j]

                # Add next greatest if exists 
                if inum < jnum:
                    if j == total_len-1:
                        return l + 1
                    else:
                        j += 1 
                        l += 1
                        total_sum += nums[j]
                else:
                    if i == 0:
                        return l + 1
                    else:
                        i -= 1
                        l += 1
                        total_sum += nums[i]

        return l




    def nlogn_subarray_scan(self, target: int, nums: List[int]) :

        # idea: pick a mid sized array, and scan all numbers. add or subtract by 1/4 to try new array and run scan until two scan are in 1 size diff and off 

        total_len = len(nums)
        prev2_size = total_len
        prev_size = total_len // 2
        prev_above_target = self.linear_scan(target, nums, prev_size)

        num_scans = 1

        while True:
            if prev_above_target:
                if prev_size <= 0:
                    return 0, num_scans
                if prev_size == 1:
                    return 1 
                elif prev_size == 2:
                    new_size = 1 
                elif prev_size == 3:
                    new_size = 2
                else:
                    decr = abs(prev_size - prev2_size) // 2
                    if decr < 1:
                        decr = 1
                    new_size = prev_size - decr

                new_above_target = self.linear_scan(target, nums, new_size)
                num_scans += 1

            else:
                if prev_size >= total_len:
                    return 0 , num_scans
                elif prev_size == total_len - 1:
                    new_size = total_len
                elif prev_size == total_len - 2:
                    new_size = total_len - 1
                else:
                    incr =  (abs(prev_size - prev2_size) // 2) 
                    if incr < 1:
                        incr = 1
                    new_size = prev_size +incr


                new_above_target = self.linear_scan(target, nums, new_size)
                num_scans += 1


            if new_above_target != prev_above_target and abs(new_size - prev_size) == 1:
                if new_above_target:
                    return new_size, num_scans
                else:
                    return prev_size, num_scans

            prev2_size = prev_size
            prev_size = new_size
            prev_above_target = new_above_target



    def linear_scan(self, target: int, nums: List[int], array_size) -> bool:

        DEBUG = False

        if DEBUG:
            print('lin scan of size: ', array_size)

        initialize_sum = 0
        j = 0
        for num in nums:
            initialize_sum += num
            j += 1 
            if j >= array_size:
                break

        if DEBUG:
            print('lin scan init sum: ', initialize_sum)

        if initialize_sum >= target:
            return True

        for i in range(j, len(nums)):
            initialize_sum += nums[i]
            initialize_sum -= nums[i-array_size]
            j += 1 

            # if DEBUG:
            #     print('lin scan', initialize_sum)

            if initialize_sum >= target:
                return True

        return False



    def n_subarray_sol(self, target: int, nums: List[int]) -> int:

        # need big idea 

        return 0






    def minSubArrayLen(self, target: int, nums: List[int]) -> int:

          
        total_len = len(nums)
       
        if total_len == 0:
            return 0 

        if total_len == 1:
            return (1 if nums[0] >= target else 0)

        answ, scans = self.nlogn_subarray_scan(target=target, nums=nums)

        print('num linear scans: ', scans , 'len:', total_len)

        return answ




s = Solution()
out = s.minSubArrayLen(15, [5,1,3,5,10,7,4,9,2,8, 12, 6, 3, 6, 4, 3, 7, 6, 12, 3])
print(out)
     
