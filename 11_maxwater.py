
from typing import List
import random

'''
11. Container With Most Water
Medium


You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).

Find two lines that together with the x-axis form a container, such that the container contains the most water.

Return the maximum amount of water a container can store.

Notice that you may not slant the container.

 

Example 1:

Input: height = [1,8,6,2,5,4,8,3,7]
Output: 49
Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. In this case, the max area of water (blue section) the container can contain is 49.

Example 2:

Input: height = [1,1]
Output: 1

 

Constraints:

    n == height.length
    2 <= n <= 10^5
    0 <= height[i] <= 10^4

 


'''

class Solution:

    # basic linear scan to see if data is strictly increasing
    def check_asc(self, height: List[int]) :

        h1 = height[0]
        diff = height[1] - height[0]
        if diff < 0 :
            return False, None, 1

        for i in range(1, len(height)):
            h2 = height[i]
            new_diff = h2 - h1
            if new_diff < 0:
                return False , None, i

            if diff is not None:
                if new_diff != diff:
                    diff = None


            h1 = h2 


        return True, diff, len(height)


    # basic linear scan to see if data is strictly decreasing
    def check_desc(self, height: List[int]) :

        h1 = height[0]
        diff = height[1] - height[0]
        if diff > 0 :
            return False, None, 1

        for i in range(1, len(height)):
            h2 = height[i]
            new_diff = h2 - h1
            if new_diff > 0:
                return False , None, i

            if diff is not None:
                if new_diff != diff:
                    diff = None


            h1 = h2 


        return True, diff, len(height)



    # check for trivial solutions
    def checks_sol(self, height: List[int]) -> int:

        hlen = len(height)

        is_equal = False
        is_asc = False 
        is_desc = False
        diff = None

        is_asc, diff, bi = self.check_asc(height=height)

        if is_asc and diff is not None:
            if diff == 0:
                is_equal = True
                is_desc = True

        if is_equal:
            return height[0] * (hlen-1) # trivial

        # linear scan
        if is_asc:
            return self.linear_scan(starting_i=hlen-1, height=height)

        # linear scan
        if is_desc:
            return self.linear_scan(starting_i=0, height=height)

        return -1 # did not find simple solution


    def linear_scan(self, starting_i, height: List[int]) -> int:

        hlen = len(height)
        max_water = 0
        start_height = height[starting_i]

        for j in range(0, hlen):
            if j == starting_i:
                continue 

            water = min(start_height, height[j]) * abs(j-starting_i)
            if water > max_water:
                max_water = water

        return max_water


    # randomized shuffle of i
    def n2sol_r(self, height: List[int]) -> int:

        max_water = 0
        hlen = len(height)
        runi = 0 
        runj = 0

        # prevents cases where data comes in sorted
        i_range = list(range(0, hlen))
        random.shuffle(i_range)

        for i in i_range:
            hi = height[i]
            i_potential = hi * (hlen-i)
            if i_potential <= max_water:
                continue

            for j in range(i, hlen):
                water = min(hi , height[j]) * abs(j-i)
                if water > max_water:
                    max_water = water
                    runi = i 
                    runj = j


        return max_water, runi, runj



    def n2sol(self, height: List[int]) -> int:

        max_water = 0
        hlen = len(height)
        runi = 0 
        runj = 0

        for i in range(0, hlen):
            hi = height[i]
            i_potential = hi * (hlen-i)
            if i_potential <= max_water:
                continue

            for j in range(i, hlen):
                water = min(hi , height[j]) * abs(j-i)
                if water > max_water:
                    max_water = water
                    runi = i 
                    runj = j


        return max_water, runi, runj


    def greedy_walk(self, height: List[int]) -> int:
        # not complete solution ... does not work !!

        hlen = len(height)
        i = 0
        j = hlen - 1

        max_water = min(height[i], height[j]) * abs(j-i)

        runi = 0 
        runj = hlen - 1

        while j >= i:

            water = min(height[i], height[j]) * abs(j-i)
            if water > max_water:
                max_water = water
                runi = i 
                runj = j

            i_water = min(height[i+1], height[j]) * abs(j-i-1)
            j_water = min(height[i], height[j-1]) * abs(j-i-1)

            if i_water >= j_water:
                i += 1 
            else:
                j -= 1

        return max_water, runi, runj



    def maxArea(self, height: List[int]) -> int:
        
        checks_water = -1
        hlen = len(height)
        print('hlen', hlen)
        if hlen > 32: 
            checks_water = self.checks_sol(height=height)

        print('checked trivial water solutions: ', checks_water)
        if checks_water >= 0:
            return checks_water  

        # run randomized N^2 scan 
        n2_water, runi, runj = self.n2sol_r(height=height) 

        print('n2_water:', n2_water, 'runi', runi, 'runj', runj)

        return n2_water





s = Solution()
out = s.maxArea([1,8,6,2,5,4,8,3,7])

print(out)

