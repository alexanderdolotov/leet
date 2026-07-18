
from typing import List



class Solution:

    def jump(self, nums: List[int]) -> int:

        '''
        45. Jump Game II

        You are given a 0-indexed array of integers nums of length n. You are initially positioned at index 0.

        Each element nums[i] represents the maximum length of a forward jump from index i. In other words, if you are at index i, you can jump to any index (i + j) where:

            0 <= j <= nums[i] and
            i + j < n

        Return the minimum number of jumps to reach index n - 1. The test cases are generated such that you can reach index n - 1.

        

        Example 1:

        Input: nums = [2,3,1,1,4]
        Output: 2
        Explanation: The minimum number of jumps to reach the last index is 2. Jump 1 step from index 0 to 1, then 3 steps to the last index.

        Example 2:

        Input: nums = [2,3,0,1,4]
        Output: 2

        '''

        l = len(nums)
        if l == 1:
            return 0
        
        if l <= 2:
            return int(nums[0] > 0)
        else:
            start = nums[0]
            if start >= l-1:
                return 1 
            
            if start == 0:
                return 0
            
            until = min(start+1, l)
            running_max = start
            m = 1
            for i in range(1, until):
                j = nums[i]
                # go for max forward reach
                if j + i >= running_max:
                    running_max = j + i
                    m = i

            # recursion is slow...
            return self.jump(nums[m:]) + 1
            
    

    def canJump(self, nums: List[int]) -> bool:

        '''
        # 55
        You are given an integer array nums. You are initially positioned at the array's first index, and each element in the array represents your maximum jump length at that position.

        Return true if you can reach the last index, or false otherwise.

        Example 1:

        Input: nums = [2,3,1,1,4]
        Output: true
        Explanation: Jump 1 step from index 0 to 1, then 3 steps to the last index.

        Example 2:

        Input: nums = [3,2,1,0,4]
        Output: false
        Explanation: You will always arrive at index 3 no matter what. Its maximum jump length is 0, which makes it impossible to reach the last index.


        '''

        
        l = len(nums)
        if l == 1:
            return True
        
        if l <= 2:
            return nums[0] > 0
        else:
            start = nums[0]
            if start >= l-1:
                return True 
            
            if start == 0:
                return False
            
            until = min(start+1, l)
            running_max = start
            m = 1
            for i in range(1, until):
                j = nums[i]
                # go for max forward reach
                if j + i >= running_max:
                    running_max = j + i
                    m = i

            # recursion is slow...
            return self.canJump(nums[m:])
            
    

s = Solution()
out = s.jump([2,3,0,1,4])
print(out)

